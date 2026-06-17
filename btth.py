from abc import ABC,abstractmethod
class Employee(ABC):
    def __init__(self,employee_id, name):
        self.employee_id = employee_id
        self.name = name
    def display_info(self):
        print(f"Mã NV:{self.employee_id} | Họ tên: {self.name:<12} | Loại:{type(self).__name__}")
    @abstractmethod
    def calculate_salary(self):
        pass
class FullTimeEmployee(Employee):
    def __init__(self,employee_id, name,salary,bonus):
        super().__init__(employee_id,name)
        self.salary = salary
        self.bonus = bonus
    def calculate_salary(self):
        return self.salary + self.bonus


class PartTimeEmployee(Employee):
    def __init__(self, employee_id, name, working_hours, hourly_rate):
        super().__init__(employee_id,name)
        self.working_hours = working_hours
        self.hourly_rate = hourly_rate
    def calculate_salary(self):
        return self.working_hours * self.hourly_rate


class InternEmployee(Employee):
    def __init__(self, employee_id, name, allowance):
        super().__init__(employee_id,name)
        self.allowance = allowance
    def calculate_salary(self):
        return self.allowance


def display_employees(employees):
    if not employees:
        print("Danh sách nhân viên trống")
        return
    else:
        for i in employees:
            i.display_info()

def display_salary(employees):
    print("--- BẢNG LƯƠNG NHÂN VIÊN ---")
    if not employees:
        print("Danh sách nhân viên trống")
        return
    else:
        for i in employees:
            salary = i.calculate_salary()
            print(f"Mã NV:{i.employee_id} | Họ tên:{i.name:<12} | Lương:{salary:,.0f} VND")

employees = [
    FullTimeEmployee("E001", "Nguyen Van A", 15000000, 3000000),
    PartTimeEmployee("E002", "Tran Thi B", 80, 50000),
    InternEmployee("E003", "Le Van C", 3000000)
]
def main():
    while True:
        print("""=== EMPLOYEE SALARY MANAGER ===
1. Xem danh sách nhân viên
2. Tính lương toàn bộ nhân viên
3. Thoát chương trình
================================""")
        try:
            choice = int(input("Chọn chức năng (1-3):"))
        except ValueError:
            print('Vui lòng nhập số')
            continue
        match choice:
            case 1:
                print("--- DANH SÁCH SINH VIÊN")
                display_employees(employees)
            case 2:
                display_salary(employees)
            case 3:
                print('Thoát chương trình')
                break
            case _:
                print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

if __name__ == "__main__":
    main()
