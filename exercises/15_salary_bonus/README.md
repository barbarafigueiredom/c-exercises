# 15 - Salario com Bonus

**Objetivo:** Leia um salario base e uma porcentagem de bonus, depois imprima o salario final apos aplicar o bonus.

**Conceitos:** porcentagens, adicao

**Entrada**
Dois numeros: salario porcentagem_do_bonus.

**Saida**
Um numero com duas casas decimais.

**Exemplo de entrada**
```text
2000 10
```

**Exemplo de saida**
```text
2200.00
```

**Como calcular**
Para calcular o bonus, pegue a porcentagem do salario base e depois some esse valor ao salario original.
Formula do bonus: `salario * porcentagem / 100`.
Formula final: `salario + bonus`.

**O que voce precisa fazer no codigo**
Na funcao `solve(double amount, double percentage)`, os valores de entrada ja chegam pelos parametros.
Voce deve calcular o resultado pedido e retornar um valor decimal com `return`.
Voce nao precisa formatar a quantidade de casas decimais dentro de `solve(...)`.
O `main(...)` deste exercicio ja imprime a resposta com duas casas decimais para voce.

**Como resolver**
1. Abra `main.c`.
2. Complete a funcao `solve(...)`.
3. Compile com `gcc -Wall -Wextra -std=c11 main.c -o program`.
4. Rode as verificacoes predefinidas com `./program --test`.
5. Se quiser consultar a resposta comentada, abra `solution.c`.

O arquivo `main.c` e o exercicio para resolver. O arquivo `solution.c` contem uma solucao comentada em PT-BR.
