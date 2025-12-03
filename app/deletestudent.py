import registerstudent

def delete_student():
    delete = int(input("Enter student id to delete : "))

    for item in registerstudent.listdata:
        if item["id"] == delete:
            registerstudent.listdata.remove(item)
            print("Student Deleted Successfully ")
            return registerstudent.listdata
        
    print("Student Not Found ")
    return registerstudent.listdata