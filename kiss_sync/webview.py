import logging
import platform
from pathlib import Path
import shutil
import os
import sys
import threading
import webview

from kiss_sync.gui.server import KissSyncGUI

import pkg_resources

LOG = logging.getLogger()


def hack_webview_dll():
    if sys.platform not in ["win32"]:
        return

    webview_dir = Path(pkg_resources.resource_filename("webview", ""))

    if platform.architecture()[0] == "64bit":
        dll_path = webview_dir / "lib" / "x64" / "WebView2Loader.dll"
    else:
        LOG.warning(
            "Unknown platform architecture, cannot do hacky Windows stuff (%s)",
            platform.architecture(),
        )
        return

    LOG.warning("Applying ultra hacky Windows stuff")

    shutil.copy(dll_path, webview_dir / "lib")


def start_kiss_gui() -> None:
    gui = KissSyncGUI()
    gui_app = gui.get_application()

    # MEGA HACK
    hack_webview_dll()

    window = webview.create_window("my window", gui_app)
    window.min_size = (800, 600)

    def _close_splash() -> None:
        import time

        time.sleep(1)
        try:
            import pyi_splash  # type: ignore
        except ImportError:
            print("no splash to close")
            return

        pyi_splash.close()

    threading.Thread(target=_close_splash, daemon=True).start()

    webview.start(debug=False)
