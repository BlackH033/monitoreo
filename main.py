#--------------------lib----------------------------
from email.mime import image
import tkinter
import customtkinter
import os
from PIL import Image
from tkinter import filedialog

import script
#--------------------------------------------------
customtkinter.set_appearance_mode("System")    #modo de apariencia del sistema
customtkinter.set_default_color_theme("blue")  #establece el color de la app en azul 
#--------------------------------------------------

class App(customtkinter.CTk):
    carpeta_raiz=os.path.dirname(__file__)          #guarda la ruta donde se encuentra este archivo .py
    carpeta_img=os.path.join(carpeta_raiz,"img")    #crea la ruta relativa a la carpeta /img - la cual se guarda en la misma ruta del archivo .py

    def __init__(self):
        super().__init__()
        self.title("Monitoreo mediante NDVI")
        self.geometry(f"{310}x{450}")  
        self.resizable(width=False, height=False)
        self.iconbitmap(os.path.join(App.carpeta_img,"icono.ico"))    
        #-----------------------------------
        self.back=customtkinter.CTkFrame(self, width=310, corner_radius=0,fg_color="transparent")
        self.back.grid(row=0,column=0,rowspan=4,sticky="nsew")
        self.back.grid_rowconfigure(4, weight=1)

        self.f1=customtkinter.CTkFrame(self.back,fg_color="transparent")
        self.f1.grid(row=0,column=0,sticky="nswe",pady=20)
        self.texto1=customtkinter.CTkLabel(self.f1,text="Monitoreo",font=customtkinter.CTkFont(size=20,weight="bold"))
        self.texto1.grid(row=0,column=0,sticky="nswe",padx=100)

        self.f2=customtkinter.CTkFrame(self.back,fg_color="transparent")
        self.f2.grid(row=1,column=0,sticky="nswe",pady=10)
        self.img1=customtkinter.CTkImage(Image.open(os.path.join(App.carpeta_img,"carpeta.png")),size=(150,150))
        self.img1_insert=customtkinter.CTkLabel(self.f2,image=self.img1,text="")
        self.img1_insert.grid(row=0,column=0,sticky="nswe",padx=80)

        self.f3=customtkinter.CTkFrame(self.back,fg_color="transparent")
        self.f3.grid(row=2,column=0,pady=(0,20))
        self.value=tkinter.IntVar(value=1)
        self.radio_boton1=customtkinter.CTkRadioButton(self.f3,variable=self.value,value=0,text="Múltiple",font=customtkinter.CTkFont(weight="bold"))
        self.radio_boton1.grid(row=0,column=0,sticky="nsew")
        self.radio_boton2=customtkinter.CTkRadioButton(self.f3,variable=self.value,value=1,text="Único",font=customtkinter.CTkFont(weight="bold"))
        self.radio_boton2.grid(row=0,column=1,sticky="nsew")

        self.f4=customtkinter.CTkFrame(self.back,fg_color="transparent")
        self.f4.grid(row=3,column=0)
        self.boton1=customtkinter.CTkButton(self.f4, text="Agregar carpeta",command=self.carpeta,font=customtkinter.CTkFont(size=18,weight="bold"),height=40,width=200)
        self.boton1.grid(row=0,column=0)

        self.f4=customtkinter.CTkFrame(self.back,width=310,corner_radius=0)
        self.f4.grid(row=4,column=0,padx=0,pady=(50,0))
        self.img2=customtkinter.CTkImage(Image.open(os.path.join(App.carpeta_img,"logo_isa.png")),size=(118,63))
        self.img2_insert=customtkinter.CTkLabel(self.f4,image=self.img2,text="")
        self.img2_insert.grid(row=0,column=0,padx=(10,10))
        self.boton2=customtkinter.CTkButton(self.f4, text ="CERRAR", command = self.destroy,fg_color="red",hover_color="#A50000",font=customtkinter.CTkFont(weight="bold"),width=70)
        self.boton2.grid(row=0,column=1,padx=(80,20),pady=30)

    def carpeta(self):
        filename = filedialog.askdirectory(
            parent=self,
            title="Agregar carpeta de trabajo | Monitoreo"
        )
        print(self.value.get())
        if filename!="":
            script.procesamiento(filename,self.value.get())



            
        
if __name__ == "__main__":
        app = App()
        app.mainloop()
    
    





