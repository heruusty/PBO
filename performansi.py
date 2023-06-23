class Performansi:
    def track(self, employee, hours):
        print("Tracking Emplyee Productivity")
        for employee in employee:
            employee.works(hours)
            print("")
