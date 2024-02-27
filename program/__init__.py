def mulai():
    print("==========================================")
    print("============= Kalkulator BMI =============")
    print("==========================================")
    while True:
        pilihan = input("Mulai Program (y/n) ? : ")
        pilihan = pilihan.lower()
        print("==========================================")
        if pilihan == "y":
            tinggi_badan = int(input("Masukan Tinggi Badan anda (Cm) : "))
            berat_badan = int(input("Masukan Berat Badan anda (Kg) : "))
            print("==========================================")
            tinggi_badan = tinggi_badan / 100
            hitung_bmi = berat_badan / tinggi_badan ** 2
            hitung_bmi = round(hitung_bmi, 1)

            if hitung_bmi < 18.5:
                print(f"Index BMI : {hitung_bmi}, Kurang Berat Badan")
            elif hitung_bmi >= 18.5 and hitung_bmi <= 22.9:
                print(f"Index BMI : {hitung_bmi}, Normal")
            elif hitung_bmi >= 23 and hitung_bmi <= 24.9:
                print(f"Index BMI : {hitung_bmi}, Kelebihan Berat Badan")
            elif hitung_bmi >= 25 and hitung_bmi <= 29.9:
                print(f"Index BMI : {hitung_bmi}, Obesitas Tingkat 1")
            else:
                print(f"Index BMI : {hitung_bmi}, Obesitas Tingkat 2")
            print("==========================================")
        elif pilihan == 'n':
            print("Program Berhenti")
            break
        else:
            print("Jawaban Invalid")


if __name__ == 'main':
    mulai()
