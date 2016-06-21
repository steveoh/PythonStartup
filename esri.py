
import arcpy
from arcpy import env
env.overwriteOutput = True


class Cache(object):
    def __init__(self):
        self.names = []
        self.workspace = None

if __name__ == '__main__':
    cache = Cache()
    print('Cache loaded from PYTHONSTARTUP')


def owner_of(name):
    if isinstance(name, basestring):
        name = [name]

    if len(cache.names) == 0:
        walk = arcpy.da.Walk(cache.workspace, followlinks=True)

        for dirpath, dirnames, filenames in walk:
            cache.names = filenames

    return [fc for fc in cache.names if fc.split('.')[2] in name]
