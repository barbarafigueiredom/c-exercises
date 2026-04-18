# 06 - Area do Circulo

**Objetivo:** Leia o raio de um circulo e imprima sua area usando PI = 3.14159.

**Conceitos:** numeros de ponto flutuante, multiplicacao, constantes

**Entrada**
Um numero: o raio.

**Saida**
Um numero com duas casas decimais.

**Exemplo de entrada**
```text
2
```

**Exemplo de saida**
```text
12.57
```

**Como calcular**
A area do circulo e calculada multiplicando PI pelo raio ao quadrado.
Neste exercicio, use `PI = 3.14159`.
Formula: `PI * raio * raio`.

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

**Comando unico a partir da pasta raiz do projeto**
```bash
gcc -Wall -Wextra -std=c11 ./exercises/06_circle_area/main.c -o ./exercises/06_circle_area/program && ./exercises/06_circle_area/program --test
```

O arquivo `main.c` e o exercicio para resolver. O arquivo `solution.c` contem uma solucao comentada em PT-BR.
