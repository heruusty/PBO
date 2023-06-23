import hr
import karyawan
import performansi

salary_employee = hr.GajiPegawai(1, "filla kurnia", 15000000)
hourly_employee = hr.PegawaiJam(2, "riskon kurnia", 40, 15)
commission_Employee = hr.KomisiPegawai(3, "heru ", 1000000, 25000)
payroll_system = hr.SistemPenggajian()
payroll_system.calculated_payroll(
    [salary_employee, hourly_employee, commission_Employee]
)

manager = karyawan.Manager(1, "kururi", 100000)
secretary = karyawan.Secretary(2, "absor", 5000000)
sales_guy = karyawan.SalesPerson(3, "bagus", 30000000, 25000)
factory_worker = karyawan.Factoryworker(2, "lutfi", 40, 15)
employees = [manager, secretary, sales_guy, factory_worker]
productivity_system = performansi.Performansi()
productivity_system.track(employees, 40)
payroll_system = hr.SistemPenggajian()
payroll_system.calculated_payroll(employees)
