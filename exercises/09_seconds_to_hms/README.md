# 09 - Segundos para Horas, Minutos e Segundos

**Objetivo:** Leia um total de segundos e converta para horas, minutos e segundos.

**Conceitos:** divisao inteira, resto, decomposicao

**Entrada**
Um inteiro: total de segundos.

**Saida**
Tres inteiros separados por espaco: horas minutos segundos.

**Exemplo de entrada**
```text
3661
```

**Exemplo de saida**
```text
1 1 1
```

**Como calcular**
Para separar segundos em horas, minutos e segundos, primeiro descubra quantas horas cabem no total.
Depois use o resto para descobrir os minutos e o que sobrar sera a quantidade final de segundos.

**O que voce precisa fazer no codigo**
Na funcao `solve(int total_seconds, int *hours, int *minutes, int *seconds)`, o total de segundos chega em `total_seconds`.
Voce deve separar a resposta e guardar cada parte em `*hours`, `*minutes` e `*seconds`.

**Como resolver**
1. Abra `main.c`.
2. Complete a funcao `solve(...)`.
3. Compile com `gcc -Wall -Wextra -std=c11 main.c -o program`.
4. Rode as verificacoes predefinidas com `./program --test`.
5. Se quiser consultar a resposta comentada, abra `solution.c`.

O arquivo `main.c` e o exercicio para resolver. O arquivo `solution.c` contem uma solucao comentada em PT-BR.
