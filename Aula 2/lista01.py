a = int(input())
b = int(input())
c = int(input())
d = int(input())

pares = 0
impares = 0

if a % 2 == 0:
    pares += a
else:
    impares +=a

if b % 2 == 0:
    pares += b
else:
    impares +=b

if c % 2 == 0:
    pares += c
else:
    impares +=c

if d % 2 == 0:
    pares += d
else:
    impares +=d

print(f"numeros pares: ", pares)
print(f"numeros impares: ", impares)