task=[]
while True:
   print("_ _  _ _ _ _ _welcome to the app_ _ _ _ _  _  _")
   print("read and select one of the opesions")
   print("1.add a task")
   print("2.remove a task")
   print("3.update a task")
   print("4.show all tasks")
   print("5. to exit")
   print("_ _ _ _ _ _ _ _ _ __ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
  
   choice=int(input("enter your choice: "))
   if choice==5:
     print("exiting...")
     break
   elif choice==1:
     in_task=input("enter your new task: ")
     task.append(in_task)
     print(f'{in_task} has been add!')

   elif choice==2:
     if not task:
      print("no tasks yet!")
     else:
      to_remove=input("enter the task name to remove:")
      if to_remove in task:
        task.remove(to_remove)
        print(f"{to_remove} has been removed!")
      else:
        print(f'{to_remove} not found in the task list!')

   elif choice==3:
      to_update = input("Enter the task name to update: ")
      if to_update in task:
       new_task = input("Enter your new task: ")
       index = task.index(to_update)
       task[index] = new_task
       print(f"{to_update} has been updated with {new_task}!")
      else:
        print(f"{to_update} not found in the task list!")

   elif choice==4:
       if not task:
         print("no task yet!")
       else:
         for item in task:
           print(item)      
   else:
     print("incorrect choice try again!")





        

  


