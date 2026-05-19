def to_do_list():
    task = []

    while True:
        print("1.Add a task")
        print("2.Remove task")
        print("3.view task")
        print("4.exit")
        choice = int(input("enter your choice"))

        if choice == "1":
            task = input("enter the task")
            task.append(task)
        elif choice == "2":
            task = input("enter the task to remove") 
            if task in task:
                task.remove(task)
            else:
                print("task not found")
        elif choice == "3":
            print("task: ")
            for task in tasks:
                print("-_" + task)
        elif choice == "4":
            break
        else:
            print("invalid choice")

to_do_list()                                       
