import os
clear = lambda: os.system('cls')

tasks=[]

class Record:
    def __init__(self, task):
        self.task=task

def draw():
    print("====TODO====")
    ind=1
    for i in tasks:
        display=str(ind)+") "+str(i.task)
        print(display)
        ind+=1
    print("====MENU====")
    print("1) Create a new task")
    print("2) Delete a task")
    print("3) Alter a task")

while True:
    clear()
    draw()
    
    while True:
        try:
            act=int(input("ACTION: "))
            break
        except ValueError:
            print('Enter a number. Try again.')
    if act==1: #CREATE
        task=input("Describe the task: ")
        if task!='':
            tasks.append(Record(task))
        else:
            print("Wrong value, You can't enter an empty task!")
            input("Press enter to continue")
    elif act==2: #DELETE
        while True:
            try:
                ind=int(input("Delete? Which one?: "))
                break
            except ValueError:
                print('Enter a number. Try again.')

        if 1 <= ind <= len(tasks):
            rem=tasks[ind-1]
            del rem
            tasks.pop(ind-1)
        else:
            print("Wrong value, Value is out of range")
            input("Press enter to continue")
    elif act==3: #ALTER
        while True:
            try:
                ind=int(input("Alter? Which one?: "))
                break
            except ValueError:
                print('Enter a number. Try again.')
        if 1 <= ind <= len(tasks):
            newtask=input("Describe the task: ")
            if task!='':
                tasks[ind-1].task=newtask
            else:
                print("Wrong value, You can't enter an empty task!")
                input("Press enter to continue")
        else:
            print("Wrong value, Value is out of range")
            input("Press enter to continue")
    else: #DEFAULT
        print("Wrong value, enter a value 1-3")
        input("Press enter to continue")
