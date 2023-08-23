#--------------------lib----------------------------
import customtkinter


#import script
#--------------------------------------------------
customtkinter.set_appearance_mode("System")    #modo de apariencia del sistema
customtkinter.set_default_color_theme("blue")  #establece el color de la app en azul 
#--------------------------------------------------

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("prueba")
        self.geometry(f"{350}x{500}")  
        self.resizable(width=False, height=False)   
        #-----------------------------------
        self.f1=customtkinter.CTkFrame(self,fg_color="transparent")
        self.f1.grid(row=0,column=0,sticky="nswe",pady=20)
        self.texto1=customtkinter.CTkLabel(self.f1,text="Monitoreo",justify="center",font=customtkinter.CTkFont(size=20,weight="bold"))
        self.texto1.grid(row=0,column=0,sticky="nswe")

        self.f2=customtkinter.CTkFrame(self,fg_color="transparent")
        self.f1.grid(row=1,column=0,sticky="nswe",pady=20)


if __name__ == "__main__":
    app = App()
    app.mainloop()





