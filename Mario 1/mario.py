from cs50 import get_int
Height = get_int("Height: ")
while Height not in range(1,9):
    Height = get_int("Height: ")

space = Height -1
sharp = 1

for i in range(Height):
    Sp = space - i
    Sh = sharp + i
    space_string = " "*Sp
    sharp_string = "#"*Sh
    print(space_string + sharp_string)