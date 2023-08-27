# Initialize an empty to-do list
taskList = []

# Function to add task in to do list. 
def addTask():
    task = input("Enter the task: ")
    taskList.append(task)
    print(f"Task '{task}' added to the list.")
    
# Function to remove task from to do list.
def removeTask():
    if taskList:
            try:
                index = int(input("Enter task's no. to remove: ")) - 1
                if 0 <= index < len(taskList):
                    removedTask = taskList.pop(index)
                    print(f"Task '{removedTask}' removed from the list.")
                else:
                    print("Invalid task.")
            except ValueError:
                print("Invalid input. Enter a valid task's no.")

# Function to display the current to-do list
def displayList():
    if taskList:
        print("Your list:")
        for i in range(len(taskList)):
            print(f"{i+1}. {taskList[i]}")
    else:
        print("Your list is empty.")
        
# Function to show choice from user.
def options():
    print("\nOptions:")
    print("1. Add task")
    print("2. Remove task")
    print("3. View tasks")
    print("4. Quit")

# Main loop for interacting with the to-do list
while True:
    options()
    choice = input("Enter your choice: ")
    print("---------------------")
    
    match choice:
        case '1':
            addTask()
        case '2':
            displayList()
            removeTask()
        case '3':
            displayList()
        case '4':
            exit("Thanks for using 'To-Do List' Application.")
        case _:
            print("Invalid choice. Please select a valid option.")