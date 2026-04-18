# 22 - Numero de Fibonacci

**Objetivo:** Leia um inteiro n e imprima o enesimo numero de Fibonacci, considerando F(0) = 0 e F(1) = 1.

**Conceitos:** lacos, geracao de sequencia, variaveis

**Entrada**
Um inteiro n, onde n e nao negativo.

**Saida**
Um inteiro: o enesimo numero de Fibonacci.

**Exemplo de entrada**
```text
7
```

**Exemplo de saida**
```text
13
```

**Como calcular**
Na sequencia de Fibonacci, cada numero novo e a soma dos dois anteriores.
Comeco da sequencia: `0, 1, 1, 2, 3, 5, 8...`.

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
gcc -Wall -Wextra -std=c11 ./exercises/22_fibonacci/main.c -o ./exercises/22_fibonacci/program && ./exercises/22_fibonacci/program --test
```

O arquivo `main.c` e o exercicio para resolver. O arquivo `solution.c` contem uma solucao comentada em PT-BR.
