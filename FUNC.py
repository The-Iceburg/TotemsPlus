import os
import getpass

def FUN():

    funconfig = open("C:/Users/" + getpass.getuser() + "/AppData/Roaming/Totems+/funconfig.txt", "r")
    funconfigread = funconfig.readlines()
    funconfig.close()

    worldLocation = funconfigread[0]
    nameList = funconfigread[1]
    loreList = funconfigread[4]
    inGameName = funconfigread[2]
    inGameLore = funconfigread[3]

    worldLocation = worldLocation.replace('\n','')
    nameList = nameList.split(';')
    loreList = loreList.split(';')
    inGameLore = inGameLore.split(';')
    inGameName = inGameName.split(';')

    os.mkdir(worldLocation + "/datapacks/Totems+ CMD/data/totemsplus")
    os.mkdir(worldLocation + "/datapacks/Totems+ CMD/data/totemsplus/functions")

    mcfunction = open(worldLocation + '/datapacks/Totems+ CMD/data/totemsplus/functions/totemload.mcfunction', 'x')
    mcfunction.close()

    mcfunction = open(worldLocation + '/datapacks/Totems+ CMD/data/totemsplus/functions/totemload.mcfunction', 'a')

    counter = 0

    while len(nameList) != counter + 1:

        mcfunction.write('give @s minecraft:totem_of_undying{')
        
        if inGameName[counter] == "True" and inGameLore[counter] == "True":

            mcfunction.write('''display:{Name:'[{"text":"''' + nameList[counter] + '''"}]',Lore:['[{"text":"''' + loreList[counter]+ '''"}]']},CustomModelData:''' + str(910340 + counter) +'} 1\n')

        elif inGameName[counter] == "True":

            mcfunction.write('''display:{Name:'[{"text":"''' + nameList[counter] + '''"}]'},CustomModelData:''' + str(910340 + counter) +'} 1\n')

        elif inGameLore[counter] == "True":

            mcfunction.write('''display:{Lore:['[{"text":"''' + loreList[counter] + '''"}]']},CustomModelData:''' + str(910340 + counter) +'} 1\n')

        else:
            mcfunction.write('CustomModelData:' + str(910340 + counter) +'} 1\n')

        counter += 1
    
    mcfunction.close()

    counter = 0

    while len(nameList) != counter + 1:

        mcfunction = open(worldLocation + '/datapacks/Totems+ CMD/data/totemsplus/functions/summon' + nameList[counter].lower() + '.mcfunction', 'x')
        mcfunction.close()

        mcfunction = open(worldLocation + '/datapacks/Totems+ CMD/data/totemsplus/functions/summon' + nameList[counter].lower() + '.mcfunction', 'a')

        mcfunction.write('give @s minecraft:totem_of_undying{')
        
        if inGameName[counter] == "True" and inGameLore[counter] == "True":

            mcfunction.write('''display:{Name:'[{"text":"''' + nameList[counter] + '''"}]',Lore:['[{"text":"''' + loreList[counter]+ '''"}]']},CustomModelData:''' + str(910340 + counter) +'} 1\n')

        elif inGameName[counter] == "True":

            mcfunction.write('''display:{Name:'[{"text":"''' + nameList[counter] + '''"}]'},CustomModelData:''' + str(910340 + counter) +'} 1\n')

        elif inGameLore[counter] == "True":

            mcfunction.write('''display:{Lore:['[{"text":"''' + loreList[counter] + '''"}]']},CustomModelData:''' + str(910340 + counter) +'} 1\n')

        else:
            mcfunction.write('CustomModelData:' + str(910340 + counter) +'} 1\n')

        mcfunction.close()

        counter += 1