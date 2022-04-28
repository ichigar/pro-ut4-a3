import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import filedialog
from tkinter import messagebox

class MainApplication():
    def __init__(self, parent):
        self.parent = parent
        self.configure_window(self.parent, 430, 670)
        self.add_widgets()
        self.add_menu()
        
    def configure_window(self, parent, width, height):
        """Inicializa ventana y la centra en pantalla"""
        parent.title("Widgets Tkinter")

        # get screen width and height
        screen_width = parent.winfo_screenwidth()
        screen_height = parent.winfo_screenheight()

        # calculate position x and y coordinates
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        parent.geometry('%dx%d+%d+%d' % (width, height, x, y))        
        
        parent.minsize(width, height)
        parent.resizable(width=False, height=False)
        
    def add_widgets(self):
        # Contenido ventana
        # Fila 0
        self.etiqueta = tk.Label(self.parent, text="Etiqueta: ", font=("Arial", 12))
        self.entrada = tk.Entry(self.parent, width=10)
        self.etiqueta.grid(padx=10, pady=5, column=0, row=0, sticky="w")
        self.entrada.grid(padx=10, pady=5, column=1, row=0, sticky="w")

        # Fila 1
        self.comboetiqueta = tk.Label(self.parent, text="Combobox: ", font=("Arial", 12))
        self.combo = ttk.Combobox(self.parent)

        self.combo['values'] = ("primer elemento", 2, 3, 4, 5, "Texto")
        self.combo.current(5)  # set the selected item

        self.comboetiqueta.grid(padx=10, pady=5, column=0, row=1, sticky="w")
        self.combo.grid(padx=10, pady=5, column=1, row=1, sticky="w")

        # Fila 2
        self.radetiqueta = tk.Label(self.parent, text="Radiobuttons: ", font=("Arial", 12))
        self.radetiqueta.grid(padx=10, pady=5, column=0, row=2, sticky="w")
        
        # Fila 3
        self.v1 = tk.StringVar()
        self.rad1 = ttk.Radiobutton(self.parent, text='First', value=1, var=self.v1)
        self.rad2 = ttk.Radiobutton(self.parent, text='Second', value=2, var=self.v1)
        self.rad3 = ttk.Radiobutton(self.parent, text='Third', value=3, var=self.v1)
        
        self.rad1.grid(padx=10, pady=5, column=0, row=3, sticky="w")
        self.rad2.grid(padx=10, pady=5, column=1, row=3, sticky="w")
        self.rad3.grid(padx=10, pady=5, column=2, row=3, sticky="w")        
        
        # Fila 4
        self.v2 = tk.StringVar()
        self.rad4 = ttk.Radiobutton(self.parent, text='Fourth', value=4, var=self.v2)
        self.rad5 = ttk.Radiobutton(self.parent, text='Fifth', value=5, var=self.v2)
        self.rad6 = ttk.Radiobutton(self.parent, text='Sixth', value=6, var=self.v2)

        self.rad4.grid(padx=10, pady=5, column=0, row=4, sticky="w")
        self.rad5.grid(padx=10, pady=5, column=1, row=4, sticky="w")
        self.rad6.grid(padx=10, pady=5, column=2, row=4, sticky="w")

        # Fila 5
        self.cuadro = scrolledtext.ScrolledText(self.parent, width=20, height=5)
        self.cuadro.insert(tk.INSERT, 'You text goes here')
        self.cuadro.grid(padx=10, pady=5, column=0, columnspan=3, row=5, sticky="ew")

        # Fila 6
        self.limpiar = ttk.Button(self.parent, text="Limpiar", command=self.limpiar_cuadro)
        self.limpiar.grid(padx=10, pady=5, column=0, row=6, sticky="w")

        # Fila 7
        self.spin = ttk.Spinbox(self.parent, values=(1, 2, 3, 4, 5, 6), width=5 )
        self.spin.set(3)
        self.spin.grid(padx=10, pady=5, column=0, row=7, sticky="w")

        # Fila 8
        self.radetiqueta = tk.Label(self.parent, text="Checkbutton: ", font=("Arial", 12))
        self.radetiqueta.grid(padx=10, pady=5, column=0, row=8, sticky="w")
        
        # Fila 9
        self.chk_value = tk.BooleanVar()
        self.chk = ttk.Checkbutton(self.parent, text="Seleccionar", var=self.chk_value) 
        self.chk.grid(padx=10, pady=5, column=0, row=9, sticky="w")
        
        # Fila 10
        self.salida = tk.Text(self.parent, background="white", width=20, height=10)
        
        self.salida.config(state=tk.NORMAL)
        self.salida.insert(tk.INSERT, 'Muestro un resultado')
        self.salida.config(state=tk.DISABLED)
        
        self.salida.grid(padx=10, pady=5, column=0, columnspan=3, row=10, sticky="ew")
        
        # Fila 11
        self.enviar = ttk.Button(self.parent, text="Enviar", command=self.enviar)
        self.enviar.grid(padx=10, pady=5, column=0, row=11, sticky="w")

        self.chk = ttk.Button(self.parent, text="Subventana", command=self.sub_ventana) 
        self.chk.grid(padx=10, pady=5, column=2, row=11, sticky="w")
        
    def add_menu(self):
        # Barra de menús
        menu = tk.Menu(self.parent)
        new_item1 = tk.Menu(menu)
        new_item1.add_command(label='Nuevo')
        new_item1.add_command(label='Abrir', command=self.abrir)
        new_item1.add_command(label='Guardar')
        new_item2 = tk.Menu(menu)
        new_item2.add_command(label='Cortar')
        new_item2.add_command(label='Copiar')
        new_item2.add_command(label='Pegar')
        menu.add_cascade(label='Archivo', menu=new_item1)
        menu.add_cascade(label='Edición', menu=new_item2)
        self.parent.config(menu=menu)
    
    def limpiar_cuadro(self):
        self.cuadro.delete("1.0", tk.END)
    
    def enviar(self):
        salida = ""
        salida += f"Entrada: {self.entrada.get()}\n"
        salida += f"Combobox: {self.combo.get()}\n"
        salida += f"Radiobuttons 1: {self.v1.get()}\n"
        salida += f"Radiobuttons 2: {self.v2.get()}\n"
        salida += f"Cuadro de texto: {self.cuadro.get('1.0', tk.END)}\n"
        salida += f"Spinbox: {self.spin.get()}\n"
        salida += f"Checkbutton: {self.chk_value.get()}\n"
        self.insertar_salida(salida)
    
    def insertar_salida(self, texto):    
        self.salida.config(state=tk.NORMAL)     # Activamos el cuadro de texto de salida
        self.salida.delete("1.0", tk.END)       # Limpiamos el cuadro de texto de salida
        self.salida.insert(tk.INSERT, texto)   # Insertamos la salida en el cuadro de texto de salida
        self.salida.config(state=tk.DISABLED)   # Desactivamos el cuadro de texto de salida
        
    def abrir(self):
        # lanzamos diálogo para leer fichero
        self.files = filedialog.askopenfilename(filetypes = (("Text files","*.txt"),("Mark Down files","*.md"),("all files","*.*")))
        self.path = tk.StringVar()
        self.path.set(self.files)
        
        messagebox.showinfo("Ruta al archivo", self.path.get())    # Mostramos la ruta del fichero
        salida = self.leer_archivo(self.path.get())                # Obtenemos el contenido del fichero
        self.insertar_salida(salida)                               # Lo mostramos en la salida
        
    def leer_archivo(self, path):
        with open(path, "r") as file:
            salida = file.read()
        return salida
    
    def insertar_salida(self, salida):
            self.salida.config(state=tk.NORMAL)     # Activamos el cuadro de texto de salida
            self.salida.delete("1.0", tk.END)       # Limpiamos el cuadro de texto de salida
            self.salida.insert(tk.INSERT, salida)   # Insertamos la salida en el cuadro de texto de salida
            self.salida.config(state=tk.DISABLED)   # Desactivamos el cuadro de texto de salida
            
    def sub_ventana(self):
        SubWindow(self.parent)
        


class SubWindow():
    def __init__(self, parent):
        self.parent = parent   # Guardamos referencia a la ventana padre
        
        # Creamos la subventana
        self.sub_w = tk.Toplevel(self.parent)
        
        # Ocultamos la ventana principal
        self.parent.withdraw() 
        self.sub_w.protocol("WM_DELETE_WINDOW", self.cerrar) # Definimos acción al cerrar sub ventana
        # Configuramos la ventana
        self.configure_window(self.sub_w, 500, 200)
        self.add_tabs()
        
    def add_tabs(self):    
        # Creamos pestañas    
        tab_control = ttk.Notebook(self.sub_w)
        self.tab1 = tk.Frame(tab_control)
        self.tab2 = tk.Frame(tab_control)
        tab_control.add(self.tab1, text='Primera')
        tab_control.add(self.tab2, text='Segunda')
        tab_control.pack(expand=1, fill='both')

        # Etiqueta en pestaña 1
        self.tab1_lab = tk.Label(self.tab1, text="Pestaña", font=("Arial", 12))
        self.tab1_lab.grid(padx=10, pady=5, column=0, row=2, sticky="w")
        
        # Tabla en pestaña 2
        self.tabla(self.tab2) 
        
    def configure_window(self, sub_w, width, height):
        # Definimos el contenido de la subventana
        sub_w.title("Sub Ventana")
        sub_w.minsize(width, height)
        # sub_w.resizable(width=False, height=False)
        

        # get screen width and height
        screen_width = sub_w.winfo_screenwidth()
        screen_height = sub_w.winfo_screenheight()

        # calculate position x and y coordinates
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        sub_w.geometry('%dx%d+%d+%d' % (width, height, x, y))        
        
        sub_w.minsize(width, height)
        sub_w.resizable(width=False, height=False)
        
    def cerrar(self):
        """Se ejecuta en caso de cerrar la sub ventana"""
        self.parent.deiconify() # Recuperar ventana principal
        # self.sub_w.withdraw()   # Ocultar subventa
        self.sub_w.destroy()    # Destruir subventana
        
    def tabla(self, tab):
        """Tabla de campos de entrada"""
        for r in range(5):
            for c in range(5):
                cell = ttk.Entry(tab, width=10)
                cell.grid(padx=5, pady=5, row=r, column=c)
                cell.insert(0, '({}, {})'.format(r, c))  

if __name__ == '__main__':
    root = tk.Tk()
    MainApplication(root)
    root.mainloop()
