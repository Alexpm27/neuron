import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from neuron import Neuron
from utilities.graphic import graphic_norm, graphic_w
from PIL import Image, ImageTk


class NeuronGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Neuron")

        self.csv = tk.StringVar()
        self.init_population_var = tk.IntVar()
        self.iterations = tk.IntVar()
        self.eta = tk.DoubleVar()
        self.tolerance = tk.DoubleVar()
        self.ep = tk.Label(self.root)
        self.ene = tk.Label(self.root)
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Load CSV:").grid(row=0, column=0, sticky="w")
        tk.Entry(self.root, textvariable=self.csv).grid(row=0, column=1)
        tk.Button(self.root, text="Browse", command=self.browse_csv).grid(row=0, column=2)

        tk.Label(self.root, text="ETA:").grid(row=1, column=0, sticky="w")
        tk.Entry(self.root, textvariable=self.eta).grid(row=1, column=1)

        tk.Label(self.root, text="Iterations:").grid(row=1, column=2, sticky="w")
        tk.Entry(self.root, textvariable=self.iterations).grid(row=1, column=3)

        tk.Label(self.root, text="Tolerance:").grid(row=2, column=0, sticky="w")
        tk.Entry(self.root, textvariable=self.tolerance).grid(row=2, column=1)

        tk.Button(self.root, text="Run", command=self.run_neuron_training).grid(row=10, column=0, columnspan=4)

        self.ep.grid(row=12, column=0, columnspan=4)
        self.ene.grid(row=13, column=0, columnspan=4)

        self.root.mainloop()

    def run_neuron_training(self):
        neuron = Neuron(csv_path=self.csv, eta=self.eta.get(),
                        tolerance=self.tolerance.get(),
                        iterations=self.iterations.get())
        errors, w_by_iterations, results = neuron.training()
        print(w_by_iterations)

        graphic_norm(errors)
        graphic_w(w_by_iterations)

        self.load_image()
        messagebox.showinfo("Alert", f"Initial w:{w_by_iterations[0]} \n\n"
                                     f"Final w: {w_by_iterations[-1]} ")

    def browse_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if file_path:
            self.csv.set(file_path)
        else:
            print("no file csv")

    def load_image(self):
        ep = "../interface/graphics/evolucion_de_pesos.png"
        ene = "../interface/graphics/evolucion_norma_error.png"
        ep_img = Image.open(ep)
        ene_img = Image.open(ene)

        photo_ep = ImageTk.PhotoImage(ep_img.resize((640, 380)))
        photo_ene = ImageTk.PhotoImage(ene_img.resize((640, 380)))

        self.ep.configure(image=photo_ep)
        self.ene.configure(image=photo_ene)
        self.ep.image = photo_ep
        self.ene.image = photo_ene


root = tk.Tk()
app = NeuronGUI(root)
