import os


#input output operation
class IOOperation:
    #value from ListData.text is stored here as a list
    ListData = []
    ListDataStatus = []

    #read user input for an option or command
    #TODO add delete all list item option
    @staticmethod
    def readUsrInput():
        usrInput = input(">> ")
        #option e: exit
        if usrInput.lower() == 'e':
            exit()
        #option d: delete
        elif usrInput.lower() == 'd':
            try:
                IOOperation.deleteListItem()
            except KeyboardInterrupt:
                return
        #option a: add
        elif usrInput.lower() == 'a':
            try:
                IOOperation.addListItem()
            except KeyboardInterrupt:
                return
        #option s: save
        elif usrInput.lower() == 's':
            IOOperation.writeFile()
            print("list has been saved.")
            input("press any key to continue...")
        #option r: reset
        elif usrInput.lower() == 'r':
            IOOperation.resetList()
        #option number: read number inputs & other inputs
        else:
            IOOperation.readNumberInput(usrInput)


    #read number & other input
    @staticmethod
    def readNumberInput(usrInput):
        #convertin usrInput to int
        try:
            usrInput = int(usrInput)-1
        except ValueError:
            print(f"{usrInput} is invalid, unknown or unhandled input.")
            input("Press any key to continue")
            return
        #mark item done or undone
        try:
            if IOOperation.ListDataStatus[usrInput] == '[    ]':
                IOOperation.ListDataStatus[usrInput] = '[done]'
            elif IOOperation.ListDataStatus[usrInput] == '[done]':
                IOOperation.ListDataStatus[usrInput] = '[    ]'
        except IndexError:
            print(f"{usrInput+1} is not available.")
            input("Press any key to continue")
            return
        #rewrite list to ListData.txt file
        IOOperation.writeFile()


    #delete an item from the list
    @staticmethod
    def deleteListItem():
        #import display module and display list to the console
        from modules.DisplayOperation import Display as d
        d.displayList()
        print("+--+--------+---------------------------+")
        usrInput = input("Input list number to delete (ctrl+c to cancel): ")
        #pop list item based on usrInput
        IOOperation.ListData.pop(int(usrInput)-1)
        IOOperation.ListDataStatus.pop(int(usrInput)-1)
        #rewrite list to ListData.txt file
        IOOperation.writeFile()


    #add an item to the list
    @staticmethod
    def addListItem():
        usrInput = input("Input item name to add to the list (ctrl+c to cancel): ")
        #append usrInput into the listData and listDataStatus
        IOOperation.ListData.append(usrInput)
        IOOperation.ListDataStatus.append("[    ]")
        #rewrite list to ListData.txt file
        IOOperation.writeFile()


    #delete an entire list of items
    @staticmethod
    def resetList():
        print("Are you sure want to reset your list? (y/n)")
        #read user input
        usrInput = input(">> ")
        if usrInput == ('y'):
            #un-done all status
            for index in range(0, len(IOOperation.ListDataStatus)):
                IOOperation.ListDataStatus[index] = "[    ]"
            #rewrite list to ListData.txt
            IOOperation.writeFile()
        else:
            return


    #read ListData.txt and store it in ListData variable
    @staticmethod
    def readDataFile():
        #check if ListData.txt is available
        if os.path.isfile("data/ListData.txt"):
            #clear List for each function call
            IOOperation.ListData = []
            #temporary list for splitting
            tempData = []
            with open("data/ListData.txt", "r") as f:
                for line in f:
                    #split items and status to append
                    tempData = line.split(':')
                    #append item and item status
                    IOOperation.ListDataStatus.append(tempData[0].strip())
                    IOOperation.ListData.append(tempData[1].strip())
        #if ListData.txt is not available
        else:
            #create ListData.txt in data folder
            IOOperation.generateDataFile()


    #read all data in listData and listDataStatus lists
    #and write it back to ListData.txt file
    @staticmethod
    def writeFile():
        #check if ListData.txt is available
        if os.path.isfile("data/ListData.txt"):
            #delete and recreate ListData.txt
            IOOperation.generateDataFile()
            with open("data/ListData.txt", "w") as f:
                for item, status in zip(IOOperation.ListData, IOOperation.ListDataStatus):
                    #join item with the status and write it to ListData.txt file
                    f.write(f"{status}:{item}\n")
        #if ListData.txt is not available
        else:                                  
            #create ListData.txt in data folder                 
            IOOperation.generateDataFile()


    #generate ListData.txt in data folder
    @staticmethod
    def generateDataFile():
        f = open("data/ListData.txt", "w+")
        f.close()