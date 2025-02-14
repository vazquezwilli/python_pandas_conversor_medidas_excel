import pandas as pd

def cm_a_pulgadas(cm):
    return cm / 2.54

#Leer archivo excel:
df = pd.read_excel("muebles_medidas.xlsx")

#añadir una columna al dataframe que sea de pulgadas y se rellene con el calculo  de cm / 2.54

df["Pulgadas"] =  df["Centimetros"].apply(cm_a_pulgadas)

df.to_excel("muebles_medida_convertidas.xlsx", index=False)

print("conversion completada")