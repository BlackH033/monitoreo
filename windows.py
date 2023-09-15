#--------------librerias --------------
import customtkinter
import os
from PIL import Image
#--------------------------------------

class ventana_secundaria(customtkinter.CTkToplevel):
    carpeta_raiz=os.path.dirname(__file__)                 #guarda la ruta donde se encuentra este archivo .py
    carpeta_img=os.path.join(carpeta_raiz,"img")  

    def __init__(self):
        super().__init__()
        self.grab_set()
        self.geometry(f"{620}x{450}")  
        self.resizable(width=False, height=False)          #no permite cambiar el tamaño de la ventana
        self.iconbitmap(os.path.join(ventana_secundaria.carpeta_img,"icono.ico"))
        self.grid_columnconfigure(1, weight=1)
        

    def generado_correctamente_unico(self,ruta,tiempo):
        self.title("Correcto")
        self.iconbitmap(os.path.join(ventana_secundaria.carpeta_img,"icono.ico"))
        self.iconocorrect=customtkinter.CTkImage(Image.open(os.path.join(ventana_secundaria.carpeta_img,"comprobado.png")),size=(90,90))
        self.iconocorrect=customtkinter.CTkLabel(self, image = self.iconocorrect,text="")
        self.iconocorrect.grid(row=0,column=0,pady=(20,20),sticky="nsew")
        self.textcorrecto=customtkinter.CTkLabel(self,text="Resultados generado correctamente en",font=customtkinter.CTkFont(size=18,weight="bold"))
        self.textcorrecto.grid(row=1,column=0,padx=40,pady=(0,20),sticky="nsew")
        self.textbox = customtkinter.CTkTextbox(self,width=580,height=30)
        self.textbox.insert("0.0",ruta)
        self.textbox.grid(row=2, column=0, sticky="nsew",padx=20)

        self.textcorrecto=customtkinter.CTkLabel(self,text=tiempo,font=customtkinter.CTkFont(size=14))
        self.textcorrecto.grid(row=3,column=0,padx=40,pady=(0,10),sticky="nsew")

        self.btn_cerrar = customtkinter.CTkButton(self, text ="Abrir carpeta", command = lambda:self.abrir_carpeta(ruta),fg_color="green",font=customtkinter.CTkFont(size=18,weight="bold"),hover_color="#0DAF0A",width=70)
        self.btn_cerrar.grid(row=4,column=0,sticky="nsew",pady=(20, 20),padx=230)

        self.f4=customtkinter.CTkFrame(self,corner_radius=0)
        self.f4.grid(row=5,column=0,padx=0,pady=(60,0))
        self.img2=customtkinter.CTkImage(Image.open(os.path.join(ventana_secundaria.carpeta_img,"logo_isa.png")),size=(118,63))
        self.img2_insert=customtkinter.CTkLabel(self.f4,image=self.img2,text="")
        self.img2_insert.grid(row=0,column=0,padx=(10,10))
        self.boton2=customtkinter.CTkButton(self.f4, text ="CERRAR", command = self.destroy,fg_color="red",hover_color="#A50000",font=customtkinter.CTkFont(weight="bold"),width=70)
        self.boton2.grid(row=0,column=1,padx=(390,20),pady=30)

    def abrir_carpeta(self,ruta):
        os.system(f'start {os.path.realpath(ruta)}')
    
    def barra(self):
        self.iconbitmap(os.path.join(ventana_secundaria.carpeta_img,"icono.ico"))
        self.texto=customtkinter.CTkLabel(self,text="Generando resultados",font=customtkinter.CTkFont(size=18,weight="bold"))
        self.texto.grid(row=0,column=0,sticky="nsew")
        self.barr = customtkinter.CTkProgressBar(self, orientation="horizontal")
        self.barr.grid(row=1,column=0)
        self.barr.start()
