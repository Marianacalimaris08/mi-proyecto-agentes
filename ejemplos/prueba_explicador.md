# Tema: listas

¡Hola! Como tu profesor de Python, hoy veremos uno de los conceptos más importantes y útiles: **las listas**.

### 1. Explicación breve
Una **lista** en Python es una estructura de datos ordenada y **mutable** (es decir, se puede modificar después de crearla) que permite almacenar una colección de elementos. Estos elementos pueden ser de cualquier tipo: números, textos, booleanos e incluso otras listas. Se definen utilizando corchetes `[]` y los elementos se separan por comas.

### 2. Ejemplo pequeño de código
```python
# Creamos una lista con diferentes tipos de datos
estudiantes = ["Ana", "Carlos", "Sofía"]

# Agregamos un nuevo elemento al final
estudiantes.append("David")

# Accedemos al primer elemento (en Python, las listas empiezan a contar desde el 0)
print(estudiantes[0])  # Salida: Ana

# Mostramos toda la lista
print(estudiantes)  # Salida: ['Ana', 'Carlos', 'Sofía', 'David']
```

### 3. Error frecuente
Un error muy común entre los principiantes es intentar acceder a una posición (índice) que no existe en la lista, lo que genera un error llamado `IndexError`.

```python
# Ejemplo del error:
numeros = [10, 20, 30]
print(numeros[3])  # ¡Error! La lista solo tiene índices 0, 1 y 2.
```
*Recuerda: si una lista tiene $N$ elementos, el último elemento está en la posición $N - 1$.*

# Tema: funciones

¡Hola! Como tu profesor de Python, hoy veremos uno de los conceptos más importantes: **las funciones**.

### 1. Explicación breve
Una función es un bloque de código reutilizable que realiza una tarea específica. En Python, se definen usando la palabra clave `def`, seguida del nombre de la función y paréntesis `()`. Pueden recibir datos (llamados *argumentos* o *parámetros*) y devolver un resultado usando la instrucción `return`. Sirven para organizar el código, evitar repetirlo y hacerlo más fácil de mantener.

### 2. Ejemplo pequeño de código
```python
# Definimos la función que calcula el área de un rectángulo
def calcular_area(base, altura):
    area = base * altura
    return area


# Llamamos a la función y guardamos el resultado
resultado = calcular_area(5, 3)
print(
    "El área es:", resultado
)  # Salida: El área es: 15
```

### 3. Error frecuente
Olvidar usar la instrucción `return` cuando necesitas que la función devuelva un valor para usarlo después. Si omites `return`, la función por defecto devolverá `None`.

**Ejemplo del error:**
```python
def sumar(a, b):
    total = a + b
    # Falta el return aquí


resultado = sumar(2, 3)
print(resultado)  # Salida: None (¡Cuidado! No guardó la suma)
```
