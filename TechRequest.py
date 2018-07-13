# Terry Ellison SPC ID: 2335229 ©2018

# Main function, entry point of application. Controls flow of the program
def main():
    print("TechRequest, a HelpDesk application by Terry Ellison for the 2018 Programming Internship course at St.Petersburg College. ")
    
    # Try/Catch block that determines whether or not the database already exists.
    # If the database does not already exist, creates a new one
    # If the database does exist, reads the database's current contents
    
    dbExists = True
    try:
        flatFile = open("flatFile.txt", "r+")
    except FileNotFoundError:
        dbExists = False
        flatFile = open("flatFile.txt", "w+")
        print("No database file found, created new file.\n")
    if dbExists == True:
        readDB()

    # Main decision loop. Prompts the user as to what to do and executes based on the user's input
    # The loop will reprompt the user until they close the program
    
    answer = ''
    while answer != 'd':
        print("\nWhat would you like to do?")
        print("a) Display current database\nb) Add new requests to database\n" +
               "c) Edit an existing request\n" + "d) Close the program")
        answer = input("Enter the letter of your choice: ")
        answer.lower()
        if answer == 'a':
            readDB()
        elif answer == 'b':
            addRequests()
        elif answer == 'c':
            editRequest()
        elif answer == 'd':
            print("\nGoodbye!")
            flatFile.close()
            exit()
        # Input validation
        else:
            print("Sorry, that's an invalid entry. Please enter one of the choices above.\n")
            
# Allows the user to add requests to the database
def addRequests():
    db = open("flatFile.txt", 'a')
    q = 'y'
    completionDate = "NA"
    
    # Prompts the user and adds new requests to the database until the user declines
    # to add another request
    while q == 'y':
        request = input("What would you like to request to be done?: ")
        dateAssigned = input("Enter the date the request was assigned (MM/DD/YYYY): ")
        reqCompleted = input("Is this request complete? [y/n]: ")
        if reqCompleted == 'y':
            reqCompleted = "Yes"
            completionDate = input("Enter the date of completion (MM/DD/YYYY): ")
        else:
            reqCompleted = "No"
        technician = input("And who would you like to assign the job to?: ")
        db.write("\n" + request + "\t" + dateAssigned + "\t" + reqCompleted + "\t"
                  + completionDate + "\t" + technician)
        q = input("Would you like to enter another request? [y/n]: ")
    db.close()
    
# Reads the current contents of the database
def readDB():
    db = open("flatFile.txt", 'r')
    print("Displaying current contents of database...\n")
    for request in db:
        splitRequest = request.split("\t")
        if splitRequest[0] != "\n":
            print("Request: " + splitRequest[0] + "\nDate Assigned: " + splitRequest[1] +
                  "\nCompleted?: " + splitRequest[2] + "\nCompletion Date: " + splitRequest[3] +
                  "\nAssigned Technician: " + splitRequest[4] + "\n")
    db.close()

# Allows a user to edit an existing request
def editRequest():
    lineNum = 1
    dbToString = ""
    db = open("flatFile.txt", 'r')
    print("Here are the current requests:\n")
    for request in db:
        splitRequest = request.split("\t")
        if splitRequest[0] != "\n":
            print(lineNum, ")Request: " + splitRequest[0] + "\nDate Assigned: " + splitRequest[1] +
                  "\nCompleted?: " + splitRequest[2] + "\nCompletion Date: " + splitRequest[3] +
                  "\nAssigned Technician: " + splitRequest[4] + "\n")
        dbToString += (request)
        lineNum += 1
    db.close()
    db = open("flatFile.txt", 'w')

    # Determine the request the user would like to edit
    reqNum = int(input("Enter the number of the request you'd like to edit: "))
    dbSplit = dbToString.split("\n")
    reqToEdit = dbSplit[reqNum - 1]
    reqPerItem = reqToEdit.split("\t")

    # Check if the selected request is already completed. If so, exit the function
    if reqPerItem[2] == "Yes":
        print("\nThe selected request has already been completed. Please try again and" +
              " select a different request.")
        # Re-write data to database to protect against data loss
        for item in dbSplit:
            db.write(item + "\n")
        db.close()
        return

    # Determine what changes to make to the request
    markComplete = input("Mark job as complete? [y/n]: ")
    if markComplete == 'y':
        compDate = input("Enter the date of completion (MM/DD/YYYY): ")
        reqPerItem[2] = "Yes"
        reqPerItem[3] = (compDate)
        changedReq = ""
        for item in reqPerItem:
            changedReq += item + "\t"
        dbSplit[reqNum - 1] = changedReq

    # Write changes to database
    for item in dbSplit:
        db.write(item + "\n")
    db.close()
main()
