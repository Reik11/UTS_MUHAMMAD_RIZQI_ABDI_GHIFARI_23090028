import bmi_calculator

def main():
    berat_badan = float(input("Masukkan berat badan (kg): "))
    tinggi_badan = float(input("Masukkan tinggi badan (m): "))

    bmi = bmi_calculator.hitung_bmi(berat_badan, tinggi_badan)
    kategori = bmi_calculator.kategori_bmi(bmi)

    print("BMI Kamu:", round(bmi, 2))
    print("Kategori BMI:", kategori)

if __name__ == "__main__":
    main()