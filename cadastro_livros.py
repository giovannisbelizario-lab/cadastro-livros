def titulo(txt):
    print('=' * len(txt))
    print(txt)
    print('=' * len(txt))
    
def cadastro_livros():
    livros = []
    while True:
        nome_livro = input('Digite o nome do livro: ').strip()
        print()
        livros.append(nome_livro)
        while True:
            opcao = input('Quer continuar? [S/N]').strip().upper()
            print()
            if opcao in ['N', 'S']:
                break
            print('Digite S ou N.')
        if opcao == 'N':
            break
    return livros

def procurar_livro(lista):
    titulo_livro = input('Digite o livro que quer encontrar: ').strip()
    for livro in lista:
        if livro.lower() == titulo_livro.lower():
            print(f'Livro encontrado: {livro}\n')
            break
    else:
        print('Livro não encontrado.\n')


def main():
    titulo('PROCURANDO LIVROS')
    lista = cadastro_livros()
    procurar_livro(lista)

if __name__ == '__main__':
    main()