def confirm_up(anysting):
    d={"upper":0, "lower":0}
    for leta in anysting:
        if leta.isupper():
            d["upper"]+=1
        elif leta.islower():
            d["lower"]+=1
        else:
            pass
    print("Original Chracters: ", anysting)
    print("Number of Capital characters : ", d["upper"])
    print("Number of lower characters : ", d["lower"])