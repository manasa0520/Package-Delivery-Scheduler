import tkinter as ti from tkinter impart ttk from queue import PriorityQueue

class ParceiDeliveryApp:

definit (self, master):

self.master = master

self.master.title("Parcel Delivery SJF Scheduling")

self.queue PriorityQueue()

self.label_parcel name tk.Label(master, text-"Parcal Name: self.label_parcel_name.grid(row=9, column=0, padx-10, pady-10)

self-entry parcel name tk.Entry(master)

self.antry parcel name.grid(row=8, column-1, padx-18, pady-18)


self.label_delivery time tk.Label(master, text-"Delivery Time:")

self-label delivery time.grid(row=1, column=-8, padx-19, pady-18)


self.entry delivery time tk.Entry(master)

self.entry_delivery time.grid(row=1, column=1, podx-10, pady=10)


self.button_add_parcel = tk.Button(master, text="Add Parcel", command-self.add_parcel)

self.button_add_parcel.grid(row=2, column=8, columspan=2, pady=10)

salf_button_add_parcel.grid(cow-2, column-d, columnspan=2, pady-18}

self.tree=tt. Trouvientmaster, column("Pars) Name", "Delivery Time"))

self.tree.heading("a", toxt="ID")

self.tree.heading("Parcel Name", text "Purzel Name)

self.tree.heading("Delivery Time", texte "Delivery Tina") self.tree.grid(round, columna, columnspan, pada-10, pady-10)

self.button_schedule_delivery tk.Button(paste, texte schedule Delivery", commandrself.schedule salf.button_schedule_delivery.grid(row-4, column-, columnapan-2, pady-18)

def add parcw1(s)

parcel name = self.entry parcel nome.get() delivery time int(self,entry_delivery_time.get())

parcel_id = len(self.queue queue) 1 self.queue.put({delivery time, parcel in, parcel name, delivery_time))

self.tree.insert("", "end", text-parcel_id, values (parcel name, delivery time))

self.entry. parcel name.delete(0, tk.END) self.entry delivery time.delete(0, th.END)

def schedule delivery(self):

reqult window = tk. oplevelfalfaston)

self.queue.put((delivery tine, parcel id, parcel name, delivery_time}}

self.tree.insert("","and", textsparcel_id, values parcel_nee, delivery_time))

self.untry parcel name.delete(e, tx.END) self entry delivery time.delete(0, END)

schedule delivery(self)

result_window= tk. Toplevel (self.master) result window.title("Delivery Schedule")

delivery_label = tk.label(result_window, text="Delivery Schedule) delivery_label.pack()

mile mit swl.queue.umpty(): parcel id, parcel name, delivery time = self.queue.get()

schedule_text = "Parcel (parcel id) (parcel name) Estimated Delivery Time: (delivery time) schedule label.Label(result_window, text-schedule_text)

schedule label.pack()

root = tx.TR()

app = Parcelielivery App(root) root_nainloop)
