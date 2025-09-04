m=float(input("Podaj masę ciała (w kg): "))
h=float(input("Podaj wzrost (w m): "))

BMI=m/(h*h)

if BMI<18.5:
    w="Niedowaga"
elif BMI<25:
    w="Waga prawidłowa"
elif BMI<30:
    w="Nadwaga"
else:
    w="Otyłość"

print(f"BMI = {BMI:.2f}\n{w}.")