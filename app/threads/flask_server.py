from threading import Thread
from app.web.app_flask import NovaViewFlask


class FlaskThread(Thread):
    def run(self):
        app = NovaViewFlask()
        app.run(port=5000)
