# imports the libaries used within Totems+ 
from tkinter.constants import S
import PySimpleGUI as sg
from OFCIT import CIT
from MCCMD import CMD

# sets window theme
sg.theme('DarkTeal10')

# declares the accepted texture file types
textureFileTypes = [("JPEG, PNG, TGA (.jpg , .png , .tga)", ".jpg , .png , .tga")]

# defines the main window
def main():

    # defines how the main window will be displayed/layed-out
    layout = [
        [
            sg.Image(filename='AppData/Roaming/Totems +/windowlogo.png', key='-LOGO-'),
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
            sg.Button('Optifine CIT', size=(20,1), button_color=('white','orange'), key='-TOGGLE-')
        ],
        [
            sg.Text("⚫ Select your totem image files here:")
        ],
        [
            sg.Text("Image File"),
            sg.Input(size=(58, 1), key="-TEXTURES-"),
            sg.FilesBrowse(file_types=textureFileTypes),
        ],
        [
            sg.Text("(Remember they will need to be in the following formats: .jpg , .png , .tga)")
        ],
        [
            sg.Text("⚫ Finally hit Compile and follow any further instructions to generate your pack(s):"),sg.Button("Compile")
        ],
    ]

    # creates the window
    window = sg.Window("Totems+", layout, icon="AppData/Roaming/Totems +/totems.ico")

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
            
            # creates config file
            config = open('AppData/Roaming/Totems +/cmdconfig.txt', 'x')
            config.close()

            # writes file locations into config file
            config = open("AppData/Roaming/Totems +/cmdconfig.txt", "a")
            config.write(values["-TEXTURES-"])
            config.close()

            # runs CMD function
            CMD()

            # breaks code (hence closing window)
            break

        # if compile and toggle true then
        elif event == 'Compile' and down == True:

            # creates config file
            config = open('AppData/Roaming/Totems +/citconfig.txt', 'x')
            config.close()

            # writes file locations into config file
            config = open("AppData/Roaming/Totems +/citconfig.txt", "a")
            config.write(values["-TEXTURES-"])
            config.close()

            # runs CIT function
            CIT()

            # breaks code (hence closing window)
            break

    # closes window if called
    window.close()

if __name__ == "__main__":
    main()
