import os
from datetime import datetime
import time

AUDIO_FOLDER = r"../sample_audio"

def data_input():
    previous_cycle = {}   # [modified time, size] according to last scan
    while True: 
        for entry in os.scandir(AUDIO_FOLDER):
            if entry.is_file():
                info = entry.stat()
                current = (info.st_mtime, info.st_size)
                if entry.name in previous_cycle and previous_cycle[entry.name] != current:
                    print(f"EDITED: {entry.name}")
                previous_cycle[entry.name] = current
        time.sleep(3)

def main():

    data_input()

if __name__ == "__main__":
    main()

