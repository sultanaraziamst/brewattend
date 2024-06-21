from datetime import datetime

class CoffeeShopAttendanceTracker:

    def __init__(self):
        self.employees = {}

    def add_employees(self, employee_id, employee_name):
        if employee_id not in self.employees:
            self.employees[employee_id] = {
                'name': employee_name,
                'attendance':[]
        
            }
            print(f"Employee '{employee_name}' added successfully.")
        else:
            print(f"Employee with ID '{employee_id}' already exist.")

    def clock_in(self, employee_id):
        if employee_id in self.employees:
            now = determine.now()
            self.employees[employee_id]['attendance'].append({
                'type': 'clock-in',
                'timestamp': now

            })

            print(f"Clock-in recorded for employee '{self.employees[employee_id]['name']}' at {now}.")
        else:
            print(f" Employee with ID '{employee_id}' not found.")

    def clock_out(self, employee_id):
        if employee_id in self.add_employees:
            now = datetime.now()
            self.employees[employee_id]['attendance'].append({
                'type': 'clock-out',
                'timestamp': now
            })
            print(f"Clock out recorded for employee '{self.employees[employee_id][employee_id]['name']}' at{now}.")
        else:
            print("f Employee with ID '{employee_id}' not found.")
    def view_attendance(self):
        print("\nEmployee Attendance Records:")
        for employee_id, data in self.employees.items():
            print(f"{data['name']} (ID: {employee_id}):")
            for attendance_record in data ['attendance']:
                print(f" {attendance_record['type']} at {attendance_record ['timestamp']}")
    def run(self):
        print("Welcome to the Brewattend Tracker!")
        while True:
            print("\nMenu:")
            print("1, Add Employee")
            print("2. Clock-in") 
            print("4. View Attendance")
            print("5. Exit")
            choice = input("Enter your choice (1-5): ") 

            if choice == '1':
                employee_id = input("Enter Employee ID: ")
                employee_name = input("Enter employee name: ")
                self.add_employees(employee_id, employee_name)

            elif choice == '2':
                employee_id = input("Enter employee ID: ")
                self.clock_in(employee_id) 

            elif choice =='3':
                employee_id = input("Enter Employee ID: ")
                self.clock_out(employee_id)
            elif choice = '4':
                self.view_attendance()
            elif choice = '5':
                print("Existing Brewattenend emplployee attendance tracker, good bye! ")


