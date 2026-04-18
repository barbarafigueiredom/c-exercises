# 03 - Antecessor e Sucessor

**Objetivo:** Leia um inteiro e imprima seu antecessor e seu sucessor.

**Conceitos:** inteiros, adicao, subtracao

**Entrada**
Um inteiro.

**Saida**
Dois inteiros separados por espaco: antecessor sucessor.

**Exemplo de entrada**
```text
10
```

**Exemplo de saida**
```text
9 11
```

**O que voce precisa fazer no codigo**
Na funcao `solve(int number, int *first, int *second)`, o valor de entrada chega pelo parametro `number`.
Voce deve colocar as duas respostas nas variaveis apontadas por `first` e `second`.
Use `*first = ...;` e `*second = ...;` para guardar os resultados.

**Como resolver**
1. Abra `main.c`.
2. Complete a funcao `solve(...)`.
3. Compile com `gcc -Wall -Wextra -std=c11 main.c -o program`.
4. Rode as verificacoes predefinidas com `./program --test`.
5. Se quiser consultar a resposta comentada, abra `solution.c`.

O arquivo `main.c` e o exercicio para resolver. O arquivo `solution.c` contem uma solucao comentada em PT-BR.
