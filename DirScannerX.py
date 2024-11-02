import requests
import sys
import time

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
}

def mostrar_menu():
    print("***************************************")
    print("* Herramienta creada por Técnicos en Hacking *")
    print("* No abuses de esta herramienta porque puedes causar ataque DoS *")
    print("* No nos hacemos responsables del mal uso que se le de a la herramienta *")
    print("***************************************")
    print("Selecciona una opción:")
    print("1. Visitar canal de YouTube")
    print("2. Página de Facebook")
    print("3. Canal de WhatsApp")
    print("4. Iniciar la herramienta")
    print("***************************************")
    opcion = input("Escribe el número de tu elección: ")
    return opcion

def dir_brute_force(url, wordlist):
    print("Iniciando escaneo en:", url)
    with open(wordlist, 'r') as f:
        for line in f:
            dir = line.strip()
            full_url = f"{url}/{dir}"
            try:
                response = requests.get(full_url, headers=HEADERS)
                print(f"Solicitando: {full_url} - Código de estado: {response.status_code}")
                if response.status_code == 200:
                    with open(f"{url.replace('http://', '').replace('https://', '').replace('/', '_')}_resultados.txt", 'a') as output_file:
                        output_file.write(f"{full_url}\n")
            except requests.exceptions.RequestException as e:
                print(f"Error al solicitar {full_url}: {e}")

def main():
    opcion = mostrar_menu()

    if opcion == '1':
        print("Visitando canal de YouTube...")
        https://www.youtube.com/@tecnicosenhacking
        sys.exit()
    elif opcion == '2':
        print("Visitando página de Facebook...")
        https://www.facebook.com/profile.php?id=61567254489160
        sys.exit()
    elif opcion == '3':
        print("Uniéndose al canal de WhatsApp...")
        https://whatsapp.com/channel/0029Vasu9Iy2ZjCsnXaOVA1E
        sys.exit()
    elif opcion == '4':
        print("***************************************")
        print("* Herramienta creada por Técnicos en Hacking *")
        print("* No abuses de esta herramienta porque puedes causar ataque DoS *")
        print("* No nos hacemos responsables del mal uso que se le de a la herramienta *")
        print("***************************************")

        url = input("Introduce la URL a escanear (ejemplo: http://example.com): ").strip()
        
        usar_diccionario = input("¿Quieres usar tu propio diccionario? (s/n): ").strip().lower()
        if usar_diccionario == 's':
            wordlist = input("Introduce la ruta completa del archivo de diccionario: ").strip()
        else:
            wordlist = "default.txt"

        print("Iniciando escaneo de directorios en", url)
        time.sleep(1)
        dir_brute_force(url, wordlist)

        print("***************************************")
        print("* Herramienta creada por Técnicos en Hacking *")
        print("* No abuses de esta herramienta porque puedes causar ataque DoS *")
        print("* No nos hacemos responsables del mal uso que se le de a la herramienta *")
        print("***************************************")
    else:
        print("Opción no válida. Saliendo...")
        sys.exit()

if __name__ == "__main__":
    main()
