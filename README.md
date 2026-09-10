# OSIB
OSIB — Herramienta de diagnóstico de red

⚠️ Proyecto personal en desarrollo activo. Todavía no está terminado, pero ya es funcional para lo que hace hasta ahora.

Qué hace

OSIB es una herramienta de diagnóstico de red escrita en Python. Actualmente:

Obtiene la IP local, el gateway y la máscara de subred de la máquina, parseando la salida de ipconfig.
Guarda los datos relevados en un archivo network_data.json para consultarlos después.
Por qué lo hice

Lo empecé para tener una herramienta propia y rápida de diagnóstico básico de red, en vez de tirar ipconfig y leer manualmente. Es también donde practico Python aplicado a networking — cada función que agrego la entiendo a fondo antes de sumarla, no copio código sin saber qué hace.

Estructura del proyecto
osib/
├── main.py      # Punto de entrada del programa
├── menu.py      # Manejo del menú interactivo
├── tools.py     # Funciones de diagnóstico de red
Cómo usarlo
bash
git clone <link-de-tu-repo>
cd osib
python main.py

Requiere Python 3 y ejecutarse en Windows (usa ipconfig para obtener los datos de red).
