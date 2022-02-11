from cs50 import get_float
change_owed = get_float("Change owed: ")
while change_owed < 0:
    change_owed = get_float("Change owed: ")

quarters = 0.25
dimes = 0.10
nickels = 0.05
pennies = 0.01
count = 0
a = change_owed // quarters
b = round(change_owed % quarters, 2) // dimes
c = round(round(change_owed % quarters, 2) % dimes, 2) // nickels
d = round(round(round(change_owed % quarters, 2) % dimes, 2) % nickels, 2) // pennies


if a > 0:
    count += a

if b > 0:
    count += b

if c > 0:
    count += c

if d > 0:
    count += d

print(int(count))