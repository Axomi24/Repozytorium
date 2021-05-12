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
    act=input("ACTION: ")
    if act=='1':
        task=input("Describe the task: ")
        tasks.append(Record(task))
    elif act=='2':
        ind=int(input("Which one?: "))
        rem=tasks[ind-1]
        del rem
        tasks.pop(ind-1)



