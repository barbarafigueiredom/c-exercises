# 01 - Soma de Dois Numeros

**Objetivo:** Leia dois inteiros e imprima a soma entre eles.

**Conceitos:** leitura de inteiros, adicao, saida formatada

**Entrada**
Dois inteiros separados por espaco.

**Saida**
Um inteiro: a soma.

**Exemplo de entrada**
```text
7 5
```

**Exemplo de saida**
```text
12
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
gcc -Wall -Wextra -std=c11 ./exercises/01_sum_two_numbers/main.c -o ./exercises/01_sum_two_numbers/program && ./exercises/01_sum_two_numbers/program --test
```

O arquivo `main.c` e o exercicio para resolver. O arquivo `solution.c` contem uma solucao comentada em PT-BR.
