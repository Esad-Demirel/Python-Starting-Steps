print("Dikkat! Bu program sadece 3 veya 4 kenarlı çokgenleri hesaplayabilir.")
def geometri(sekil):

    if len(sekil) == 3:
        a = sekil[0]
        b = sekil[1]
        c = sekil[2]

        if a+b > c and a+c > b and b+c > a:

            if a == b and b == c:
                print("Bu bir eşkenar üçgen")
            elif a == b or b == c or a == c:
                print("Bu bir ikizkenar üçgen")
            else:
                print("Bu bir çeşitkenar üçgen")

        else:
            print("Bu uzunluklar ile üçgen oluşturulamaz")

    elif len(sekil) == 4:
        a = sekil[0]
        b = sekil[1]
        c = sekil[2]
        d = sekil[3]

        if a+b+c > d and a+b+d > c and a+c+d > b and b+c+d > a:

            if a == b and b == c and c == d:

                aci_ab = int(input("a ve b kenarının oluşturduğu açıyı giriniz:"))

                if aci_ab == 90:
                    print("Bu bir kare")
                else:
                    print("Bu bir eşkenar dörtgen")

            elif a == c and b == d:

                aci_ab = int(input("a ve b kenarının oluşturduğu açıyı giriniz:"))

                if aci_ab == 90:
                    print("Bu bir dikdörtgen")
                else:
                    print("Bu bir paralelkenar")

            else:
                print("Bu sıradan bir dörtgen")

        else:
            print("Bu uzunluklar ile dörtgen oluşturulamaz.")


while True:
    eleman_sayisi = int(input("Hesaplanacak çokgenin kenar sayısını giriniz:"))

    if eleman_sayisi == 3:
        a = int(input("a kenarının uzunluğunu giriniz:"))
        b = int(input("b kenarının uzunluğunu giriniz:"))
        c = int(input("c kenarının uzunluğunu giriniz:"))
        geometri([a,b,c])

    elif eleman_sayisi == 4:
        a = int(input("a kenarının uzunluğunu giriniz:"))
        b = int(input("b kenarının uzunluğunu giriniz:"))
        c = int(input("c kenarının uzunluğunu giriniz:"))
        d = int(input("d kenarının uzunluğunu giriniz:"))
        geometri([a,b,c,d])

    elif eleman_sayisi < 3:
        print("Bir çokgen oluşturulabilmesi için en az 3 uzunluk gerekmektedir. Lütfen tekrar deneyiniz.")

    else:
        print("Bu program sadece 3 ve 4 kenarlı çokgenleri hesaplayabilir. Lütfen tekrar deneyiniz.")
