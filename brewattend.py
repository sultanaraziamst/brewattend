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
                
