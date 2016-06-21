
import arcpy
from pprint import PrettyPrinter
from os.path import join
from os.path import dirname
from os.path import abspath


class Cache(object):
    '''A class to hold stuff
    '''
    def __init__(self):
        self.names = []
        self.workspace = None

    def set_workspace(self, workspace):
        self.workspace = workspace
        self.names = []


def find(name):
    '''find a layer by its name. Helpful when searching through large
    db.owner.name workspaces. The tables are cached after the first run for speed
    wins on successive runs.

    set the workspace with `cache.set_workspace`

    name: [Strings]'''
    if cache.workspace is None:
        return 'cache.set_workspace(workspace)'

    if isinstance(name, basestring):
        name = [name]

    if len(cache.names) == 0:
        walk = arcpy.da.Walk(cache.workspace, followlinks=True)

        for dirpath, dirnames, filenames in walk:
            cache.names = filenames

    return [fc for fc in cache.names if fc.split('.')[2] in name]

if __name__ == '__main__':
    arcpy.env.overwriteOutput = True

    pp = PrettyPrinter(indent=2, width=20)
    pprint = pp.pprint

    cache = Cache()
    print('Cache loaded from PYTHONSTARTUP')
