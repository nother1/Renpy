# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define e = Character("Eileen")


# El juego comienza aquí.

label start:
    e "Hey , bienvenido a renpy"
    e "Esto es un hola mundo"
    e "Puede que te tomes tu tiempo y sientas que no puedas continuar"
    e "Pero si aun tienes la llama, seguro podras avanzar"
    e "Creo en ti, y tu deberias creer en ti igual"
    e "Ten las fuerzas, y buena suerte"
    return
label examplestart:

    # Muestra una imagen de fondo: Aquí se usa un marcador de posición por
    # defecto. Es posible añadir un archivo en el directorio 'images' con el
    # nombre "bg room.png" or "bg room.jpg" para que se muestre aquí.

    scene bg room

    # Muestra un personaje: Se usa un marcador de posición. Es posible
    # reemplazarlo añadiendo un archivo llamado "eileen happy.png" al directorio
    # 'images'.

    show eileen happy

    # Presenta las líneas del diálogo.

    e "Has creado un nuevo juego Ren'Py."

    e "Añade una historia, imágenes y música, ¡y puedes presentarlo al mundo!"

    # Finaliza el juego:

    return
