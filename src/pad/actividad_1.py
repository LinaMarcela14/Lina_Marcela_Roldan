import json
import requests



class Actividad1():
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


    def leer_api(self, url):
        # El get()método envía una solicitud de GET a la url especificada.
        response = requests.get("https://www.amiiboapi.com/api/amiibo/?name=zelda")
        return response.json()


        
    def escribir_json(self,nombre,datos):
        ruta_json = "{}/json/{}".format(self.ruta_static,nombre)
        with open(ruta_json, 'w', encoding='utf-8') as f:
            json.dump(datos, f, ensure_ascii=False, indent=4)
          
    def escribir_txt(self,nombre_archivo="",datos=None): # "" '' """ """
        if nombre_archivo=="":
            nombre_archivo="datos.txt"
        if datos is None:
            datos = "No hay datos"
        ruta_txt = "{}/txt/{}".format(self.ruta_static,nombre_archivo)
        with open(ruta_txt, 'w', encoding='utf-8') as f:
            json.dump(datos, f, ensure_ascii=False, indent=4)
            f.write(str(datos))
        return True # booleano True (1) False (0)

ingestion =Actividad1()
#datos_json = Actividad1.leer_api("https://www.amiiboapi.com/api/amiibo/?name=zelda")
#"https://www.amiiboapi.com/api/amiibo/?name=zelda"
datos_json = ingestion.leer_api("https://www.amiiboapi.com/api/amiibo/?name=zelda")
print("datos json:",datos_json)
#if ingestion.escribir_json(nombre_archivo="entrega_actividad1.json",datos=datos_json):
 #   print("se creo el archivo json")
ingestion.escribir_txt("Actividad1.txt",datos_json) 
ingestion.escribir_json("Actividad1.json",datos_json)
print("se creo el archivo json")



