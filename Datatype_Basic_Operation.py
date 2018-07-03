"""To Practice Basic Operation"""
#==========Numbers==============#
a = 2
salary = 120034.24

# streaming_bit_octal = 0o12
# streaming_bit_hex = 0x12
#
# print (a, type(a))
# print (salary, type(salary))
# print (streaming_bit_octal, type(streaming_bit_octal))
# print (streaming_bit_hex, type(streaming_bit_hex))

#=========Strings=====================#
message = 'Hello World'
message2 = "Hello World"

print (message == message2)

# Multi-line String
message3 = """Hello
            this is multi-line string.
            used for documenting functions,modules, classes
            methods"""
print (message3)

message4 = "Hello this is single line string, " \
           "and it should not more than 120 " \
           "characters in same line"
print (message4)

#===============List & Tuple ==================#
list1 = [1, 20.2, "Python", [1, 3, 4]]
tuple1 = (1, 20.2, "Python", [1, 3, 4])
print (list1)
print (tuple1)
print (type(tuple1))

# Use ',' if single data in tuple
a, b = 1,2
print (a)
print (b)
print (type(a))

# ========= Dict & Set  & Frozenset ==========#
employee_id_data = {"xyz": 1,
                    "mn" : 2,
                    "ll" : 5
                    }
print (employee_id_data)
print(type(employee_id_data))

unique_employee_set ={1,2,3,3,5.6,1}
print(unique_employee_set)
print(type(unique_employee_set))

set_with_empty = {}
print(set_with_empty)
print(type(set_with_empty))

employee_data = frozenset (employee_id_data)
print(employee_data)
print (type(employee_data))