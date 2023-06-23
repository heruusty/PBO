class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class SalaryEmployee(Employee):
    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary


class hourlyEmployee(Employee):
    def __init__(self, id, name, hours_worked, hour_rate):
        super().__init__(id, name)
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate

    def calculated_payroll(self):
        return self.hours_worked + self.hour_rate


class CommissionEmployee(Employee):
    def __init__(self, id, name, weekly_salary, commission):
        super().__init__(id, name, weekly_salary)
        self.commision = commission

        def calculated_payroll(self):
            fixed = super().calculated_payroll()
            return fixed + self.commission


class Manager(SalaryEmployee):
    def work(self, hours):
        print(f"{self.name} Menghabiskan {hours} hours.")


class Secretary(SalaryEmployee):
    def work(self, hours):
        print(f"{self.name} Menghabiskan {hours} hours.")


class SalesPerson(CommissionEmployee):
    def work(self, hours):
        print(f"{self.name} Menghabiskan {hours} hours.")


class Factoryworker(hourlyEmployee):
    def work(self, hours):
        print(f"{self.name} Menghabiskan {hours} hours.")
