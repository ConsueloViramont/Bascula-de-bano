
class Usuario:
    def __init__(self, id, nombre, altura):
        self.id = id
        self.nombre = nombre
        self.altura = altura
class Bascula:
    def __init__(self):
        self.mediciones = []
    def registrar_medicion(self, usuario, peso):
        medicion = {"usuario_id": usuario.id, "fecha": "2024-08-31", "peso": peso}
        self.mediciones.append(medicion)
        return True
    
    def calcular_masa_corporal(self, usuario):
   
        ultima_medicion = next((m for m in self.mediciones if m["usuario_id"] == usuario.id), None)
    
        if ultima_medicion:
       
            masa_corporal = ultima_medicion["peso"] / (usuario.altura ** 2)
            return round(masa_corporal, 2)
        else:
            return None