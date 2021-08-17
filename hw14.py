#!/usr/bin/python3


# =========   (+) and (-) of module "pickle"   =========
#
# + It is the serialization of objects of different types into a binary stream (or file)
#
# - Binary data cannot be read by humans.
#   If you don't trust a resource, then you shouldn't read data from that resource.
#   You may not be able to read data from the file.
#   Data could be serialized with a specific version and a specific protocol.
#   You need to know how the object was serialized.
#


# The file 'mary_obj_pickle' will be created in your directory
import pickle


class Employee:

    def __init__(self, employee_id, employee_name):
        self.__employee_id = employee_id
        self.__employee_name = employee_name

    @property
    def employee_id(self):
        return self.__employee_id

    @employee_id.setter
    def employee_id(self, employee_id):
        self.__employee_id = employee_id

    @property
    def employee_name(self):
        return self.__employee_name

    @employee_name.setter
    def employee_name(self, employee_name):
        self.__employee_name = employee_name

    def __str__(self):
        return "It is '" + self.__employee_name + "' with 'id' = " + str(self.__employee_id)


mary_employee = Employee(1, "Mary")

with open('mary_obj_pickle', 'wb') as output_file:
    pickle.dump(mary_employee, output_file)

with open('mary_obj_pickle', 'rb') as input_file:
    new_mary_employee = pickle.load(input_file)

print(new_mary_employee)
