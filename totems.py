###################################################################
#                             Totems+                             #
# A new and unique way to integrate custom totems into Minecraft! #
#    Learn More here:https://github.com/The-Iceburg/TotemsPlus    #
#        Created By The Totems+ Team - Ormatist + Dockuin         #
###################################################################

# imports the libaries used within Totems+ 
import os.path, PySimpleGUI as sg, getpass
from OFCIT import CIT
from MCCMD import CMD

# sets window theme
sg.theme('DarkTeal10')

# declares the accepted texture file types
textureFileTypes = [("JPEG, PNG, TGA, GIF (.jpg , .png , .tga , .gif)", ".jpg , .png , .tga , .gif")]

# checks if the Totems+ roaming folder exists, if it doesn't one is created
if not os.path.exists('C:/Users/' + getpass.getuser() + '/AppData/Roaming/Totems+'):
    os.mkdir("C:/Users/" + getpass.getuser() + "/AppData/Roaming/Totems+")

# defines the main window
def main():

    # defines how the main window will be displayed/layed-out
    layout = [
        [
            sg.Image(filename='img/windowlogo.png', key='-LOGO-'),
            sg.Text('Totems + is a new and unique way to intergrate custom totems into Minecraft!\n' + 
            'This program currently provides support for:\n' + 
            'Minecraft CMD\n' + 
            'Optifine CIT\n' + 
            'To get started follow the instructions below \/\n' + 
            ' '),
        ],
        [
            sg.Text('⚫ You will want to start by choosing your integration type here:\n' + 
            ' \n' + 
            'Optifine CIT - Allows for existing Totems to be renamed to a given string\n' + 
            '                    e.g "Totem of Axolotl" and have its texture change.\n' + 
            ' \n' +
            'Minecraft CMD - Allows for custom totems using custom model data and adds\n' + 
            '                    these with a given weight to the evoker loot_tabel.'),
            sg.Button('Optifine CIT', size=(15,1), button_color=('white','orange'), key='-TOGGLE-')
        ],
        [
            sg.Text("⚫ Select your totem image files here:")
        ],
        [
            sg.Text("Image File :"),
            sg.Input(size=(57, 1), key="-TEXTURES-"),
            sg.FilesBrowse(file_types=textureFileTypes),
        ],
        [
            sg.Text("(Remember they will need to be in the following formats: .jpg , .png , .tga)\n" + "\n" + "⚫ Select which version of minecraft you wish to create the packs for:")
        ],
        [
            sg.DropDown(["1.14","1.14.1","1.14.2","1.14.3","1.14.4","1.15","1.15.1","1.15.2","1.16","1.16.1","1.16.2","1.16.3","1.16.4","1.16.5","1.17","1.17.1","1.18","1.18.1","1.18.2","1.19","1.19.1"],default_value="1.19.1",key="-DROPDOWN-")
        ],
        [
            sg.Text("⚫ Finally hit Compile and follow any further instructions to generate your pack(s):"),sg.Button("Compile")
        ],
    ]

    # creates the window
    window = sg.Window("Totems+", layout, icon="img/totems.ico")

    # sets the toggle preset
    down = True

    # while window (GUI) is open
    while True:

        # read all events/actions
        event, values = window.read()

        # if window closed break while loop and end code
        if event == sg.WIN_CLOSED:
            break
        
        # if Toggle pressed
        elif event == '-TOGGLE-':

            # program toggle the toggle
            down = not down

            # visual toggle the toggle
            window.Element('-TOGGLE-').Update(('Minecraft CMD','Optifine CIT')[down], button_color=(('white', ('teal','orange')[down])))

        # if compile and toggle false then
        elif event == 'Compile' and down == False:

            # runs CMD function
            CMD(values["-TEXTURES-"], values["-DROPDOWN-"])

            # breaks code (hence closing window)
            break

        # if compile and toggle true then
        elif event == 'Compile' and down == True:

            # runs CIT function
            CIT(values["-TEXTURES-"], values["-DROPDOWN-"])

            # breaks code (hence closing window)
            break

    # closes window if called
    window.close()

if __name__ == "__main__":
    main()