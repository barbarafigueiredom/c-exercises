# 25 - Potencia Inteira

**Objetivo:** Leia um inteiro base e um inteiro nao negativo expoente, depois imprima base elevada a expoente usando um laco.

**Conceitos:** lacos, multiplicacao, operacoes repetidas

**Entrada**
Dois inteiros separados por espaco: base expoente.

**Saida**
Um inteiro: base^expoente.

**Exemplo de entrada**
```text
2 5
```

**Exemplo de saida**
```text
32
```

**Como calcular**
Uma potencia inteira pode ser calculada multiplicando a base por ela mesma varias vezes.
Exemplo: `2^5 = 2 * 2 * 2 * 2 * 2`.

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
gcc -Wall -Wextra -std=c11 ./exercises/25_power_loop/main.c -o ./exercises/25_power_loop/program && ./exercises/25_power_loop/program --test
```

O arquivo `main.c` e o exercicio para resolver. O arquivo `solution.c` contem uma solucao comentada em PT-BR.
