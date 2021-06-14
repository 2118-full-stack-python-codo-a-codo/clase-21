import datetime

def reverse(myString):
    elements = longitud - 1

    revString = ""

    for index in range(elements,0,-1):
        revString  =  revString + myString[index]

    return revString

myString = input("Ingrese una cadena de texto")

longitud = len(myString)

print(myString[2:5])
print(longitud)
print(reverse(myString))

isPython = ("python" in myString) # chequeo que la palabra python este en myString

print(isPython)

print("El texto tiene estas vocales: ", myString.count("a") + myString.count("e") + myString.count("i") + myString.count("o") + myString.count("u"))

myTemplate = "<label> Hola Mundo desde PLACEHOLDER</label>"

print(myTemplate.replace("PLACEHOLDER", "Python"))

myNewTemplate = myTemplate.replace("PLACEHOLDER", "Python")

print(myNewTemplate.center(len(myNewTemplate) * 2 , "*"))

myInput = input("Ingrese el numero de mes")

if myInput.isnumeric():
    myNumber = int(myInput)

name = 'Fred'
age = 50
anniversary = datetime.date(1991, 10, 12)
myFNotationString = f'My name is {name}, my age next year is {age+1}, my anniversary is {anniversary:%A, %B %d, %Y}.'

print(myFNotationString)

#tupla

myTupla = "Alejandro", 21231313, datetime.date(1991, 10, 12)

print(myTupla)

nombre, dni, birthday  = myTupla
print(nombre)
print(dni)
print(birthday)

print(set(myTupla))