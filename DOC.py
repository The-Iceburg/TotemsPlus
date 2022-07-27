###################################################################
#                             Totems+                             #
# A new and unique way to integrate custom totems into Minecraft! #
#    Learn More here:https://github.com/The-Iceburg/TotemsPlus    #
#        Created By The Totems+ Team - Ormatist + Dockuin         #
###################################################################

# imports the libaries used within Totems+
import os
import getpass

# defines the DOC function
def DOC():

    # grabs all required info from docconfig file
    docconfig = open("C:/Users/" + getpass.getuser() + "/AppData/Roaming/Totems+/docconfig.txt", "r")
    docconfigread = docconfig.readlines()
    docconfig.close()

    # sorts info into appropriate variables
    worldLocation = docconfigread[0]
    weightList = docconfigread[2]
    nameList = docconfigread[1]
    loreList = docconfigread[5]
    inGameName = docconfigread[3]
    inGameLore = docconfigread[4]

    # derives lists from sorted info where appropriate
    worldLocation = worldLocation.replace('\n','')
    weightList = weightList.split(';')
    nameList = nameList.split(';')
    loreList = loreList.split(';')
    inGameLore = inGameLore.split(';')
    inGameName = inGameName.split(';')

    # creates the documentation file
    doc = open(worldLocation + "/datapacks/Totems+ CMD/documentation.txt", 'x')
    doc.close()

    # writes basic opening info into file
    doc = open(worldLocation + "/datapacks/Totems+ CMD/documentation.txt", 'a')
    doc.write('Totems+ Custom Datapack Documentation\n')
    doc.write('\n')
    doc.write('List of Totems:\n')

    # sets counter to 0
    counter = 0
    
    # cycles through the name list
    while len(nameList) != counter + 1:

        # writes the totem name and their associated CMD value
        doc.write('Totem Name: ' + nameList[counter] + '   Custom Model Data ID: ' + str(910340 + counter) +'\n')

        # increases the counter 
        counter += 1

    # writes a new line and heading
    doc.write('\n')
    doc.write('Give Commands:\n')

    # re-sets the counter to 0
    counter = 0
    
    # cycles through the name list
    while len(nameList) != counter + 1:
        
        # writes universal info
        doc.write(nameList[counter] + ':   /give @s minecraft:totem_of_undying{')
        
        # writes the rest of the command dependent on if the in-game box was checked for lore or name
        if inGameName[counter] == "True" and inGameLore[counter] == "True":

            doc.write('''display:{Name:'[{"text":"''' + nameList[counter] + '''"}]',Lore:['[{"text":"''' + loreList[counter]+ '''"}]']},CustomModelData:''' + str(910340 + counter) +'} 1\n')

        elif inGameName[counter] == "True":

            doc.write('''display:{Name:'[{"text":"''' + nameList[counter] + '''"}]'},CustomModelData:''' + str(910340 + counter) +'} 1\n')

        elif inGameLore[counter] == "True":

            doc.write('''display:{Lore:['[{"text":"''' + loreList[counter] + '''"}]']},CustomModelData:''' + str(910340 + counter) +'} 1\n')

        else:
            doc.write('CustomModelData:' + str(910340 + counter) +'} 1\n')

        # increases counter by 1
        counter += 1

    # writes a new line and title
    doc.write('\n')
    doc.write('Totem Drop Chance\n')

    # sets counter and total to 0
    counter = 0
    total = 0

    # cycles through totems
    while len(nameList) != counter + 1:

        # finds sum of weights
        total += int(weightList[counter])

        # increases counter by 1
        counter += 1

    # re-sets counter to 1
    counter = 0

    # cycles through totems
    while len(nameList) != counter + 1:

        # calculates the drop chance
        dropChance = (int(weightList[counter]) / total) * 100
        dropChance = round(dropChance, 2)

        # writes the drop chance to the file
        doc.write(nameList[counter] + ':   ' + str(dropChance) + '%\n')

        # increases counter by 1
        counter += 1

    # closes the documenation file
    doc.close()