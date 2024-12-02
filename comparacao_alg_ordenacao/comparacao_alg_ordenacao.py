import random
import matplotlib.pyplot as plt
from algoritimos_ordenacao import*
from  tempo.time import medir_tempo_comparacoes



algoritmos = [
    ordenacao_selecao_comparacoes,
    ordenacao_shell_comparacoes,
    ordenacao_merge_comparacoes,
    ordenacao_quick_comparacoes,
    ordenacao_bucket_comparacoes,
    ordenacao_radix_comparacoes
]

nomes_algoritmos = [
    "Selection Sort", "Shell Sort", "Merge Sort",
    "Quick Sort", "Bucket Sort", "Radix Sort"
]

tempos = []
comparacoes = []

lista_teste = random.sample(range(1, 10001), 1000)

for alg, nome in zip(algoritmos, nomes_algoritmos):
    tempo, comp = medir_tempo_comparacoes(alg, lista_teste, iteracoes=1)
    tempos.append(tempo)
    comparacoes.append(comp)

plt.figure(figsize=(14, 7))

plt.subplot(1, 2, 1)
plt.bar(nomes_algoritmos, tempos, color='blue')
plt.title("Tempo de Execução")
plt.ylabel("Tempo (segundos)")

plt.subplot(1, 2, 2)
plt.bar(nomes_algoritmos, comparacoes, color='red')
plt.title("Número de Comparações")
plt.ylabel("Número de Comparações")

plt.tight_layout()
plt.show()
