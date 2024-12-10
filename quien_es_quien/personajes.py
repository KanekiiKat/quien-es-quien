
class Personajes:
    def __init__(self, nombre, color_cabello, color_ojos, genero, accesorios = False, barba = False, mejillas = False, expresion = False):
        self.nombre = nombre
        self.color_cabello = color_cabello
        self.color_ojos = color_ojos
        self.genero = genero
        self.accesorios = accesorios
        self.barba = barba
        self.mejillas = mejillas
        self.expresion = expresion  
        
    def __str__(self):
        return f"{self.nombre} {self.color_cabello} {self.color_ojos} {self.genero} {self.accesorios}, {self.barba}, {self.mejillas}, {self.expresion}"

integrantes = [
    Personajes("alex", color_cabello="negro", color_ojos="marrones", genero="masculino", accesorios=["bigote"], expresion="sonrisa"),
    Personajes("alfred", color_cabello="pelirrojo", color_ojos="azules", genero="masculino", expresion="triste"),
    Personajes("anita", color_cabello="rubio", color_ojos="azules", genero="femenino", accesorios=["lazos"], expresion="sonrisa"),
    Personajes("anne", color_cabello="negro", color_ojos="marrones", genero="femenino", accesorios=["pendientes"], expresion="seria"),
    Personajes("bernard", color_cabello="castano", color_ojos="marrones", genero="masculino", accesorios=["sombrero"], expresion="serio"),
    Personajes("bill", color_cabello="calvo", color_ojos="marrones", genero="masculino", barba=True, mejillas="gordas"),
    Personajes("charles", color_cabello="rubio", color_ojos="marrones", genero="masculino", expresion="sonrisa"),
    Personajes("claire", color_cabello="pelirrojo", color_ojos="marrones", genero="femenino", accesorios=["sombrero", "gafas"], expresion="sonrisa"),
    Personajes("david", color_cabello="rubio", color_ojos="castanos", genero="masculino", barba=True),
    Personajes("eric", color_cabello="rubio", color_ojos="marrones", genero="masculino", accesorios=["sombrero"], expresion="sonrisa"),
    Personajes("frans", color_cabello="pelirrojo", color_ojos="marrones", genero="masculino", expresion="sonrisa"),
    Personajes("george", color_cabello="blanco", color_ojos="marrones", genero="masculino", accesorios=["sombrero"], expresion="seria"),
    Personajes("herman", color_cabello="calvo", color_ojos="marrones", genero="masculino", expresion="sonrisa"),
    Personajes("joe", color_cabello="rubio", color_ojos="marrones", genero="masculino", accesorios=["gafas"], mejillas="redondeadas"),
    Personajes("maria", color_cabello="castano", color_ojos="marrones", genero="femenino", accesorios=["pendientes"], expresion="sonrisa"),
    Personajes("max", color_cabello="negro", color_ojos="marrones", genero="masculino", accesorios=["bigote"]),
    Personajes("paul", color_cabello="blanco", color_ojos="marrones", genero="masculino", accesorios=["gafas"], expresion="seria"),
    Personajes("peter", color_cabello="blanco", color_ojos="azul", genero="masculino", expresion="sonrisa"),
    Personajes("philip", color_cabello="castano", color_ojos="marrones", genero="masculino", expresion="sonrisa"),
    Personajes("richard", color_cabello="calvo", color_ojos="marrones", genero="masculino", barba=True),
    Personajes("robert", color_cabello="castano", color_ojos="azules", genero="masculino", mejillas="sonrojadas"),
    Personajes("sam", color_cabello="calvo", color_ojos="marrones", genero="masculino", accesorios=["gafas"], mejillas="redondeadas"),
    Personajes("susan", color_cabello="blanco", color_ojos="marrones", genero="femenino", expresion="sonrisa"),
    Personajes("tom", color_cabello="calvo", color_ojos="azules", genero="masculino", accesorios=["gafas"], expresion="seria"),
]