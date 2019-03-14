'''
Name: Pat Birkeland
Date: 03102019
Class: IT FDN 100 B
Assignment: Homework 5
'''

#-- Data --#
# declare variables and constants#
# objFile = An object that represents a file
# strData = A row of text data from the file
# dicRow = A row of data separated into elements of a dictionary (Task, Priority)
# lstTable = A dictionary that acts as a 'table' of rows
# strMenu = A menu of user options
# strChoice = Capture the user option selection

#-- Input/Output --#
# User can see a Menu (Step 2)
# User can see data (Step 3)
# User can insert or delet data (Step 4 and 5)
# User can save to a file (Step 6)

#-- Processing --#
# Step 1
# When the program starts, load any data you have
# in a text file called ToDo.txt into a python Dictionary

# Step 2
# Display a menu of choices to the user

# Step 3
# Display all todo items to user

# Step 4
# Add a new item to the list/Table

# Step 5
# Remove a new item to the list/Table

# Step 6
# Save tasks to the ToDo.txt file

# Step 7
# Exit program
#-----------------------------------------------------

objFileName = "./Todo.txt"
StrData = " "
dicRow = {}
lstTable = []

# Step 1 - Load data from a file
    # When the program starts, load each "row" of data
    # in "ToDo.txt" into a python Dictionary.
    # Add each dictionary "row" to a python list "table"

# Load Data from file
list = open(objFileName, "r")

# When the program starts, load each "row" of data
for line in list.readlines():
    # Split each line at the comma, assign parts into string objects
    str_task, str_priority = line.split(",")

    # Create a temp dictionary from key:task and priority:value as read in
    temp_dict = dict([("task", str_task.strip()), ("priority", str_priority.strip())])

    # Append temp dict to table
    lstTable.append(temp_dict)

    print(lstTable)
    '''
    # used the print statement below to confirm that program is reading file
    print(line)
    '''
# Step 2 - Display a menu of choices to the user
while(True):
    print ("""
    Menu of options
    1) Show current data
    2) Add a new item
    3) Remove an existing item
    4) Save Data to File
    5) Exit Program
    """)

    strChoice = str(input("Which option would you like to perform? [1 to 4] - "))

    # Add a new line
    print()

    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        #Print current items which are in the lstTable
        print(lstTable)
        continue

    # Step 4 - Add a new item to the list/Table
    elif(strChoice.strip() == '2'):
        #Ask user for input
        strInputTask = input("What task would you like to add to the list?:  ")
        strInputPriority = input("What priority would you like to assign to this task? [low, medium, high]: ")

        #Add input to list/Table
        # Create a temp dictionary from key:task and priority:value as read in
        temp_dict2 = dict([("task", strInputTask.strip()), ("priority", strInputPriority.strip())])

        # Append temp dict to table
        lstTable.append(temp_dict2)

        '''
        #check to make sure the list is being updated properly
        print(lstTable)
        '''

        continue

    # Step 5 - Remove a new item from the list/Table
        #This isn't fully working correctly
    elif(strChoice.strip() == '3'):
        lstTable_remove = int(input("What is the number of the item you which to remove?:  "))
        lstTable.pop(lstTable_remove - 1)
        continue

    # Step 6 - Save tasks to the ToDo.txt file
    elif(strChoice == '4'):
        list = open(objFileName, "a")
        # replace ',' with \n and : with ',' before writing to file
        lstTable = (str(lstTable)).replace(",", "\n").replace(":", ",")
        # strip away the rest of the brackets and spaces
        chars = "{}[]"
        for c in chars:
            lstTable = lstTable.replace(c, "")
        #write lstTable to ToDo.txt
        list.write("\n" + lstTable + "\n")
        list.close()

        continue
    elif (strChoice == '5'):

    #exit the program
        break


