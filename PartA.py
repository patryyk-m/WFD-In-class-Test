class Staff:
    def __init__(self, name, DoB, sex, staffID, address):
        self.name = name
        self.DoB = DoB
        self.sex = sex
        self.staffID = staffID
        self.address = address

    def print_details(self):
        print(f"Name: {self.name}")
        print(f"Date of Birth: {self.DoB}")
        print(f"Sex: {self.sex}")
        print(f"Staff ID: {self.staffID}")
        print(f"Address: {self.address}")

    def update_name(self, new_name):
        if isinstance(new_name, str):
            self.name = new_name
        else:
            print("Error: Name must be a string")

    def update_DoB(self, new_DoB):
        if isinstance(new_DoB, str):
            self.DoB = new_DoB
        else:
            print("Error: DoB must be a string")

    def update_sex(self, new_sex):
        if isinstance(new_sex, str):
            self.sex = new_sex
        else:
            print("Error: Sex must be a string")

    def update_staffID(self, new_staffID):
        if isinstance(new_staffID, str):
            self.staffID = new_staffID
        else:
            print("Error: StaffID must be a string")

    def update_address(self, new_address):
        if isinstance(new_address, str):
            self.address = new_address
        else:
            print("Error: Address must be a string")


class TeachingStaff(Staff):
    def __init__(self, name, DoB, sex, staffID, address, subject, level):
        super().__init__(name, DoB, sex, staffID, address)
        self.subject = subject
        self.level = level

    def print_details(self):
        super().print_details()
        print(f"Subject: {self.subject}")
        print(f"Level: {self.level}")

    def update_subject(self, new_subject):
        if isinstance(new_subject, str):
            self.subject = new_subject
        else:
            print("Error: Subject must be a string")

    def update_level(self, new_level):
        if isinstance(new_level, str):
            self.level = new_level
        else:
            print("Error: Level must be a string")


# Create instances and test functionality
# Staff instance
staff1 = Staff("John Smith", "01/01/1990", "M", "123", "123 Street")

# Print staff details
print("Staff Details:")
staff1.print_details()

# Update staff attributes
print("\nUpdating staff attributes:")
staff1.update_name("John Doe")
staff1.update_address("789 Street")
staff1.print_details()

# Teaching Staff instance
teacher1 = TeachingStaff("Jane Doe", "05/05/1985", "F", "456", "789 Road", "Maths", "Higher")

# Print teaching staff details
print("\nTeaching Staff Details:")
teacher1.print_details()

# Update teaching staff attributes
print("\nUpdating teaching staff attributes:")
teacher1.update_subject("Physics")
teacher1.update_level("Ordinary")
teacher1.print_details()
