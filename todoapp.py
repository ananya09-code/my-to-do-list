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

   elif choice==3:
      if task is None:
        print("no task yet!")
      else:
        to_update=input("enter the task name to update: ")
        for i,to_update in enumerate(task):
          new_task=input("enter your new task: ")
          task[i]=new_task
          print(f"{to_update} has been updated with {new_task} !")
   elif choice==4:
       if not task:
         print("no task yet!")
       else:
         for item in task:
           print(item)      
   else:
     print("incorrect choice try again!")





        

  


