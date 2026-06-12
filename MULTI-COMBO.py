import sys
import os

NOME = 'Multi-Combo'

if sys.platform.startswith('win'):
    import ctypes
    ctypes.windll.kernel32.SetConsoleTitleW(NOME)
else:
    sys.stdout.write(f''']2;{NOME}''')
    
if not os.path.exists('/sdcard/Multi-Combo'):
    os.makedirs('/sdcard/Multi-Combo')
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    clear()
    print("""    \33[0;30;103m𝐌𝐔𝐋𝐓𝐈𝐅𝐔𝐍𝐂𝐎𝐄𝐒 𝐃𝐎 𝐊𝐀𝐊𝐀𝐒𝐇𝐈   \33[0m""")

def get_combo_lines_count(path):
    return sum(1 for _ in open(path, 'r'))

def split_and_save_combos(input_path=None, output_path=None):
    if input_path is None:
        input_path = '/sdcard/combo/'

    if output_path is None:
        output_path = '/sdcard/Multi-Combo/'

    combo_files = os.listdir(input_path)
    
    if not combo_files:
        print("\33[31mNenhum combo encontrado na pasta.\33[0m")
        quit()

    say = 0
    dsy = ""

    for idx, files in enumerate(combo_files, start=1):
        say = idx
        dsy = dsy + f"{say}= {files}\n"

    print(""" ESCOJA UN COMBO DE LA LISTA DE ABAJO:\n""" + dsy + """\33[33m\n Foram encontrados """ + str(say) + """ Combos! Escolha um.  """)
    
    dsyno = int(input(" \33[32mCombo N°: \33[0m"))
    
    if dsyno <= 0 or dsyno > say:
        print("\33[31mOpcion inválida.\33[0m")
        quit()

    clear()
    banner() 
    say = 0

    selected_file = combo_files[dsyno - 1]
    dosyaa = os.path.join(input_path, selected_file)

    print(dosyaa)

    # Mostrar a quantidade de linhas no combo
    combo_lines_count = get_combo_lines_count(dosyaa)
    print(f"\n \33[33mEste combo contém {combo_lines_count} linhas.\33[0m\n")

    with open(dosyaa, 'r') as c:
        totLen = c.readlines()

    temiz = dosyaa
    storehouse = set()

    for i in totLen:
        line = (i.replace(' ', '').replace('\n', ''))  # Remover espaços e nova linha
        storehouse.add(line)

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    num_parts = int(input(" Digite o número de partes para dividir el combo: "))
    lines_per_part = len(storehouse) // num_parts

    for part_num in range(num_parts):
        start_idx = part_num * lines_per_part
        end_idx = (part_num + 1) * lines_per_part
        part_lines = list(storehouse)[start_idx:end_idx]

        filename = f"{selected_file}_part{part_num + 1}.txt"
        output_file_path = os.path.join(output_path, filename)

        with open(output_file_path, 'w') as part_file:
            for line in part_lines:
                part_file.write(line + '\n')

        print(f"\n Parte {part_num + 1} salva en '{output_file_path}'.")

    quit()

def join_combos_and_save(input_path=None, output_path=None):
    if input_path is None:
        input_path = '/sdcard/Combo/'

    if output_path is None:
        output_path = '/sdcard/Multi-Combo/'

    combo_files = os.listdir(input_path)

    if not combo_files:
        print("\33[31mNenhum combo encontrado na pasta.\33[0m")
        quit()

    say = 0
    dsy = ""

    for idx, files in enumerate(combo_files, start=1):
        say = idx
        dsy = dsy + f"{say}= {files}\n"

    print(""" ESCOJA COMBOS DE LA LISTA DE ABAJO PARA UNIR:\n""" + dsy + """\33[33m\n Foram encontrados """ + str(say) + """ Combos!\n Escolha um ou mais (separados por espaço).  """)
    
    dsynos = input(" \33[32mCombos N° (separados por espacio): \33[0m").split()

    selected_files = [combo_files[int(dsyno) - 1] for dsyno in dsynos]

    clear()
    banner() 
    say = 0

    combined_lines = set()

    for selected_file in selected_files:
        dosyaa = os.path.join(input_path, selected_file)

        print(dosyaa)

        with open(dosyaa, 'r') as c:
            totLen = c.readlines()

        temiz = dosyaa

        for i in totLen:
            line = (i.replace(' ', '').replace('\n', ''))  # Remover espaços e nova linha
            combined_lines.add(line)

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    filename = input(" Digite o nome de arquivo \n para salvar (sem a extensão .txt): ")

    if not filename.endswith('.txt'):
        filename += '.txt'

    output_file_path = os.path.join(output_path, filename)

    with open(output_file_path, 'w') as combined_file:
        for line in combined_lines:
            combined_file.write(line + '\n')

    print(f"""\n Pronto, Los combos seran unidos.\n Resultado salvado en \n '{output_file_path}'. """)
    quit()

def remove_duplicates_and_save(input_path=None, output_path=None):
    if input_path is None:
        input_path = '/sdcard/combo/'

    if output_path is None:
        output_path = '/sdcard/Multi-Combo/'

    combo_files = os.listdir(input_path)
    
    if not combo_files:
        print("\33[31mNenhum combo encontrado na pasta.\33[0m")
        quit()

    say = 0
    dsy = ""

    for idx, files in enumerate(combo_files, start=1):
        say = idx
        dsy = dsy + f"{say}= {files}\n"

    print(""" ESCOJA UN COMBO DE LA LISTA DE ABAJO:\n""" + dsy + """\33[33m\n Foram encontrados """ + str(say) + """ Combos! Escolha um.  """)
    
    dsyno = int(input(" \33[32mCombo N°: \33[0m"))
    
    if dsyno <= 0 or dsyno > say:
        print("\33[31mOpcion inválida.\33[0m")
        quit()

    clear()
    banner() 
    say = 0

    selected_file = combo_files[dsyno - 1]
    dosyaa = os.path.join(input_path, selected_file)

    print(dosyaa)

    # Mostrar a quantidade de linhas no combo
    combo_lines_count = get_combo_lines_count(dosyaa)
    print(f"\n \33[33mEste combo contiene {combo_lines_count} lineas.\33[0m\n")

    with open(dosyaa, 'r') as c:
        totLen = c.readlines()

    temiz = dosyaa
    storehouse = set()

    for i in totLen:
        line = (i.replace(' ', '').replace('\n', ''))  # Remover espaços e nova linha
        storehouse.add(line)

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    filename = input(" Digite o nombre del arquivo \n para salvar (con  extension .txt): ")

    if not filename.endswith('.txt'):
        filename += '.txt'

    output_file_path = os.path.join(output_path, filename)

    with open(output_file_path, 'w') as removed_lines_file:
        for line in storehouse:
            removed_lines_file.write(line + '\n')

    # Adicionar a contagem de linhas removidas e restantes
    total_lines = len(totLen)
    removed_lines = total_lines - len(storehouse)

    print(f"""\n Pronto, Foram Removidos \33[33m{removed_lines} \33[0m Duplicados. \n Restam \33[33m{len(storehouse)}\33[0m linhas.\n\n Os resultados foram salvos em \n '{output_file_path}'. """)
    quit()

# Menu principal
while True:
    clear()
    print("\n\n\33[0;30;103m〓〓〓〓〓 𝗠𝗘𝗡𝗨 〓〓〓〓〓\033[0m")    
    print("Seleccione una opcion:")
    print("1. Dividir combos")
    print("2. Unir combos")
    print("3. Remover duplicados")
    print("4. Salir")

    choice = input("Opcion: ")

    if choice == '1':
        split_and_save_combos()
    elif choice == '2':
        join_combos_and_save()
    elif choice == '3':
        remove_duplicates_and_save()
    elif choice == '4':
        quit()
    else:
        print("\33[31mOpcion inválida. Intente nuevamente.\33[0m")