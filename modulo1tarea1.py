import random
elementos = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
tamaño = int(input("Elige la cantidad de caracteres que tiene la contraseña"))
contraseña = ""
for i in range(tamaño):
    letra = random.choice(elementos)
    contraseña += letra

print(contraseña)
