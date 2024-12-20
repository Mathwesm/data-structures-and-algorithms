# Algoritmos de Busca e Ordenação

## 1. Busca Binária (Binary Search)

[Busca_Binária](algoritimos_busca/busca_binaria.py)

**Descrição**: A **Busca Binária** é um algoritmo de busca eficiente utilizado em listas ordenadas. O algoritmo divide a lista ao meio a cada iteração, comparando o valor central com o elemento alvo. Dependendo do resultado, a busca continua na metade superior ou inferior da lista. A complexidade do algoritmo é O(log n).

**Requisitos**: A lista deve estar ordenada porque o algoritmo depende da comparação do valor central para decidir se a busca deve continuar à esquerda ou à direita. Se a lista não for ordenada, o algoritmo falhará.

**Exemplo**: Se você estiver procurando o número 7 em uma lista ordenada `[1, 3, 5, 7, 9]`, o algoritmo começará verificando o número no meio da lista (5), depois ajusta a busca para a metade superior (onde 7 está localizado).

## 2. Busca por Interpolação (Interpolation Search)

[Busca_Interpolação](algoritimos_busca/busca_interpolacao.py)

**Descrição**: A **Busca por Interpolação** é uma melhoria da Busca Binária, mas só funciona de maneira eficiente quando a lista está ordenada e os elementos são distribuídos de maneira relativamente uniforme. Em vez de dividir a lista ao meio, ela usa a fórmula de interpolação para estimar a posição do elemento alvo. A complexidade do algoritmo pode ser O(log log n) em casos ideais, mas no pior caso, pode ser O(n).

**Vantagens**: Em listas com distribuição uniforme, a Busca por Interpolação pode ser mais rápida que a Busca Binária. Caso contrário, se os elementos não estiverem uniformemente distribuídos, o desempenho da Busca por Interpolação pode ser pior.

**Exemplo**: Para uma lista de inteiros entre 1 e 100 e uma busca pelo número 47, o algoritmo tenta estimar a posição do 47 com base no valor mínimo e máximo da lista, em vez de ir diretamente ao meio.

## 3. Busca por Saltos (Jump Search)

[Busca_Jump](algoritimos_busca/busca_jump.py)

**Descrição**: A **Busca por Saltos** divide a lista em blocos de tamanho fixo e, a partir da primeira posição, realiza uma busca linear para encontrar o bloco que contém o valor desejado. Em seguida, realiza uma busca linear dentro do bloco. O tempo de execução é O(√n), onde n é o número de elementos na lista.

**Escolha do "salto"**: O tamanho ideal do salto é √n, onde n é o tamanho da lista. Isso garante que o número de saltos seja mínimo e a busca linear dentro do bloco seja eficiente.

**Exemplo**: Se a lista tiver 100 elementos e o "salto" for 10, o algoritmo vai verificar o elemento nas posições 0, 10, 20, e assim por diante, até encontrar o bloco correto.

## 4. Busca Exponencial (Exponential Search)

[Busca_Expotencial](algoritimos_busca/busca_expotencial.py)

**Descrição**: A **Busca Exponencial** começa verificando a posição 1, depois 2, 4, 8, 16, etc., dobrando o índice a cada passo até ultrapassar o valor procurado ou chegar ao final da lista. Após isso, o algoritmo realiza uma busca binária entre o último índice válido e o anterior. A complexidade é O(log n).

**Combinação com Busca por Saltos e Busca Binária**: A Busca Exponencial combina a "expansão" de índices (como no Jump Search) com a busca binária para localizar a posição exata do elemento.

**Exemplo**: Se você estiver procurando o número 67 em uma lista crescente, o algoritmo começa verificando os índices 1, 2, 4, 8, até encontrar um índice maior que 67, e depois aplica a Busca Binária entre os índices onde o número poderia estar.


## 5. Ternary Search

[Busca_Ternary](algoritimos_busca/busca_ternaria.py)

**Descrição**: O **Ternary Search** é uma variação do Binary Search, onde a lista é dividida em três partes ao invés de duas. O algoritmo compara o elemento com os dois pontos de divisão e decide em qual terço a busca continuará. Ele tem complexidade O(log₃ n), que é ligeiramente melhor que o Binary Search em algumas situações.

**Exemplo**: Em uma lista ordenada, ao invés de comparar com o elemento do meio, o Ternary Search divide a lista em três partes e faz duas comparações em cada iteração.

## 6. Shell Sort

[Shell_Sort](algoritimos_ordenacao/shell_sort.py)

**Descrição**: O **Shell Sort** é uma generalização do Insertion Sort. Ele ordena a lista por "intervalos" que diminuem progressivamente até que a lista esteja ordenada. A eficiência do algoritmo depende da sequência de intervalos utilizada. As versões mais comuns das sequências de intervalo são: Shell, Knuth e Hibbard.

**Escolha da sequência de intervalo**: A sequência de intervalo afeta a eficiência do algoritmo. Sequências mais eficientes reduzem a quantidade de comparações necessárias. O algoritmo é mais eficiente que o Insertion Sort para listas grandes.

**Exemplo**: Para uma lista de tamanho 10, a sequência de intervalos pode começar com 5, depois 3, e, finalmente, 1.

## 7. Merge Sort

[Merge_Sort](algoritimos_ordenacao/merge_sort_Int.py)

**Descrição**: O **Merge Sort** é um algoritmo de ordenação baseado no princípio de "dividir para conquistar". Ele divide a lista em duas metades, ordena cada metade recursivamente e depois as combina (merge). A complexidade do Merge Sort é O(n log n), o que o torna eficiente para listas grandes.

**Dividir para conquistar**: A lista é dividida em sublistas cada vez menores até que cada sublista tenha um único elemento. Em seguida, as sublistas são combinadas de forma ordenada.

**Exemplo**: Para ordenar `[38, 27, 43, 3, 9, 82, 10]`, o Merge Sort divide a lista em duas metades, ordena cada metade recursivamente e depois as mescla para formar a lista ordenada.

## 8. Selection Sort

[Selection_Sort](algoritimos_ordenacao/selection_sort.py)

**Descrição**: O **Selection Sort** é um algoritmo simples que encontra o menor (ou maior) elemento em uma lista e o coloca na posição correta. Esse processo é repetido até que a lista esteja ordenada. Sua complexidade é O(n²), tornando-o ineficiente para listas grandes.

**Exemplo**: Para ordenar `[29, 10, 14, 37, 13]`, o Selection Sort seleciona o menor valor (10), troca-o com o primeiro elemento, e continua o processo com o restante da lista.

## 9. Bucket Sort

[Bucket_Sort](algoritimos_ordenacao/bucket_sort.py)

**Descrição**: O **Bucket Sort** divide os elementos em intervalos chamados de "baldes". Cada balde é ordenado separadamente, e os resultados são combinados. O algoritmo é mais eficiente para listas com valores distribuídos uniformemente em um intervalo fixo. A complexidade média é O(n + k), onde n é o número de elementos e k é o número de baldes.

**Exemplo**: Para ordenar a lista `[0.42, 0.32, 0.63, 0.53, 0.51]`, o Bucket Sort distribui os elementos nos baldes e, em seguida, ordena cada balde individualmente antes de combinar os resultados.

## 10. Radix Sort

[Radix_Sort](algoritimos_ordenacao/radix_sort.py)

**Descrição**: O **Radix Sort** é um algoritmo não comparativo de ordenação que ordena os números por cada dígito, começando pelo dígito menos significativo até o mais significativo. Ele pode ser aplicado em qualquer base (como base 10 ou base 2) e tem complexidade O(nk), onde n é o número de elementos e k é o número de dígitos.

**Exemplo**: Para ordenar a lista `[170, 45, 75, 90, 802, 24, 2, 66]`, o algoritmo começa classificando os números com base no primeiro dígito, depois no segundo, e assim por diante.

## 11. Quick Sort

[Quick_Sort](algoritimos_ordenacao/quick_sort.py)

**Descrição**: O **Quick Sort** é um algoritmo eficiente de ordenação baseado na estratégia "dividir para conquistar". Ele escolhe um pivô, particiona a lista em torno desse pivô e recursivamente ordena as sublistas. A complexidade média é O(n log n), mas no pior caso pode ser O(n²).

**Escolha do pivô**: O desempenho do Quick Sort depende da escolha do pivô. Se o pivô for escolhido de maneira eficiente (como o pivô médio ou o pivô aleatório), o algoritmo pode ter bom desempenho mesmo em listas grandes.

## 12. Comparação dos Algoritmos de Busca
![algoritmos de busca](assets/comparcao_alg_busca.png)

[Comparacação_alg_busca](comparacao_alg_busca/comparcao_alg_busca.py)

### 1. Busca Binária (Eficiente)
**Por quê?** Divide a lista ordenada em partes iguais a cada iteração, garantindo tempo logarítmico em média.  
**Exemplo:**  
- **Lista original:** `[10, 20, 30, 40, 50]`  
- **Busca por 30:** Verifica 30 na segunda divisão da lista e encontra o valor rapidamente.

---

### 2. Busca por Interpolação (Mais eficiente em listas uniformes)
**Por quê?** Calcula posições de busca com base nos valores dos elementos e sua distribuição. Ideal para listas com elementos bem espaçados.  
**Exemplo:**  
- **Lista original:** `[10, 20, 30, 40, 50]`  
- **Busca por 40:** A interpolação estima diretamente a posição próxima, reduzindo o número de verificações.

---

### 3. Busca Jump (Desempenho ruim)
**Por quê?** Divide a lista em blocos e busca elementos em saltos, mas não é eficiente para listas grandes.  
**Exemplo:**  
- **Lista original:** `[5, 15, 25, 35, 45]`  
- **Busca por 35:** O algoritmo faz saltos grandes inicialmente e depois realiza buscas lineares dentro de um bloco, tornando-o mais lento.

---

### 4. Busca Exponencial (Intermediário)
**Por quê?** É eficiente em casos onde o elemento pode estar próximo ao início, mas perde desempenho em listas maiores.  
**Exemplo:**  
- **Lista original:** `[1, 2, 3, ..., 1000]`  
- **Busca por 900:** Expande exponencialmente o intervalo até ultrapassar o valor e realiza busca binária no intervalo identificado.

---

### 5. Busca Ternária (Simples, mas ligeiramente inferior à Binária)
**Por quê?** Divide a lista em três partes ao invés de duas, aumentando o número de comparações para determinar o segmento correto.  
**Exemplo:**  
- **Lista original:** `[10, 20, 30, 40, 50]`  
- **Busca por 20:** Compara simultaneamente dois elementos para decidir em qual dos três intervalos continuar a busca.

## 13. Comparação dos Algoritmos de Ordenação
![algoritmos de ordenação](assets/comparacao_alg_ordenacao.png)

[Comparacação_alg_ord](comparacao_alg_ordenacao/comparacao_alg_ordenacao.py)


### Estabilidade dos Algoritmos de Ordenação  
1. **Selection Sort (Instável)**  
   **Por quê?** Durante as trocas, o algoritmo pode colocar elementos iguais fora de ordem.  
   **Exemplo:**  
   - Lista original: `[4a, 4b, 3]`  
   - Após ordenação: `[3, 4b, 4a]`  
   Elementos `4a` e `4b` trocaram de ordem.  

2. **Shell Sort (Geralmente instável)**  
   **Por quê?** Depende da sequência de incrementos usada, mas em muitos casos as trocas de elementos iguais não mantêm a ordem original.  
   **Exemplo:**  
   - Lista original: `[5a, 3, 5b, 2]`  
   - Após ordenação: `[2, 3, 5b, 5a]`  

3. **Merge Sort (Estável)**  
   **Por quê?** Divide e conquista sem modificar a ordem relativa de elementos iguais.  
   **Exemplo:**  
   - Lista original: `[2a, 1, 2b]`  
   - Após ordenação: `[1, 2a, 2b]`  

4. **Quick Sort (Instável)**  
   **Por quê?** Depende de como o pivô é escolhido e como os elementos são particionados, podendo trocar a ordem de elementos iguais.  
   **Exemplo:**  
   - Lista original: `[6a, 3, 6b]`  
   - Após ordenação: `[3, 6b, 6a]`  

5. **Bucket Sort (Pode ser estável)**  
   **Por quê?** Depende da implementação. Se os baldes preservarem a ordem dos elementos, será estável.  
   **Exemplo Estável:**  
   - Lista original: `[1a, 3, 1b]`  
   - Após ordenação: `[1a, 1b, 3]`  
   **Exemplo Instável:** O contrário pode ocorrer se os baldes forem reorganizados de forma arbitrária.  

6. **Radix Sort (Estável)**  
   **Por quê?** Processa dígitos individuais dos números de forma estável, mantendo a ordem relativa.  
   **Exemplo:**  
   - Lista original: `[21a, 13, 21b]`  
   - Após ordenação: `[13, 21a, 21b]`  

## 14. Busca Binária vs Busca por Interpolação
![binario_vs_interpolação](assets/busca_binaria_vs_busca_interpolacao.png)

[Binario_vs_interpolação](comparacao_alg_busca/binaria_vs_Interpolacao.py)

### Busca Binária
**Descrição:**  
A Busca Binária é eficiente para listas ordenadas, dividindo-as ao meio em cada iteração. O algoritmo reduz o intervalo de busca de forma logarítmica, tornando-se ideal para listas de qualquer distribuição.  

**Complexidade:**  
- Melhor caso: O(1)  
- Caso médio e pior caso: O(log n)  

**Exemplo:**  
- **Lista original:** `[10, 20, 30, 40, 50]`  
- **Busca por 30:**  
  1. Verifica o elemento no meio (30).  
  2. Valor encontrado na primeira tentativa.

**Vantagens:**  
- Funciona com qualquer lista ordenada.  
- Simples de implementar.  

**Desvantagens:**  
- Não aproveita a distribuição dos valores na lista.  

---

### Busca por Interpolação
**Descrição:**  
A Busca por Interpolação utiliza uma estimativa baseada na distribuição dos valores na lista, tornando-a mais eficiente quando os dados são uniformemente espaçados.  

**Complexidade:**  
- Melhor caso: O(1)  
- Caso médio: O(log log n) (quando os valores estão uniformemente distribuídos)  
- Pior caso: O(n) (para listas desordenadas ou mal distribuídas)  

**Exemplo:**  
- **Lista original:** `[10, 20, 30, 40, 50]`  
- **Busca por 40:**  
  1. Calcula a posição estimada do valor usando a fórmula de interpolação.  
  2. Encontra diretamente a posição próxima ao valor, reduzindo o número de verificações.

**Vantagens:**  
- Mais rápida que a Busca Binária em listas uniformemente distribuídas.  
- Reduz o número de comparações.  

**Desvantagens:**  
- Menos eficiente em listas não uniformes.  
- Complexa de implementar em relação à Busca Binária.

---

## 14. Busca Binária vs Busca Jump
![binario_vs_Jump](assets/comparacao_jump_binaria.png)

[Jump_vs_Binario](comparacao_alg_busca/jump_vs_binaria.py)

 **Busca Jump** (Linha Azul):
   - Apresenta crescimento linear no tempo de execução conforme o tamanho da lista aumenta.
   - É eficiente em listas menores, mas perde desempenho em listas grandes devido à necessidade de verificações lineares após os saltos.

2. **Busca Binária** (Linha Vermelha):
   - Mantém um tempo de execução consistentemente baixo, mesmo com o aumento do tamanho da lista.
   - Sua eficiência logarítmica \(O(\log n)\) a torna ideal para grandes volumes de dados.
