# 19 - Troca de Dois Numeros

**Objetivo:** Leia dois inteiros e imprima os dois em ordem invertida.

**Conceitos:** variaveis, atribuicoes

**Entrada**
Dois inteiros separados por espaco.

**Saida**
Dois inteiros separados por espaco: segundo primeiro.

**Exemplo de entrada**
```text
4 9
```

**Exemplo de saida**
```text
9 4
```

**O que voce precisa fazer no codigo**
Na funcao `solve(int first_input, int second_input, int *first_output, int *second_output)`, os dois valores de entrada chegam pelos dois primeiros parametros.
Voce deve guardar as duas respostas nas variaveis apontadas por `first_output` e `second_output`.
Use `*first_output = ...;` e `*second_output = ...;`.

**Como resolver**
1. Abra `main.c`.
2. Complete a funcao `solve(...)`.
3. Compile com `gcc -Wall -Wextra -std=c11 main.c -o program`.
4. Rode as verificacoes predefinidas com `./program --test`.
5. Se quiser consultar a resposta comentada, abra `solution.c`.

**Comando unico a partir da pasta raiz do projeto**
```bash
gcc -Wall -Wextra -std=c11 ./exercises/19_swap_two_numbers/main.c -o ./exercises/19_swap_two_numbers/program && ./exercises/19_swap_two_numbers/program --test
```

O arquivo `main.c` e o exercicio para resolver. O arquivo `solution.c` contem uma solucao comentada em PT-BR.
