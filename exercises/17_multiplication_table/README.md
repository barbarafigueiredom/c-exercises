# 17 - Tabuada

**Objetivo:** Leia um inteiro e imprima sua tabuada de 1 ate 10, uma linha por resultado.

**Conceitos:** lacos, multiplicacao, saida formatada

**Entrada**
Um inteiro.

**Saida**
Dez linhas no formato number x i = result.

**Exemplo de entrada**
```text
3
```

**Exemplo de saida**
```text
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 5 = 15
3 x 6 = 18
3 x 7 = 21
3 x 8 = 24
3 x 9 = 27
3 x 10 = 30
```

**O que voce precisa fazer no codigo**
Na funcao `solve(int number, char *output, size_t output_size)`, o numero da tabuada chega em `number`.
Voce deve montar o texto da resposta dentro de `output`, respeitando o tamanho maximo informado por `output_size`.
A resposta final deve ficar pronta para ser impressa exatamente como os testes esperam.

**Como resolver**
1. Abra `main.c`.
2. Complete a funcao `solve(...)`.
3. Compile com `gcc -Wall -Wextra -std=c11 main.c -o program`.
4. Rode as verificacoes predefinidas com `./program --test`.
5. Se quiser consultar a resposta comentada, abra `solution.c`.

**Comando unico a partir da pasta raiz do projeto**
```bash
gcc -Wall -Wextra -std=c11 ./exercises/17_multiplication_table/main.c -o ./exercises/17_multiplication_table/program && ./exercises/17_multiplication_table/program --test
```

O arquivo `main.c` e o exercicio para resolver. O arquivo `solution.c` contem uma solucao comentada em PT-BR.
