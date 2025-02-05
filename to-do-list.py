class todo_list:
    def __init__(self):
        self.task_list = []

    def add_task(self, task):
        self.task_list.append(task)

    def display_tasks(self):
        for i, item in enumerate(self.task_list, start = 1):
            print(f"{i}. {item}") 

    def mark_task(self, index):
        self.task_list[index - 1] = str(self.task_list[index - 1] + " (Completed)")
    
    def remove_task(self, index):
        self.task_list.pop(index - 1)

    def clear_all_task(self):
        self.task_list.clear()

if __name__ == '__main__':
    tasklist = todo_list()
    while True:
        print("Good Day!\n\n1. Add Task\n2. Display Task\n3. Mark Task as Done\n4. Remove Task\n5. Clear all tasks\n6. Exit Program\n")
        try:
           reply = int(input("Reply : "))
        except: print("Invalid Reply! Enter reply from 0 to 6")
            
        if reply in (1,2,3,4,5,6):
            if reply == 1:
                task_to_add = str(input("Enter task to add: "))
                tasklist.add_task(task_to_add)
        
            elif reply == 2:
                if tasklist == []:
                    print("No task to show!")
                else:
                    tasklist.display_tasks()
        
            elif reply == 3:
                index = int(input("Enter Task to mark as completed: "))
                tasklist.mark_task(index)
                print("Task is marked as completed")
        
            elif reply == 4:
                index = int(input("Enter Task to remove: "))
                tasklist.remove_task(index)
                print("Task removed successfully")
        
            elif reply == 5:
                tasklist.clear_all_task()
                print("All tasks cleared succesfully.")

            elif reply == 6:
                print("Exitting Program. Good Bye!")
                break
        else: print("Invalid Reply! Enter reply from 0 to 6")