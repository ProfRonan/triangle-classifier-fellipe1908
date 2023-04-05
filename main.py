print("Digie os tem angulos do triangulo: ")
a =int( input("DIgite o primeiro angulo: "))
b =int( input("DIgite o segundo angulo: "))
c =int( input("DIgite o terceiro angulo: "))
r = int(a + b +c)
if a < 1 and b < 1 and c < 1:
    if r == 180 :
        if  a == b and a == c and c == b:
            print("Equilátero")
        elif a == b or b == c or a == c:
            print("Isósceles")
        else:
            print("Escaleno")
    else:
        print("Não é um triângulo")
else:
    print("Não é um triângulo")
