print("System managemnet system")
while True:
    print("Enter\n 1 to add Student \n 2 to view student data \n 3 to search student data\n 4 to exit from system")

    num=input("Enter your choice")
    if num=="1":
        name=input(("Enter Student name:"))
        rollnum=input("enter roll number:")
        marks=int(input("enter marks:"))
        if marks>=90:
           grade="Outstanding"
        elif marks>=80:
           grade="Excellent"
        elif marks>=70:
           grade="Very good"
        elif marks>=60:
           grade="Good"
        else:
           print("Satisfactory")

           
        with open("student.txt","a") as file:
         file.write(f"{name},{rollnum},{marks},{grade}\n")
    elif num=="2":
       with open("student.txt","r") as record:
          print (record.read())
    elif num=="3":
       with open("student.txt","r") as search:
          searchbyrollnumber=input("Enter roll number of student to view data:")
          for line in search:
             if searchbyrollnumber in line:
                print(f"Student record of rollnumber,{searchbyrollnumber}")
                print(line)
                break
             else:
                print("student record not found of rollnumber:",searchbyrollnumber)
    elif num=="4":
       print("Thankyou  for using system")
       break
    elif num=="5":
       alert=("are you sure ypu want to clear all data?(y/n)")
       if alert.lower()=="y":
          with open("student.txt","w") as clear:
             clear.write()
             print("successfully cleared all data!")



       
    else:
       print("invalid choice,please enter valid options")


             


          


                   
        