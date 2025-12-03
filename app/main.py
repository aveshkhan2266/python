import registerstudent
import searchstudent
import deletestudent


while True:
        print("Student Menu ")
        print("1. Register Student")
        print("2. Search Student")
        print("3. Delete Student")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            data=registerstudent.register_student()       
        elif choice == "2":
            result=searchstudent.search_student()          
        elif choice == "3":
            data=deletestudent.delete_student()          
        elif choice == "4":
            print("Program Exit")
            break
        else:
            print("Invalid Choice")
