import tkinter as tk

root = tk.Tk()
root.title("Handy App")
root.geometry("360x640")

main_frame = tk.Frame(root, bg="#f0f0f0")
main_frame.grid(row=0, column=0, sticky="nsew")



def erstelle_label(parent, text_inhalt, zeile, spalte):
    label = tk.Label( parent , text=text_inhalt , font=("Arial", 14) , bg="#f0f0f0" , fg="#333333" )
    label.pack(side="left",padx=10)
    return text_inhalt

def erstelle_checkbox(parent, zeile, spalte):
    var = tk.IntVar()
    checkbox = tk.Checkbutton(parent , variable=var , command=berechne)
    checkbox.pack(side="left",padx=10)
    return var

def erstelle_dropdown(parent,options,standart,zeile,spalte):
    var = tk.StringVar(parent)
    var.set(standart)
    dropdown = tk.OptionMenu(parent,var,*options)
    dropdown.config(font=("Arial", 12), bg="white", fg="#333333")
    dropdown.pack(side="left",padx=10)
    return var

def berechne():
    print(leinwand_label,leinwand_auswahl.get(),leinwand_check.get())


zeile0_frame = tk.Frame(main_frame, bg="#f0f0f0")
zeile0_frame.grid(row=0, column=0, sticky="w", pady=10)

leinwand_standart = "A4"
leinwand_optionen = ["A5","A4","A3"]
leinwand_label = erstelle_label(zeile0_frame, "Leinwand:", zeile=0, spalte=0)
leinwand_check = erstelle_checkbox(zeile0_frame,zeile=0,spalte=1)
leinwand_auswahl = erstelle_dropdown(zeile0_frame,leinwand_optionen,leinwand_standart,zeile=0,spalte=2)


zeile1_frame = tk.Frame(main_frame, bg="#f0f0f0")
zeile1_frame.grid(row=1, column=0, sticky="w", pady=10)

style_standart = "Schwarz-Weiß"
style_optionen = ["Schwarz-Weiß"]
style_lable = erstelle_label(zeile1_frame, "Style:",   zeile=1, spalte=0)
style_auswahl = erstelle_dropdown(zeile1_frame,style_optionen,style_standart,zeile=1,spalte=1)



root.mainloop()

