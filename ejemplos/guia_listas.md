# Guía de estudio: listas

## Explicación

¡Hola! Como tu profesor de Python, hoy vamos a ver uno de los conceptos más importantes: las **listas**.

### 1. Explicación breve
Una lista en Python es una estructura de datos ordenada y mutable (lo que significa que se puede cambiar) que sirve para almacenar múltiples elementos en una sola variable. Los elementos se colocan entre corchetes `[]` y se separan por comas. Cada elemento tiene un índice numérico que empieza en `0`.

### 2. Ejemplo de código
```python
# Crear una lista de frutas
frutas = ["manzana", "banana", "cereza"]

# Acceder a un elemento por su índice
print(frutas[0])  # Salida: manzana

# Añadir un nuevo elemento
frutas.append("naranja")

print(frutas)  # Salida: ['manzana', 'banana', 'cereza', 'naranja']
```

### 3. Error frecuente
Un error muy común es intentar acceder a un índice que no existe, olvidando que en Python **contamos desde el 0**. Si una lista tiene 3 elementos, sus índices válidos son 0, 1 y 2. Si intentas usar el 3, obtendrás un error.

**Error:**
```python
frutas = ["manzana", "banana", "cereza"]
print(frutas[3])  # ¡ IndexError: list index out of range !
```

## Práctica

### 1. Ejercicio
Crea una lista llamada `inventario` que contenga inicialmente tres herramientas: `"martillo"`, `"destornillador"` y `"alicates"`. 
Posteriormente, realiza las siguientes operaciones en orden:
1. Añade la herramienta `"taladro"` al final de la lista utilizando el método correspondiente.
2. Modifica el segundo elemento de la lista (índice 1) para que ahora sea `"llave inglesa"`.
3. Imprime por pantalla la lista final resultante.

---

### 2. Criterios de aceptación
* **Creación correcta:** La variable `inventario` debe definirse usando corchetes `[]` con los tres elementos iniciales exactos.
* **Mutabilidad y métodos:** Se debe utilizar el método adecuado para agregar `"taladro"` y la asignación por índice para actualizar el segundo elemento.
* **Resultado final:** Al imprimir la lista al final del programa, el resultado exacto debe ser `['martillo', 'llave inglesa', 'alicates', 'taladro']`.

---

### 3. Pista
Recuerda que para modificar un elemento existente no necesitas usar métodos, sino acceder directamente a su posición numérica (teniendo en cuenta que el conteo empieza en `0`) y asignarle un nuevo valor con el signo `=`.

## Revisión

¡Hola! Como `revisor_python`, he analizado tu guía de estudio y está excelente. 

* **Observaciones:** 
  1. Se eliminó el saludo inicial conversacional ("¡Hola! Con gusto diseño la práctica...") en la sección de práctica para mantener un formato de guía didáctica más limpio y profesional.
  2. La explicación, los ejemplos de código y los criterios de aceptación son coherentes, precisos y están muy bien explicados para estudiantes que se inician en Python. 

¡Buen trabajo! La guía está lista para ser utilizada.