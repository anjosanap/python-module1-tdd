nota1 = float(input("Nota1: "))

nota2 = float(input('Nota 2: '))

nota3 = float(input('Nota 3: '))

nota4 = float(input('Nota 4: '))

media = (float(nota1) + float(nota2) + float(nota3) + float(nota4))/4
print (media)

if media > 7:
   print("Você está aprovado")

elif 7 >= media >= 5.5:
  print("Você está de recuperação!")

else:
  print("Você foi reprovado!")