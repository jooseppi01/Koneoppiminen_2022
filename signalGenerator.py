import teht3
from teht3 import signalAnalyser as SA

aika = int (input("Anna aika 1-10: "))
taajuus = int(input("Anna taajuus 0-500: "))
print("aika:", aika)
print("taajuus:", taajuus)


obj = SA(100, aika)
obj.create(taajuus)
obj.plot(0, 100)