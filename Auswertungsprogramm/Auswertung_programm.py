# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 20:56:07 2019

@author: mario
"""

import pandas as pd
import numpy as np
url='https://matheli.github.io/Herzinsuffizienz/Attribute_erkl%C3%A4rt.html' # Link zu den erklärten Attributen
def error(Name,Beschreibung):
    from tkinter import messagebox
    messagebox.showinfo(Name,Beschreibung)
    close()
def close():
    try:
        fenster.destroy()
       
    except:
     
        fenster2.destroy()
      
def open_att():
    import webbrowser
    webbrowser.open_new(url)        
def build_model():
    import tensorflow as tf
    from numpy.random import seed
    seed(1)
    init='glorot_uniform'
    
    model = tf.keras.Sequential([     
    tf.keras.layers.Flatten(), 
  
    tf.keras.layers.Dense(40,kernel_initializer=init, activation=tf.nn.sigmoid), 
    tf.keras.layers.Dense(20,kernel_initializer=init, activation=tf.nn.sigmoid), 
    tf.keras.layers.Dense(10,kernel_initializer=init, activation=tf.nn.sigmoid),
    tf.keras.layers.Dense(1,kernel_initializer=init, activation=tf.nn.sigmoid),   
    ]) 
    optimizer=tf.keras.optimizers.RMSprop()
    model.compile(optimizer=optimizer, loss=tf.keras.losses.mean_squared_error, metrics=['accuracy'])    
    model.build(input_shape=(1,28))
    return model


def eingabe_2(fenster2,werte,model):
   
   model.load_weights(r"C:\Users\mario\Desktop\GitHub\Heart_disease_prediction\Python_Dateien\data\model_weights.h5")

   data2=pd.DataFrame(werte,columns = ["age","sex","cp","trestbps","chol","fbs","restecg","thalach","exang","slope","ca"])
  
   data=np.genfromtxt(r"C:\Users\mario\Desktop\GitHub\Heart_disease_prediction\Python_Dateien\data\dataset_vollstandig.csv",delimiter=",")
   data = pd.DataFrame(data[1:], columns = ["age","sex","cp","trestbps","chol","fbs","restecg","thalach","exang","oldpeak","slope","ca","thal","target"])
   data = data.drop(['oldpeak'], axis = 1)
   data = data.drop(['thal'], axis = 1)
   data = data.drop(['target'], axis = 1)
   data = pd.concat([data2, data], axis=0)
   
   data = pd.get_dummies(data, columns = ['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'ca'])
   data=np.array(data)
   y = np.expand_dims(data[0], axis=0)
   print(y)
   ergebnis=model.predict(y)
 
   print(ergebnis)
   message=f"Die eingegebenen Patientendaten sprechen zu {str(round(ergebnis[0][0],7)*100)} Prozent für einen erkrankten Patienten"
   tk.Label(fenster2,text=message,font=("Architects Daughter",16)).pack()
   
def save():
    werte=[entpacken(entries,fenster)]
    werte=np.array(werte)
    print(werte.shape)
    fenster.destroy()
    fenster2 = tk.Tk()
    fenster2.title("Vorhersagen einer Herzinfsuffizienz")
    fenster2.geometry("1500x900") 
    
    menu_bar(fenster2)
    eingabe_2(fenster2,werte,model)
    
import tkinter as tk
fenster = tk.Tk()
fenster.title("Vorhersagen einer Herzinfsuffizienz")
fenster.geometry("1500x900") 
def menu_bar(fenster):
    menubar = tk.Menu(fenster)
    filemenu = tk.Menu(menubar, tearoff=1)
    info = tk.Menu(menubar, tearoff=1)
    filemenu.add_command(label="Beenden", command=close)
    info.add_command(label="Attribute erklärt", command=open_att)
    menubar.add_cascade(label="Programm", menu=filemenu)
    menubar.add_cascade(label="Info", menu=info)
    fenster.config(menu=menubar)

def eingabe():

    fields = 'Alter', 'Geschlecht', 'Art der Schmerzen in der Brust', 'Blutdruck im Ruhezustand', 'Cholesterin Spiegel','Blutzucker vor dem Essen','EKG Ergebnis','Höchster erreichter Puls','Schmerz in der Brust bei Belastung','Steigung des ST-Segments','Anzahl der Hauptgefäße'

    tk.Label(fenster,text="Vorhersagen einer Herzinsuffizienz",font=("Architects Daughter",16)).pack()
    tk.Label(fenster,text="",font=("Architects Daughter",30)).pack()
    
    global entries 
    entries = []
    for field in fields:
       if field=='Geschlecht':
           male = tk.IntVar()
           female = tk.IntVar()
           row = tk.Frame(fenster)
           lab = tk.Label(row, width=47, text=field, anchor='w')
           check1= tk.Checkbutton(row,text='männlich',variable=male)
           check2= tk.Checkbutton(row,text='weiblich',variable=female)
           row.pack(side=tk.TOP, padx=5, pady=5)
           lab.pack(side=tk.LEFT)
           check1.pack(side=tk.RIGHT, expand=tk.YES)
           check2.pack(side=tk.RIGHT, expand=tk.YES)
           entries.append((field, male))
           entries.append((field, female))
       elif field=='Art der Schmerzen in der Brust':
           a_angina = tk.IntVar()
           t_angina = tk.IntVar()
           n_angina = tk.IntVar()
           asymptomatic = tk.IntVar()
           
           row = tk.Frame(fenster)
           lab = tk.Label(row,width=67,text=field, anchor='w')
           lab2 = tk.Label(row,text="")
           row.pack(side=tk.TOP, padx=5, pady=5)
           lab.pack(side=tk.LEFT)
           lab2.pack(side=tk.RIGHT, expand=tk.YES)
           #\n
           row = tk.Frame(fenster)
           lab = tk.Label(row, width=16, text="", anchor='w')
           check3= tk.Checkbutton(row,text='Keine Brustschmerzen',variable=n_angina)
           check4= tk.Checkbutton(row,text='Überhaupt keine Beschwerden',variable=asymptomatic)
           check1= tk.Checkbutton(row,text='Kurzer Stichartiger Schmerz',variable=a_angina)
           check2= tk.Checkbutton(row,text='Druckgefühl',variable=t_angina)
           row.pack(side=tk.TOP, padx=5, pady=5)
           lab.pack(side=tk.LEFT)
           check4.pack(side=tk.RIGHT, expand=tk.YES)
           check3.pack(side=tk.RIGHT, expand=tk.YES)
           check1.pack(side=tk.RIGHT, expand=tk.YES)
           check2.pack(side=tk.RIGHT, expand=tk.YES)
           
           entries.append((field,t_angina))
           entries.append((field,a_angina))
           entries.append((field,n_angina))
           entries.append((field, asymptomatic))
           
       elif field=='Blutzucker vor dem Essen':
           blutz_h = tk.IntVar()
           blutz_t = tk.IntVar()
           
           row = tk.Frame(fenster)
           lab = tk.Label(row, width=36, text=field, anchor='w')
           check1= tk.Checkbutton(row,text='über 120 mg/dl',variable=blutz_h)
           check2= tk.Checkbutton(row,text='unter 120 mg/dl',variable=blutz_t)
           row.pack(side=tk.TOP, padx=5, pady=5)
           lab.pack(side=tk.LEFT)
           check1.pack(side=tk.RIGHT, expand=tk.YES)
           check2.pack(side=tk.RIGHT, expand=tk.YES)
           entries.append((field, blutz_t))
           entries.append((field, blutz_h))
       elif field=='EKG Ergebnis':
           normal = tk.IntVar()
           st = tk.IntVar()
           lh = tk.IntVar()
           row = tk.Frame(fenster)
           lab = tk.Label(row, width=16, text=field, anchor='w')
           check1= tk.Checkbutton(row,text='Normal',variable=normal)
           check2= tk.Checkbutton(row,text='St-Depression',variable=st)
           check3= tk.Checkbutton(row,text='Linksventrikuläre Hypertrophie',variable=lh)
           row.pack(side=tk.TOP, padx=5, pady=5)
           lab.pack(side=tk.LEFT)
           check3.pack(side=tk.RIGHT, expand=tk.YES)
           check2.pack(side=tk.RIGHT, expand=tk.YES)
           check1.pack(side=tk.RIGHT, expand=tk.YES)
           entries.append((field, normal))
           entries.append((field, st))
           entries.append((field, lh))
       elif field=='Schmerz in der Brust bei Belastung':
           ja = tk.IntVar()
           nein = tk.IntVar()
          
           row = tk.Frame(fenster)
           lab = tk.Label(row, width=55, text=field, anchor='w')
           check1= tk.Checkbutton(row,text='Ja',variable=ja)
           check2= tk.Checkbutton(row,text='Nein',variable=nein)
          
           row.pack(side=tk.TOP, padx=5, pady=5)
           lab.pack(side=tk.LEFT)
           check1.pack(side=tk.RIGHT, expand=tk.YES)
           check2.pack(side=tk.RIGHT, expand=tk.YES)
           entries.append((field, nein))
           entries.append((field, ja))
           #ab slope
       elif field=='Steigung des ST-Segments':
           up = tk.IntVar()
           flat = tk.IntVar()
           down = tk.IntVar()
           row = tk.Frame(fenster)
           lab = tk.Label(row, width=40, text=field, anchor='w')
           check1= tk.Checkbutton(row,text='Steigend',variable=up)
           check2= tk.Checkbutton(row,text='Flach',variable=flat)
           check3= tk.Checkbutton(row,text='Fallend',variable=down)
           row.pack(side=tk.TOP, padx=5, pady=5)
           lab.pack(side=tk.LEFT)
           check1.pack(side=tk.RIGHT, expand=tk.YES)
           check2.pack(side=tk.RIGHT, expand=tk.YES)
           check3.pack(side=tk.RIGHT, expand=tk.YES)
           entries.append((field, up))
           entries.append((field, flat))    
           entries.append((field, down))    
       elif field=='Anzahl der Hauptgefäße':
           z= tk.IntVar()
           o = tk.IntVar()
           t = tk.IntVar()
           th = tk.IntVar()
           row = tk.Frame(fenster)
           lab = tk.Label(row, width=48, text=field, anchor='w')
           check1= tk.Checkbutton(row,text='1',variable=o)
           check2= tk.Checkbutton(row,text='2',variable=t)
           check3= tk.Checkbutton(row,text='3',variable=th)
           check4= tk.Checkbutton(row,text='0',variable=z)
           row.pack(side=tk.TOP, padx=5, pady=5)
           lab.pack(side=tk.LEFT)
           check3.pack(side=tk.RIGHT, expand=tk.YES)
           check2.pack(side=tk.RIGHT, expand=tk.YES)
           check1.pack(side=tk.RIGHT, expand=tk.YES)
           check4.pack(side=tk.RIGHT, expand=tk.YES)
           entries.append((field, z))  
           entries.append((field, o))
           entries.append((field, t))     
           entries.append((field, th))   
       else:    
           row = tk.Frame(fenster)
           lab = tk.Label(row, width=50, text=field, anchor='w')
           ent = tk.Entry(row)
           row.pack(side=tk.TOP, padx=5, pady=5)
           lab.pack(side=tk.LEFT)
           ent.pack(side=tk.RIGHT, expand=tk.YES)
           entries.append((field, ent))
    tk.Label(fenster,text="",font=("Architects Daughter",30)).pack()  
    tk.Button(fenster,text="Weiter",font=("Architects Daughter",10),command=save).pack()
    tk.Label(fenster,text="",font=("Architects Daughter",8)).pack()  
    tk.Button(fenster,text="Abbrechen",font=("Architects Daughter",10),command=close).pack()
 
    return entries  
def umformer(liste,typ,text):
    
    if typ=='G':
        if np.where(liste==np.amax(liste))[0].shape[0]>=2:
            error("Eingabefehler","Beide Geschlechter angekreuzt") 
        else:
            if np.where(liste==np.amax(liste))[0][0]==0:
                text.append(1)
               
                return text
            
            if np.where(liste==np.amax(liste))[0][0]==1:
                text.append(0)
                 
               
                return text
    if typ=='cp':
        
        if np.where(liste==np.amax(liste))[0].shape[0]>=2:
            error("Eingabefehler","Bitte nur ein Brustschmerztyp angeben") 
            
        else:
            if np.where(liste==np.amax(liste))[0][0]==0:
                text.append(0)
                 
               
                return text
            if np.where(liste==np.amax(liste))[0][0]==1:
                text.append(1)
                 
               
                return text  
            if np.where(liste==np.amax(liste))[0][0]==2:
                text.append(2)
                 
               
                return text
            if np.where(liste==np.amax(liste))[0][0]==3:
                text.append(3)
                 
               
                return text
    if typ=='fbs':
        if np.where(liste==np.amax(liste))[0].shape[0]>=2:
            error("Eingabefehler","Bitte nur einen Wert beim Blutzucker angeben") 
        else:
            if np.where(liste==np.amax(liste))[0][0]==0:
                text.append(0)
                 
               
                return text
            if np.where(liste==np.amax(liste))[0][0]==1:
                text.append(1)
                 
               
                return text    
    if typ=='rest':
        if np.where(liste==np.amax(liste))[0].shape[0]>=2:
            error("Eingabefehler","Bitte nur ein Wert beim EKG angeben") 
        else:
            if np.where(liste==np.amax(liste))[0][0]==0:
                text.append(0)
                 
               
                return text
            if np.where(liste==np.amax(liste))[0][0]==1:
                text.append(1)
                 
               
                return text    
            if np.where(liste==np.amax(liste))[0][0]==2:
                text.append(2)
                 
               
                return text
    if typ=='exang':
        if np.where(liste==np.amax(liste))[0].shape[0]>=2:
            error("Eingabefehler","Bitte nur ein Wert beim Belastungs bedingten Brustschmerz angeben") 
        else:
            if np.where(liste==np.amax(liste))[0][0]==0:
                text.append(0)
                 
               
                return text
            if np.where(liste==np.amax(liste))[0][0]==1:
                text.append(1)
                 
               
                return text  
    
    if typ=='slope':
        print(liste)
        if np.where(liste==np.amax(liste))[0].shape[0]>=2:
            error("Eingabefehler","Bitte nur ein Wert bei der typisierung der ST-Depression angeben") 
           
        else:
        
            if np.where(liste==np.amax(liste))[0][0]==0:
                text.append(0)
                 
               
                return text
            if np.where(liste==np.amax(liste))[0][0]==1:
                text.append(1)
                 
               
                return text   
            if np.where(liste==np.amax(liste))[0][0]==2:
                text.append(2)
             
           
            
            return text
    
    if typ=='ca':
        print(liste)
        if np.where(liste==np.amax(liste))[0].shape[0]>=2:
            error("Eingabefehler","Bitte nur ein Wert bei der Anzahl der Hauptgefäße angeben") 
        else:
            if np.where(liste==np.amax(liste))[0][0]==0:
                text.append(0)
                 
               
                return text
            if np.where(liste==np.amax(liste))[0][0]==1:
                text.append(1)
                 
               
                return text   
            if np.where(liste==np.amax(liste))[0][0]==2:
                text.append(2)
                 
               
                return text        
            if np.where(liste==np.amax(liste))[0][0]==3:
                text.append(3)
                 
               
                return text    

def entpacken(entries,fenster):
   liste_g=[] 
   liste_cp=[] 
   liste_fbs=[]
   liste_rest=[]
   liste_ex=[]
   liste_slope=[]
   liste_ca=[]
   i=0
  
   text=[]
   for feld in entries:
      i=i+1
      
      print(i,feld[1].get())
     
      #print("TEXT:",text,"länge",len(text))   
    
      
      if i==2:
          liste_g.append(feld[1].get())
      elif i==3:
          liste_g.append(feld[1].get())
          text=umformer(liste_g,'G',text)
          
      elif i==4:
          liste_cp.append(feld[1].get())    
      elif i==5:
          liste_cp.append(feld[1].get())
      elif i==6:
          liste_cp.append(feld[1].get())
      elif i==7:
          liste_cp.append(feld[1].get())
          
          text=umformer(liste_cp,'cp',text)
          
      elif i==10:
          liste_fbs.append(feld[1].get())    
      elif i==11:
          liste_fbs.append(feld[1].get())
          text=umformer(liste_fbs,'fbs',text)    
          
      elif i==12:
          liste_rest.append(feld[1].get())  
      elif i==13:
          liste_rest.append(feld[1].get())  
      elif i==14:
          liste_rest.append(feld[1].get())  
          text=umformer(liste_rest,'rest',text)
         
      elif i==16:
          liste_ex.append(feld[1].get())      
      elif i==17:
          liste_ex.append(feld[1].get())    
          text=umformer(liste_ex,'exang',text) 
         
      elif i==18:
          liste_slope.append(feld[1].get())  
      elif i==19:
          liste_slope.append(feld[1].get())
      elif i==20:
          liste_slope.append(feld[1].get())    
          text=umformer(liste_slope,'slope',text)
          
      elif i==21:
          
          liste_ca.append(feld[1].get())   
      elif i==22:
          
          liste_ca.append(feld[1].get())  
      elif i==23:
          
          liste_ca.append(feld[1].get())  
      elif i==24:
          
          liste_ca.append(feld[1].get())      
          right=umformer(liste_ca,'ca',text)
      else:    
          text.append(int(feld[1].get()))
       
   print(right)    
   print("\n","\n","\n","\n","Alter:",right[0],"\n","Geschlecht:",right[1],"\n","Art der Schmerzen in der Brust:",right[2],"\n","Blutdruck im Ruhezustand:",right[3],"\n","Cholesterin Spiegel:",right[4],"\n","Blutzucker vor dem Essen:",right[5],"\n","EKG Ergebnis:",right[6],"\n","Höchster erreichter Puls:",right[7],"\n","Schmerzen in der Brust bei Belastung",right[8],"\n","Steigung des ST-Segments:",right[9],"\n","Anzahl der Hauptgefäße:",right[10],"\n","\n","\n","\n","\n")
   return right       
model=build_model()
menu_bar(fenster)
entries=eingabe()






fenster.mainloop()

