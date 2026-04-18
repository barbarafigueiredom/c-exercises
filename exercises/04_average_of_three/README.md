# 04 - Media de Tres Numeros

**Objetivo:** Leia tres numeros e imprima a media aritmetica com duas casas decimais.

**Conceitos:** numeros de ponto flutuante, adicao, divisao

**Entrada**
Tres numeros separados por espacos.

**Saida**
Um numero com duas casas decimais.

**Exemplo de entrada**
```text
4 5 6
```

**Exemplo de saida**
```text
5.00
```

**Como calcular**
A media aritmetica de tres numeros e calculada somando os tres valores e dividindo o total por 3.
Formula: `(a + b + c) / 3`.

**O que voce precisa fazer no codigo**
Na funcao `solve(double a, double b, double c)`, os tres valores de entrada ja chegam pelos parametros.
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
