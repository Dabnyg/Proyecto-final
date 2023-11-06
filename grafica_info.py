import tkinter as tk
import mysql.connector
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

ventana_grafica_infonutri = None  # Declarar ventana_graficas en el ámbito de nivel superior
opciones_frame = None

def cerrar_ventana_grafica_infonutri():
    global ventana_grafica_infonutri
    if ventana_grafica_infonutri is not None:
        ventana_grafica_infonutri.destroy()

def mostrar_ventana_grafica_infonutri():
    global ventana_grafica_infonutri
    if ventana_grafica_infonutri is None:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456",  # Cambia esto a tu contraseña de MySQL
            database="grupal_10"  # Cambia esto a tu base de datos
        )
        
        if ventana_grafica_infonutri is None:
            ventana_grafica_infonutri = tk.Tk()
        ventana_grafica_infonutri.title("Gráfica de Informacion nutricional")
        ventana_grafica_infonutri.geometry("800x600")
        ventana_grafica_infonutri.configure(bg="#FAF865")
        
        cursor = mydb.cursor()
        cursor.execute("SELECT producto, carbohidratos FROM información_nutricional")  # Ajusta la consulta según tus necesidades
        result = cursor.fetchall()
        
        productos = [row[0] for row in result]
        carbohidratos = [row[1] for row in result]

        # Crear un gráfico de pastel
        fig, ax = plt.subplots()
        ax.pie(carbohidratos, labels=productos, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')  # Esto asegura que el gráfico de pastel sea un círculo.

        ax.set_title("Gráfico de Carbohidratos")
        
        container = tk.Frame(ventana_grafica_infonutri, bg="#FAF865")
        container.place(relx=0, rely=0.1, relwidth=1, relheight=0.9)
        
        canvas = FigureCanvasTkAgg(fig, master=container)
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        boton_volver = tk.Button(ventana_grafica_infonutri, text="Volver al menú", command=cerrar_ventana_grafica_infonutri, bg="#FAF865", fg="#20201E", font=("Helvetica", 12))
        boton_volver.place(relx=0.5, rely=0.02, anchor='n')

def abrir_ventana_grafica_infonutri():
    global ventana_grafica_infonutri
    ventana_grafica_infonutri = tk.Tk()
    ventana_grafica_infonutri.title("Grafica Informacion nutricional")
    ventana_grafica_infonutri.geometry("800x600")
    ventana_grafica_infonutri.configure(bg="#FAF865")
    
    opciones_frame = tk.Frame(ventana_grafica_infonutri, bg="#FAF865")
    opciones_frame.place(relx=0, rely=0, relwidth=1, relheight=0.1)
    productos_button = tk.Button(opciones_frame, text="Grafica Informacion nutricional", command=mostrar_ventana_grafica_infonutri, bg="#FAF865", fg="white", font=("Helvetica", 12))
    productos_button.pack(side="left", padx=10)