from safeout import safeout
from os import path, unlink

def test_smoke(tmpdir):
    ofile = str(tmpdir / "test.txt")
    with safeout(ofile, "wt") as out:
        out.write("Hello World\n")
    assert path.exists(ofile)
    assert open(ofile).readlines() == ["Hello World\n"]

def test_exception():
    try:
        with safeout("test.2.txt", "wt") as out:
            out.write("Hello")
            raise ValueError("Nope")
    except ValueError:
        pass
    assert not path.exists("test.2.txt")
