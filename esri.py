#!/usr/bin/env python
# * coding: utf8 *
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
        import arcpy
        walk = arcpy.da.Walk(cache.workspace, followlinks=True)

        for dirpath, dirnames, filenames in walk:
            cache.names = filenames

    matches = [fc for fc in cache.names if fc.split('.')[2] in name]

    data = {}
    for match in matches:
        db, owner, name = match.split('.')
        data.setdefault(owner, []).append(name)

    pprint(data)

if __name__ == '__main__':
    pp = PrettyPrinter(indent=2, width=20)
    pprint = pp.pprint

    cache = Cache()
    print('Cache loaded from PYTHONSTARTUP')
