from doctest import master
import tkinter
import tkinter.filedialog

import tkinter.messagebox
import customtkinter
from PIL import Image, ImageTk
import numpy as np
from utils import inference
import warnings
warnings.filterwarnings("ignore")

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):

    WIDTH = 784
    HEIGHT = 520

    def __init__(self):
        super().__init__()

        self.title("Cartoonizer App")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed

        # ============ create two frames ============

        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)
        
            
            
            

        # ============ frame_left ============

        # configure grid layout (1x11)
        self.frame_left.grid_rowconfigure(0, minsize=10)   # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(5, weight=1)  # empty row as spacing
        self.frame_left.grid_rowconfigure(8, minsize=10)    # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing

        self.label_1 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="Cartoonizer App",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_1.grid(row=1, column=0, pady=10, padx=10)
        
        self.label_2 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="This is a simple app to cartoonize images.",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_2.grid(row=2, column=0, pady=10, padx=10)

        self.button_upload = customtkinter.CTkButton(master=self.frame_left, text="Upload Image", command=self.upload_image)
        self.button_upload.grid(row=4, column=0, pady=10, padx=20)
        
        self.button_cartoonize = customtkinter.CTkButton(master=self.frame_left, text="Cartoonize Image", command=self.inference_image)
        self.button_cartoonize.grid(row=5, column=0, pady=10, padx=20)
        
        
        self.button_save = customtkinter.CTkButton(master=self.frame_left, text="Save Image", command=self.save_file)
        self.button_save.grid(row=5, column=1, pady=10, padx=20)


        self.label_mode = customtkinter.CTkLabel(master=self.frame_left, text="Appearance Mode:")
        self.label_mode.grid(row=6, column=0, pady=0, padx=20, sticky="w")

        self.optionmenu_1 = customtkinter.CTkOptionMenu(master=self.frame_left,
                                                        values=["Light", "Dark", "System"],
                                                        command=self.change_appearance_mode)
        self.optionmenu_1.grid(row=7, column=0, pady=10, padx=20, sticky="w")

        # ============ frame_right ============

        # configure grid layout (3x7)
        self.frame_right.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right.rowconfigure(7, weight=10)
        self.frame_right.columnconfigure((0, 1), weight=1)
        self.frame_right.columnconfigure(2, weight=0)

        # # configure grid layout (1x1)
        # self.frame_info.rowconfigure(0, weight=1)
        # self.frame_info.columnconfigure(0, weight=1)


        # set default values
        self.optionmenu_1.set("Dark")
        
    def upload_image(self):
        file_path = tkinter.filedialog.askopenfilename(defaultextension=".png, .jpg, .jpeg, .gif",filetypes=[("Image Files", ".png .jpg .jpeg .gif")])
        myimage = Image.open(file_path)
        myimage.save("input.png")
        # display image
        myimage2 = Image.open("input.png").resize((256, 256), Image.ANTIALIAS)
        myimage2 = ImageTk.PhotoImage(myimage2)
        self.display_image = customtkinter.CTkButton(master=self.frame_right,bg_color="black",text="Your Image", text_font=("Roboto Medium", -16), image=myimage2)
        self.display_image.grid(row=2, column=0, columnspan=1, rowspan=1, pady=1, padx=1, sticky="nsew")
        #self.display_image.configure(image=ImageTk.PhotoImage("input.png"))
        
        
        
        
    def inference_image(self):
        myimage = Image.open("input.png")
        myimage= np.asarray(myimage)
        inference(myimage)
        myimage2 = Image.open("output.png").resize((256, 256), Image.ANTIALIAS)
        myimage2 = ImageTk.PhotoImage(myimage2)
        self.display_cartoon_image = customtkinter.CTkButton(master=self.frame_right, bg_color=None, text=None,text_font=("Roboto Medium", -16), image=myimage2)
        self.display_cartoon_image.grid(row=3, column=0, columnspan=1, rowspan=1, pady=10, padx=10, sticky="nsew")
        # display image to the right
        
    def save_file(self):
        file_path = tkinter.filedialog.asksaveasfilename(initialfile="output.png",defaultextension=".png",filetypes=[("Image Files", ".png")])
        myimage = Image.open("output.png")
        myimage.save(file_path)

    def change_appearance_mode(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def on_closing(self, event=0):
        self.destroy()


if __name__ == "__main__":
    app = App()
    app.iconbitmap('logo.ico')
    app.update()
    app.mainloop()
    