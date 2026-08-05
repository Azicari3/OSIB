
import json
import tools



def show_ascii():
    print(" ███   ████ ███ ████  ")
    print("█   █ █      █  █   █ ")
    print("█   █  ███   █  ████  ")
    print("█   █     █  █  █   █ ")
    print(" ███  ████  ███ ████  ")
    print()
    print("Hola, soy OSIB, asistente de red")


def menu_options():
    print("[1]Añadir una red")
    print("[2] Diagnosticar problemas")
    print("[3] Información relevante")
    print("[4] Sobre OSIB")
    print()
    main_answer = int(input())
    if main_answer == 1:
        tools.network_scan()
    if main_answer == 3:
        tools.bring_ndata()

       

