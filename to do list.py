import tkinter
import tkinter.messagebox
import pickle

root= tkinter.Tk()
root.title("To Do List by @NISHI")

#functions for buttons
def add_task():
    task =entry_task.get()
    if task!="":
        listbox_tasks.insert(tkinter.END,task)
        entry_task.delete(0,tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Waring!", message="you must enter a message")

def delete_task():
    try:
        task_index=listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title="Waring!", message="you must select the task")


def load_task():
    try:
        tasks=pickle.load(open("tasks.dat","rb"))
        listbox_tasks.delete(0,tkinter.END)
        for task in tasks:
            listbox_tasks.insert(tkinter.END,task)
    except:
        tkinter.messagebox.showwarning(title="Waring!", message="Can't find tasks.dat")

def save_task():
    try:
        tasks=listbox_tasks.get(0,listbox_tasks.size())
        pickle.dump(tasks,open("tasks.dat","wb"))
    except:
        tkinter.messagebox.showwarning(title="Waring!", message="Can't find tasks.dat")

#create GUI
#frames
frame_task=tkinter.Frame(root)
frame_task.pack()
#height and width of block and list box creation
listbox_tasks=tkinter.Listbox(frame_task,height=30,width=50)
listbox_tasks.pack(side=tkinter.LEFT)

#scrollbar
scrollbar_tasks=tkinter.Scrollbar(frame_task)
scrollbar_tasks.pack(side=tkinter.RIGHT,fill=tkinter.Y)
#scrollbar configuration
listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

#entry area
entry_task=tkinter.Entry(root,width=50)
entry_task.pack()
 

#buttons
button_add_task= tkinter.Button(root, text="Add Task",width=48,height=2, command=add_task,bg="aqua" )
button_add_task.pack()
button_delete_task= tkinter.Button(root, text="Delete Task",width=48,height=2, command=delete_task,bg="aqua" )
button_delete_task.pack()
button_load_task= tkinter.Button(root, text="Load Task",width=48,height=2, command=load_task,bg="aqua" )
button_load_task.pack()
button_save_task= tkinter.Button(root, text="Save Task",width=48,height=2, command=save_task,bg="aqua" )
button_save_task.pack()
root.mainloop()