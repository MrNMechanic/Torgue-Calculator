import Tkinter as tk



fields = ('Link Length_1 (m)', 'Link Length_2 (m)', 'Link Length_3 (m)','Link Mass_1 (kg)','Link Mass_2 (kg)','Link Mass_3 (kg)','Actuator Weight_1 (kg)','Actuator Weight_2 (kg)','Actuator Weight_3 (kg)','Torgue_1 (kg m)','Torgue_2 (kg m)','Torgue_3 (kg m)')

def Torgue_1(entries):
    L_1 = (float(entries['Link Length_1 (m)'].get()))
    W_1 = ((float(entries['Link Mass_1 (kg)'].get())))
    A_1 = (float(entries['Actuator Weight_1 (kg)'].get()))
    T_1 = (L_1*A_1)+((L_1/2)*W_1)
    T_1 = ("%8.2f" % T_1).strip()
    entries['Torgue_1 (kg m)'].delete(0, tk.END)
    entries['Torgue_1 (kg m)'].insert(0, T_1 )
    print("Torgue_1: %f" % float(T_1))

def Torgue_2(entries):
    L_1 = (float(entries['Link Length_1 (m)'].get()))
    W_1 = (float(entries['Link Mass_1 (kg)'].get()))
    A_1 = (float(entries['Actuator Weight_1 (kg)'].get()))
    L_2 = (float(entries['Link Length_2 (m)'].get()))
    W_2 = (float(entries['Link Mass_2 (kg)'].get()))
    A_2 = (float(entries['Actuator Weight_2 (kg)'].get()))
    T_2 = ((L_2+L_1)*A_1)+((L_1/2+L_2)*W_1)+(L_2*A_2)+((L_2/2)*W_2)
    T_2 = ("%8.2f" % T_2).strip()
    entries['Torgue_2 (kg m)'].delete(0, tk.END)
    entries['Torgue_2 (kg m)'].insert(0, T_2 )
    print("Torgue_2: %f" % float(T_2))

def Torgue_3(entries):
    L_1 = (float(entries['Link Length_1 (m)'].get()))
    W_1 = (float(entries['Link Mass_1 (kg)'].get()))
    A_1 = (float(entries['Actuator Weight_1 (kg)'].get()))
    L_2 = (float(entries['Link Length_2 (m)'].get()))
    W_2 = (float(entries['Link Mass_2 (kg)'].get()))
    A_2 = (float(entries['Actuator Weight_2 (kg)'].get()))
    L_3 = (float(entries['Link Length_3 (m)'].get()))
    W_3 = (float(entries['Link Mass_3 (kg)'].get()))
    A_3 = (float(entries['Actuator Weight_3 (kg)'].get()))
    T_3 = ((L_1+L_2+L_3)*A_1)+(((L_1/2)+L_2+L_3)*W_1)+((L_2+L_3)*A_2)+(((L_2/2)+L_3)*W_2)+(L_3*A_3)+((L_3/2)*W_3)
    T_3 = ("%8.2f" % T_3).strip()
    entries['Torgue_3 (kg m)'].delete(0, tk.END)
    entries['Torgue_3 (kg m)'].insert(0, T_3 )
    print("Torgue_3: %f" % float(T_3))

def makeform(root, fields):
    root.winfo_toplevel().title("Torgue Calculator")
    entries = {}
    for field in fields:
        print(field)
        row = tk.Frame(root)
        lab = tk.Label(row, width=22, text=field+": ", anchor='w')
        ent = tk.Entry(row)
        ent.insert(0, "0")
        row.pack(side=tk.TOP,
                 fill=tk.X,
                 padx=5,
                 pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT,
                 expand=tk.YES,
                 fill=tk.X)
        entries[field] = ent
    return entries

if __name__ == '__main__':
    root = tk.Tk()
    ents = makeform(root, fields)
    b1 = tk.Button(root, text='Calculate Torgue_1',
           command=(lambda e=ents: Torgue_1(e)))
    b1.pack(side=tk.LEFT, padx=5, pady=5)
    b1 = tk.Button(root, text='Calculate Torgue_2',
           command=(lambda e=ents: Torgue_2(e)))
    b1.pack(side=tk.LEFT, padx=5, pady=5)
    b1 = tk.Button(root, text='Calculate Torgue_3',
           command=(lambda e=ents: Torgue_3(e)))
    b1.pack(side=tk.LEFT, padx=5, pady=5)
    b3 = tk.Button(root, text='Quit', command=root.quit)
    b3.pack(side=tk.LEFT, padx=5, pady=5)
    root.mainloop()