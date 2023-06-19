###################################################################
#                             Totems+                             #
# A new and unique way to integrate custom totems into Minecraft! #
#    Learn More here:https://github.com/The-Iceburg/TotemsPlus    #
#        Created By The Totems+ Team - Ormatist + Dockuin         #
###################################################################

# imports the required libaries
from tkinter import *
from tkinter import filedialog
import customtkinter
from PIL import ImageTk, Image
from integrations.MCCMD import CMD
from integrations.OFCIT import CIT
from integrations.MCRTX import RTX

# outlines the deafult appearance of the window
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Totems+")
        self.iconbitmap("img/totems.ico")

        self.my_font = customtkinter.CTkFont(family="TkDefaultFont", size=15, weight="bold")

        #########################

        self.logo_image = customtkinter.CTkImage(dark_image=Image.open("img/pack.png"), size=(320,320))
        self.logo_label = customtkinter.CTkLabel(self, image=self.logo_image, text="")
        self.logo_label.grid(row=0, column=0, padx=(20, 0), pady=(20, 5))

        #########################

        self.tabview = customtkinter.CTkTabview(self, width=250, height=200)
        self.tabview.grid(row=0, column=1, padx=(20, 20), pady=(0, 5))
        self.tabview.add("MCCMD")
        self.tabview.add("MCRTX")
        self.tabview.add("OFCIT")

        #########################

        self.label_mccmd_title = customtkinter.CTkLabel(self.tabview.tab("MCCMD"), text="Minecraft Custom Model Data", font=self.my_font)
        self.label_mccmd_title.grid(row=0, column=0, padx=20, pady=0)
        self.label_mccmd_title.place(relwidth=1)

        self.label_mccmd_desc = customtkinter.CTkLabel(self.tabview.tab("MCCMD"), text="Utilises a datapacks to allow users to\n generate custom totems which are\n dropped by evokers among other\n numerous features.")
        self.label_mccmd_desc.grid(row=1, column=0, padx=5, pady=(30, 0))

        self.label_mccmd_req = customtkinter.CTkLabel(self.tabview.tab("MCCMD"), text="Requires:", font=self.my_font)
        self.label_mccmd_req.grid(row=2, column=0, padx=5, pady=(0, 0))

        self.datapack_icon = ImageTk.PhotoImage(Image.open("img/datapack.png"))
        self.datapack_icon_label = Label(self.tabview.tab("MCCMD"), image=self.datapack_icon, border=0)
        self.datapack_icon_label.grid(row=3, column=0, padx=(0, 45), pady=(0, 0))

        self.resourcepack_icon_mccmd = ImageTk.PhotoImage(Image.open("img/resourcepack.png"))
        self.resourcepack_icon_mccmd_label = Label(self.tabview.tab("MCCMD"), image=self.resourcepack_icon_mccmd, border=0)
        self.resourcepack_icon_mccmd_label.grid(row=3, column=0, padx=(45, 0), pady=(0, 0))

        #########################

        self.label_mcrtx_title = customtkinter.CTkLabel(self.tabview.tab("MCRTX"), text="Minecraft Re-Texture", font=self.my_font)
        self.label_mcrtx_title.grid(row=0, column=0, padx=20, pady=0)
        self.label_mcrtx_title.place(relwidth=1)

        self.label_mccmd_desc = customtkinter.CTkLabel(self.tabview.tab("MCRTX"), text="Simply re-textures the orginal totem\n in Minecraft to a texture of your\n choosing using just a resource\n pack")
        self.label_mccmd_desc.grid(row=1, column=0, padx=5, pady=(30, 0))

        self.label_mcrtx_req = customtkinter.CTkLabel(self.tabview.tab("MCRTX"), text="Requires:", font=self.my_font)
        self.label_mcrtx_req.grid(row=2, column=0, padx=5, pady=(0, 0))

        self.resourcepack_icon_mcrtx = ImageTk.PhotoImage(Image.open("img/resourcepack.png"))
        self.resourcepack_icon_mcrtx_label = Label(self.tabview.tab("MCRTX"), image=self.resourcepack_icon_mcrtx, border=0)
        self.resourcepack_icon_mcrtx_label.grid(row=3, column=0, padx=(0, 0), pady=(0, 0))

        #########################

        self.label_ofcit_title = customtkinter.CTkLabel(self.tabview.tab("OFCIT"), text="Optifine Custom Item Texture", font=self.my_font)
        self.label_ofcit_title.grid(row=0, column=0, padx=20, pady=0)
        self.label_ofcit_title.place(relwidth=1)

        self.label_ofcit_desc = customtkinter.CTkLabel(self.tabview.tab("OFCIT"), text="Uses Optifine to allow you to simply\n rename a totem in an anvil and\n have it change to different\n textures of your choosing.")
        self.label_ofcit_desc.grid(row=1, column=0, padx=5, pady=(30, 0))

        self.label_ofcit_req = customtkinter.CTkLabel(self.tabview.tab("OFCIT"), text="Requires:", font=self.my_font)
        self.label_ofcit_req.grid(row=2, column=0, padx=5, pady=(0, 0))

        self.optifine_icon = ImageTk.PhotoImage(Image.open("img/optifine.png"))
        self.optifine_icon_label = Label(self.tabview.tab("OFCIT"), image=self.optifine_icon, border=0)
        self.optifine_icon_label.grid(row=3, column=0, padx=(0, 45), pady=(0, 0))

        self.resourcepack_icon_ofcit = ImageTk.PhotoImage(Image.open("img/resourcepack.png"))
        self.resourcepack_icon_ofcit_label = Label(self.tabview.tab("OFCIT"), image=self.resourcepack_icon_ofcit, border=0)
        self.resourcepack_icon_ofcit_label.grid(row=3, column=0, padx=(45, 0), pady=(0, 0))

        #########################

        self.logo_text = ImageTk.PhotoImage(Image.open("img/text.png"))
        self.logo_text_label = Label(self, image=self.logo_text, border=0)
        self.logo_text_label.grid(row=1, column=0, padx=(20, 0), pady=(5, 20))

        self.version_frame = customtkinter.CTkFrame(self, width=250, height=200)
        self.version_frame.grid(row=1, column=1, padx=(0, 0), pady=(10, 20))

        self.version_label = customtkinter.CTkLabel(self.version_frame, text="Version:", font=self.my_font)
        self.version_label.grid(row=0, column=0, padx=(20, 5), pady=0)

        self.version = customtkinter.CTkOptionMenu(self.version_frame, values=["1.20.1", "1.20", "1.19.4", "1.19.3", "1.19.2", "1.19.1", "1.19", "1.18.2", "1.18.1", "1.18", "1.17.1", "1.17", "1.16.5", "1.16.4", "1.16.3", "1.16.2", "1.16.1", "1.16", "1.15.2", "1.15.1", "1.15", "1.14.4", "1.14.3", "1.14.2", "1.14.1", "1.14"])
        self.version.grid(row=0, column=1, padx=(5, 20), pady=5)

        self.textures_frame = customtkinter.CTkFrame(self, width=490, height=200)
        self.textures_frame.pack_propagate(False)
        self.textures_frame.grid(row=2, column=0, padx=(0, 0), pady=(0, 0), columnspan=2)

        self.images_label = customtkinter.CTkLabel(self.textures_frame, text="Textures:", font=self.my_font)
        self.images_label.grid(row=0, column=0, padx=(20,128), pady = (5,5))

        self.progressbar = customtkinter.CTkProgressBar(self.textures_frame, orientation="horizontal", width=480)
        self.progressbar.grid(row=1, column=0, pady=(5,5), columnspan = 2)
        self.progressbar.set(0)

        def UploadAction(event=None):
            filelist = filedialog.askopenfiles(filetypes=[("JPEG, PNG, TGA, GIF (.jpg , .png , .tga , .gif)", ".jpg , .png , .tga , .gif")])
            counter = 1
            for i in filelist:
                split = str(i).split("'")
                split = split[1] + "\n"
                self.textbox.insert("0.0", split)
                self.progressbar.set(1/(len(filelist))*counter)
                counter += 1

        self.upload = customtkinter.CTkButton(self.textures_frame, text='Upload', command=UploadAction)
        self.upload.grid(row=0, column=1, padx=(127,20), pady=(5,5))

        self.textbox = customtkinter.CTkTextbox(self.textures_frame, width=480)
        self.textbox.grid(row=2, column=0, pady=(5,5), columnspan = 2)

        def TotemsPlus():
            print(self.version.get())
            if self.tabview.get() == "MCCMD":
                CMD(self.textbox.get("1.0",END),self.version.get())
            elif self.tabview.get() == "OFCIT":
                CIT(self.textbox.get("1.0",END),self.version.get())
            elif self.tabview.get() == "MCRTX":
                RTX(self.textbox.get("1.0",END),self.version.get())

        self.compile = customtkinter.CTkButton(self, text="Compile", command=TotemsPlus)
        self.compile.grid(row=3, column=0, padx=(0, 0), pady=(10, 10), columnspan=2)

        
if __name__ == "__main__":
    app = App()
    app.mainloop()

