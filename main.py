
import requests
import random
import string
import time
import os
from colorama import Fore, Style,init



def center_text(text: str, space: int = 0):
    lines = text.splitlines()
    if not space:
        space = (os.get_terminal_size().columns - len(lines[len(lines) // 2])) // 2
    return '\n'.join((' ' * space) + line for line in lines)




print(center_text("""

████████╗██████╗ ██╗██████╗     ██╗  ██╗██╗   ██╗██████╗      ██████╗ ███████╗███╗   ██╗
╚══██╔══╝██╔══██╗██║██╔══██╗    ██║  ██║██║   ██║██╔══██╗    ██╔════╝ ██╔════╝████╗  ██║
   ██║   ██████╔╝██║██████╔╝    ███████║██║   ██║██████╔╝    ██║  ███╗█████╗  ██╔██╗ ██║
   ██║   ██╔══██╗██║██╔═══╝     ██╔══██║██║   ██║██╔══██╗    ██║   ██║██╔══╝  ██║╚██╗██║
   ██║   ██║  ██║██║██║         ██║  ██║╚██████╔╝██████╔╝    ╚██████╔╝███████╗██║ ╚████║
   ╚═╝   ╚═╝  ╚═╝╚═╝╚═╝         ╚═╝  ╚═╝ ╚═════╝ ╚═════╝      ╚═════╝ ╚══════╝╚═╝  ╚═══╝
                                                                                        

""").replace('█', Fore.BLUE + '█' + Fore.RESET))
print(center_text('[ https://triphub.ga/ ~ https://github.com/elxocasXD/Trip-Hub ]')
        .replace('[', f"{Fore.LIGHTBLUE_EX}[{Fore.RESET}")
        .replace('~', f"{Fore.LIGHTBLUE_EX}~{Fore.RESET}")
        .replace(']', f"{Fore.LIGHTBLUE_EX}]{Fore.RESET}")
        + '\n\n'
    )

print(center_text("Send Friend Request to Space#0234 in case of bugs\n"))
time.sleep(0.2)
 
num = int(input(center_text('Input How Many Codes to Generate and Check: ')))

with open("Nitro Codes.txt", "w", encoding='utf-8') as file:
    print(center_text("Your nitro codes are being generated, be patient if you entered the high number!"))

    start = time.time()

    for i in range(num):
        code = "".join(random.choices(
            string.ascii_uppercase + string.digits + string.ascii_lowercase,
            k = random.randint(14, 16)
        ))

        file.write(f"https://discord.gift/{code}\n")

    print(center_text(f"Generated {num} codes | Time taken: {time.time() - start}\n"))


with open("Nitro Codes.txt") as file:
    for line in file.readlines():
        nitro = line.strip("\n")

        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(center_text(Fore.LIGHTGREEN_EX + f" Valid | {nitro} " + Style.RESET_ALL))
            break
        else:
            print(center_text(Fore.LIGHTRED_EX + f" Invalid | {nitro} "  + Style.RESET_ALL))
input("\nYou have generated, Now press enter to close this, you'll get valid codes in Valid Codes.txt if you see its empty then you got no luck, generate 10.000 codes for luck or else.")


