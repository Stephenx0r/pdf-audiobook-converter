import tkinter
  
# Create the default window
root = tkinter.Tk()
root.title("Simple test")
root.geometry('700x500')
  
# Create the list of options
options_list = ["Option 1", "Option 2", "Option 3", "Option 4"]
  
# Variable to keep track of the option
# selected in OptionMenu
value_inside = tkinter.StringVar(root)
  
# Set the default value of the variable
value_inside.set("Select an Option")
  
# Create the optionmenu widget and passing 
# the options_list and value_inside to it.
question_menu = tkinter.OptionMenu(root, value_inside, *options_list)
question_menu.pack()
  
# Function to print the submitted option-- testing purpose
  
  
def print_answers():
    print("Selected Option: {}".format(value_inside.get()))
    return None
    
print_answers()
root.mainloop()