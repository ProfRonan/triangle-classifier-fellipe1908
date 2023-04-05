print("Digie os tem angulos do triangulo: ")
a =int( input("DIgite o primeiro angulo: "))
b =int( input("DIgite o segundo angulo: "))
c =int( input("DIgite o terceiro angulo: "))
if  a == b and a == c and c == b:
    print("Equilátero")
elif a == b or b == c or a == c:
    print("Isósceles")
else:
    print("Escaleno")
