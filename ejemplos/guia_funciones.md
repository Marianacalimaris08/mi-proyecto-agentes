# Guía de estudio: funciones

## Explicación

¡Hola! Como tu profesor de Python, hoy veremos uno de los conceptos más importantes: las **funciones**.

### 1. Explicación breve
Una función es un bloque de código reutilizable que realiza una tarea específica. En Python, se definen usando la palabra reservada `def`, seguida del nombre de la función y paréntesis `()`. Pueden recibir datos de entrada (llamados *parámetros* o *argumentos*) y pueden devolver un resultado usando la palabra reservada `return`. Ayudan a que nuestro código sea más organizado, legible y fácil de mantener.

### 2. Ejemplo pequeño de código
```python
# Definimos la función que saluda y suma dos números
def sumar_y_saludar(nombre, a, b):
    resultado = a + b
    return f"Hola {nombre}, el resultado de la suma es: {resultado}"


# Llamamos a la función
mensaje = sumar_y_saludar("Ana", 5, 3)
print(mensaje)
```

### 3. Error frecuente
Un error muy común entre los principiantes es **olvidar usar `return`** cuando necesitan que la función devuelva un valor para usarlo después en el programa. Si no pones `return`, la función por defecto devolverá `None`, lo que puede causar confusiones si intentas hacer operaciones con ese resultado.

*Ejemplo del error:*
```python
def calcular_area(base, altura):
    area = base * altura
    # Falta el return aquí


resultado = calcular_area(10, 5)
print(resultado * 2)  # Esto dará un TypeError porque 'resultado' es None
```

## Práctica

¡Hola! Aquí tienes tu ejercicio práctico basado en el concepto de funciones.

### 1. Ejercicio
Crea una función llamada `calcular_precio_final` que reciba dos parámetros: el precio original de un producto (`precio`) y el porcentaje de descuento (`descuento`). La función debe calcular el precio aplicando el descuento correspondiente y **devolver** ese valor final. 

Luego, llama a la función con un precio de `200` y un descuento del `15`, guarda el resultado en una variable e imprímela.

### 2. Criterios de aceptación
1. La función debe estar definida correctamente utilizando la palabra reservada `def` y los parámetros `precio` y `descuento`.
2. La función debe utilizar la palabra reservada `return` para devolver el precio con el descuento aplicado (no debe usar `print` dentro de la función).
3. Se debe invocar la función pasando los argumentos correctos (`200` y `15`), y el resultado impreso en consola debe ser `170.0`.

### 3. Pista
Recuerda que para calcular el valor con descuento, puedes restar al precio original el resultado de multiplicar el precio por el descuento dividido entre 100. Y asegúrate de que tu función devuelva el cálculo usando `return` para que no obtengas `None` al imprimir la variable exterior.

---

## Revisión

¡Hola! Soy `revisor_python`. He revisado tu guía de estudio y está excelente. 

**Observaciones:**
- El texto es claro, motivador y tiene una estructura pedagógica muy sólida.
- Los ejemplos de código son correctos y el error frecuente ilustra muy bien el problema de omitir `return` (incluyendo la excepción `TypeError` que se generaría).
- La sección práctica define claramente las expectativas y los criterios de aceptación. No se encontraron contradicciones ni errores técnicos. 

¡Buen trabajo! La guía está lista para ser utilizada por los estudiantes.