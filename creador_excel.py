import pandas as pd
#Dataframe es la informacion basica  de las piezas y centrimetros  para armar el excel
data = {
    "Piezas":["Pata", "Tablero","Peruta","Mesa","Panel Lateral"],
    "Centimetros":[10,50,100,39,120]
}

dt = pd.DataFrame(data)

#Guardar el dataframe en un archivo excel
dt.to_excel("muebles_medidas.xlsx",index=False)