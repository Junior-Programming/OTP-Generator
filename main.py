import random as r

# Function untuk OTP Generator


def otpgen():
    otp = ""
    for i in range(4):
        otp += str(r.randint(1, 9))
    print("Kode OTP kamu adalah :")
    print(otp)


otpgen()
