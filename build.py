import sys
import PyInstaller.__main__ as pyinstaller


if __name__ != "__main__":
    print("this is not the import you're looking for", file=sys.stderr)
    exit(1)

args = []

# args.extend(["--clean"])
args.extend(["--noconfirm"])
args.extend(["--name", "kiss_sync"])
args.extend(["--hidden-import", "kiss_sync.gui.dist"])
args.extend(["--collect-all", "kiss_sync.gui.dist"])
args.extend(["kiss_sync/__main__.py"])

pyinstaller.run(args)
