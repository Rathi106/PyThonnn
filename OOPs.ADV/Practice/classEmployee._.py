class Employee:
    def __init__(self, salary=106, increment=20):
        self.salary = salary
        self._increment = increment   # actual storage, different name from the property

    @property
    def increment(self):
        return self._increment

    @increment.setter
    def increment(self, new_salary):
        # interpreting: setting m.increment = 280 means "my new salary is 280,
        # back-calculate what % increment that represents"
        self._increment = ((new_salary / self.salary) - 1) * 100

    @property
    def salary_after_increment(self):
        return self.salary + self.salary * (self.increment / 100)


m = Employee()
print(m.increment)                 # 20
m.increment = 280                  # triggers the setter
print(m.increment)                 # recalculated %
print(m.salary_after_increment)    # uses the getter