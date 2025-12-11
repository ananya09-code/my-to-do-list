task={}
def menu():
   print("_ _  _ _ _ _ _welcome to the app_ _ _ _ _  _  _")
   print("read and select one of the opesions")
   print("1.Add a new task")
   print("2.Remove a task")
   print("3.Update/edit a task ")
   print("4.Mark a task as completed ")
   print("5.Show only completed tasks")
   print("6.Show only pending tasks ")
   print("7.to exit")
   print("_ _ _ _ _ _ _ _ _ __ _ _ _ _ _ _ _ _ _ _ _ _ _ ")

  
def add_task():
     new_task=input("enter your new task: ")
     status=input("enter the progress of task(done,not done,in progress): ")
     task[new_task]=status
     print(print(f"task {new_task} with status-{status} has been added!"))


def remove_task():
    if not task:
        print("there is no tasks yet!")
    else:
       task_remove=input("enter the task to remove: ")
       if task_remove in task:
           task.pop(task_remove)
           print(f"task name-{task_remove} has been removed!")
       else:
           print(f"task with name-{task_remove} not found!")
           

    
while True:
   menu()
   choice=int(input("enter your choice: ").strip())
   if choice==7:
      print("exiting.....")
      break
   elif choice==1:
       add_task()
       print(task)
   elif choice==2:
       remove_task()
       print(task)
   
    
  
   