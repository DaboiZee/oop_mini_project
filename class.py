class patient():
    rooms=[101,102,103,104]
    def __init__(self,name,age,heart_rate,room):
        self.name=name
        self.age=age
        self.heart_rate=heart_rate
        if room in patient.rooms:
            self.room=room
            patient.rooms.remove(room)
        else:
            raise AttributeError("invalid room ")
    def show_info(self):
        print(f"name:{self.name}\nAge: {self.age}")
        print(f"Heart Rate: {self.heart_rate}\nRoom: {self.room}")
    def update_heart_rate(self,new_heart_rate):
        if 30<=new_heart_rate<=250:
            self.heart_rate=new_heart_rate
        else:
            print("invalid heart rate")
    def change_rooms(self, new_room):
        if new_room==self.room:
            print(f"room is already occopied by {self.name}")
        elif new_room in patient.rooms:
            patient.rooms.append(self.room)
            patient.rooms.remove(new_room)
            self.room=new_room
        else:
            print("room is unavailable at the moment")
class staff():
    def __init__(self,name,employee_id):
        self.name=name
        self.employee_id=employee_id
    def status(self):
        print(f"{self.name} works at the hospital")
class doctor(staff):
    def __init__(self,name,employee_id,specalty):
        staff.__init__(self, name, employee_id) 
        self.specalty=specalty
    def status(self):
        print(f"dr.{self.name} is examining patient")
class nurse(staff):       
    def __init__(self,name,employee_id,department):
        staff.__init__(self, name, employee_id) 
        self.department=department
    def status(self):
        print(f"nurse {self.name} is chekcing on patient")
class receptionist(staff):
    def status(self):
        print(f"{self.name} is addmiting patients")
class technician(staff):
    def status(self):
        print(f"{self.name} is prepairing medical equipment for patients operation")
sara=patient("sara", 21, 65, 101)
doctor_hannah=doctor("hannah", 10340,"cardiology")
nurse_jack=nurse("jack", 20547, "emergency")
receptionist_billy=receptionist("billy", 30895)
technician_chris=technician("chris", 40975)
sara.change_rooms(104)
sara.update_heart_rate(75)
sara.show_info()
employees=[receptionist_billy,doctor_hannah,nurse_jack,technician_chris]
for employee in employees:
    employee.status()       