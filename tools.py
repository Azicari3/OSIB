import subprocess
import socket
import json
import menu




def network_scan():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    p_ip = s.getsockname()[0]
    s.close()



    scan_ans = subprocess.run(
        ["ipconfig"],
        capture_output=True,
        text=True,
        encoding="cp850",
        shell=False
    )
    text = scan_ans.stdout
    lineas = text.split("\n")

    adaptador_actual = ""
    gateway = ""
    mascara = ""

    for i, linea in enumerate(lineas):
        linea_limpia = linea.strip()

        if "adaptador" in linea_limpia.lower():
            adaptador_actual = linea_limpia

        if "Wi-Fi" in adaptador_actual or "Ethernet" in adaptador_actual:
            if "Máscara de subred" in linea_limpia:
                mascara = linea_limpia.split(":")[-1].strip()

            if "Puerta de enlace predeterminada" in linea_limpia:
                valor = linea_limpia.split(":")[-1].strip()
                if valor and "." in valor:
                    gateway = valor
                else:
                    siguiente = lineas[i + 1].strip()
                    if "." in siguiente:
                        gateway = siguiente
    network_name = input("Introduzca el nombre de esta red")
    network_d = {
        "name" : network_name,
        "local_ip" : p_ip,
        "gateway" : gateway,
        "mask" : mascara
    }

    try:
        with open("network_data.json", "r", encoding="utf-8") as archivo:
            redes_guardadas = json.load(archivo)
    except FileNotFoundError:
        redes_guardadas = {}
    redes_guardadas[network_name] = network_d

    with open("network_data.json", "w", encoding="utf-8") as archivo:
        json.dump(redes_guardadas, archivo, indent=4, ensure_ascii=False)

    print("La red ha sido registrada correctamente, redirigiendo al menu principal...")
    menu.show_ascii()
    menu.menu_options()
    



def bring_ndata():
    try:
        with open ("network_data.json", "r", encoding = "utf-8") as file:
            data = json.load(file)
            
    except FileNotFoundError:
        print("No se registraron redes guardadas o no se puede acceder a las mismas.")
    print()

    n_table = list(data.keys())
    print("\n -----REDES REGISTRADAS-----\n")
    for i, nombre in enumerate(n_table, start=1):
        print(f"{i}. {nombre}")
    print()
    print("Porfavor seleccione la red a consultar:")
    selected_n = int(input())
    translate_table = n_table[selected_n -1]
    print()
    print("\n -----DATOS DE RED-----\n")
    network = data[translate_table]
    print(f"Nombre registrado:{network["name"]}")
    print(f"La ultima ip local registrada es: {network["local_ip"]}")
    print(f"Mascara de subred: {network["mask"]}")
    print(f"La dirección gateway:{network["gateway"]}")
    



      
 
