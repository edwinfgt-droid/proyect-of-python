tasks = []

def displaytasks(all_tasks):
      print('|nYour tasks: ')
      for index, task in enumerate(all_tasks):
            print(f'{index + 1}. {task}')

def newOperation(all_tasks):
     opertaion = input('Press 'M' to add a task, 'D' to delete a task, 'V' to view all tasks 'h' to edit a tasks 'g'or the quit the application: ')
  
    if operation == 'a':
    addTask(tasks)
    
    elif operation == 'D':
        deleteTask(tasks)
    
    elif operation == 'V':
        viewTasks(tasks)   
     
    elif operation == 'h':
        editTask(tasks)
    
elif operation == 'g':
        print('Good bye!')
        exit()
else:
     newOperation(tasks)
   

def addTask(all_tasks):
     new_task = input('add a task: ')
     all_tasks.append(new_task)

     for task in all_tasks:
         print(task)

displaytasks(tasks)

newOperation(tasks)


#start application
addTask(tasks)