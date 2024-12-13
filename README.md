**Tabla de contenidos**

-   [**Introducción**](#introducción)
-   [**Manual**](#manual)
    -   [**Pre-requisitos**](#pre-requisitos)
    -   [**Instalación**](#instalación)
    -   [**Uso**](#uso)
-   [**Metodología**](#metodología)
-   [**Descripción técnica**](#descripción-técnica)
    -   [**Requisitos funcionales/no funcionales, NOT LIST**](#partes-interesadas-y-requisitos-funcionalesno-funcionales)
    -   [**Historias de usuario**](#historias-de-usuario)
    -   [**Arquitectura de la aplicación**](#arquitectura-de-la-aplicación)
-   [**Diseño**](#diseño)
    -   [**Diagrama de Componentes**](#componentes)
-   [**Implementacion**](#implementacion)
    -   [**Tecnologías y Herramientas utilizadas**](#tecnologías-y-herramientas-elegidas)
    -   [**Backend**](#backend)
    -   [**Frontend**](#frontend)
-   [**Pruebas**](#pruebas)
    -   [**Coverage**](#coverage)
    -   [**Test de unidad**](#test-de-unidad)
    -   [**Test de integración**](#test-de-integración)
-   [**Análisis del tiempo invertido**](#Tiempo-invertido)
    -   [**Clockify + Wakatime**](#clockify)
    -   [**Justificación temporal**](#justificación-temporal)
-   [**Conclusiones**](#conclusiones)
    -   [**Posibles mejoras**](#posibles-mejoras)
    -   [**Dificultades**](#dificultades)

# **Introducción**
Claro, aquí tienes el texto con algunos ajustes para que suene más fluido y profesional:  

---

Proyecto de 1ºDAM desarrollado por Alexander Gil y Edgar Gómez.  el proyecto de crear un juego de ¿Quién es quién? utilizando el framework open source **[Reflex](https://reflex.dev/)**.  
Este framework fue seleccionado por nuestro Product Owner debido a su facilidad.

---  
# **Manual**
## **Pre-requisitos**
-   `Git`
-   `Python`
-   `reflex`

## Uso
**1. Una vez instalada la aplicacion y puesto todos los comandos,entraremos al localhost que se nos ha proporcionado**

**2. Dentro de la pagina web veras un boton que te dira "Comenzar juego"**

**3. Veras un cambio y apareceran los personajes y un chat**

**4. Ya puedes jugar**

# **Metodología**
La metodologia que usamos para este codigo fue apoyarnos en la pagina de reflex que tenia bastantes codigos ya pre-creados y esto facilito mucho el trabajo, y para el frontend pusimos dentro las definiciones los tamaños de alto y ancho, y colocamos las imagenes que tenemos dentro de assets.

# **Descripción Técnica**
La aplicación, desarrollada con el framework Reflex, toma como referencia el clásico juego de ¿Quién es quién?
En el cual es un tablero con unos personajes, de los cuales a base de preguntas tienes que conseguir adivinar el personaje que se ha escogido aleatoriamente por el codigo.

## **Historias de usuario**
!



## **Arquitectura de la aplicación**

*Configuraciones y requerimientos*
- **/assets** : Guardamos las imagenes necesarias,
- **/rxconfig.py** : Configuracion de reflex,
- **/requirements.txt** : En este .txt se encuentran las dependencias,
- **test** : Aqui se encuentran los casos test.

*Front y backend*
- **/Quien_es_Quien/test** : Ubicación de los casos test,
- **/Quien_es_Quien/personaje_aleatorio.py** : Se encuentra la lista de los personajes, con sus caracteristicas y ruta de imagen, y la funcion para que escoja un personaje aleatoriamente
- **/Quien_es_Quien/Quien_es_Quien** : El juego, no separamos front y backend(error nuestro), por lo cual en este archivo encontraras el codigo con sus funciones.
- **/Quien_es_Quien/style/style.py** : Estilos.


## **Diagrama de Componentes**
![Component Design](assets/Diagrama%20de%20componentes.png)


# **Implementación**
## **Tecnologías y Herramientas Elegidas**
- [Reflex](https://reflex.dev/)
    - Este framework fue seleccionado por nuestro Product Owner (profesor) para llevar a cabo el desarrollo del proyecto.
- [Python](https://www.python.org/)
    - [Pytest](https://docs.pytest.org/en/stable/) 
        - Biblioteca esencial para los casos test


# **Tiempo invertido**
## **Wakatime**
![Wakatime](assets/alex%201.png)
![Wakatime 2](assets/edgar%201.png)
![Wakatime 3](assets/alex%202.png)
![Wakatime 4](assets/edgar%202.png)
nos faltan capturas y tuvimos algun problema con el wakatime porque no nos cogia el tiempo correcto y a veces no recogia el tiempo

# **Conclusiones**
Nos gustaria implementar mas cosas, pero con el tiempo que tuvimos y el conocimiento fue hasta donde pudimos llegar.
Por lo general ha sido una experiencia nueva esto de programar un trabajo de este calibre. 
## **Posibles mejoras**
Hay muchas cosas por mejorar, como ya mencione es nuestro primer proyecto, deberiamos haber creado 2 ramas o mas, separar el backend y frontend, la organizacion nos costo al principio, miraremos al pasado y mejoraremos para el futuro.
## **Dificultades**
Al principio tuvimos dificultades con la logica para responder las preguntas porque la logica que teniamos era un poco ambigua, ya que a veces preguntabas si era un personaje te lo tomaba como una caracteristica y viceversa, tambien tuvimos dificultades con el evento para que desaparecieran los personajes cuando no tenian la caracteristica preguntada.