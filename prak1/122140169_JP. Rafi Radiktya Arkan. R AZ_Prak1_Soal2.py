jariJari = int(input("jari-jari : "))
pi = 3.14

if jariJari < 0 :
    print("jari-jari lingkaran tidak boleh negatif")
else :
    luas = pi * jariJari ** 2
    keliling = 2 * pi * jariJari

    print("Luas : ", luas)
    print("Keliling : ", keliling)