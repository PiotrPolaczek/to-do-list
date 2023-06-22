a = input("Give tasks to be done: ")
b = input("What do you want to do next: ")

while True:
    try:
        if b == "open task list":
            print(a)
        elif b == "delete":
            print("job deleted")
            b=input("Enter a new task")
        elif b == "done":
            print("Job done")
            b = input("Enter a new task")
        else:
            print("Unknown command")

        b = input("What do you want to do next: ")

    except Exception as e:
        print("An error occured:", e)