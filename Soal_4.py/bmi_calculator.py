def hitung_bmi(berat_badan, tinggi_badan):
    bmi = berat_badan / tinggi_badan ** 2
    return bmi

def kategori_bmi(bmi):
    if bmi < 18.5:
        return "Berat Kamu badan kurang"
    elif 18.5 <= bmi < 24.9:
        return "Berat Kamu badan normal"
    elif 25 <= bmi < 29.9:
        return "Kamu Kelebihan berat badan"
    else:
        return "Kamu Obesitas"
