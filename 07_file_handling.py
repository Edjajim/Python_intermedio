### Manejo de ficheros ###

import os

# .txt file

txt_file = open("my_file.txt", "w+") # r+ = Leer y escribir   w+ = sobreescribir
txt_file.write("Mi nombre es Eduardo\nMi apellido es Jara\nMi lenguaje preferido es Python\nTengo 18 Años")
#print(txt_file.read())
#print(txt_file.read(10)) #Lectura de un límite de caracteres
#print(txt_file.readline()) #Lectura línea a línea
#print(txt_file.readline())
for line in txt_file.readlines():
    print(line)

txt_file.write("\nMe gusta jugar volleybol")
print(txt_file.readline())

txt_file.close()

with open("my_file.txt", "a") as my_other_file:
    my_other_file.write("\nSwift")

#os.remove("my_file.txt")

# .json file
import json

json.dump

json_file = open("my_file.json", "w+")

json_test = {
    "name":"Eduardo",
    "surname":"Jara",
    "age":18,
    "language":"Python",
    "school":"ITO"
}

json.dump(json_test, json_file, indent=4)

json_file.close()

with open("my_file.json") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

json_dict = json.load(open("my_file.json"))
print(json_dict)
print(json_dict["name"])

# .csv file

import csv

csv_file = open("my_file.csv", "w+")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name", "surname", "age", "language", "school"])
csv_writer.writerow(["Eduardo", "Jara", 18, "Python", "ITO"])
csv_writer.writerow(["Avi", "", 0, "Python", ""])

csv_file.close()

with open("my_file.csv") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

# .xlsx file

#import xlrd Necesita instalación

# .xml file

import xml