score = input("Enter Score: ")
sc = float(score)
if sc >1.0 :
    print("Error, please enter the score in between 0 and 1.0")
if sc >= 0.9:
    print("A")
elif sc >= 0.8:
    print("B")
elif sc >= 0.7:
    print("C")
elif sc >= 0.6:
    print("D")
elif sc < 0.6:
    print("F")
