
class caracteristicas_personajes:
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
        return f"Nombre: {self.nombre}, Cabello: {self.color_cabello}, Ojos: {self.color_ojos}, Género: {self.genero}, Accesorios: {self.accesorios}, Barba: {self.barba}, Mejillas: {self.mejillas}, Expresion: {self.expresion}"

integrantes = [
    caracteristicas_personajes("Susan.jpg", color_cabello="blanco", color_ojos="marrones", genero="femenino", expresion="sonrisa"),
    caracteristicas_personajes("Claire.jpg", color_cabello="pelirrojo", color_ojos="marrones", genero="femenino", accesorios=["sombrero", "gafas"], expresion="sonrisa"),
    caracteristicas_personajes("Davidj.jpg", color_cabello="rubio", color_ojos="castaños", genero="masculino", barba=True),
    caracteristicas_personajes("Anne.jpg", color_cabello="negro", color_ojos="marrones", genero="femenino", accesorios=["pendientes"], expresion="seria"),
    caracteristicas_personajes("Robert.jpg", color_cabello="castaño", color_ojos="azules", genero="masculino", mejillas="sonrojadas"),
    caracteristicas_personajes("Anita.jpg", color_cabello="rubio", color_ojos="azules", genero="femenino", accesorios=["lazos"], expresion="sonrisa"),
    caracteristicas_personajes("Joe.jpg", color_cabello="rubio", color_ojos="marrones", genero="masculino", accesorios=["gafas"], mejillas="redondeadas"),
    caracteristicas_personajes("George.jpg", color_cabello="blanco", color_ojos="marrones", genero="masculino", accesorios=["sombrero"], expresion="seria"),
    caracteristicas_personajes("Bill.jpg", color_cabello="calvo", color_ojos="marrones", genero="masculino", barba=True, mejillas="gordas"),
    caracteristicas_personajes("Alfred.jpg", color_cabello="pelirrojo", color_ojos="azules", genero="masculino", expresion="triste"),
    caracteristicas_personajes("Max.jpg", color_cabello="negro", color_ojos="marro  nes", genero="masculino", accesorios=["bigote"]),
    caracteristicas_personajes("Tom.jpg", color_cabello="calvo", color_ojos="azules", genero="masculino", accesorios=["gafas"], expresion="seria"),
    caracteristicas_personajes("Alex.jpg", color_cabello="negro", color_ojos="marrones", genero="masculino", accesorios=["bigote"], expresion="sonrisa"),
    caracteristicas_personajes("Sam.jpg", color_cabello="calvo", color_ojos="marrones", genero="masculino", accesorios=["gafas"], mejillas="redondeadas"),
    caracteristicas_personajes("Richard.jpg", color_cabello="calvo", color_ojos="marrones", genero="masculino", barba=True),
    caracteristicas_personajes("Paul.jpg", color_cabello="blanco", color_ojos="marrones", genero="masculino", accesorios=["gafas"], expresion="seria"),
    caracteristicas_personajes("Maria.jpg", color_cabello="castaño", color_ojos="marrones", genero="femenino", accesorios=["pendientes"], expresion="sonrisa"),
    caracteristicas_personajes("Frans.jpg", color_cabello="pelirrojo", color_ojos="marrones", genero="masculino", expresion="sonrisa"),
    caracteristicas_personajes("Herman.jpg", color_cabello="calvo", color_ojos="marrones", genero="masculino", expresion="sonrisa"),
    caracteristicas_personajes("Bernard.jpg", color_cabello="castaño", color_ojos="marrones", genero="masculino", accesorios=["sombrero"], expresion="serio"),
    caracteristicas_personajes("Philip.jpg", color_cabello="castaño", color_ojos="marrones", genero="masculino", expresion="sonrisa"),
    caracteristicas_personajes("Eric.jpg", color_cabello="rubio", color_ojos="marrones", genero="masculino", accesorios=["sombrero"], expresion="sonrisa"),
    caracteristicas_personajes("Charles.jpg", color_cabello="rubio", color_ojos="marrones", genero="masculino", expresion="sonrisa"),
    caracteristicas_personajes("Peter.jpg", color_cabello="blanco", color_ojos="azul", genero="masculino", expresion="sonrisa")
]