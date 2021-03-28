# stream-scribe

## Setup

Requires Python 3.

```
pip install keyboard
```

## Usage

Must be run as Adminstrator.

Mac example:

```
(env) macbook:stream-scribe danielsabsay$ sudo python main.py
Password:
Enter filename: stream_03_27_21.txt
Press [ENTER] to start (the timer will start immediately): 
Recording. Press Ctrl+C to stop...
00:00:07 - funny
 00:00:10 - funny
00:00:38 - funny
^CTraceback (most recent call last):
  File "main.py", line 33, in <module>
    keyboard.wait()
  File "/Users/danielsabsay/git/stream-scribe/env/lib/python3.8/site-packages/keyboard/__init__.py", line 886, in wait
    _time.sleep(1e6)
KeyboardInterrupt

(env) macbook:stream-scribe danielsabsay$
```

Contents of `stream_03_27_21.txt`:

```
00:00:07 - funny
00:00:10 - funny
00:00:38 - funny
```
