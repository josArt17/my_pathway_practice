grade = input('Cual es tu promedio? ');
grade = int(grade)
if grade >= 90:
    final_letter = 'A'
elif grade >= 80:
    final_letter = 'B'
elif grade >= 70:
    final_letter = 'C'
elif grade >= 60:
    final_letter = 'D'
else:
    final_letter = 'F'

letter = final_letter


if letter == "A" or letter == "B" or letter == "C":
    mensaje = "Haz pasado este curso, felicidades"
else:
    mensaje = "No haz pasado este curso, te invito a volver a intentarlo la proxima vez"

if (grade % 10) >= 7 and letter != "A" and letter != "F":
    simbolo = "+"
elif (grade % 10) <3 and letter != "F":
    simbolo = "-"
else:
    simbolo = ""
print(f"Tu calificacion es: {letter}{simbolo}")
print(mensaje)
