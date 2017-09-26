# # commentaarlijn
# # variabelenaam x wordt 3
# #python return is einde van een statement
# x = -3
# a = 3.0
# b = "3"
# y = 5
# x = y
# print(type(x))
# print(type(a))
# print(type(b))
#
#
#
#
# naam = input("Geef uw naam : ")
#
# #print("Hoi" + naam + "!")  #slechte manier plakt 3 strings aan elkaar
#
# #format => 1 string formateren
# print("Hoi {0} !!!".format(naam))
#
# #iets tussen quotes
# print("Hoi \"iets tussen quotes\" {0} !!!".format(naam))

# print("naam : {0} voornaam : {1}".format(naam,voornaam))
#
# # print("eerste lijn nu  \teen tab \ntweede lijn")
#
# # om de opp van een driehoek te berekenen
# #de variabele met naam basis wordt het resultaat van de functie input
# #basis = input("geef de basis") basis is van het type string => can't multiply
# #met float() kan je een string of int omzetten naar een type float
# # basis = float(input("geef de basis van een driehoek : "))
# # hoogte = input("geef de hoogte : ")
# # hoogte = float(hoogte)
# # oppervlakte = basis * hoogte /2
# # print("De oppervlakte van de driehoek is {0}".format(oppervlakte))
#
#
# n = input("geef een getal n : ")
# n = int(n)
# nn = n*n
# nnn = n*n*n
# som = n + nn + nnn
# print("de som is {0}".format(som))
import  sys
import math

dec = 12
octaal = 0o73
hexa = 0xAA
binair = 0b000111

print("{0:x}".format(octaal))
print (octaal)
print(hexa)
print(binair)

print(input.__doc__)

print(sys.version)
import  calendar

print(calendar.month(1973,1,3))

print("sdflkj")

print("button")