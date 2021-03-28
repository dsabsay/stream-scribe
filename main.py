from datetime import datetime
import os
import sys
import time

import keyboard


global start_time

def log(filename, note):
    global start_time
    d = int((datetime.now() - start_time).total_seconds())
    hours, remainder = d // 3600, d % 3600
    minutes, seconds = remainder // 60, remainder % 60
    with open(filename, 'a') as f:
        f.write(f'{hours:02}:{minutes:02}:{seconds:02} - {note}\n')
    print(f'{hours:02}:{minutes:02}:{seconds:02} - {note}')


if __name__ == '__main__':
    filename = input('Enter filename: ')
    if os.path.isfile(filename):
        print('File already exists. Exiting.')
        sys.exit(1)

    input('Press [ENTER] to start (the timer will start immediately): ')
    global start_time
    start_time = datetime.now()
    print('Recording. Press Ctrl+C to stop...')

    keyboard.add_hotkey('space', log, args=[filename, 'funny'])
    keyboard.wait()
