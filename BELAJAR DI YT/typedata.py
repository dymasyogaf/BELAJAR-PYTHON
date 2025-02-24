# TYPE DATA
"""
integer -> list
float -> tuple
boolean -> set
string -> dictionary
"""

# Integer, type data integer adalah bilangan bulat
data = 8
print(type(data))

# Float, adalah bilangan desimal
data = 8.3
print(type(data))

# Boolean, adalah data biner / hanya memiliki 2 nilai
# Yaitu: True dan False
data1 = False
data2 = True
print(type(data1))
print(type(data2))

# Type data string adalah kumpulan karakter (" ") --> kutip
data3 = "spiderman"
data4 = "8"
data5 = "9.0"
data6 = "False"
print(type(data3),(data4), (data5), (data6))

# List adalah kumpulan element yg dapat di ubah
# Format : [element1, element2, dst]
data = ["spiderman", "ironman", "superman"]
print(type(data))

# Tuple adalah kumpulan element yg tidak dapat di ubah
# Format: (element1, element2, dst)
data = ("spiderman", "ironman", "superman")
print(type(data))

# Set adalah kumpulan element yg pasti unik dan tidak berurutan
data = {1, 4, 4, 4, 3, 4, 2}
print(data)
print(type(data))

# Dictionary adalah kumpulan pasangan Key-Value/Kunci-Nilai
# Format {key1:value1, key2:value2,dst}
data_dic = {"eat": "makan", "run": "berlari", "sad": "sedih"}

print(data_dic)
print(type(data_dic))

"""
integer = 8
float = 8.0
boolean = True 
string = spiderman
list = [1,2,3]
tuple = (1,2,3)
set = {1,2,3}
dictionary = {type1:1, type=2}
"""