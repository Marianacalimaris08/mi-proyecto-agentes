"""Validación determinista de guías de estudio."""

import os
import re

MARCADOR_PRUEBA = "TRAINING_SECRET_TEST_VALUE"
SECCIONES = ("## Explicación", "## Práctica", "## Revisión")


def validar_guia(contenido):
    """Devuelve si una guía cumple la estructura."""
    if not isinstance(contenido, str) or not contenido.strip():
        return {"valida": False, "faltantes": ["contenido no vacío"]}

    faltantes = []
    lineas = [linea.strip() for linea in contenido.splitlines()]
    primera = next((linea for linea in lineas if linea), "")

    if not primera.startswith("# Guía de estudio:"):
        faltantes.append("título")

    for seccion in SECCIONES:
        if not any(linea.startswith(seccion) for linea in lineas):
            faltantes.append(seccion)

    if not re.search(r"^```python[ \t]*\n.*?^```", contenido, re.DOTALL | re.MULTILINE):
        faltantes.append("bloque de código Python")

    clave = os.getenv("GOOGLE_API_KEY", "").strip()
    if MARCADOR_PRUEBA in contenido or (clave and clave in contenido):
        faltantes.append("contenido sensible")

    return {"valida": not faltantes, "faltantes": faltantes}