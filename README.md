# ¿Quién es Quién?


- [Introduccion](#Introduccion)
- [Manual](#manual)
- [Metodologia](#metodologia)
- [Descripcion técnica](#Descripcion-tecnica)
- [Diseño](diseño)
- [Implementación](#Implementacion)
- [Pruebas](#Pruebas)
- [Análisis del tiempo invertido](#analisis-del-tiempo-invertido)
- [Conclusiones](#Conclusiones)

## Introducción
Este proyecto ha sido creado por [<ins>Alejando Villar Rioja</ins>](https://github.com/KanekiiKat) y [<ins>Pablo González Temes</ins>](https://github.com/Pistacho14) dos alumnos de 1º de DAM del centro [<ins>IES de Teis</ins>](http://www.edu.xunta.gal/centros/iesteis/). Se trata de un "*¿Quién es Quién?*" un juego de mesa tradicional que trata de adivinar un personaje, el cual se elige aleatoriamente, y el jugador debe adivinarlo preguntando sobre las características faciales del elegido. En cualquier momento, el usuario puede tratar de adivinar el personaje, aunque aun tenga dudas sobre cual es el correcto. Si lo acierta se considerará como una victoria, mientras que en el caso contrario será una derrota.

## Manual

### Requisitos
Los requisitos para el funcionamiento son:
- [<ins>Pip</ins>](https://pypi.org/project/pip/)
- [<ins>Git</ins>](https://git-scm.com)
- [<ins>Python</ins>](https://www.python.org)
- [<ins>Venv</ins>](https://docs.python.org/es/3.8/library/venv.html)
- [<ins>Reflex</ins>](https://reflex.dev)

### Instalación
---


#### Windows

Para instalar Python puedes instalarlo desde la web de [<ins>*Python*</ins>](https://www.python.org/downloads/) y seguir los pasos de la instalación.

Para instalar [<ins>Pip</ins>](https://pypi.org/project/pip/) ejecutamos el siguiente comando `> python get-pip.py`

Para instalar [<ins>Git</ins>](https://git-scm.com) se puede instalar siguiendo la documentación oficial [<ins>aquí</ins>](https://git-scm.com/downloads/win).

Para instalar [<ins>*Venv*</ins>](https://docs.python.org/es/3.8/library/venv.html), se puede serguir su documentación oficial [<ins>aquí</ins>](https://docs.python.org/es/3.8/library/venv.html).


---
#### Linux

Para instalar *Python* en Linux se puede hacer con el siguiente comando.

`$ sudo apt install python3`

Para instalar *venv* en Linux se puede instalar con el siguiente comando.

`$ sudo apt install python3-venv`

---
Una vez instalados los requisitos creamos un archivo para la aplicación.

` mkdir ./mi-proyecto`

Y accedemos a la carpeta creada.

` cd mi-proyecto`

Una vez que estemos en la carpeta creada, clonamos el repositorio de github.

` git clone git@github.com:<tuusuario>/tuproyecto.git`

Una vez clonado, activamos *venv*. 

Windows: `> .\.venv\Scripts\activate`

Linux: `$ source nombre_del_entorno/bin/activate`

Una vez activado el *venv*, instalamos el [<ins>Reflex</ins>](https://reflex.dev) con el comando.

`pip install reflex` 

Una vez instalado todo, inicializamos *Reflex*.

`reflex run`

## Metodologia
A la hora de afontar la lógica, decidimos utilizar TDD (Test Driven Development) con la idea de que cada funcion nueva que se implementa pase una serie de casos test, para minimizar los errores en el código.

Inicialmente nos planteamos trabajar con una metodología prototipada, tratándo de crear una version extremadamente básica del software para poco a poco ir mejorando parte de la misma hasta conseguir el producto ya terminado. Pero a medida que hicimos las primeras *dailies*, ante el temor de no ir por buen camino debido a la inexperiencia, nos decantamos por una metodología en espiral, que era la recomendada en clase.

El marco de trabajo utilizado ha sido Kanban.

## Descripcion técnica
### Diagrama de casos de uso
[placeholder]
### Arquitectura de la aplicación
[placeholder]
### Posibles tecnologías
| Testing GUI        |
| ------------- |
| [<ins>Selenium</ins>](https://www.selenium.dev/)      |
| [<ins>Axiom.ai</ins>](https://axiom.ai/automate/web-ui-testing)      |

## Dieño
!["Imagen de el diseño alpha del la interfaz"](/assets/img-docs/diseño-alpha.png)

## Implementación

En este proyecto hemos usado:

- [Python](https://www.python.org)
- [Reflex](https://reflex.dev)
    - CSS
    - XML
- Git
- Markdown

## Pruebas


## Análisis del tiempo invertido


## Conclusiones