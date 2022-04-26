import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import filedialog
from tkinter import messagebox

class MainApplication():
    def __init__(self, parent):
        self.parent = parent

        self.parent.title("Widgets Tkinter")
        self.parent.minsize(460,450)
        self.parent.resizable(width=False, height=False)
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
        self.enviar = ttk.Button(self.parent, text="Enviar", command=self.enviar)
        self.enviar.grid(padx=10, pady=5, column=0, row=10, sticky="w")

        self.chk = ttk.Button(self.parent, text="Subventana", command=self.sub_ventana) 
        self.chk.grid(padx=10, pady=5, column=2, row=10, sticky="w")
        
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
        messagebox.showinfo('Valores recogidos', salida)
        
    def sub_ventana(self):
        SubWindow(self.parent)

    def abrir(self):
        self.files = filedialog.askopenfilenames()
        self.texto = tk.StringVar()
        self.texto.set("Examinar....")
        self.texto.set(self.files)
        #file = filedialog.askopenfilename(filetypes = (("Text files","*.txt"),("all files","*.*")))


class SubWindow():
    def __init__(self, parent):
        self.parent = parent   # Guardamos referencia a la ventana padre
        
        # Creamos la subventana
        self.sub_w = tk.Toplevel(self.parent)
        
        # Ocultamos la ventana principal
        self.parent.withdraw() 
        self.sub_w.protocol("WM_DELETE_WINDOW", self.cerrar) # Definimos acción al cerrar sub ventana
        
        # Definimos el contenido de la subventana
        self.sub_w.title("Sub Ventana")
        self.sub_w.minsize(480, 180)
        # self.sub_w.resizable(width=False, height=False)
        
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
