from tkinter import *
from tkinter import messagebox,ttk
from parser import *
import os.path

department_list = ["Biology", "Chemistry", "Computer and Information Sciences", "Human Physiology", "Mathematics", "Physics", "Psychology"]
include_GS = 1 # variable indicating whether graduate student instructors are shown
type_of_graph_to_show = 1 # variable indicating which type of graph to show (1 for % As 0 for % Ds/Fs)

# function called when search button is pressed
def search_button(event):
    departmentName = getDepartmentNames()[deptNamecombo.current()]
    classLevel = classLevelcombo.get()
    classNumber = classNumbercombo.get()
    messagebox.showinfo(
        title="Searching",
        message=f"Department: {departmentName}\nClass Level: {classLevel}\nClass Number: {classNumber}\nInclude GS: {include_GS}\nAs or Fs: {type_of_graph_to_show}"
    )
    return

# function called when selecting a class level, gets all class numbers for current department at specific class level
def set_class_numbers(event):
    current_class_level = classLevelcombo.get()
    if (current_class_level == ""):
        classNumbercombo.config(values=[""])
    else:
        current_department = getDepartmentNames()[deptNamecombo.current()]
        current_class_numbers = getClassNumbers(current_department)
        current_class_numbers[int(current_class_level)].insert(0, "")
        classNumbercombo.config(value=current_class_numbers[int(current_class_level)])
    classNumbercombo.set("")
    searchButton.focus()
    return

# function called when changing current department, sets class level and class number to blank
def change_departemnt(event):
    classLevelcombo.set("")
    set_class_numbers(event)
    return

# function called when the radio buttons are used
def change_graph_type():
    global type_of_graph_to_show
    if type_of_graph_to_show:
        type_of_graph_to_show = 0
    else:
        type_of_graph_to_show = 1
    return

# function called when the GS checkbox is ticked or unticked
def change_GS():
    global include_GS
    if include_GS:
        include_GS = 0
    else:
        include_GS = 1
    return

# main window configuration
window = Tk(className=" Easy A")
window.geometry("325x480")
window.resizable(False, False)
window.config(bg="#007030")

# UO logo image
if (os.path.isfile("uoo.png")):
    UOimage = PhotoImage(file="uoo.png")
    imageLabel = Label(image=UOimage, bg="#007030")
    imageLabel.place(x=-7, y=-10)

# labels indicating what each combobox is for
label1 = Label(text="Department Name", font=("Helvetica 15 bold"), bg="#007030", fg="#FEE11A")
label2 = Label(text="Class Level", font=("Helvetica 15 bold"), bg="#007030", fg="#FEE11A")
label3 = Label(text="Class Number", font=("Helvetica 15 bold"), bg="#007030", fg="#FEE11A")
# combobox selections
deptNamecombo = ttk.Combobox(
    state="readonly",
    values=department_list,
    font=("Helvetica 15"),
    width=16
)
classLevelcombo = ttk.Combobox(
    state="readonly",
    values=["", "100", "200", "300", "400", "500", "600"],
    font=("Helvetica 15"),
    width=16
)
classNumbercombo = ttk.Combobox(
    state="readonly",
    values=[""],
    font=("Helvetica 15"),
    width=16
)
# GS selection checkbox and type of graph selector radio buttons
GSButton = Checkbutton(text="Include GS Instructors",
    onvalue=1,
    offvalue=0, 
    font=("Helvetica 12 bold"), 
    height=2,
    bg="#007030", 
    fg="#FEE11A", 
    selectcolor="#007030", 
    activebackground="#007030", 
    activeforeground="#FEE11A", 
    command=change_GS
)
R1 = Radiobutton(text="Show Percent As", 
    value=1,
    font=("Helvetica 12 bold"), 
    height=1,
    bg="#007030", 
    fg="#FEE11A", 
    selectcolor="#007030", 
    activebackground="#007030", 
    activeforeground="#FEE11A", 
    command=change_graph_type
)
R2 = Radiobutton(text="Show Percent Ds/Fs", 
    value=0,
    font=("Helvetica 12 bold"), 
    height=1,
    bg="#007030", 
    fg="#FEE11A", 
    selectcolor="#007030", 
    activebackground="#007030", 
    activeforeground="#FEE11A", 
    command=change_graph_type
)
# search button
searchButton = Button(text="Search", 
    width=15, 
    font=("Helvetica 15 bold"), 
    bg="#FEE11A", 
    fg="#007030", 
    activebackground="#FEE11A", 
    activeforeground="#007030"
)

# setting default values for widgets
deptNamecombo.set("Biology")
classLevelcombo.set("")
classNumbercombo.set("")
GSButton.select()
R1.select()
R2.deselect()

# binding functions to events
deptNamecombo.bind('<<ComboboxSelected>>', change_departemnt)
classLevelcombo.bind('<<ComboboxSelected>>', set_class_numbers)
classNumbercombo.bind("<<ComboboxSelected>>",lambda e: searchButton.focus())
searchButton.bind("<Button-1>", search_button)

# placing widgets
label1.place(relx=.5, y=35, anchor=CENTER)
label2.place(relx=.5, y=125, anchor=CENTER)
label3.place(relx=.5, y=215, anchor=CENTER)
deptNamecombo.place(relx=.5, y=70, anchor=CENTER)
classLevelcombo.place(relx=.5, y=160, anchor=CENTER)
classNumbercombo.place(relx=.5, y=250, anchor=CENTER)
GSButton.place(x=65, y=275)
R1.place(x=65, y=315)
R2.place(x=65, y=345)
searchButton.place(relx=.5, y=410, anchor=CENTER)

# mainloop so window stays open
window.mainloop()
