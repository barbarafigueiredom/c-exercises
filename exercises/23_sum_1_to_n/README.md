# 23 - Soma de 1 ate N

**Objetivo:** Leia um inteiro positivo n e imprima a soma de todos os inteiros de 1 ate n.

**Conceitos:** lacos, acumulacao, inteiros

**Entrada**
Um inteiro positivo n.

**Saida**
Um inteiro: a soma de 1 ate n.

**Exemplo de entrada**
```text
5
```

**Exemplo de saida**
```text
15
```

**Como calcular**
Voce deve somar todos os inteiros de 1 ate `n`.
Exemplo: se `n = 5`, entao a soma e `1 + 2 + 3 + 4 + 5 = 15`.

**O que voce precisa fazer no codigo**
Na funcao `solve(int value)`, o valor de entrada ja chega pelo parametro `value`.
Voce deve calcular o resultado pedido e retornar um unico valor inteiro com `return`.

**Como resolver**
1. Abra `main.c`.
2. Complete a funcao `solve(...)`.
3. Compile com `gcc -Wall -Wextra -std=c11 main.c -o program`.
4. Rode as verificacoes predefinidas com `./program --test`.
5. Se quiser consultar a resposta comentada, abra `solution.c`.

**Comando unico a partir da pasta raiz do projeto**
```bash
gcc -Wall -Wextra -std=c11 ./exercises/23_sum_1_to_n/main.c -o ./exercises/23_sum_1_to_n/program && ./exercises/23_sum_1_to_n/program --test
```

O arquivo `main.c` e o exercicio para resolver. O arquivo `solution.c` contem uma solucao comentada em PT-BR.
