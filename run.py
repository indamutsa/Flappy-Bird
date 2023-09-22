# from watchdog.observers import Observer
# from watchdog.events import FileSystemEventHandler
# import time
# import os

# class Watcher:
#     DIRECTORY_TO_WATCH = "."

#     def __init__(self):
#         self.observer = Observer()

#     def run(self):
#         event_handler = Handler()
#         self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
#         self.observer.start()

#         try:
#             while True:
#                 time.sleep(5)
#         except KeyboardInterrupt:
#             self.observer.stop()
#             self.observer.join()

# class Handler(FileSystemEventHandler):

#     @staticmethod
#     def process(event):
#         os.system("python main.py")

#     def on_modified(self, event):
#         self.process(event)

# if __name__ == "__main__":
#     w = Watcher()
#     w.run()
