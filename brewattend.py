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
            
