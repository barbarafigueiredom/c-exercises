# 08 - Fahrenheit para Celsius

**Objetivo:** Leia uma temperatura em Fahrenheit e converta para Celsius.

**Conceitos:** conversao de unidades, subtracao, multiplicacao, divisao

**Entrada**
Um numero: a temperatura em Fahrenheit.

**Saida**
Um numero com duas casas decimais.

**Exemplo de entrada**
```text
77
```

**Exemplo de saida**
```text
25.00
```

**Como calcular**
Para transformar Fahrenheit em Celsius, subtraia 32 da temperatura, multiplique por 5 e divida por 9.
Formula: `(F - 32) * 5 / 9`.

**O que voce precisa fazer no codigo**
Na funcao `solve(double value)`, o valor de entrada ja chega pelo parametro `value`.
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
