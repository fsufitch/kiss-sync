import cherrypy

import pkg_resources

DIST_DIR = pkg_resources.resource_filename(__name__, "dist")


class KissSyncGUI:
    def get_application(self) -> cherrypy.Application:
        app = cherrypy.Application(
            self,
            config={
                "/": {
                    "tools.staticdir.on": True,
                    "tools.staticdir.dir": DIST_DIR,
                    "tools.staticdir.index": "index.html",
                }
            },
        )
        return app
