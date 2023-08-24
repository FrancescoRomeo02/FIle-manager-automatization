import time
import os
from dotenv import load_dotenv
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from move_file import files_detection


class Watcher:
    # path of the directory to be watched
    DIRECTORY_TO_WATCH = os.environ['PATH_TO_SCAN']

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(
            event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()

        self.observer.join()


class Handler(FileSystemEventHandler):
    @staticmethod
    def on_any_event(event):
        if event.event_type == 'created':
            # Take any action here when a file is created.
            files_detection()

if __name__ == '__main__':
    w = Watcher()
    w.run()
