import os
import getpass

def FUN():

    funconfig = open("C:/Users/" + getpass.getuser() + "/AppData/Roaming/Totems+/funconfig.txt", "r")
    funconfigread = funconfig.readlines()
    funconfig.close()

    worldLocation = funconfigread[0]
    nameList = funconfigread[1]

    worldLocation = worldLocation.replace('\n','')
    nameList = nameList.split(';')

    print(nameList)

    os.mkdir(worldLocation + "/datapacks/Totems+ CMD/data/totemsplus")
    os.mkdir(worldLocation + "/datapacks/Totems+ CMD/data/totemsplus/functions")

    mcfunction = open(worldLocation + '/datapacks/Totems+ CMD/data/totemsplus/functions/totemload.mcfunction', 'x')
    mcfunction.close()

    mcfunction = open(worldLocation + '/datapacks/Totems+ CMD/data/totemsplus/functions/totemload.mcfunction', 'a')

    counter = 0

    while len(nameList) != counter + 1:

        mcfunction.write('give @s minecraft:totem_of_undying{CustomModelData:' + str(910340 + counter) +'} 1\n')

        counter += 1
    
    mcfunction.close()

    counter = 0

    while len(nameList) != counter + 1:

        mcfunction = open(worldLocation + '/datapacks/Totems+ CMD/data/totemsplus/functions/summon' + nameList[counter] + '.mcfunction', 'x')
        mcfunction.close()

        mcfunction = open(worldLocation + '/datapacks/Totems+ CMD/data/totemsplus/functions/summon' + nameList[counter] + '.mcfunction', 'a')

        mcfunction.write('give @s minecraft:totem_of_undying{CustomModelData:' + str(910340 + counter) +'} 1\n')
        mcfunction.close()

        counter += 1