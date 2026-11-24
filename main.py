"""Aplicación principal: flujo secuencial de agentes."""

import os
import re
import unicodedata
from datetime import datetime

from agentes.disenador_practica import crear_agente_disenador
from agentes.explicador import crear_agente_explicador
from agentes.revisor import crear_agente_revisor
from herramientas.archivos import guardar_markdown
from herramientas.validacion import validar_guia
from runtime.ejecutor import ejecutar_agente
from runtime.errores import (
    ConfiguracionIncompleta,
    ErrorDeArchivo,
    LimiteTemporal,
    RespuestaVacia,
    ServicioNoDisponible,
)


def _nombre_archivo(tema):
    """Convierte el tema en un nombre de archivo seguro."""
    texto = unicodedata.normalize("NFKD", tema)
    texto = texto.encode("ascii", "ignore").decode("ascii").lower()
    texto = re.sub(r"[^a-z0-9]+", "_", texto).strip("_")
    return f"guia_{texto or 'tema'}.md"


def _con_titulo(texto, titulo):
    """Asegura que la sección tenga su encabezado."""
    texto = texto.strip()
    if texto.startswith(titulo):
        return texto
    return f"{titulo}\n\n{texto}"


def _leer_validacion(resultado):
    """Devuelve (ok, faltantes) a partir de lo que responde validar_guia."""
    if isinstance(resultado, dict):
        valida = resultado.get("valida", resultado.get("ok"))
        return bool(valida), list(resultado.get("faltantes", []))
    if isinstance(resultado, (tuple, list)) and len(resultado) == 2:
        return bool(resultado[0]), list(resultado[1] or [])
    return bool(resultado), []


def ejecutar_flujo(tema, ejecutar=ejecutar_agente, permitir_correccion=False):
    """Coordina los agentes usando un ejecutor reemplazable en las pruebas."""
    tema = (tema or "").strip()
    if not tema:
        raise ValueError("El tema no puede estar vacío.")

    # 1. Explicador
    explicacion = ejecutar(crear_agente_explicador(), tema)

    # 2. Diseñador (recibe la explicación completa)
    practica = ejecutar(crear_agente_disenador(), explicacion)

    # 3. Borrador completo
    borrador = (
        f"# Guía de estudio: {tema}\n\n"
        f"{_con_titulo(explicacion, '## Explicación')}\n\n"
        f"{_con_titulo(practica, '## Práctica')}\n"
    )

    # 4. Revisor (recibe el borrador completo) -> guía final
    revisor = crear_agente_revisor()
    guia = ejecutar(revisor, borrador)

    # 5. Validación antes de guardar
    ok, faltantes = _leer_validacion(validar_guia(guia))

    # Extensión: una sola corrección
    if not ok and permitir_correccion:
        mensaje = (
            "Corrige esta guía. Debe incluir '# Guía de estudio', "
            "'## Explicación', '## Práctica' y '## Revisión'. "
            f"Faltantes: {faltantes}\n\n{guia}"
        )
        guia = ejecutar(revisor, mensaje)
        ok, faltantes = _leer_validacion(validar_guia(guia))

    if not ok:
        return {"ok": False, "faltantes": faltantes}

    # 6. Guardar (solo si la guía es válida)
    guardado = guardar_markdown(_nombre_archivo(tema), guia)
    if isinstance(guardado, dict):
        if not guardado.get("ok"):
            return {
                "ok": False,
                "faltantes": [guardado.get("error", "No se pudo guardar")],
            }
        return {"ok": True, "ruta": str(guardado.get("ruta"))}
    return {"ok": True, "ruta": str(guardado)}


def main():
    tema = input("Tema de Python: ").strip()
    if not tema:
        print("El tema no puede estar vacío.")
        return 1
    try:
        resultado = ejecutar_flujo(tema)
    except ValueError as error:
        print(error)
        return 1
    except ConfiguracionIncompleta:
        print("Falta configurar la clave o el modelo. Revisa tu archivo .env.")
        return 1
    except LimiteTemporal:
        print("Se alcanzó el límite de uso de la API. Espera un momento y reintenta.")
        return 1
    except ServicioNoDisponible:
        modelo = os.getenv("GEMINI_MODEL", "(sin definir)")
        hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(
            "El servicio no está disponible (503). Espera un momento y "
            "reintenta una sola vez."
        )
        print(f"Si persiste, anota: modelo={modelo}, hora={hora}.")
        print("Consulta también el estado del servicio de Gemini.")
        return 1
    except RespuestaVacia:
        print("El agente no devolvió texto. Intenta de nuevo con otro tema.")
        return 1
    except ErrorDeArchivo:
        print("No se pudo guardar el archivo. No se guardó contenido parcial.")
        return 1

    if resultado["ok"]:
        print(f"Guía guardada en: {resultado['ruta']}")
        return 0
    print(f"No se guardó la guía. Faltantes: {resultado['faltantes']}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())