"""Agente explicador de temas de Python."""

import os

from google.adk.agents import Agent


def crear_agente_explicador():
    """Crea el agente que explica un tema de Python."""
    return Agent(
        name="explicador_python",
        model=os.getenv("GEMINI_MODEL"),
        description="Explica temas de Python de forma breve y clara.",
        instruction=(
            "Eres un profesor de Python. Responde siempre en español. "
            "Dado un tema, produce: 1) una explicación breve, "
            "2) un ejemplo pequeño de código en Python y "
            "3) un error frecuente relacionado con el tema."
        ),
    )