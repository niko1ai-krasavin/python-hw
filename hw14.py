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
    employee_id = None
    employee_name = "Unknown"

    def __init__(self):
        pass

    def set_id(self, empl_id):
        self.employee_id = empl_id

    def set_name(self, empl_name):
        self.employee_name = empl_name

    def get_id_and_name(self):
        print("It is " + self.employee_name + " with id=" + str(self.employee_id))


mary_employee = Employee()
mary_employee.set_id(1)
mary_employee.set_name("Mary")

with open('mary_obj_pickle', 'wb') as output_file:
    pickle.dump(mary_employee, output_file)

with open('mary_obj_pickle', 'rb') as input_file:
    new_mary_employee = pickle.load(input_file)

new_mary_employee.get_id_and_name()
