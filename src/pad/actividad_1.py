import json
import requests



class Ingestiones():
    def __init__(self):
        self.ruta_static="src/pad/static/"
        
    def leer_json(self):
        # r read w write

        ruta_json = "{}json/datos_persona.json".format(self.ruta_static)
        datos=""
        with open(ruta_json,"r",encoding="utf-8") as f:
            datos = json.load(f)
        return datos    
    
    def leer_txt(self):
        # r read w write

        ruta_json = "{}txt/info.txt".format(self.ruta_static)
        datos=""
        with open(ruta_json,"r",encoding="utf-8") as f:
            datos = f.read()
        return datos 

    def leer_varios_txt(self,nombre=""):
        # r read w write

        ruta_txt = "{}txt/{}".format(self.ruta_static,nombre)
        datos=""
        with open(ruta_txt,"r",encoding="utf-8") as f:
            datos = f.read()
        return datos   
    
    def  leer_cualquier_excel(self,nombre=""):
        pass
    
    def  leer_cualquier_csv(self,nombre=""):
        pass
    
    def  leer_html(self,url=""):
        pass
    
    def  leer_bd(self,nombre_bd="",servidor="",puerto=0000):
        pass
    
    def  leer_api(self,url):
        url = 'https://exoplanetarchive.ipac.caltech.edu/TAP/sync'
        query = """SELECT * FROM planet WHERE pl_status='C'""" 
        params = {
        'request': 'doQuery',
        'lang': 'ADQL',
         'format': 'csv',
        'query': query
    }

        if response.status_code == 200:
            print ("Datos obtenidos:")
            print(response.text)

        else:
             print(f"Error {response.status_code}: No se pudo obtener los datos.")


        response = requests.get(url)
        return response.json()
    print 


        
    def escribir_json(self,datos):
        pass
    
    def escribir_txt(self,nombre,datos):
        # r read w write

        ruta_txt = "{}.txt".format(nombre)
        datos=""
        with open(ruta_txt,"w",encoding="utf-8") as f:
            #f.write(datos)
            f.writelines(datos)







inges = Ingestiones() 
datos_json = inges.leer_json()
print(datos_json)
print("************************************************************")
print("************************************************************")
datos_txt = inges.leer_txt()
print(datos_txt)
print("************************************************************")
print("************************************************************")
nombre_archivo = "info copy.txt"
datos_txt_dos = inges.leer_varios_txt(nombre_archivo)
print(datos_txt_dos)

#inges.escribir_txt(nombre="archivo_json",datos=datos_json)
#inges.escribir_txt(nombre="archivo_txt",datos=datos_txt)
#inges.escribir_txt(nombre="archivo_txt_copy",datos=datos_txt_dos)
    
    
    
    
