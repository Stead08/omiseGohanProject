import csv

with open("NaturalLpractiveData.csv") as f:
    reader = csv.reader(f)
    list_1 = [row for row in reader]

#asari
from asari.api import Sonar
sonar = Sonar()
for i in list_1:
    res = sonar.ping(i[0])
    print(res)
