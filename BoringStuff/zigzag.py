import sys
import time

indent = 0  # How many spaces to indent.
indentIncreasing = True  # Whether the indentation is increasing or not.
try:
    for i in range(1000):  # The main program loop.
        print(" " * indent, end="")
        print("********")
        time.sleep(0.001)  # Pause for 1/10 of a second.
        if indentIncreasing:
            # Increase the number of spaces:
            indent = indent + 1
            if indent == 20:
                # Change direction:
                indentIncreasing = False
        else:
            # Decrease the number of spaces:
            indent = indent - 1
            if indent == 0:
                # Change direction:
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()
