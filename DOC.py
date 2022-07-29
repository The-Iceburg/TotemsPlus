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
def DOC(worldLocation, nameList, weightList, inGameName, inGameLore, loreList):

    # creates the documentation file
    doc = open(worldLocation + "/datapacks/Totems+ CMD/documentation.txt", 'w+')

    doc.write('Totems+ Custom Datapack Documentation\n')
    doc.write('\n')
    doc.write('List of Totems:\n')
    
    # cycles through the name list
    for i in range(len(nameList)):

        # writes the totem name and their associated CMD value
        doc.write('Totem Name: ' + nameList[i] + '   Custom Model Data ID: ' + str(910340 + i) +'\n')

    # writes a new line and heading
    doc.writelines(['\n',
    'Give Commands:\n'])

    # cycles through the name list
    for i in range(len(nameList)):
        
        # writes universal info
        doc.write(nameList[i] + ':   /give @s minecraft:totem_of_undying{')
        
        # writes the rest of the command dependent on if the in-game box was checked for lore or name
        if inGameName[i] == True and inGameLore[i] == True:

            doc.write('''display:{Name:'[{"text":"''' + nameList[i] + '''"}]',Lore:['[{"text":"''' + loreList[i]+ '''"}]']},CustomModelData:''' + str(910340 + i) +'} 1\n')

        elif inGameName[i] == True:

            doc.write('''display:{Name:'[{"text":"''' + nameList[i] + '''"}]'},CustomModelData:''' + str(910340 + i) +'} 1\n')

        elif inGameLore[i] == True:

            doc.write('''display:{Lore:['[{"text":"''' + loreList[i] + '''"}]']},CustomModelData:''' + str(910340 + i) +'} 1\n')

        else:

            doc.write('CustomModelData:' + str(910340 + i) +'} 1\n')

    # writes a new line and title
    doc.writelines(['\n',
    'Totem Drop Chance\n'])

    # defines total
    total = 0

    # cycles through totems
    for i in range(len(nameList)):

        # finds sum of weights
        total += int(weightList[i])

    # cycles through totems
    for i in range(len(nameList)):

        # calculates the drop chance
        dropChance = (int(weightList[i]) / total) * 100
        dropChance = round(dropChance, 2)

        # writes the drop chance to the file
        doc.write(nameList[i] + ':   ' + str(dropChance) + '%\n')

    # closes the documenation file
    doc.close()