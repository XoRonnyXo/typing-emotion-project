"""
Keystroke Data Collector (local)
- Records key press & release durations and inter-key delays.
- Requires: pip install pynput
- Output: events_<timestamp>.csv

IMPORTANT: For ethics/privacy, do NOT log the actual text by default. Only record key names.
"""

import time, csv, os
from datetime import datetime
from pynput import keyboard

OUT_DIR = "keystroke_events"
os.makedirs(OUT_DIR, exist_ok=True)

press_times = {}
last_event_time = None
session_id = f"S{int(time.time())}"
user_id = "U01"
text_domain = "free_text"  # or email, coding, chat, etc.

out_path = os.path.join(OUT_DIR, f"events_{session_id}.csv")
fields = [
    "user_id","session_id","utc_timestamp_iso","key","press_duration_ms",
    "inter_key_delay_ms","is_error_backspace","word_len_context","text_domain"
]

def on_press(key):
    global press_times
    press_times[key] = time.time()

def on_release(key):
    global press_times, last_event_time
    t = time.time()
    key_str = str(key)
    press_t = press_times.pop(key, t)
    duration_ms = (t - press_t) * 1000.0
    delay_ms = (t - last_event_time) * 1000.0 if last_event_time else 0.0
    last_event_time = t

    is_backspace = 1 if key == keyboard.Key.backspace else 0
    word_len_context = 0  # placeholder

    with open(out_path, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if f.tell() == 0:
            w.writerow(fields)
        w.writerow([
            user_id, session_id, datetime.utcnow().isoformat(), key_str,
            round(duration_ms,3), round(delay_ms,3), is_backspace, word_len_context, text_domain
        ])

    if key == keyboard.Key.esc:
        return False

if __name__ == "__main__":
    print("Recording... Press ESC to stop.")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
    print("Saved:", out_path)
