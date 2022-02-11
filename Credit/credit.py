from cs50 import get_int

# luhm's algorithm
def luhm_algorithm(credit_card):
    a = credit_card
    b = a[-2::-2]
    e = a[-1::-2]
    c = ""
    for i in b:
        ans = int(i) * 2
        c += str(ans)
    d = 0
    for i in c:
        d += int(i)
    f = 0
    for i in e:
        f += int(i)
    return d + f
    

# input credit card number
credit_card = str(get_int("Number: "))

# check the valid length of the card and confirm the card type
if len(credit_card) in [13, 15, 16]:
    ans = luhm_algorithm(credit_card) % 10
    if ans == 0:
        # check if the number is either AMEX, MASTERCARD OR VISA
        if len(credit_card) == 15 and (credit_card[0:2] in ["34", "37"]):
            print("AMEX")

        if len(credit_card) == 16 and (credit_card[0:2] in ["51", "52", "53", "54", "55"]):
            print("MASTERCARD")

        if (len(credit_card) == 13 or 16) and (credit_card[0] in ["4"]):
            print("VISA")
    else:
        print("INVALID")
else:
    print("INVALID")