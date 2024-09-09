while True:

    try:
        veri = input("Herhangi bir şey gir\n")
        if type(int(veri)) == type(1):
            print("Bu bir integer")
    except ValueError:
        try:
            if type(float(veri)) == type(1.0):
                print("Bu bir float")
        except ValueError:
                print("Bu bir string")