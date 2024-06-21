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

