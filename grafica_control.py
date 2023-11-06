import tkinter as tk
import mysql.connector
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

ventana_control = None
opciones_frame = None

def cerrar_ventana_control():
    global ventana_control
    if ventana_control is not None:
        ventana_control.destroy()

def mostrar_ventana_control():
    global ventana_control
    if ventana_control is None:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456",  # Cambia esto a tu contraseña de MySQL
            database="grupal_10"  # Cambia esto a tu base de datos
        )
        
        if ventana_control is None:
            ventana_control = tk.Tk()
        ventana_control.title("Control de Produccion")
        ventana_control.geometry("800x600")
        ventana_control.configure(bg="#9A74F6")
        
        cursor = mydb.cursor()
        cursor.execute("SELECT producto, cantidad, estado_de_produccion FROM estado_de_produccion")  # Ajusta la consulta según tus necesidades
        result = cursor.fetchall()
        
        productos = [row[0] for row in result]
        cantidad = [row[1] for row in result]
        fases = [row[2] for row in result]

        # Crear un gráfico de barras apiladas
        fig, ax = plt.subplots()
        fases_unicas = list(set(fases))
        data = []

        for fase in fases_unicas:
            data.append([cantidad[i] if f == fase else 0 for i, f in enumerate(fases)])

        bottom = None
        for i in range(len(fases_unicas)):
            ax.bar(productos, data[i], label=fases_unicas[i], bottom=bottom)
            if bottom is None:
                bottom = data[i]
            else:
                bottom = [bottom[j] + data[i][j] for j in range(len(data[i]))]

        ax.set_xlabel('Productos')
        ax.set_ylabel('Cantidad')
        ax.set_title('Control de Producción por Producto')
        ax.legend()
        
        container = tk.Frame(ventana_control, bg="#9A74F6")
        container.place(relx=0, rely=0.1, relwidth=1, relheight=0.9)
        
        canvas = FigureCanvasTkAgg(fig, master=container)
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        boton_volver = tk.Button(ventana_control, text="Volver al menú", command=cerrar_ventana_control, bg="#9A74F6", fg="#20201E", font=("Helvetica", 12))
        boton_volver.place(relx=0.5, rely=0.02, anchor='n')

def abrir_ventana_control():
    global ventana_control
    ventana_control = tk.Tk()
    ventana_control.title("Control de Produccion")
    ventana_control.geometry("800x600")
    ventana_control.configure(bg="#9A74F6 ")
    
    opciones_frame = tk.Frame(ventana_control, bg="#FAF865")
    opciones_frame.place(relx=0, rely=0, relwidth=1, relheight=0.1)
    productos_button = tk.Button(opciones_frame, text="Control de Produccion", command=mostrar_ventana_control, bg="#9A74F6 ", fg="white", font=("Helvetica", 12))
    productos_button.pack(side="left", padx=10)