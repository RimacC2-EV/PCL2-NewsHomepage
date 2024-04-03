from Core.Debug import LogWarning, LogInfo
import re

SNAPSHOT_PATTERN = re.compile(r'^[0-9]{2}[w|W][0-9]{2}[A-Fa-f]$')
PRE_RELEASE_PATTERN = re.compile(r'^.*-pre[0-9]+$')
RELEASE_CANDIDATE_PATTERN = re.compile(r'^.*-rc[0-9]+$')
RELEASE_PATTERN = re.compile(r'^1\.[0-9]+(\.[0-9]+)?$')

def gen_official_link(vid:str):
    if re.match(SNAPSHOT_PATTERN,vid):
        return f'https://minecraft.net/article/minecraft-snapshot-{vid.lower()}'
    if re.match(PRE_RELEASE_PATTERN,vid):
        version,sub=vid.split('-pre')
        return f'https://minecraft.net/article/minecraft-{version.replace(".","-")}-pre-release-{sub}'
    if re.match(RELEASE_CANDIDATE_PATTERN,vid):
        version,sub=vid.split('-rc')
        return f'https://minecraft.net/article/minecraft-{version.replace(".","-")}-release-candidate-{sub}'
    if re.match(RELEASE_PATTERN,vid):
        return f'https://minecraft.net/article/minecraft-java-edition-{vid.replace(".","-")}'
    return ''

def script(card,args,res):
    name:str = card['version-id']
    if card.get('not_finished') == 'true' and args[1] != 'Official':
        return ''
    data = res.data[f'{args[1]}Link']
    if len(args) >= 3:
        return data[args[2]]
    if '${' in name:
        raise KeyError()
    if args[1] == 'Official' and name not in data:
        return gen_official_link(name)
    return data[name]