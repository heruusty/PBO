class SistemPenggajian:
    def calculated_payroll(self, employee):
        print("perhitungan gaji")
        print("================")
        for employee in employee:
            print(f"Gaji untuk: {employee.id} - {employee.name}")
            print(f"- check jumlah: {employee.calculated_payroll()}")
            print("")


class Pegawai:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class GajiPegawai(Pegawai):
    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)
        self.weekly_salary = weekly_salary

    def calculated_payroll(self):
        return self.weekly_salary


class PegawaiJam(Pegawai):
    def __init__(self, id, name, hours_worked, hour_rate):
        super().__init__(id, name)
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate

    def calculated_payroll(self):
        return self.hours_worked * self.hour_rate


class KomisiPegawai(GajiPegawai):
    def __init__(self, id, name, weekly_salary, commission):
        super().__init__(id, name, weekly_salary)
        self.commission = commission

    def calculated_payroll(self):
        fixed = super().calculated_payroll()
        return fixed + self.commission
