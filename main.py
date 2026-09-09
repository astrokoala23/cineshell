import argparse
import os
import sys
import time
import cv2
import numpy as np

# Dense ASCII gradient ordered by luminance
RAMP = np.array(list(" .:-=+*#%@"), dtype="U1")

def cineshell(filepath):
    cap = cv2.VideoCapture(filepath)
    if not cap.isOpened():
        print("ERROR: Could not open video!")
        return

    fps = cap.get(cv2.CAP_PROP_FPS)
    if not fps or fps <= 0:
        fps = 30
    frame_space = 1.0 / fps

    # Terminal sizing
    term_cols, term_lines = os.get_terminal_size()
    # Reserve 1 line to avoid terminal auto-scrolling
    target_lines = max(1, term_lines - 1)
    target_size = (term_cols, int(target_lines))

    # Clear screen initially and hide cursor
    sys.stdout.write("\x1b[2J\x1b[?25l")
    sys.stdout.flush()

    try:
        while True:
            t_start = time.perf_counter()
            suc, frame = cap.read()
            if not suc:
                break

            # Downsample frame
            resized = cv2.resize(frame, target_size, interpolation=cv2.INTER_NEAREST)
            
            # Convert to grayscale in OpenCV C++ layer
            gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

            # Map 0-255 luminance to ramp indices (0-9) via NumPy vectorization
            indices = (gray.astype(np.uint16) * len(RAMP)) // 256
            ascii_matrix = RAMP[indices]

            # Create frame string
            rows = ["".join(row) for row in ascii_matrix]
            frame_str = "\x1b[H" + "\n".join(rows)

            # Print frame
            sys.stdout.write(frame_str)
            sys.stdout.flush()

            # Keep constant FPS (rather than what the terminal feels like)
            elapsed = time.perf_counter() - t_start
            sleep_time = frame_space - elapsed
            if sleep_time > 0:
                time.sleep(sleep_time)

    finally:
        cap.release()
        sys.stdout.write("\x1b[?25h\x1b[0m\n")
        sys.stdout.flush()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Display a video in the terminal.")
    parser.add_argument("-fp", "--filepath", type=str, help="Path to video file", required=True, dest="filepath")
    args = parser.parse_args()

    cineshell(args.filepath)