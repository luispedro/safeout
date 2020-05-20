import os
from tempfile import NamedTemporaryFile
from os import path

class safeout(object):
    def __init__(self, oname, mode='w+b'):
        self.oname = oname
        self.mode = mode
        self.tfile = None

    def __enter__(self):
        dirname, oname = path.split(path.abspath(self.oname))
        self.tfile = NamedTemporaryFile(prefix=oname, dir=dirname, mode=self.mode, delete=False)
        return self.tfile

    def __exit__(self, exc, _1, _2):
        self.tfile.close()
        if exc is None:
            os.rename(self.tfile.name, self.oname)
        else:
            os.unlink(self.tfile.name)
