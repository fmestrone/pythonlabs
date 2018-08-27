counter = 0
prevValue = -1
curValue = 1

while counter <= 20:
    counter += 1
    nextValue = prevValue + curValue
    print(counter, ": ", nextValue)
    prevValue = curValue
    curValue = nextValue

