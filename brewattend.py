from datetime import datetime

class CoffeeShopAttendanceTracker:

    def __init__(self):
        self.employees = {}

    def add_employees(self, employee_id, employee_name):
        if employee_id not in self.employees:
            