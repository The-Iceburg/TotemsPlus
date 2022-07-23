import os
import getpass

def DOC():

    docconfig = open("C:/Users/" + getpass.getuser() + "/AppData/Roaming/Totems+/docconfig.txt", "r")
    docconfigread = docconfig.readlines()
    docconfig.close()

    worldLocation = docconfigread[0]
    weightList = docconfigread[2]
    nameList = docconfigread[1]
    loreList = docconfigread[5]
    inGameName = docconfigread[3]
    inGameLore = docconfigread[4]

    worldLocation = worldLocation.replace('\n','')
    weightList = weightList.split(';')
    nameList = nameList.split(';')
    loreList = loreList.split(';')
    inGameLore = inGameLore.split(';')
    inGameName = inGameName.split(';')

    doc = open(worldLocation + "/datapacks/Totems+ CMD/documentation.txt", 'x')
    doc.close()

    doc = open(worldLocation + "/datapacks/Totems+ CMD/documentation.txt", 'a')
    doc.write('Totems+ Custom Datapack Documentation\n')
    doc.write('\n')
    doc.write('List of Totems:\n')

    counter = 0
    
    while len(nameList) != counter + 1:

        doc.write('Totem Name: ' + nameList[counter] + '   Custom Model Data ID: ' + str(910340 + counter) +'\n')

        counter += 1

    doc.write('\n')
    doc.write('Give Commands:\n')

    counter = 0
    
    while len(nameList) != counter + 1:

        doc.write(nameList[counter] + ':   /give @s minecraft:totem_of_undying{')
        
        if inGameName[counter] == "True" and inGameLore[counter] == "True":

            doc.write('''display:{Name:'[{"text":"''' + nameList[counter] + '''"}]',Lore:['[{"text":"''' + loreList[counter]+ '''"}]']},CustomModelData:''' + str(910340 + counter) +'} 1\n')

        elif inGameName[counter] == "True":

            doc.write('''display:{Name:'[{"text":"''' + nameList[counter] + '''"}]'},CustomModelData:''' + str(910340 + counter) +'} 1\n')

        elif inGameLore[counter] == "True":

            doc.write('''display:{Lore:['[{"text":"''' + loreList[counter] + '''"}]']},CustomModelData:''' + str(910340 + counter) +'} 1\n')

        else:
            doc.write('CustomModelData:' + str(910340 + counter) +'} 1\n')

        counter += 1

    doc.write('\n')
    doc.write('Totem Drop Chance\n')

    counter = 0

    total = 0

    while len(nameList) != counter + 1:

        total += int(weightList[counter])

        counter += 1

    counter = 0
    
    while len(nameList) != counter + 1:

        dropChance = (int(weightList[counter]) / total) * 100

        dropChance = round(dropChance, 2)

        doc.write(nameList[counter] + ':   ' + str(dropChance) + '%\n')

        counter += 1

    doc.close()