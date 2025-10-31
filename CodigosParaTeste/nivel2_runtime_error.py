# Nível 2 - Runtime Error
# Erro: divisão por zero e acesso fora do índice
def process_scores(scores):
    # Pode gerar ZeroDivisionError se scores for vazio
    avg = sum(scores) / len(scores)
    print("Média:", avg)
    # Acesso fora dos limites - IndexError
    print("Primeiro:", scores[0], "Último:", scores[len(scores)])
    return avg

if __name__ == "__main__":
    # teste intencional para explodir
    process_scores([])
