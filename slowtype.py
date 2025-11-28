import sys, time
def slowtype(str, speed):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(speed)
    print("\n")