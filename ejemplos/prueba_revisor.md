# Borrador coherente (revisado)

# Guía de estudio: Listas de Python

## Explicación

Una lista es una estructura de datos mutable y ordenada que permite almacenar múltiples valores bajo una misma variable. Los elementos dentro de una lista conservan el orden en el que fueron insertados y se accede a ellos mediante índices numéricos que comienzan en `0`.

```python
nombres = ["Ana", "Luis"]
print(nombres[0])  # Imprime "Ana"
```

Las listas también permiten almacenar elementos de diferentes tipos de datos, modificarse después de su creación (añadir, eliminar o cambiar elementos) y utilizar diversas funciones integradas como `len()` para conocer su tamaño.

## Práctica

Escribe una función en Python que reciba una lista de nombres como parámetro y devuelva la cantidad total de elementos que contiene.

```python
def contar_nombres(lista_nombres):
    return len(lista_nombres)

# Ejemplo de uso:
nombres = ["Ana", "Luis", "Carlos"]
print(contar_nombres(nombres))  # Debería imprimir 3
```

## Revisión

- Se amplió ligeramente la sección de **Explicación** para ofrecer una definición más clara y completa sobre las características principales de las listas en Python.
- Se mantuvo el ejemplo original por ser claro y directo.
- Se agregó un bloque de código sugerido en la sección de **Práctica** para mostrar una solución clara al ejercicio planteado.

# Contradicción introducida



Nota: las listas son inmutables y no se pueden modificar después de crearlas.


# Borrador con contradicción (revisado)

# Guía de estudio: Listas de Python

## Explicación

Una lista conserva varios valores en un orden definido. A diferencia de las tuplas, las listas son **mutables**, lo que significa que sus elementos pueden modificarse, agregarse o eliminarse después de haber sido creadas.

```python
nombres = ["Ana", "Luis"]
print(nombres[0])  # Imprime: Ana

# Las listas se pueden modificar
nombres.append("Carlos")
print(nombres)  # Imprime: ['Ana', 'Luis', 'Carlos']
```

## Práctica

Escribe una función que devuelva la cantidad de nombres de una lista utilizando la función incorporada `len()`.

```python
def contar_nombres(lista_nombres):
    return len(lista_nombres)

# Ejemplo de uso:
nombres = ["Ana", "Luis", "Carlos"]
print(contar_nombres(nombres))  # Imprime: 3
```

## Revisión

- Se corrigió la contradicción final del borrador: se aclaró correctamente que las listas son **mutables** (no inmutables).
- Se añadió un ejemplo de modificación en la sección de explicación para reforzar el concepto de mutabilidad.
- Se complementó la sección práctica con un ejemplo de código funcional para guiar mejor al estudiante.
