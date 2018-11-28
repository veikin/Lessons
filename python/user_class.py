class User():
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        print("Name: " + self.first_name.title() + ".")
        print("Last name: " + self.last_name.title() + ".")
        print("Age: " + self.age + ".")

    def greet_user(self):
        print("Hello, " + self.first_name.title() + " " 
                + self.last_name.title() + "!")

    def print_login_attempts(self):
        print("Login: " + str(self.login_attempts) + ".")

    def incremet_login_attempts(self, add_login):
        self.login_attempts += add_login

    def reset_login_attempts(self):
        self.login_attempts = 0

class Privileges():
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print("Privileges: " + self.privileges)

class Admin(User):
    def __init__(self, first_name, last_name, age, privileges):
        super().__init__(first_name, last_name, age)
        self.privileges = Privileges(privileges)

admin = Admin('sergei', 'Pushkin', '24', 'superadmin')
admin.greet_user()
admin.privileges.show_privileges()
