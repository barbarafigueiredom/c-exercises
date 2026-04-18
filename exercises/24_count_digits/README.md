# 24 - Contar Digitos

**Objetivo:** Leia um inteiro nao negativo e imprima quantos digitos ele possui. O numero 0 possui 1 digito.

**Conceitos:** lacos, divisao inteira, condicionais

**Entrada**
Um inteiro nao negativo.

**Saida**
Um inteiro: a quantidade de digitos.

**Exemplo de entrada**
```text
4502
```

**Exemplo de saida**
```text
4
```

**Como calcular**
Para contar os digitos de um numero inteiro, voce pode dividir o numero por 10 varias vezes ate ele chegar a 0.
Cada divisao remove o ultimo digito e aumenta a contagem em 1.

**O que voce precisa fazer no codigo**
Na funcao `solve(int value)`, o valor de entrada ja chega pelo parametro `value`.
Voce deve calcular o resultado pedido e retornar um unico valor inteiro com `return`.

**Como resolver**
1. Abra `main.c`.
2. Complete a funcao `solve(...)`.
3. Compile com `gcc -Wall -Wextra -std=c11 main.c -o program`.
4. Rode as verificacoes predefinidas com `./program --test`.
5. Se quiser consultar a resposta comentada, abra `solution.c`.

O arquivo `main.c` e o exercicio para resolver. O arquivo `solution.c` contem uma solucao comentada em PT-BR.
