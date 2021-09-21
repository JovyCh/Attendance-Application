def login():
    login_file = open("Login_details.txt", "r")
    list_name = []
    list_password = []
    print("Module Record System\n"
          "-------------------")
    username = input("Name:")
    password = input("Password:")
    for login_details in login_file:
        login_details = login_details.rstrip().split(", ")
        list_name.append(login_details[0])
        list_password.append(login_details[1])
    if username in list_name:
        i = list_name.index(username)
        if password == list_password[i]:
            print(f"Welcome {username}")
            return username
    login_file.close()


def menu():
    while True:
        print("Module Record System - Options\n"
              "--------------------------------\n"
              "1. Record Attendance\n"
              "2. Generate Statistics\n"
              "3. Exit")
        selection = input(">\t")
        break
    return selection


def list_module(selection):
    list_module_name = []
    list_module_code = []
    connection = open("modules.txt", "r")
    while True:
        if selection == 1:
            for modules_data in connection:
                modules_data = modules_data.rstrip()
                line_info = modules_data.split(",")
                list_module_code.append(line_info[0])
                list_module_name.append(line_info[1])
            print(f"Module Record System(Attendance) - Choose Module\n"
                  "-----------------------------------------------")
            for i, module in enumerate(list_module_code):
                i = i + 1
                print(i, module, "-", list_module_name[i - 1])
            break
        elif selection == 2:
            for modules_data in connection:
                modules_data = modules_data.rstrip()
                line_info = modules_data.split(",")
                list_module_code.append(line_info[0])
                list_module_name.append(line_info[1])
            print(f"Module Record System(Statistics) - Choose Module\n"
                  "-----------------------------------------------")
            for i, module in enumerate(list_module_code):
                i = i + 1
                print(i, module, "-", list_module_name[i - 1])
            break
        else:
            print("Please retry and enter a valid module number.")
            break
    module_selection = int(input(">\t"))
    return module_selection


def attendance(file):
    student_name = []
    student_present_days = []
    student_absent_days_no_excuse = []
    student_absent_days_excuse = []
    attendance_file = open(file, "r")
    for student_data in attendance_file:
        student_data = student_data.rstrip()
        line_info = student_data.split(",")
        student_name.append(line_info[0])
        student_present_days.append(int(line_info[1]))
        student_absent_days_no_excuse.append(int(line_info[2]))
        student_absent_days_excuse.append(int(line_info[3]))
    return student_name, student_present_days, student_absent_days_no_excuse, student_absent_days_excuse


def attendance_taking(name, student_present, absent, excused, attendance_file):
    new_student_attendance = []
    override_file = open(attendance_file, "w")
    for i, student in enumerate(name):
        i = i + 1
        no_student = len(name)
        print(f"There are {no_student} enrolled in this module.\n"
              f"Student #", i, ";", student, "\n"
              "1. Present\n"
              "2. Absent\n"
              "3. Excused")
        add_attendance = int(input(">\t"))
        if add_attendance == 1:
            line = f"{name[i - 1]}, {student_present[i - 1] + 1}, {absent[i - 1]}, {excused[i - 1]}"
            new_student_attendance.append(line)
        elif add_attendance == 2:
            line = f"{name[i - 1]}, {student_present[i - 1]}, {absent[i - 1] + 1}, {excused[i - 1]}"
            new_student_attendance.append(line)
        elif add_attendance == 3:
            line = f"{name[i - 1]}, {student_present[i - 1]}, {absent[i - 1]}, {excused[i - 1] + 1}"
            new_student_attendance.append(line)
        else:
            print("Please retry and enter a valid number.")
    count = 0
    for n in new_student_attendance:
        if count == 0:
            override_file.write(n)
            count = count + 1
        elif count == 1:
            override_file.write(f"\n{n}")

    override_file.close()


def stats(name, present, absent, excused, module_file):
    total_enrolled = len(name)
    low_attenders = []
    non_attenders = []
    best_attenders = []
    no_classes = present[1] + excused[1] + absent[1]
    avg_attendance = sum(absent) + sum(present) + sum(excused)
    bestest_attender = max(present)
    lowest_attender = min(present)
    lowest_percentage = round((lowest_attender / no_classes) * 100) + 1
    print(f"Module: {module_file}\n"
          f"Number of students: {total_enrolled}\n"
          f"Number of Classes: {no_classes}\n"
          f"Average Attendance: {avg_attendance}")
    for i in present:
        if i < (no_classes * .7):
            lowest_name = present.index(i)
            low_name = name[lowest_name]
            low_attenders.append(low_name)
        if i == 0:
            nones_name = present.index(i)
            non_name = name[nones_name]
            non_attenders.append(non_name)
        if i == bestest_attender:
            bestest_name = present.index(i)
            best_name = name[bestest_name]
            best_attenders.append(best_name)
    print(f"Low Attender(s): under 70 %")
    for i in low_attenders:
        print(i)
    print(f"Non Attender(s):")
    for i in non_attenders:
        print(f"\t{i}")
    print(f"Best Attender(s):\n"      
          f"\tAttended {bestest_attender}/{no_classes} days")
    for i in best_attenders:
        print(f"\t{i}")


def main():
    module_file1 = "SOFT_6017.txt"
    module_file2 = "SOFT_6018.txt"
    username = login()
    if username is not None:
        while True:
            selection = menu()
            if selection == "1":
                selection_modules = list_module(1)
                if selection_modules == 1:
                    attendance(module_file1)
                    name, present, absent, excused = attendance(module_file1)
                    attendance_taking(name, present, absent, excused, module_file1)
                elif selection_modules == 2:
                    attendance(module_file2)
                    name, present, absent, excused = attendance(module_file2)
                    attendance_taking(name, present, absent, excused, module_file2)
                else:
                    print("Please enter a valid number.")
            elif selection == "2":
                stats_modules = list_module(2)
                if stats_modules == 1:
                    attendance(module_file1)
                    name, present, absent, excused = attendance(module_file1)
                    stats(name, present, absent, excused, module_file1)
                elif stats_modules == 2:
                    attendance(module_file2)
                    name, present, absent, excused = attendance(module_file2)
                    stats(name, present, absent, excused, module_file2)
                else:
                    print("Please retry.")
            elif selection == "3":
                print("Have a nice day!")
                break
            else:
                print("Please enter a valid number and retry.")
    else:
        print("Login failed")


main()