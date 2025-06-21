###Definino la clase cancion
class Cancion:
    """
    Esto es una clase que representa una cancian.
    Las clases son como moldes para crear objetos.
    """
    
    # Lista de generos permitidos (variable de clase)
    generos = ['Rock', 'Jazz', 'Rock', 'Funk', 'Reggae', 'Rap']
    """
    Esta lista está FUERA de __init__ por lo que es compartida por
    todas las canciones. Es constante (no cambia).
    Se accede con self.generos dentro de la clase.
    """
###Parte 1: El Constructor (__init__)
    def __init__(self, nombre, artista, duracion, genero, anio, num_likes=0):
        """
        El constructor es un método ESPECIAL que Python llama automáticamente
        cuando creas un nuevo objeto: Cancion(...)
        
        self: Es una referencia al objeto que se está creando (obligatorio)
        Los demas parametros son los datos de la cancion.
        
        num_likes=0: Parámetro opcional (si no se especifica, será 0)
        """
        
        # Chequeando del nombre
        if not isinstance(nombre, str) or nombre.strip() == "":
            raise ValueError("El nombre tiene ser un texto")
        """
        isinstance() verifica el tipo de dato
        nombre.strip() == "" verifica si es string vaciio o solo espacios
        raise ValueError lanza un error si la Chequeando falla
        """
        self.nombre = nombre  # Guardamos el nombre en el objeto
        
        # Chequeando del artista (similar al nombre)
        if not isinstance(artista, str) or artista.strip() == "":
            raise ValueError("El artista tiene ser un texto")
        self.artista = artista
        
        # Chequeando de la duracion
        if not isinstance(duracion, int) or duracion <= 0:
            raise ValueError("La duracion tiene ser un numero entero")
        """
        duracion debe ser int (no float) y mayor que 0
        """
        self.duracion = duracion
        
        # Chequeando el genero
        if genero not in self.generos:
            raise ValueError(f"genero no valido. tiene ser uno de: {', '.join(self.generos)}")
        """
        Verificamos que el genero esté en la lista permitida
        f-string (f"...") permite incluir variables dentro del string
        ", ".join() convierte la lista en un string separado por comas
        """
        self.genero = genero
        
        # Chequeando el año
        if not isinstance(anio, int) or anio <= 0:
            raise ValueError("El año de edición tiene ser un numero entero")
        self.anio = anio
        
        # Chequeando likes
        if not isinstance(num_likes, int) or num_likes < 0:
            raise ValueError("El numero de likes tiene ser un entero o cero")
        self.num_likes = num_likes
###Parte 2: Método __str__
    def __str__(self):
        """
        Método ESPECIAL que Python usa cuando s imprime el objetocon print()
        o se lo convierte a string con str()
        
        Debe devolver un string con el formato especificado.
        """
        return f"'{self.nombre}' - '{self.artista}' ({self.duracion})"
        """
        f-strings permiten incluir variables directamente:
        Ejemplo: si nombre="Cancioncita", artista="Pepito", duracion=354
        Devuelve: 'Canciocista' - 'Pepito' (354)
        """
###Parte 3: Metodo static de mayorDuracion
    @staticmethod
    def mayorDuracion(cancion1, cancion2):
        """
        @staticmethod indica que este método NO necesita acceso al objeto (self)
        y se llama directamente desde la clase: Cancion.mayorDuracion(c1, c2)
        
        Compara dos canciones y devuelve la de mayor duracion.
        """
        if not isinstance(cancion1, Cancion) or not isinstance(cancion2, Cancion):
            raise TypeError("Los parametros tienen ser de tipo Cancion")
            """
            Verificamos que ambos parametros sean objetos cancion
            """
            
        return cancion1 if cancion1.duracion > cancion2.duracion else cancion2
        """
        Operador ternario: 
        Devuelve cancion1 SI su duracion es mayor, SINO devuelve cancion2
        """
###Parte 4: Metodo agregaLikes
    def agregaLikes(self, cantidad):
        """
        Metodo normal (usa self) que modifica los likes de la cancion.
        """
        if not isinstance(cantidad, int) or cantidad <= 0:
            raise ValueError("La cantidad tiene ser un numero entero")
            
        self.num_likes += cantidad
        """
        += es equivalente a: self.num_likes = self.num_likes + cantidad
        """
###Parte 5: Metodo static de masVotada
    @staticmethod
    def masVotada(cancion1, cancion2):
        """
        Compara dos canciones del MISMO artista y genero.
        Si no cumplen, explica por que.
        """
        if cancion1.artista != cancion2.artista or cancion1.genero != cancion2.genero:
            raise Exception("Las canciones tienen que ser del mismo artista y genero")
            
        return cancion1 if cancion1.num_likes > cancion2.num_likes else cancion2
        """
        Misma logica que mayorDuracion pero comparando num_likes
        """
##Conceptos claves y su explicacion(que me sirve para entender mi code):
"""Clase: Molde para crear objetos (como una ficha tacnica o recetario)

Objeto: Instancia concreta de una clase (ej: una cancion específica)

self: Referencia al objeto actual (siempre en metodos normales)

@staticmethod: Metodo que no usa self (pertenece a la clase)

Validaciones: Garantizan que el objeto siempre esté en estado correcto

raise: Lanza excepciones cuando algo falla

f-strings: Forma de formatear strings con variables
"""

#ULTIMO: PRUEBA DEL CODIGO al ejecutarse el compilador
# PRIMERO: Creacionn de algunas canciones para probar
print("=== Canciones de prueba ===")

# cancion 1 - Todos los datos correctos para ser valida con el codigo
cancion1 = Cancion("The Change", "Evanescence", 125, "Rock", 2012, 1000000)
print(f"cancion 1 creada: {cancion1}")  # tendria que mostrar: 'The Change' - 'Evanescence' (125)

# cancion 2 - Otra cancion valida que no va a dar error
cancion2 = Cancion("New Born", "Muse", 168, "Rock", 2009, 750000)
print(f"cancion 2 creada: {cancion2}\n")

# SEGUNDO: Probar de  comparar duraciones
print("=== Probando que cancion es mas larga ===")
mas_larga = Cancion.mayorDuracion(cancion1, cancion2)
print(f"Entre '{cancion1.nombre}' y '{cancion2.nombre}', la mas larga es: {mas_larga.nombre}\n")

# TERCERO: Probar el agregar likes
print("=== Probando agregar likes ===")
print(f"Likes antes: {cancion1.num_likes}")
cancion1.agregaLikes(5000)  # Agregamos 5000 likes
print(f"Likes después: {cancion1.num_likes}\n")

# CUARTO: Probamos comparar votos (caso exitoso)
print("=== Probando que cancion tiene mas likes (mismo artista y genero) ===")
# Creamos otra cancion de los Evanesncence para probar
cancion3 = Cancion("Bring me to life", "Evanescence", 200, "Rock", 1970, 1200000)
try:
    mas_votada = Cancion.masVotada(cancion1, cancion3)
    print(f"Entre '{cancion1.nombre}' y '{cancion3.nombre}', la mas votada es: {mas_votada.nombre}")
except Exception as e:
    print(f"Error: {e}")
print()

# QUINTO: Probamos comparar votos (caso con error)
print("=== Probando que cancion tiene mas likes (artistas diferentes - tiene que dFALLAR) ===")
try:
    mas_votada = Cancion.masVotada(cancion1, cancion2)  # Evanescence vs Muse
    print(f"Resultado: {mas_votada.nombre}")
except Exception as e:
    print(f"Funciona. Se encontro un error como tiene ser: {e}\n")

# SEXTO: Probamos crear canciones invalidas
print("=== Probando validaciones (tienen q fallar) ===")

print("Intento 1: Nombre vacio")
try:
    mala_cancion = Cancion("", "Artista", 180, "Rock", 2020)
except ValueError as e:
    print(f"Error correcto: {e}")

print("\nIntento 2: genero incorrecto")
try:
    mala_cancion = Cancion("Título", "Artista", 180, "Pop", 2020)
except ValueError as e:
    print(f"Error correcto: {e}")

print("\nIntento 3: Likes negativos")
try:
    mala_cancion = Cancion("Título", "Artista", 180, "Rock", 2020, -100)
except ValueError as e:
    print(f"Error correcto: {e}")