# 16 - Preco com Desconto

**Objetivo:** Leia o preco original e uma porcentagem de desconto, depois imprima o preco final apos o desconto.

**Conceitos:** porcentagens, subtracao

**Entrada**
Dois numeros: preco porcentagem_de_desconto.

**Saida**
Um numero com duas casas decimais.

**Exemplo de entrada**
```text
80 25
```

**Exemplo de saida**
```text
60.00
```

**Como calcular**
Para calcular o desconto, pegue a porcentagem do preco original e depois subtraia esse valor do preco inicial.
Formula do desconto: `preco * porcentagem / 100`.
Formula final: `preco - desconto`.

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

**Comando unico a partir da pasta raiz do projeto**
```bash
gcc -Wall -Wextra -std=c11 ./exercises/16_discount_price/main.c -o ./exercises/16_discount_price/program && ./exercises/16_discount_price/program --test
```

O arquivo `main.c` e o exercicio para resolver. O arquivo `solution.c` contem uma solucao comentada em PT-BR.
