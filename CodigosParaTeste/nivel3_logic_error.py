# Nível 3 - Logical Error
# Erro: algoritmo implementado errado (cálculo de média ponderada com pesos mal aplicados)
def weighted_average(values, weights):
    # A pessoa que escreveu inverteu valores e pesos sem checar lengths
    if len(values) != len(weights):
        return 0  # mau tratamento: deveria lançar exceção
    total = 0
    for i in range(len(values)):
        # erro lógico: multiplicando índice pelo peso em vez do valor
        total += i * weights[i]
    # uso errado do divisor: soma dos valores em vez de soma dos pesos
    divisor = sum(values)
    return total / divisor

if __name__ == "__main__":
    vals = [10, 20, 30]
    wts = [1, 2, 3]
    print("Weighted average (esperado ~23.33):", weighted_average(vals, wts))
