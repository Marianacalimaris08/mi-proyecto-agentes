"""Guardado seguro de archivos Markdown."""

import os
import tempfile
from pathlib import Path

CARPETA_SALIDA = "salida"


def guardar_markdown(nombre_archivo, contenido):
    """Guarda contenido dentro de salida/."""
    if not isinstance(nombre_archivo, str) or not isinstance(contenido, str):
        return {"ok": False, "error": "El nombre y el contenido deben ser texto."}
    if not nombre_archivo.endswith(".md") or nombre_archivo == ".md":
        return {"ok": False, "error": "El nombre debe terminar en .md."}
    if (
        "/" in nombre_archivo
        or "\\" in nombre_archivo
        or "\0" in nombre_archivo
        or Path(nombre_archivo).is_absolute()
    ):
        return {
            "ok": False,
            "error": "Nombre no válido: no se permiten rutas ni subcarpetas.",
        }

    carpeta = Path(CARPETA_SALIDA)
    destino = carpeta / nombre_archivo
    temporal = None
    try:
        carpeta.mkdir(parents=True, exist_ok=True)
        descriptor, temporal = tempfile.mkstemp(dir=carpeta, suffix=".tmp")
        with os.fdopen(descriptor, "w", encoding="utf-8") as archivo:
            archivo.write(contenido)
        os.chmod(temporal, 0o644)
        os.replace(temporal, destino)
    except (OSError, UnicodeError) as error:
        if temporal and os.path.exists(temporal):
            os.remove(temporal)
        return {"ok": False, "error": f"No se pudo guardar el archivo: {error}"}

    return {"ok": True, "ruta": f"{CARPETA_SALIDA}/{nombre_archivo}"}