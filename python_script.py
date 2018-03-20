#!"C:\Program Files (x86)\Python36-32\python.exe"
# coding utf-8

# In[139]:
import cgi;
print ("Content-Type: text/plain\n")

import numpy as np
import pandas as pd
from firebase import firebase
firebase = firebase.FirebaseApplication('https://rajasthanhackath-1521470169570.firebaseio.com/',None)

temp = firebase.get('temp',None)
c = temp['category']
city = temp['city']
arr=[c]
interests=["Monuments","Religious","fun","Museum","Nature"]
cities=[city]
total_cities=["Jaipur","Udaipur","Ajmer"]

if "Jaipur" in cities:
    if "Monuments" in arr:
        df_monu_jai = pd.read_csv(r"jaipur\Jaipur_monument1 (1).csv", index_col="places")
    if "Religious" in arr:
        df_reli_jai = pd.read_csv(r"jaipur\Jaipur_Religious1 (1).csv",index_col="places")
    if "fun" in arr:
        df_fun_jai = pd.read_csv(r"jaipur\Jaipur_fun1.csv",index_col="places")
    if "Nature" in arr:
        df_nat_jai = pd.read_csv(r"jaipur\Jaipur_Nature1.csv",index_col="places")
    if "Museum" in arr:
        df_mus_jai = pd.read_csv(r"jaipur\Jaipur_Museum1.csv",index_col="places")
if "Udaipur" in cities:
    if "Monuments" in arr:
        df_monu_ud = pd.read_csv(r"udaipur\Udaipur_monument.csv", index_col="places")
    if "Religious" in arr:
        df_reli_ud = pd.read_csv(r"udaipur\Udaipur_Religious.csv",index_col="places")
    if "fun" in arr:
        df_fun_ud = pd.read_csv(r"udaipur\Udaipur_fun.csv",index_col="places")
    if "Nature" in arr:
        df_nat_ud = pd.read_csv(r"udaipur\Udaipur_Nature.csv",index_col="places")
    if "Museum" in arr:
        df_mus_ud = pd.read_csv(r"udaipur\Udaipur_Museum.csv",index_col="places")
if "Ajmer" in cities:
    if "Monuments" in arr:
        df_monu_aj = pd.read_csv(r"ajmer\Ajmer_monument.csv", index_col="places")
    if "Religious" in arr:
        df_reli_aj = pd.read_csv(r"ajmer\Ajmer_Religious.csv",index_col="places")
    if "fun" in arr:
        df_fun_aj = pd.read_csv(r"ajmer\Ajmer_fun.csv",index_col="places")
    if "Nature" in arr:
        df_nat_aj = pd.read_csv(r"ajmer\Ajmer_Nature.csv",index_col="places")
    if "Museum" in arr:
        df_mus_aj = pd.read_csv(r"ajmer\Ajmer_Museum.csv",index_col="places")




def normalise(df,name):
    a=0
    b=0
    for j,i in df.iteritems():
        a=a+i[name]
        if i[name]!=0:
            b=b+1
    c=a/b
    for j,i in df.iteritems():
        if i[name]!=0:
            i[name]=i[name]-c
if "Jaipur" in cities:
    if "Monuments" in arr:
        df_monu_jai = df_monu_jai.fillna(0)
        for j,i in df_monu_jai.iterrows():
            normalise(df_monu_jai,j)
    if "Religious" in arr:
        df_reli_jai = df_reli_jai.fillna(0)
        for j,i in df_reli_jai.iterrows():
            normalise(df_reli_jai,j)
    if "fun" in arr:
        df_fun_jai = df_fun_jai.fillna(0)
        for j,i in df_fun_jai.iterrows():
            normalise(df_fun_jai,j)
    if "Museum" in arr:
        df_mus_jai = df_mus_jai.fillna(0)
        for j,i in df_mus_jai.iterrows():
            normalise(df_mus_jai,j)
    if "Nature" in arr:
        df_nat_jai = df_nat_jai.fillna(0)
        for j,i in df_nat_jai.iterrows():
            normalise(df_nat_jai,j)
if "Udaipur" in cities:
    if "Monuments" in arr:
        df_monu_ud = df_monu_ud.fillna(0)
        for j,i in df_monu_ud.iterrows():
            normalise(df_monu_ud,j)
    if "Religious" in arr:
        df_reli_ud = df_reli_ud.fillna(0)
        for j,i in df_reli_ud.iterrows():
            normalise(df_reli_ud,j)
    if "fun" in arr:
        df_fun_ud = df_fun_ud.fillna(0)
        for j,i in df_fun_ud.iterrows():
            normalise(df_fun_ud,j)
    if "Museum" in arr:
        df_mus_ud = df_mus_ud.fillna(0)
        for j,i in df_mus_ud.iterrows():
            normalise(df_mus_ud,j)
    if "Nature" in arr:
        df_nat_ud = df_nat_ud.fillna(0)
        for j,i in df_nat_ud.iterrows():
            normalise(df_nat_ud,j)
if "Ajmer" in cities:
    if "Monuments" in arr:
        df_monu_aj = df_monu_aj.fillna(0)
        for j,i in df_monu_aj.iterrows():
            normalise(df_monu_aj,j)
    if "Religious" in arr:
        df_reli_aj = df_reli_aj.fillna(0)
        for j,i in df_reli_aj.iterrows():
            normalise(df_reli_aj,j)
    if "fun" in arr:
        df_fun_aj = df_fun_aj.fillna(0)
        for j,i in df_fun_aj.iterrows():
            normalise(df_fun_aj,j)
    if "Museum" in arr:
        df_mus_aj = df_mus_aj.fillna(0)
        for j,i in df_mus_jai.iterrows():
            normalise(df_mus_jai,j)
    if "Nature" in arr:
        df_nat_aj = df_nat_aj.fillna(0)
        for j,i in df_nat_aj.iterrows():
            normalise(df_nat_aj,j)            


# In[142]:


def val_max(df,name):
    l=[]
    for j,i in df.iteritems():
        l.append(i[name])
    return max(l)
if "Jaipur" in cities:
    place_Jaipur=[]
    if "Monuments" in arr:
        max_val=[]
        names=[] 
        for j,i in df_monu_jai.iterrows():
            names.append(j)
            max_val.append(val_max(df_monu_jai,j))   
        for i in range(0,5):
            place_Jaipur.append(names[max_val.index(max(max_val))])
            a=max_val.index(max(max_val))
            max_val.remove(max(max_val))
            names.remove(names[a])  
    if "fun" in arr:
        max_val=[]
        names=[] 
        for j,i in df_fun_jai.iterrows():
            names.append(j)
            max_val.append(val_max(df_fun_jai,j))   
        for i in range(0,5):
            place_Jaipur.append(names[max_val.index(max(max_val))])
            a=max_val.index(max(max_val))
            max_val.remove(max(max_val))
            names.remove(names[a])   
    if "Religious" in arr:
        max_val=[]
        names=[] 
        for j,i in df_reli_jai.iterrows():
            names.append(j)
            max_val.append(val_max(df_reli_jai,j))   
        for i in range(0,5):
            place_Jaipur.append(names[max_val.index(max(max_val))])
            a=max_val.index(max(max_val))
            max_val.remove(max(max_val))
            names.remove(names[a])   
    if "Museum" in arr:
        max_val=[]
        names=[] 
        for j,i in df_mus_jai.iterrows():
            names.append(j)
            max_val.append(val_max(df_mus_jai,j))   
        for i in range(0,5):
            place_Jaipur.append(names[max_val.index(max(max_val))])
            a=max_val.index(max(max_val))
            max_val.remove(max(max_val))
            names.remove(names[a])     
    if "Nature" in arr:
        max_val=[]
        names=[] 
        for j,i in df_nat_jai.iterrows():
            names.append(j)
            max_val.append(val_max(df_nat_jai,j))
        for i in range(0,5):
            place_Jaipur.append(names[max_val.index(max(max_val))])
            a=max_val.index(max(max_val))
            max_val.remove(max(max_val))
            names.remove(names[a])
    
if "Udaipur" in cities:
    place_Udaipur=[]
    if "Monuments" in arr:
        max_val=[]
        names=[] 
        for j,i in df_monu_ud.iterrows():
            names.append(j)
            max_val.append(val_max(df_monu_ud,j))   
        for i in range(0,5):
            place_Udaipur.append(names[max_val.index(max(max_val))])
            a=max_val.index(max(max_val))
            max_val.remove(max(max_val))
            names.remove(names[a]) 
            
    if "fun" in arr:
        max_val=[]
        names=[] 
        for j,i in df_fun_ud.iterrows():
            names.append(j)
            max_val.append(val_max(df_fun_ud,j))   
        for i in range(0,5):
            place_Udaipur.append(names[max_val.index(max(max_val))])
            a=max_val.index(max(max_val))
            max_val.remove(max(max_val))
            names.remove(names[a])   
    if "Religious" in arr:
        max_val=[]
        names=[] 
        for j,i in df_reli_ud.iterrows():
            names.append(j)
            max_val.append(val_max(df_reli_ud,j))   
        for i in range(0,5):
            place_Udaipur.append(names[max_val.index(max(max_val))])
            a=max_val.index(max(max_val))
            max_val.remove(max(max_val))
            names.remove(names[a])   
    if "Museum" in arr:
        max_val=[]
        names=[] 
        for j,i in df_mus_ud.iterrows():
            names.append(j)
            max_val.append(val_max(df_mus_ud,j))   
        for i in range(0,5):
            place_Udaipur.append(names[max_val.index(max(max_val))])
            a=max_val.index(max(max_val))
            max_val.remove(max(max_val))
            names.remove(names[a])     
    if "Nature" in arr:
        max_val=[]
        names=[] 
        for j,i in df_nat_ud.iterrows():
            names.append(j)
            max_val.append(val_max(df_nat_ud,j))
        for i in range(0,5):
            place_Udaipur.append(names[max_val.index(max(max_val))])
            a=max_val.index(max(max_val))
            max_val.remove(max(max_val))
            names.remove(names[a])  
              
if "Ajmer" in cities:
    place_Ajmer=[]
    if "Monuments" in arr:
        max_val=[]
        names=[] 
        for j,i in df_monu_aj.iterrows():
            names.append(j)
            max_val.append(val_max(df_monu_aj,j))   
        for i in range(0,5):
            place_Ajmer.append(names[max_val.index(max(max_val))])
            a=max_val.index(max(max_val))
            max_val.remove(max(max_val))
            names.remove(names[a])  
    if "fun" in arr:
        max_val=[]
        names=[] 
        for j,i in df_fun_aj.iterrows():
            names.append(j)
            max_val.append(val_max(df_fun_aj,j))   
        for i in range(0,5):
            place_Ajmer.append(names[max_val.index(max(max_val))])
            a=max_val.index(max(max_val))
            max_val.remove(max(max_val))
            names.remove(names[a])   
    if "Religious" in arr:
        max_val=[]
        names=[] 
        for j,i in df_reli_aj.iterrows():
            names.append(j)
            max_val.append(val_max(df_reli_aj,j))   
        for i in range(0,5):
            place_Ajmer.append(names[max_val.index(max(max_val))])
            a=max_val.index(max(max_val))
            max_val.remove(max(max_val))
            names.remove(names[a])   
    if "Museum" in arr:
        max_val=[]
        names=[] 
        for j,i in df_mus_aj.iterrows():
            names.append(j)
            max_val.append(val_max(df_mus_aj,j))   
        for i in range(0,5):
            place_Ajmer.append(names[max_val.index(max(max_val))])
            a=max_val.index(max(max_val))
            max_val.remove(max(max_val))
            names.remove(names[a])     
    if "Nature" in arr:
        max_val=[]
        names=[] 
        for j,i in df_nat_aj.iterrows():
            names.append(j)
            max_val.append(val_max(df_nat_aj,j))
        for i in range(0,5):
            place_Jaipur.append(names[max_val.index(max(max_val))])
            a=max_val.index(max(max_val))
            max_val.remove(max(max_val))
            names.remove(names[a])


# In[145]:



jai_crd=pd.read_csv(r"jaipur\Coordinates.csv", index_col="NAME")
ud_crd=pd.read_csv(r"udaipur\Coordinates.csv", index_col="NAME")
aj_crd=pd.read_csv(r"ajmer\Coordinates.csv", index_col="NAME")
def coordinates(place,crd):
    crd_list=[]
    for i in place:
        for j,k in crd.iterrows():
            if i == j:
                crd_list.append(k["NORTH"])
                crd_list.append(k["EAST"])
    name_str=""
    for i in place:
        if name_str=="":
            name_str=i
        else:    
            name_str=name_str+","+i
    crd_list = [str(i) for i in crd_list]
    crd_str=""
    for i in crd_list:
        if crd_str=="":
            crd_str=i
        else:
            crd_str=crd_str+","+i
    print(name_str)
    print(crd_str)                        
if "Ajmer" in cities:
    coordinates(place_Ajmer,aj_crd)
if "Jaipur" in cities:
    coordinates(place_Jaipur,jai_crd)
if "Udaipur" in cities:
    coordinates(place_Udaipur,ud_crd)
      



