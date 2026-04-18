# 02 - Subtracao de Dois Numeros

**Objetivo:** Leia dois inteiros e imprima o resultado do primeiro menos o segundo.

**Conceitos:** leitura de inteiros, subtracao, saida formatada

**Entrada**
Dois inteiros separados por espaco.

**Saida**
Um inteiro: o resultado da subtracao.

**Exemplo de entrada**
```text
9 4
```

**Exemplo de saida**
```text
5
```

**O que voce precisa fazer no codigo**
Na funcao `solve(int a, int b)`, os dois valores de entrada ja chegam prontos pelos parametros `a` e `b`.
Voce deve calcular o resultado pedido no enunciado e retornar um unico valor inteiro com `return`.

**Como resolver**
1. Abra `main.c`.
2. Complete a funcao `solve(...)`.
3. Compile com `gcc -Wall -Wextra -std=c11 main.c -o program`.
4. Rode as verificacoes predefinidas com `./program --test`.
5. Se quiser consultar a resposta comentada, abra `solution.c`.

**Comando unico a partir da pasta raiz do projeto**
```bash
gcc -Wall -Wextra -std=c11 ./exercises/02_subtract_two_numbers/main.c -o ./exercises/02_subtract_two_numbers/program && ./exercises/02_subtract_two_numbers/program --test
```

O arquivo `main.c` e o exercicio para resolver. O arquivo `solution.c` contem uma solucao comentada em PT-BR.
