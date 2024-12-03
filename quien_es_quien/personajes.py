
class CaracteristicasPersonajes:
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
    CaracteristicasPersonajes("alex", color_cabello="negro", color_ojos="marrones", genero="masculino", accesorios=["bigote"], expresion="sonrisa"),
    CaracteristicasPersonajes("alfred", color_cabello="pelirrojo", color_ojos="azules", genero="masculino", expresion="triste"),
    CaracteristicasPersonajes("anita", color_cabello="rubio", color_ojos="azules", genero="femenino", accesorios=["lazos"], expresion="sonrisa"),
    CaracteristicasPersonajes("anne", color_cabello="negro", color_ojos="marrones", genero="femenino", accesorios=["pendientes"], expresion="seria"),
    CaracteristicasPersonajes("bernard", color_cabello="castano", color_ojos="marrones", genero="masculino", accesorios=["sombrero"], expresion="serio"),
    CaracteristicasPersonajes("bill", color_cabello="calvo", color_ojos="marrones", genero="masculino", barba=True, mejillas="gordas"),
    CaracteristicasPersonajes("charles", color_cabello="rubio", color_ojos="marrones", genero="masculino", expresion="sonrisa"),
    CaracteristicasPersonajes("claire", color_cabello="pelirrojo", color_ojos="marrones", genero="femenino", accesorios=["sombrero", "gafas"], expresion="sonrisa"),
    CaracteristicasPersonajes("david", color_cabello="rubio", color_ojos="castanos", genero="masculino", barba=True),
    CaracteristicasPersonajes("eric", color_cabello="rubio", color_ojos="marrones", genero="masculino", accesorios=["sombrero"], expresion="sonrisa"),
    CaracteristicasPersonajes("frans", color_cabello="pelirrojo", color_ojos="marrones", genero="masculino", expresion="sonrisa"),
    CaracteristicasPersonajes("george", color_cabello="blanco", color_ojos="marrones", genero="masculino", accesorios=["sombrero"], expresion="seria"),
    CaracteristicasPersonajes("herman", color_cabello="calvo", color_ojos="marrones", genero="masculino", expresion="sonrisa"),
    CaracteristicasPersonajes("joe", color_cabello="rubio", color_ojos="marrones", genero="masculino", accesorios=["gafas"], mejillas="redondeadas"),
    CaracteristicasPersonajes("maria", color_cabello="castano", color_ojos="marrones", genero="femenino", accesorios=["pendientes"], expresion="sonrisa"),
    CaracteristicasPersonajes("max", color_cabello="negro", color_ojos="marrones", genero="masculino", accesorios=["bigote"]),
    CaracteristicasPersonajes("paul", color_cabello="blanco", color_ojos="marrones", genero="masculino", accesorios=["gafas"], expresion="seria"),
    CaracteristicasPersonajes("peter", color_cabello="blanco", color_ojos="azul", genero="masculino", expresion="sonrisa"),
    CaracteristicasPersonajes("philip", color_cabello="castano", color_ojos="marrones", genero="masculino", expresion="sonrisa"),
    CaracteristicasPersonajes("richard", color_cabello="calvo", color_ojos="marrones", genero="masculino", barba=True),
    CaracteristicasPersonajes("robert", color_cabello="castano", color_ojos="azules", genero="masculino", mejillas="sonrojadas"),
    CaracteristicasPersonajes("sam", color_cabello="calvo", color_ojos="marrones", genero="masculino", accesorios=["gafas"], mejillas="redondeadas"),
    CaracteristicasPersonajes("susan", color_cabello="blanco", color_ojos="marrones", genero="femenino", expresion="sonrisa"),
    CaracteristicasPersonajes("tom", color_cabello="calvo", color_ojos="azules", genero="masculino", accesorios=["gafas"], expresion="seria"),
]