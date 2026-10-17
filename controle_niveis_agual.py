import os # Biblioteca para verificar o sistema operacional e limpar a tela
os.system ("cls" if os.name == "nt" else "clear" ) # Limpa a tela do terminal, dependendo do sistema operacional (Windows ou Linux/Mac).
import colorama # Biblioteca para colorir o texto no terminal, permitindo destacar mensagens importantes.
colorama.init() # Inicializa a biblioteca colorama, preparando-a para uso no terminal.
# **Início do programa:**
def linha ():
    print (f"{colorama.Fore.CYAN}\n{'-' * 50}{colorama.Style.RESET_ALL}") # Função para imprimir uma linha de separação no terminal, utilizando a cor azul claro para destaque.
    print(colorama.Fore.CYAN + "\n          CONTROLE DE NÍVEIS DE ÁGUA" + colorama.Style.RESET_ALL) # Exibe o título do programa no terminal
    print (f"{colorama.Fore.CYAN}\n{'-' * 50}{colorama.Style.RESET_ALL}") # Função para imprimir uma linha de separação no terminal, utilizando a cor azul claro para destaque.
linha () #chamando a função linha ex: -------------

niveis_reservatorio = ["1", "2", "3", "4", "5"] # Lista de níveis do reservatório, representando diferentes alturas de água.

def verificar_nivel(nivel): # Função para verificar o nível do reservatório, recebendo o nível como parâmetro.
    print(colorama.Fore.CYAN + f"\nNível {nivel} do reservatório" + colorama.Style.RESET_ALL) # Exibe o nível atual do reservatório em azul claro.
    if nivel == "1": # Condição para o nível 1, indicando que o reservatório está vazio.
        print(colorama.Fore.RED + "Alerta: Reservatório vazio! Nível crítico!" + colorama.Style.RESET_ALL) # Mensagem de alerta em vermelho para nível crítico.
    elif nivel == "2": # Condição para o nível 2, indicando que o reservatório está baixo.
        print(colorama.Fore.YELLOW + "Atenção: Reservatório baixo! Nível de atenção!" + colorama.Style.RESET_ALL) # Mensagem de atenção em amarelo para nível baixo.
    elif nivel == "3": # Condição para o nível 3, indicando que o reservatório está em nível médio.
        print(colorama.Fore.GREEN + "Reservatório em nível médio. Nível seguro." + colorama.Style.RESET_ALL) # Mensagem de segurança em verde para nível médio.
    elif nivel == "4": # Condição para o nível 4, indicando que o reservatório está alto.
        print(colorama.Fore.BLUE + "Reservatório alto. Nível seguro." + colorama.Style.RESET_ALL) # Mensagem de segurança em azul para nível alto.
    elif nivel == "5": # Condição para o nível 5, indicando que o reservatório está cheio.
        print(colorama.Fore.MAGENTA + "Reservatório cheio. Nível máximo!" + colorama.Style.RESET_ALL) # Mensagem de alerta em magenta para nível máximo.

for nivel in niveis_reservatorio: # Loop para iterar sobre cada nível do reservatório.
    verificar_nivel(nivel) # Chama a função verificar_nivel() para cada nível, exibindo as mensagens correspondentes no terminal.
