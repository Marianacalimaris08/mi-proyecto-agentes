"""Agente revisor de guías de estudio."""

import os

from google.adk.agents import Agent


def crear_agente_revisor():
    """Crea el agente que entrega la guía Markdown revisada."""
    return Agent(
        name="revisor_python",
        model=os.getenv("GEMINI_MODEL"),
        description="Revisa un borrador de guía de Python y devuelve la guía completa revisada.",
        instruction=(
            "Eres un revisor de guías de estudio de Python. Responde siempre en español. "
            "Recibirás un borrador en Markdown. Devuelve la guía completa en Markdown, "
            "conservando el título, las secciones ## Explicación y ## Práctica y los "
            "bloques de código útiles. Aplica solamente las correcciones necesarias y "
            "corrige cualquier contradicción. Agrega al final una sección ## Revisión "
            "con observaciones breves y respetuosas."
        ),
    )