#Lab06-4 (Bowling)

total = 0
frame = 1

while frame <= 10:
    remaining = 10
    print("Frame # {:d}" .format(frame))
    pin = int(input("  Number of pins down: "))
    remaining -= pin
    total += pin
    if remaining > 0:
        print("Frame # {:d}" .format(frame))
        pin = int(input("  Number of pins down (0-{:d}): ". format(remaining)))
        remaining -= pin
        total += pin
    frame += 1

print("Total score is {:d}" .format(total))