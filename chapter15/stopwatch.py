#! python3
# stopwatch.py -- A simple stopwatch program.

import time


# Display the program's instructions.
print("Press ENTER to begin. Afterwards, press ENTER to 'click' the stopwatch."
      " Press Ctrl-C to quit.")
input()  # Press Enter to begin.
print("Started.")
START_TIME = time.time()  # Get the first lap's start time.
LAST_TIME = START_TIME
LAP_NUM = 1

# Start tracking the lap times.
try:

    while True:

        input()
        LAP_TIME = round(time.time() - LAST_TIME, 2)
        TOTAL_TIME = round(time.time() - START_TIME, 2)
        print("Lap #%s: %s (%s)" % (LAP_NUM, TOTAL_TIME, LAP_TIME), end="")
        LAP_NUM += 1
        LAST_TIME = time.time()  # Reset the last lap time.

except KeyboardInterrupt:

    # Handle the Ctrl-C exception to keep its error message from displaying.
    print("\nDone.")
