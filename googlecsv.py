import pandas as pd
#creamos las columnas necesarias
columns = ['datos','Name','Email']
#cargamos los archivos segun sus caracteristicas
file = pd.read_csv("AllDetails.csv",header=None, names=columns,sep=';', dtype = str,lineterminator = ';')
#cortamos la columna datos a la mitad a la altura del caracter <
file[['Name', 'Email']] = file['datos'].str.split('<', expand=True)
#quitamos el caracter >
file['Email'] = file['Email'].str.replace('>', '')
#borramos la columna datos
file.drop(['datos'], axis='columns', inplace=True)
#seleccionamos como columna principal Name
file.set_index('Name', inplace=True)
print(file)
file.to_csv("churraco.csv", sep=';', encoding='utf-8')
