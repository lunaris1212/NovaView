from threading import Thread
from app.threads.flask_server import FlaskThread
from app.threads.process_watcher import ProcessWatcher
from app.utils.json_handler import reset_temp_data


class App:
    def __init__(self):
        reset_temp_data()
        self.threads = []

    def start(self):
        flask_thread = FlaskThread()
        # process_thread = ProcessWatcher()

        self.threads.append(flask_thread)
        # self.threads.append(process_thread)

        for t in self.threads:
            t.start()
