# ------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# Charles Hodges(hodges11@uw.edu), 2021-Aug-08, Created File
# ------------------------------------------#


# Variables
dctRow = {}  # Dictionary data row.
lstTbl = []  # List of dictionaries to hold data.
objFile = None  # file object.
strChoice = ''  # User input.

# Strings
keyArtist = 'Artist'
keyId = 'ID'
keyTitle = 'Title'
strAdd = 'a'
strAddSuccessMsg = 'Added a CD to the inventory.'
strArtistName = 'Enter the Artist\'s Name: '
strCdTitle = 'Enter the CD\'s Title: '
strCdWasDeletedMsg = "CD with ID {} was deleted."
strDelete = 'd'
strDeleteById = "Which CD would you like to remove? Indicate using 'ID': "
strDisplay = 'i'
strEnterId = 'Enter an ID#: '
strErrorMsg = 'Please choose either l, a, i, d, s or x!'
strExit = 'x'
strFileName = 'CDInventory.txt'
strInputHdr = '\nThe Magic CD Inventory'
strLoad = 'l'
strLoadSuccessMsg = 'Loading complete.'
strMenu1 = """
[l] Load Inventory from file(*This will overwrite any unsaved data*)
[a] Add CD
[i] Display Current Inventory
[d] Delete CD from Inventory
[s] Save Inventory to file
[x] exit
"""
strMenuOptions = 'l, a, i, d, s, or x: '
strRead = 'r'
strSave = 's'
strSaveSuccessMsg = 'Saved to text file.'
strWrite = 'w'


# Get user Input
print(strInputHdr)
while True:

    # Display menu allowing the user to choose usage intent.
    print(strMenu1)

    # convert choice to lower case at time of input.
    strChoice = input(strMenuOptions).lower()
    print()  # Empty line for readability.

    # Exit the program.
    if strChoice == strExit:
        break

    # Load existing data.
    if strChoice == strLoad:
        # If the file does not yet exist, create it, to avoid
        # a FileNotFoundError. This will NOT overwrite
        # the current data, if it exists already.
        text_file = open(strFileName, strAdd)
        text_file.close()

        # Reset the Table first
        lstTbl = []

        # Then load data from text file.
        with open(strFileName, strRead) as objFile:
            for row in objFile:
                lstRow = row.strip().split(',')
                dicRow = {
                          'ID': int(lstRow[0]),
                          'Title': lstRow[1],
                          'Artist': lstRow[2]
                         }
                lstTbl.append(dicRow)
            print(strLoadSuccessMsg)
            print()  # Empty line for readability

    # Add data to the table.
    elif strChoice == strAdd:
        intId = int(input(strEnterId))
        strTitle = input(strCdTitle)
        strArtist = input(strArtistName)
        dctRow = {keyId: intId, keyTitle: strTitle, keyArtist: strArtist}
        lstTbl.append(dctRow)
        print()  # Empty line for readability
        print(strAddSuccessMsg)
        print()  # Empty line for readability

    # Display the current data to the user.
    elif strChoice == strDisplay:
        print("{: <5} {: <20} {: <20}".format("ID", "| Title", "| Artist"))
        print("{: <5} {: <20} {: <20}".format("--", "| -----", "| ------"))
        counter = 0
        for row in lstTbl:
            dctRowToLst = list(lstTbl[counter].values())
            lstToStr = ','.join([str(elem) for elem in dctRowToLst])
            split_lines = lstToStr.split(",")
            id_num, title, artist = split_lines
            print("{: <5} {: <20} {: <20}".format
                  (
                      id_num, "| " + title, "| " + artist)
                  )
            counter += 1
        print()  # Empty line for readability.

    # Delete an entry
    elif strChoice == strDelete:
        deleteId = int(input(strDeleteById))
        for items in range(len(lstTbl)):
            if lstTbl[items]['ID'] == deleteId:
                del lstTbl[items]
                print(strCdWasDeletedMsg.format(deleteId))
                break
        print()  # Empty line for readability.

    # Save the data to a text file.
    elif strChoice == strSave:
        with open(strFileName, strWrite) as objFile:
            counter = 0
            for row in lstTbl:
                idNum, title, artist = lstTbl[counter].values()
                objFile.write(str(idNum) + ',' + title + "," + artist + '\n')
                counter += 1
        print(strSaveSuccessMsg)
        print()  # Empty line for readability.

    else:
        print(strErrorMsg)
