lower = int(input("Batas Bawah : "))
upper = int(input("Batas Atas : "))

if lower < 0 or upper < 0 :
    print("Batas bawah dan atas yang dimasukan tidak boleh di bawah Nol")
else :
    sum = 0
    for i in range (lower, upper) :
        if i % 2 == 1 :
            print(i)
            sum += i
    print("Total : ", sum)