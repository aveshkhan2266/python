listdata=[]

def register_student():
    studentdict={}
    studentdict["id"]=int(input("please enter your id: "))
    studentdict["name"]=input("please enter your name: ")
    studentdict["address"]=input("please enter your address: ")

    qualifications=[]

    morequalification="yes"

    while morequalification.lower()=="yes":
        qualification={}
        qualification["qualification_name"]=input("enter qualification: ")
        qualification["passing_year"]=input("enter qualification year: ")
        qualifications.append(qualification)

        morequalification=input("add more qualification (yes/no): ")

    studentdict["qualification"]=qualifications

    listdata.append(studentdict)

    print("student registered successfully")

    return listdata

    