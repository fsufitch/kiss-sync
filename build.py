import os
import shutil
import sys
import PyInstaller.__main__ as pyinstaller


if __name__ != "__main__":
    print("this is not the import you're looking for", file=sys.stderr)
    exit(1)

args = []

SEP = os.pathsep

print(SEP)
args.extend(["--clean"])
args.extend(["--noconfirm"])
args.extend(["--name", "kiss"])
args.extend(["--hidden-import", "qtpy"])  # Qt support
args.extend(["--add-data", f"kiss_sync/gui/dist{SEP}kiss_sync/gui/dist"])
args.extend(["kiss_sync/__main__.py"])

print(args)

pyinstaller.run(args)
