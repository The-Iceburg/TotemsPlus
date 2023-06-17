###################################################################
#                             Totems+                             #
# A new and unique way to integrate custom totems into Minecraft! #
#    Learn More here:https://github.com/The-Iceburg/TotemsPlus    #
#        Created By The Totems+ Team - Ormatist + Dockuin         #
###################################################################

# imports the libaries used within totems+
import json

# defines the DOC function
def DOC(worldLocation, nameList, weightList, inGameName, loreList, exportType):

    # if the export type is a txt file
    if exportType:

        # creates the documentation file
        with open(worldLocation + "/datapacks/Totems+ CMD/documentation.txt", 'w+') as doc:

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
                if inGameName[i] == True and loreList[i] != "":
                    doc.write('''display:{Name:'[{"text":"''' + nameList[i] + '''"}]',Lore:['[{"text":"''' + loreList[i]+ '''"}]']},CustomModelData:''' + str(910340 + i) +'} 1\n')

                elif inGameName[i] == True:
                    doc.write('''display:{Name:'[{"text":"''' + nameList[i] + '''"}]'},CustomModelData:''' + str(910340 + i) +'} 1\n')

                elif loreList[i] != "":
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
                doc.write(f'{nameList[i]}:   {dropChance}%\n')
    
    # otherwise if the export type is a json file
    elif not exportType:

        # defines the json as a dictionary
        jsonDict = {}

        # defines total
        total = 0

        # cycles through totems
        for i in range(len(nameList)):

            # finds sum of weights
            total += int(weightList[i])

        # for each totem
        for i in range(len(nameList)):

            # calculates the drop chance
            dropChance = (int(weightList[i]) / total) * 100
            dropChance = round(dropChance, 2)

            # writes universal info
            command = '/give @s minecraft:totem_of_undying{'

            # writes the rest of the command dependent on if the in-game box was checked for lore or name
            if inGameName[i] == True and loreList[i] != "":
                command += '''display:{Name:'[{"text":"''' + nameList[i] + '''"}]',Lore:['[{"text":"''' + loreList[i]+ '''"}]']},CustomModelData:''' + str(910340 + i) +'} 1'

            elif inGameName[i] == True:
                command += '''display:{Name:'[{"text":"''' + nameList[i] + '''"}]'},CustomModelData:''' + str(910340 + i) +'} 1'

            elif loreList[i] != "":
                commnd += '''display:{Lore:['[{"text":"''' + loreList[i] + '''"}]']},CustomModelData:''' + str(910340 + i) +'} 1'

            else:
                command += 'CustomModelData:' + str(910340 + i) +'} 1'

            # assigns all determined values to json dictionary
            jsonDict[nameList[i]] = {"customModelData": 910340 + i, "dropChance": dropChance, "command": command}

        # creates the documentation json file
        with open(worldLocation + "/datapacks/Totems+ CMD/documentation.json", 'w+') as jsonDoc:

            # writes data in JSON form to file
            jsonDoc.write(json.dumps(jsonDict))
