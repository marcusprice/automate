import time

forward: bool = False
left_pad: str = " " * 5
stars: str = "*****"

while True:
    print(left_pad + stars)
    time.sleep(.05)

    if forward:
        left_pad = left_pad + " "

        if len(left_pad) >= 5:
            forward = False
    else:
        left_pad = left_pad[0:-1]

        if len(left_pad) <= 0:
            forward = True
