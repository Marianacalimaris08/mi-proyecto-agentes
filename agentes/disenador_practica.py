"""Agente diseñador de prácticas de Python."""

import os

from google.adk.agents import Agent


def crear_agente_disenador():
    """Crea el agente que diseña una práctica breve."""
    return Agent(
        name="disenador_practica",
        model=os.getenv("GEMINI_MODEL"),
        description="Diseña una práctica breve a partir de un tema y su explicación.",
        instruction=(
            "Eres un diseñador de prácticas de Python. Responde siempre en español. "
            "Recibirás un tema y una explicación previa. Usa los conceptos de esa "
            "explicación sin repetirla completa. Entrega: 1) un ejercicio, "
            "2) tres criterios de aceptación y 3) una pista que no revele la solución."
        ),
    )