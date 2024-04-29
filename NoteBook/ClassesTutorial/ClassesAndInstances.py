
#Classes allow us to logically group data and functions in a way that's easy to reuse and build upon.

# Methods are functions that are associated with a class.

class Employee:
    # Instance variables are unique for each instance. Class variables need to be the same for each instance.
    # raise_amount is a class variable.
    # To access this class variable, we need to either access them through the class itself
    # or through an instance of the class
    raise_amount = 1.04
    num_of_emps = 0
    def __init__(self, first, last, pay):
        # When we create methods within a class, they receive the instance as the first argument automatically.
        # Call the instance "self" by convention.
        self.first = first
        self.last = last
        self.pay = pay

        Employee.num_of_emps += 1 # Will instantiate every time a new employee is created.

    #The init stores information.
    #To use that information, we need methods.
    def fullname(self):
        #Remember that whatever in the brackets is the argument. In this case, the only argument necessary is the init.
        #Init is always passed automatically, hence why we need the 'self' so that the method knows what is being passed.
        return '{} {}'.format(self.first, self.last)


    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) # Employee.raise_amount would work too (accessing through class)

    @classmethod #This decorator alters the functionality of the method.
        #The class is received as the first argument, instead of the instance.
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    #Static methods work like a normal function. They are included in the class structure because they have
    #some relevance to the class, but they do not access the instance or the class.
    #Static method below:

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    def __repr__(self):
        return "Employee('{}','{}','{}')".format(self.first, self.last, self.pay)
        #return a string that can be used to re-create the object.
        #this code will return the same code that was used to create the instance in the first place

    def __str__(self):
        return'{} {}'.format(self.fullname(), self.email)

        # @property allows use to define a method like an attribute.
    @property
    def email(self):
        return ('{}.{}@email.com'.format(self.first, self.last))
    # Now when accessing the email, even though it is a method, you access it like an attribute.




emp_1 = Employee('Corey', 'Smith', 10000)
emp_2 = Employee('Jim', 'Smith', 10200)

Employee.set_raise_amount(1.06)

print(emp_1.fullname()) # Need parentheses, because this is a method instead of an attribute.

emp_1.fullname() # The self argument is automatically passed into the fullname method.
Employee.fullname(emp_1) # By calling the method on the class, the code doesn't know which instance we want.
# Hence, emp_1 (i.e. the instance) needs to be specified

emp_1.raise_amount = 1.05 # We can modify class variables for one single instance. See output below.

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print(Employee.num_of_emps)


# Inheritance
class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, programming_language):
        super().__init__(first,last,pay) #Passes first,last,pay to employee init method and let that class handle those argument.
        # Employee.__init__(self,first,last,pay) also works
        self.programming_language = programming_language

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())

dev_1 = Developer("Brandon", "Isaac", 200000, "French")
dev_2 = Developer("Novak", "Nike", 13021, "Java")
dev_1.apply_raise()
print(dev_1.email)
print(dev_1.programming_language)

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

mgr_1.add_emp(dev_2)
mgr_1.print_emps()

print(isinstance(mgr_1,Developer))

