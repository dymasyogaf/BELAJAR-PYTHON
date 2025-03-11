"""
# Jenis Casting
Integer int() ->-- List list()
float float() ->-- Tuple tuple()
Boolean bool() ->-- Set set()
string str() ->-- Dictionary dict()
"""

# To Integer
# Float --> Integer
# Boolean --> Integer
data = 9.9
data_int = int(data) #Ini integernya

print(data, type(data))
print(data_int)

# To Float
data = False
data_float = float(data) #Ini Float nya

print(data, type(data))
print(data_float)

# To Boolean
# Float/int -->

#String, list, set, tuple, dict ---> boolean
data = {"Nama": "Dymas", "Kelas": "XII Mipa"}
data_convert = bool(data) #Ini integernya

print(data, type(data))
print(data_convert, type(data_convert))

# String
# All Type --> String
data = ["marvel", "Dc"]
data_convert = str(data)

print(data, type(data))
print(data_convert, type(data_convert))
print(data, data_convert)

# To list
# String, tuple, set --> list
data = ["spiderman", "batman"]
data_convert = list(data)

print(data, type(data))
print(data_convert, type(data_convert))
print(data, data_convert)



