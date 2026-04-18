# 21 - Fatorial

**Objetivo:** Leia um inteiro nao negativo n e imprima n!.

**Conceitos:** lacos, multiplicacao, acumulacao

**Entrada**
Um inteiro n, onde n e nao negativo.

**Saida**
Um inteiro: o fatorial de n.

**Exemplo de entrada**
```text
5
```

**Exemplo de saida**
```text
120
```

**Como calcular**
O fatorial de um numero e calculado multiplicando esse numero por todos os inteiros positivos menores que ele ate chegar em 1.
Exemplo: `5! = 5 * 4 * 3 * 2 * 1`.

**O que voce precisa fazer no codigo**
Na funcao `solve(int value)`, o valor de entrada ja chega pelo parametro `value`.
Voce deve calcular o resultado pedido e retornar um valor inteiro usando `return`.

**Como resolver**
1. Abra `main.c`.
2. Complete a funcao `solve(...)`.
3. Compile com `gcc -Wall -Wextra -std=c11 main.c -o program`.
4. Rode as verificacoes predefinidas com `./program --test`.
5. Se quiser consultar a resposta comentada, abra `solution.c`.

**Comando unico a partir da pasta raiz do projeto**
```bash
gcc -Wall -Wextra -std=c11 ./exercises/21_factorial/main.c -o ./exercises/21_factorial/program && ./exercises/21_factorial/program --test
```

O arquivo `main.c` e o exercicio para resolver. O arquivo `solution.c` contem uma solucao comentada em PT-BR.
