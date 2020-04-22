# Define a Python class named Student. This class will have 5 properties.
# First name (string)
# Last name (string)
# Age (integer)
# Cohort number (integer)
# Full name (read-only string)
# Define getters for all properties.
# Define a setter for all but the read only property.
# Ensure that only the appropriate value can be assigned to each.
# The full name property should return first name and last name separated
# by a space. It's value cannot be set.


class Student():

    @property # The getter
    def first_name(self):
        try:
            return self.__first_name # Note there are 2 underscores here
        except AttributeError:
            return print("not a string")

    @first_name.setter # The setter
    def first_name(self, new_first_name):
        if type(new_first_name) is str:
            self.__first_name = new_first_name
        else:
            raise TypeError('Please enter a string')


    @property 
    def last_name(self):
        try:
            return self.__last_name
        except AttributeError:
            return print("not a string")

    @last_name.setter 
    def last_name(self, new_last_name):
        if type(new_last_name) is str:
            self.__last_name = new_last_name
        else:
            raise TypeError('Please enter a string')


    @property 
    def age(self):
        try:
            return self.__age
        except AttributeError:
            return print("not a number")

    @age.setter
    def age(self, new_age):
        if type(new_age) is int:
            self.__age = new_age
        else:
            raise TypeError('Please enter a number')



    @property 
    def cohort_number(self):
        try:
            return self.__cohort_number
        except AttributeError:
            return print("not a number")

    @cohort_number.setter 
    def cohort_number(self, new_cohort_number):
        if type(new_cohort_number) is int:
            self.__cohort_number = new_cohort_number
        else:
            raise TypeError('Please enter a number')

    @property
    def full_name(self):
        try:
            return f'{self.first_name} {self.last_name}'
        except AttributeError:
            return 0


castle = Student()
castle.first_name = "castle"
castle.last_name = "crawford"
castle.age = 28
castle.cohort_number= 38


print(castle.first_name)
print(castle.last_name)
print(castle.age)
print(castle.cohort_number)
print(castle.full_name)



        


