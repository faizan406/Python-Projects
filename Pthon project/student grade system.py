student_grades={}

#add student
def add_student(name,grade):
    student_grades[name]=grade
    
#updated
def update_student(name,grade):
    if name in student_grades:
        student_grades[name]=grade
        print(f"{name} with marks are updated {grade}")
        
    else:
        print(f"{name} is not found")
        
#deleted

def delete_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"{name} is successfuly deleted")
    else:
        print(f"{name} is not found")
        
#view
def display_all_student():
    if student_grades:
     for name,grade in student_grades.items():
        print(f"{name} : {grade}")
    else:
        print("No student found/added")
        
def main():
    while True:
        print("\nStudent Grade Management system")
        print("1-Add Student")
        print("2-Updated Student")
        print("3-Delete Student")
        print("4-view Student")
        print("5-Exit Student")
        
        choice=int(input("Enter Your Choice = "))
        if choice==1:
            name=input("Enter student name = ")
            grade=int(input("Enter student grade = "))
            add_student(name,grade)
            
        elif choice==2:
             name=input("Enter student name = ")
             grade=int(input("Enter student grade = "))
             update_student(name,grade)
             
        elif choice==3:
            name=input("Enter student name = ")
            delete_student(name)
        
        elif choice==4:
            display_all_student()
            
        elif choice==5:
            break
        
        else:
            print("Invlaid Enter again ")

main()
        