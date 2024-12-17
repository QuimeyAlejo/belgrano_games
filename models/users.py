from datetime import datetime

class Account:
    def __init__(self, nickname, name, lastname, email, password, birthdate):
        self.nickname = nickname    
        self.name = name
        self.lastname = lastname   
        self.email = email
        self.password = password
        self.birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
            
    def show_info(self):
        return f"Nickname: {self.nickname}, Name: {self.name} {self.lastname}, Email: {self.email}, Birthdate: {self.birthdate.date()}"   
    

class User(Account):
    def __init__(self, nickname, name, lastname, email, password, birthdate, level):
        super().__init__(nickname, name, lastname, email, password, birthdate)
        self.level = level
        
    def show_user(self):
        info_base = super().show_info()  
        return f"{info_base}, Level: {self.level}"    
    
    
class Admin(Account):
    def __init__(self, nickname, name, lastname, email, password, birthdate, permissions):
        super().__init__(nickname, name, lastname, email, password, birthdate)
        self.permissions = permissions
        
    def show_admin(self):
        info_base = super().show_info()  
        return f"{info_base}, Permissions: {', '.join(self.permissions)}"        
