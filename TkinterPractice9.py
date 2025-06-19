from tkinter import *
from tkinter import ttk

class name:
    def __init__(self):
        self.root = Tk()
        self.root.title("Superhero Name")
        self.root.configure(highlightthickness=2, highlightcolor="black", bd=0)

        self.qualities=["Happy", "Awesome", "Outgoing", "Funky"]
        self.animals=["Shark", "Dog", "Cat", "mouse"]
        self.root.configure(bg="white")
        self.j = 1
        self.a = StringVar()

        self.style = ttk.Style()
        self.style.configure("TRadiobutton", background="White", )


        self.root.rowconfigure(list(range(10)), weight=1)
        self.root.columnconfigure(0, weight=1)


        self.title = Label(self.root, font = "Verdana 16 bold", text="Hero Name Generator", bg="purple", fg= "white"  )
        self.title.grid(row=0, column=0, sticky=NSEW)


        self.quality = StringVar()




        for i in self.qualities:
            self.qual = ttk.Radiobutton(self.root, text=i, variable= self.quality, value = self.j, style="TRadiobutton").grid(row=self.j, column=0,)
            self.j += 1
        

        self.colours = Label(self.root, font = "Verdana 12 bold", text="Enter a Colour",bg="white"  )
        self.colours.grid(column=0, sticky=NSEW, pady=5)

        self.colour = Entry(self.root, justify=CENTER,bg="white", width= 23)
        self.colour.grid(column=0, pady=5)

        self.animal_label = Label(self.root, font = "Verdana 12 bold", text="Select an animal",bg="white"  )
        self.animal_label.grid(column=0, sticky=NSEW, pady=5)

        self.animal = StringVar()
        self.animal.set("")
        animal_combo = ttk.Combobox(self.root, textvariable=self.animal, state='readonly')
        animal_combo["values"] = self.animals
        animal_combo.grid(column=0)


        self.make = Button(self.root,font = "Verdana 12 bold", text="Create Name", command=self.name_maker,bg="white")
        self.make.grid(column=0, pady=10)

        self.outcome = Label(self.root, font = "Verdana 12 bold", textvariable=self.a,bg="white")
        self.outcome.grid(column=0)

    def name_maker(self):
        self.name = self.qualities[int(self.quality.get())-1] + self.colour.get() + self.animal.get()
        self.a.set(f"You are the " + self.name)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = name()
    app.run()


