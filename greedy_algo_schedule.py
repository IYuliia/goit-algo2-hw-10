class Teacher:
    def __init__(self, first_name, last_name, age, email, can_teach_subjects):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = can_teach_subjects
        self.assigned_subjects = set()

    def assign_subject(self, subject):
        self.assigned_subjects.add(subject)

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.age} years, email: {self.email}"


def create_schedule(subjects, teachers):
    remaining_subjects = set(subjects)
    schedule = []

    while remaining_subjects:
        teachers_sorted = sorted(teachers, key=lambda t: (-len(t.can_teach_subjects & remaining_subjects), t.age))

        selected_teacher = None
        for teacher in teachers_sorted:
            can_cover_subjects = teacher.can_teach_subjects & remaining_subjects
            if can_cover_subjects:
                selected_teacher = teacher
                subject_to_assign = can_cover_subjects.pop()
                teacher.assign_subject(subject_to_assign)
                remaining_subjects.remove(subject_to_assign)
                if selected_teacher not in schedule:
                    schedule.append(selected_teacher)
                break
        
        if not selected_teacher:
            print("It is impossible to cover all subjects with the available teachers.")
            return None

    if remaining_subjects:
        print("It is impossible to cover all subjects with the available teachers.")
        return None

    return schedule


if __name__ == '__main__':
    subjects = {'Mathematics', 'Physics', 'Chemistry', 'Informatics', 'Biology'}

    teachers = [
        Teacher("Alexander", "Ivanenko", 45, "o.ivanenko@example.com", {'Mathematics', 'Physics'}),
        Teacher("Maria", "Petrenko", 38, "m.petrenko@example.com", {'Chemistry'}),
        Teacher("Sergey", "Kovalenko", 50, "s.kovalenko@example.com", {'Informatics', 'Mathematics'}),
        Teacher("Natalia", "Shevchenko", 29, "n.shevchenko@example.com", {'Biology', 'Chemistry'}),
        Teacher("Dmitro", "Bondarenko", 35, "d.bondarenko@example.com", {'Physics', 'Informatics'}),
        Teacher("Olena", "Hrytsenko", 42, "o.grytsenko@example.com", {'Biology'})
    ]

    schedule = create_schedule(subjects, teachers)

    if schedule:
        print("Schedule:")
        for teacher in schedule:
            print(f"{teacher.first_name} {teacher.last_name}, {teacher.age} years, email: {teacher.email}")
            print(f"   Teaches subjects: {', '.join(teacher.assigned_subjects)}\n")
    else:
        print("It is impossible to cover all subjects with the available teachers.")
