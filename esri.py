
import arcpy
arcpy.env.overwriteOutput = True


class Cache(object):
    def __init__(self):
        self.names = []
        self.workspace = None

    def set_workspace(self, workspace):
        self.workspace = workspace
        self.names = []

if __name__ == '__main__':
    cache = Cache()
    print('Cache loaded from PYTHONSTARTUP')


def owner_of(name):
    if cache.workspace is None:
        return 'cache.set_workspace(workspace)'

    if isinstance(name, basestring):
        name = [name]

    if len(cache.names) == 0:
        walk = arcpy.da.Walk(cache.workspace, followlinks=True)

        for dirpath, dirnames, filenames in walk:
            cache.names = filenames

    return [fc for fc in cache.names if fc.split('.')[2] in name]
