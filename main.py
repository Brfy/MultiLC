
# Python program to create a basic GUI 
# application using the customtkinter module
 
import customtkinter as ctk
import tkinter #as tk
from tkinter import simpledialog
import promptlib
from pathlib import Path
import shutil
import os
 
# Basic parameters and initializations
# Supported modes : Light, Dark, System
ctk.set_appearance_mode("System") 
 
# Supported themes : green, dark-blue, blue
ctk.set_default_color_theme("dark-blue")    
 
appWidth, appHeight = 900, 700

Lethal_Company_Directory = ""
InstancesFolder = ""
do_stuff = True

# App Class
class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        self.title("MultiLC")
        self.geometry(f"{appWidth}x{appHeight}")

        InstancesFolder = f"{Lethal_Company_Directory}\\BepInEx\\Instances"


        has_instances = os.path.isdir(InstancesFolder)


        if has_instances == False:
            print("Doesn't have instances folder, making one now.")
            os.makedirs(InstancesFolder)
        
        subfolders = [item.name for item in Path(InstancesFolder).iterdir() if item.is_dir()]
        print(subfolders)

        # Name Label
        #self.nameLabel = ctk.CTkLabel(self,
        #                              text="Name")
        #self.nameLabel.grid(row=0, column=0,
        #                    padx=20, pady=20,
        #                    sticky="ew")
 
        # Generate Button
        self.makeInstanceButt = ctk.CTkButton(self,
                                         text="Create instance",
                                         command=self.newInstancePrompt,
                                         height=70, width=200)
        self.makeInstanceButt.grid(row=5, column=1,
                                        columnspan=2, padx=20, 
                                        pady=20, sticky="ew")
        
        # Generate Button
        self.deleteInstanceButt = ctk.CTkButton(self,
                                         text="Delete instance",
                                         command=self.deleteInstancePrompt,
                                         fg_color="darkred",
                                         height=70, width=200)
        self.deleteInstanceButt.grid(row=5, column=6,
                                        columnspan=2, padx=20, 
                                        pady=20, sticky="ew")

        self.instance_buttons = []
        
        col = -220
        colc1 = 0
        rowa = 120
        for s in subfolders:
            print(s)
            col += 240
            colc1 += 1
            if (colc1 == 4):
                colc1 = 0
                col = 20
                rowa += 300

            self.makeStartButt = ctk.CTkButton(self,
                                         text=s,
                                         command=lambda s=s: self.playInstance(s),
                                         height=200, width=200)
            self.makeStartButt.place(x=col, y=rowa)

            self.editModsButt = ctk.CTkButton(self,
                                         text="Edit mods",
                                         command=lambda s=s: self.editModsOf(s),
                                         fg_color="#103f74",
                                         height=60, width=200)
            self.editModsButt.place(x=col, y=rowa+200)

            self.instance_buttons.append(self.makeStartButt)
            self.instance_buttons.append(self.editModsButt)
 
    # This function is used to insert the 
    # details entered by users into the textbox

    def editModsOf(self, instanceName):
        the_path = f"{Lethal_Company_Directory}\\BepInEx\\Instances\\{instanceName}"
        path = os.path.realpath(the_path)
        os.startfile(path)


    def destroy(self):
       self.quit()

    def deleteInstancePrompt(self):
        del_instance_name = simpledialog.askstring("Input", "Enter the name of the instance you wish to delete:")
        if del_instance_name is None or del_instance_name == "":
            # If the user clicked "Cancel" or closed the dialog box, don't create a new instance
            return
        
        try:
            shutil.rmtree(f"{Lethal_Company_Directory}\\BepInEx\\Instances\\{del_instance_name}")
        except OSError as e:
            print("Error: %s - %s." % (e.filename, e.strerror))
        
        # Update the list of instances
        InstancesFolder = f"{Lethal_Company_Directory}\\BepInEx\\Instances"
        subfolders = [item.name for item in Path(InstancesFolder).iterdir() if item.is_dir()]

        # Delete old buttons
        for button in self.instance_buttons:
           button.destroy()

        # Clear the list of instance buttons
        self.instance_buttons.clear()

        # Recreate buttons for each instance
        col = -220
        colc1 = 0
        rowa = 120
        for s in subfolders:
            print(s)
            col += 240
            colc1 += 1
            if (colc1 == 4):
                colc1 = 0
                col = 20
                rowa += 300

            self.makeStartButt = ctk.CTkButton(self,
                                         text=s,
                                         command=lambda s=s: self.playInstance(s),
                                         height=200, width=200)
            self.makeStartButt.place(x=col, y=rowa)

            self.editModsButt = ctk.CTkButton(self,
                                         text="Edit mods",
                                         command=lambda s=s: self.editModsOf(s),
                                         fg_color="#103f74",
                                         height=60, width=200)
            self.editModsButt.place(x=col, y=rowa+200)

            self.instance_buttons.append(self.makeStartButt)
            self.instance_buttons.append(self.editModsButt)

    def newInstancePrompt(self):
        new_instance_name = simpledialog.askstring("Input", "Enter a name for the new instance:")
        if new_instance_name is None or new_instance_name == "":
            # If the user clicked "Cancel" or closed the dialog box, don't create a new instance
            return

        new_instance = f"{Lethal_Company_Directory}\\BepInEx\\Instances\\{new_instance_name}"
        os.mkdir(new_instance)
        path = os.path.realpath(new_instance)
        os.startfile(path)

        # Update the list of instances
        InstancesFolder = f"{Lethal_Company_Directory}\\BepInEx\\Instances"
        subfolders = [item.name for item in Path(InstancesFolder).iterdir() if item.is_dir()]

        # Delete old buttons
        for button in self.instance_buttons:
           button.destroy()

        # Clear the list of instance buttons
        self.instance_buttons.clear()

        # Recreate buttons for each instance
        col = -220
        colc1 = 0
        rowa = 120
        for s in subfolders:
            print(s)
            col += 240
            colc1 += 1
            if (colc1 == 4):
                colc1 = 0
                col = 20
                rowa += 300

            self.makeStartButt = ctk.CTkButton(self,
                                         text=s,
                                         command=lambda s=s: self.playInstance(s),
                                         height=200, width=200)
            self.makeStartButt.place(x=col, y=rowa)

            self.editModsButt = ctk.CTkButton(self,
                                         text="Edit mods",
                                         command=lambda s=s: self.editModsOf(s),
                                         fg_color="#103f74",
                                         height=60, width=200)
            self.editModsButt.place(x=col, y=rowa+200)

            self.instance_buttons.append(self.makeStartButt)
            self.instance_buttons.append(self.editModsButt)
            
    def playInstance(self, nameofInstance):
        print(f"Playing instance {nameofInstance}...")
        filesa = f"{Lethal_Company_Directory}\\BepInEx\\plugins"

        source_directory = f"{Lethal_Company_Directory}\\BepInEx\\Instances\\{nameofInstance}"
        destination_directory = f"{Lethal_Company_Directory}\\BepInEx\\plugins"

        for filename in os.listdir(filesa):
            file_path = os.path.join(filesa, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f'Failed to delete {file_path}. Reason: {e}')
        

        for filename in os.listdir(source_directory):
            source_file = os.path.join(source_directory, filename)
            destination_file = os.path.join(destination_directory, filename)
            
            for filename in os.listdir(filesa):
                file_path = os.path.join(filesa, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                except Exception as e:
                    print(f'Failed to delete {file_path}. Reason: {e}')

            for filename in os.listdir(source_directory):
                source_file = os.path.join(source_directory, filename)
                destination_file = os.path.join(destination_directory, filename)
                
                if os.path.isfile(source_file):
                    shutil.copy(source_file, destination_directory)
                elif os.path.isdir(source_file):
                    shutil.copytree(source_file, destination_file)
        
                # Specify the path to your .exe file
        exe_path = f"{Lethal_Company_Directory}\\Lethal Company.exe"

        # Run the .exe file
        os.startfile(exe_path)
        self.quit()
        
    


# App Class
class pickDirClass(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        self.title("MultiLC")

        self.resizable(False,False)

        self.nameLabel = ctk.CTkLabel(self,
                                      text="No directory selected. Would you like to pick one now?")
        self.nameLabel.grid(row=0, column=0,
                            padx=20, pady=20,
                            sticky="ew")
 
        # Generate Button
        self.pickFolderButt = ctk.CTkButton(self,
                                         text="Yes",
                                         command=self.pickDir,
                                         height=70, width=200)
        self.pickFolderButt.grid(row=5, column=1,
                                        columnspan=2, padx=20, 
                                        pady=20, sticky="ew")
 
    # This function is used to insert the 
    # details entered by users into the textbox
    def pickDir(self):
        global Lethal_Company_Directory
        prompter = promptlib.Files()

        dir = prompter.dir()

        print(dir)
        with open('lc_loc.txt', 'w') as fi:
            fi.write(dir)
        contents_real = os.path.isdir(dir)
        if contents_real == True:
            Lethal_Company_Directory = dir
            self.pickFolderButt.destroy()
            self.nameLabel = ctk.CTkLabel(self,
                                      text="Close this window and re-open the program.")
            self.nameLabel.grid(row=0, column=0,
                                padx=20, pady=20,
                                sticky="ew")
            #self.quit()
            self.destroy()
            app = App()
            app.mainloop()
            app.quit()
            #self.destroy()


if __name__ == "__main__":

    open('lc_loc.txt', 'a').close()


    with open('lc_loc.txt') as f:
        contents = f.read()
        contents_real = os.path.isdir(contents)
        if contents_real == False:
            contents = ""
        if contents == "":
            nerd = pickDirClass()
            nerd.mainloop()
        else:
            Lethal_Company_Directory = contents
            app = App()
            app.mainloop()

    #prompter = promptlib.Files()

    #dir = prompter.dir()
    #file = prompter.file()

    #print(dir, '\n', file)

    #app = App()
    #app.mainloop()
