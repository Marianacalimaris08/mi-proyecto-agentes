# Agentes de IA con Python

Aplicación que genera guías de estudio de Python: un agente explica el tema, otro propone una práctica y un tercero revisa el borrador.

Documentación de la aplicación. Amplía este README, situado junto a `main.py`,
con las decisiones, los ejemplos y la reflexión del proyecto.

La imagen creó estos archivos con `iniciar-proyecto`. Consulta la
[guía de trabajo con Docker y VS Code](docs/trabajar-con-docker.md).

## Antes de comenzar

La imagen Docker proporcionada contiene Python, ADK y las dependencias necesarias.

Configura la imagen pública preparada para este proyecto una vez en cada
terminal y descárgala:

```bash
export AGENTS_IMAGE="ghcr.io/hbtn-edu/ai-agents-python:0.4.0"
docker pull "$AGENTS_IMAGE"
```

Ubícate en la carpeta local creada al inicializar el proyecto. `"$PWD"` comparte la carpeta
actual con el contenedor para que puedas editarla con tus herramientas habituales.

```bash
# Comprobar Python, ADK y el entorno sin consumir API
docker run --rm -it --user "$(id -u):$(id -g)" -v "$PWD:/workspace" -w /workspace \
  "$AGENTS_IMAGE" python -m runtime.diagnostico --sin-api

# Ejecutar las pruebas básicas del starter pack
docker run --rm -it --user "$(id -u):$(id -g)" -v "$PWD:/workspace" -w /workspace \
  "$AGENTS_IMAGE" \
  python -m pytest -q pruebas/test_entorno.py pruebas/test_runtime.py

# Ejecutar todas las pruebas públicas de las tareas obligatorias durante el proyecto
docker run --rm -it --user "$(id -u):$(id -g)" -v "$PWD:/workspace" -w /workspace \
  "$AGENTS_IMAGE" python -m pytest -q -k 'not extension'

# Ejecutar la aplicación después de configurar .env
docker run --rm -it --user "$(id -u):$(id -g)" --env-file .env -v "$PWD:/workspace" -w /workspace \
  "$AGENTS_IMAGE" python main.py
```

La prueba de la extensión opcional se ejecuta con `python -m pytest -q pruebas/test_flujo.py`,
usando el mismo comando Docker y sin el filtro `-k`.

Las pruebas de agentes, archivos, validación y flujo fallan al comienzo porque
corresponden al trabajo que debes completar. Las pruebas de entorno y runtime
deben pasar desde el primer momento.

## Configuración segura de Gemini

1. Abre [Google AI Studio](https://aistudio.google.com/apikey) e inicia sesión.
2. Crea una clave en la sección de claves de API. Si la cuenta requiere asociar
   un proyecto de Google Cloud, sigue la
   [guía de creación y gestión de claves](https://ai.google.dev/gemini-api/docs/api-key?hl=es-419).
3. Edita el `.env` creado al inicializar y completa `GOOGLE_API_KEY` con la clave.
4. Conserva `GEMINI_MODEL=gemini-3.5-flash` y las demás variables del archivo.
5. Comprueba con `git check-ignore .env` que Git ignora el archivo.

```bash
git check-ignore .env

docker run --rm -it --user "$(id -u):$(id -g)" --env-file .env -v "$PWD:/workspace" -w /workspace \
  "$AGENTS_IMAGE" python -m runtime.diagnostico --sin-api
```

La siguiente comprobación realiza una llamada real y consume cuota. Ejecútala
una vez para verificar el acceso:

```bash
docker run --rm -it --user "$(id -u):$(id -g)" --env-file .env -v "$PWD:/workspace" -w /workspace \
  "$AGENTS_IMAGE" python -m runtime.diagnostico --con-api
```

El diagnóstico informa si la clave está configurada, pero nunca muestra su
valor ni una parte de ella.

### Si el servicio no está disponible

El modelo configurado es `gemini-3.5-flash`, probado con este starter pack.
Si aparece `503 UNAVAILABLE` o «El servicio no está disponible», termina esa
ejecución, espera al menos un minuto y vuelve a ejecutar manualmente el mismo
comando una sola vez. Si vuelve a fallar, registra el modelo, la hora y el
mensaje, y consulta el [estado del servicio](https://aistudio.google.com/status).
Mientras se restablece, el modo simulado permite comprobar las operaciones locales.

Ante un error de cuota (`429`), detén las llamadas y revisa los límites de la
cuenta antes de una nueva ejecución. Consulta la
[guía de solución de problemas](https://ai.google.dev/gemini-api/docs/troubleshooting?hl=es-419),
solamente «Estrategia de reintentos» y «Verifica si tienes el modelo correcto».

## Modo simulado

Las respuestas fijas incluidas permiten comprobar el flujo sin consumir API.
La calidad de las respuestas a temas diferentes se verifica con ejecuciones reales.

```bash
docker run --rm -it --user "$(id -u):$(id -g)" --env-file .env -e MODO_SIMULADO=1 \
  -v "$PWD:/workspace" -w /workspace "$AGENTS_IMAGE" python main.py
```

## Estructura

- `agentes/`: archivos que completarás para cada agente.
- `herramientas/`: guardado seguro y validación determinista.
- `runtime/`: infraestructura de ejecución suministrada.
- `pruebas/`: pruebas públicas que no consumen API.
- `ejemplos/`: respuestas fijas y guías de ejemplo.
- `salida/`: archivos generados, ignorados por Git.

## Recomendaciones de seguridad y privacidad

- Utiliza datos ficticios y limita el contexto enviado a la información necesaria.
- Mantén la clave en `.env`, excluida de Git, documentación, capturas y mensajes.
- Si una clave se expone, revócala y reemplázala.

## Descripción

Aplicación en Python que genera guías de estudio sobre un tema de Python mediante un flujo secuencial de agentes con Google ADK y Gemini. Se ejecuta en Docker.

## Agentes y herramientas

- `explicador` (`agentes/explicador.py`): explica el tema con un ejemplo de código.
- `disenador_practica` (`agentes/disenador_practica.py`): propone un ejercicio con criterios de evaluación.
- `revisor` (`agentes/revisor.py`): une todo y entrega la guía final con la sección `## Revisión`.
- `guardar_markdown` (`herramientas/archivos.py`): guarda la guía en `salida/` de forma segura. Si falla, lanza `ErrorDeArchivo` y no deja contenido parcial.
- `validar_guia` (`herramientas/validacion.py`): comprueba título, secciones, bloque de código y que no haya datos sensibles.

## Configuración

El archivo `.env` (ignorado por Git) define la clave de Gemini y `GEMINI_MODEL=gemini-3.5-flash-lite`. Nunca se debe compartir ni subir la clave.

## Ejecución con Gemini

```bash
export AGENTS_IMAGE="ghcr.io/hbtn-edu/ai-agents-python:0.4.0"
docker run --rm -it --user "$(id -u):$(id -g)" --env-file .env \
  -v "$PWD:/workspace" -w /workspace "$AGENTS_IMAGE" python main.py
```

Pruebas:

```bash
docker run --rm -it --user "$(id -u):$(id -g)" -v "$PWD:/workspace" -w /workspace "$AGENTS_IMAGE" \
  python -m pytest -q pruebas/test_flujo.py -k 'not extension'
```

## Ejemplo de ejecución

```text
Tema de Python: listas
Guía guardada en: salida/guia_listas.md
```

Guías de ejemplo generadas con Gemini y validadas con `validar_guia`:

- [ejemplos/guia_listas.md](ejemplos/guia_listas.md)
- [ejemplos/guia_funciones.md](ejemplos/guia_funciones.md)

## Limitaciones

- Depende de la disponibilidad y las cuotas de Gemini (errores 429 y 503).
- La calidad del contenido puede variar entre ejecuciones.
- La validación comprueba la estructura, no que el contenido sea correcto.
- Solo hace una corrección automática cuando se activa `permitir_correccion`.

## Reflexión

1. **¿Qué diferencia hay entre una llamada directa a un modelo y un agente?** La llamada directa envía un texto y recibe una respuesta. Un agente tiene instrucciones propias, un rol y puede usar herramientas, y un ejecutor gestiona la sesión y los errores.
2. **¿Qué responsabilidad tiene cada agente y cada herramienta?** Cada agente hace una sola tarea: explicar, diseñar la práctica o revisar. Las herramientas hacen lo mecánico: guardar el archivo y validar la estructura.
3. **¿Qué parte es determinista y cuál puede variar?** Es determinista el orden del flujo, la validación, el nombre del archivo y el guardado. Varía el texto que genera el modelo.
4. **¿Por qué se valida con Python además de usar un revisor?** El revisor es un modelo y puede equivocarse o ignorar el formato. Python comprueba siempre las mismas reglas antes de guardar, sin depender del azar.
5. **¿Qué cambiaría al utilizar otro proveedor o un modelo local?** Habría que cambiar la configuración, la clave y el ejecutor. Los errores, la cuota y la calidad también serían distintos, pero el flujo, las herramientas y la validación seguirían igual.
