import os
import subprocess
import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class CodeChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory:
            return
        if event.src_path.endswith('.py') and os.path.abspath(event.src_path) == os.path.abspath(sys.argv[0]):
            print(f'File {event.src_path} has been modified. Executing...')
            try:
                output = subprocess.check_output(['python', event.src_path], stderr=subprocess.STDOUT, universal_newlines=True)
                print(output)
            except subprocess.CalledProcessError as e:
                print(f'Error occurred: {e.output}')

if __name__ == "__main__":
    print('hisdf')
    path = os.path.abspath(os.path.dirname(sys.argv[0]))
    event_handler = CodeChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()
    print('hi')
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
