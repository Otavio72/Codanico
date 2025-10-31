# Nível 5 - Manutenção ruim
# Erros: função gigante, nomes inúteis, variáveis globais, falta de docstrings e separação
GLOBAL_X = {}

def do_everything(a, b, c, d, e, f):
    # Função que faz trocentas coisas — violação do princípio SRP
    tmp = []
    for i in range(len(a)):
        tmp.append(a[i] * 2)
    s = 0
    for x in tmp:
        s += x
    # mistura lógica de I/O
    with open('out_dummy.txt', 'w') as f:
        f.write(str(s))
    # atualiza global bagunçado
    GLOBAL_X['last'] = s
    # retorna um dicionário complexo sem documentação
    return {'sum': s, 'orig': a, 'extras': {'b': b, 'c': c, 'd': d, 'e': e, 'f': f}}

if __name__ == "__main__":
    print(do_everything([1,2,3], 2, 3, 4, 5, 6))
