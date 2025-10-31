# Nível 6 - Bug oculto / armadilha
# Erros: mascaramento de exceções, corrupção silenciosa, condição de corrida simples
import threading
import time

shared = {'counter': 0, 'data': []}

def worker(n):
    for i in range(n):
        try:
            # operação que pode falhar em cenários reais
            if i % 10 == 0:
                raise ValueError("simulated intermittent error")
            shared['data'].append(i)
            # condição de corrida: sem lock, duas threads podem pisar aqui
            temp = shared['counter']
            time.sleep(0.0001)
            shared['counter'] = temp + 1
        except Exception:
            # exceção mascarada — não loga nada, perde-se contexto
            pass

if __name__ == "__main__":
    threads = [threading.Thread(target=worker, args=(1000,)) for _ in range(4)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print("Counter (esperado 4000):", shared['counter'])
    print("Len data (esperado <4000 por erros simulados):", len(shared['data']))
