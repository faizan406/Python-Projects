def task():
    tasks = []
    print("_____Welcome to TASK MANAGEMENT______")
    
    total_task = int(input("Enter total task you want to add: "))
    for i in range(1, total_task + 1):
        task_name = input(f"Enter task {i}: ").strip()
        tasks.append(task_name)
        
    print(f"\nToday's Tasks:\n{tasks}\n") 
    
    while True:
        operation = int(input("Enter\n1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/Stop\nYour choice: "))
        
        if operation == 1:
            add = input("Enter task you want to add: ").strip()
            tasks.append(add)
            print(f"Task '{add}' has been successfully added...\n")
        
        elif operation == 2:
            update_val = input("Enter the task name you want to update: ").strip()
            if update_val in tasks:
                up = input("Enter new task: ").strip()
                ind = tasks.index(update_val)
                tasks[ind] = up
                print(f"Updated Task to '{up}'\n")
            else:
                print("Task not found!\n")
        
        elif operation == 3:
            del_val = input("Which task you want to delete: ").strip()
            if del_val in tasks:
                tasks.remove(del_val)
                print(f"Task '{del_val}' has been deleted successfully...\n")
            else:
                print("Task not found!\n")
        
        elif operation == 4:
            print(f"Current Tasks:\n{tasks}\n")
        
        elif operation == 5:
            print("Closing the program...")
            break
        
        else:
            print("Invalid input!\n")
            
task()
