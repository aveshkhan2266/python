import registerstudent

def search_student():
    delete = int(input("Enter student id to search: "))

    for item in registerstudent.listdata:
        if item["id"] == delete:
            print("Student Found:")
            for key, value in item.items():
                print(f"{key} = {value}")
            return item
        
    print("Student Not Found")