# 20 - Resto da Divisao

**Objetivo:** Leia dois inteiros e imprima o resto da divisao do primeiro pelo segundo.

**Conceitos:** divisao inteira, operador de resto

**Entrada**
Dois inteiros separados por espaco. Nos testes, o segundo valor nunca sera zero.

**Saida**
Um inteiro: o resto.

**Exemplo de entrada**
```text
10 3
```

**Exemplo de saida**
```text
1
```

**Como calcular**
O resto da divisao e o valor que sobra depois de dividir um numero pelo outro.
Em C, isso pode ser calculado com o operador `%`.

**O que voce precisa fazer no codigo**
Na funcao `solve(int a, int b)`, os dois valores de entrada ja chegam prontos pelos parametros `a` e `b`.
Voce deve calcular o resultado pedido no enunciado e retornar um unico valor inteiro com `return`.

**Como resolver**
1. Abra `main.c`.
2. Complete a funcao `solve(...)`.
3. Compile com `gcc -Wall -Wextra -std=c11 main.c -o program`.
4. Rode as verificacoes predefinidas com `./program --test`.
5. Se quiser consultar a resposta comentada, abra `solution.c`.

O arquivo `main.c` e o exercicio para resolver. O arquivo `solution.c` contem uma solucao comentada em PT-BR.
