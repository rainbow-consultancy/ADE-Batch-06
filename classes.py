# class

# casing 
# 1. camel casing -> goodMorningSandeepReddy
# 2. pascal casing -> GoodMorningSandeepReddy
# 3. snake casing -> good_morning_sandeep_reddy

class ClassName:
    pass


class Students:
    pass

Rahul = Students()
Ganga = Students()



class Students:
    def get_student(self, name, age):
        return f"Student Name - {name} and age - {age}"


# rahul_object = Students()
# print(rahul_object.get_student("Rahul", 17))

# ganga_obj = Students()
# print(ganga_obj.get_student("Ganga", 16))


# constructor

class Students:
    def __init__(self, name, age):
        print("Intialized Constructor Method")
        self.name = name
        self.age = age

    def get_student(self):
        return f"Student Name - {self.name} and age - {self.age}" 
    
    def get_name(self):
        return f"Student Name - {self.name}"
    
    # to be implemented later point of time
    def get_grade(self):
        pass
    
    
# rahul_object = Students("Rahul", 17)
# print(rahul_object.get_student())
# print(rahul_object.get_name())

# ganga_obj = Students("Ganga", 16)
# print(ganga_obj.get_student())

# Types of Variables

# 1. public variable
# 2. private variable
# 3. global variable

class Employee:
    company_name = "QuantCloud" # Public Variable
    
    global building_name    # Global Variable
    building_name = "RT Square"
    
    __trainer_name = "Sandeep"  # Private Variable
    
    def get_private(self):
        return self.__trainer_name
    
    def get_company(self):
        return f"Company Name - {self.company_name}"


obj_ins = Employee()

print(obj_ins.company_name)
print(obj_ins.get_company())

print(building_name)
# print(company_name)

# print(obj_ins.__trainer_name)

print(obj_ins.get_private())
    

