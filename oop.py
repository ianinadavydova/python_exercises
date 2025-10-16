class Student:
    def __init__(self,
                 last_name="unknown",
                 first_name="unknown",
                 patronymic="unknown",
                 age=0,
                 gender="unknown",
                 faculty="unknown",
                 course=1,
                 specialty="unknown",
                 group="unknown",
                 expelled=False):

        self.last_name = last_name
        self.first_name = first_name
        self.patronymic = patronymic
        self.age = age
        self.gender = gender
        self.faculty = faculty
        self.course = course
        self.specialty = specialty
        self.group = group
        self.expelled = expelled

    def change_faculty(self, new_faculty):
        self.faculty = new_faculty

    def raise_course(self):
        self.course += 1

    def change_course(self, new_course):
        if new_course < 1:
            raise ValueError("Course must be greater than 0")
        self.course = new_course

    def change_specialty(self, new_specialty):
        self.specialty = new_specialty

    def change_group(self, new_group):
        self.group = new_group

    def change_status(self, expelled):
        self.expelled = expelled

    def info_text(self):
        status = "expelled" if self.expelled else "studying"
        return (
            f"ФИО: {self.last_name} {self.first_name} {self.patronymic}\n"
            f"Age: {self.age}, Gender: {self.gender}\n"
            f"Faculty: {self.faculty}\n"
            f"Course: {self.course}, Speciality: {self.specialty}\n"
            f"Group: {self.group}\n"
            f"Status: {status}"
        )

    def print_info(self):
        print(self.info_text())


def main():
    group = [
        Student("Potter", "Harry", "Potterovic", 17, "male", "Science", 1, "Programming", "group1", False),
        Student("Smith", "John", "Johnovich", 16, "male", "Science", 1, "Programming", "group1", False),
        Student("Petrova", "Jana", "Petrovna", 77, "female", "Economy", 3, "Business", "group2", False),
        Student("Super", "Peter", "Super puper", 22, "male", "Rocket science", 4, "Space engineering", "group3", False),
        Student(last_name="Haha", first_name=50, patronymic="Vasilevich", age=20, gender="male", faculty="Programming", course=4, specialty="Python" , group="group3", expelled=False)
    ]

    print("students info:")
    for i in range(len(group)):
        print(f"\nStudent {i + 1}:")
        group[i].print_info()

    print("\nfirst student:")
    s = group[0]

    print("\nbefore:")
    s.print_info()


    s.change_faculty("Economy")
    s.raise_course()
    s.change_course(3)
    s.change_specialty("Business")
    s.change_group("group3")
    s.change_status(True)

    print("\nafter:")
    s.print_info()


if __name__ == "__main__":
    main()
