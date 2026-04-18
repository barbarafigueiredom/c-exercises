# 05 - Area e Perimetro de um Retangulo

**Objetivo:** Leia a largura e a altura de um retangulo e imprima sua area e seu perimetro.

**Conceitos:** multiplicacao, adicao, geometria basica

**Entrada**
Dois inteiros: largura e altura.

**Saida**
Dois inteiros separados por espaco: area perimetro.

**Exemplo de entrada**
```text
5 3
```

**Exemplo de saida**
```text
15 16
```

**Como calcular**
A area de um retangulo e calculada multiplicando largura por altura.
Formula da area: `largura * altura`.
O perimetro de um retangulo e a soma de todos os lados.
Formula do perimetro: `2 * largura + 2 * altura`.

**O que voce precisa fazer no codigo**
Na funcao `solve(int width, int height, int *area, int *perimeter)`, a largura e a altura chegam pelos parametros `width` e `height`.
Voce deve guardar a area em `*area` e o perimetro em `*perimeter`.

**Como resolver**
1. Abra `main.c`.
2. Complete a funcao `solve(...)`.
3. Compile com `gcc -Wall -Wextra -std=c11 main.c -o program`.
4. Rode as verificacoes predefinidas com `./program --test`.
5. Se quiser consultar a resposta comentada, abra `solution.c`.

**Comando unico a partir da pasta raiz do projeto**
```bash
gcc -Wall -Wextra -std=c11 ./exercises/05_rectangle_area_perimeter/main.c -o ./exercises/05_rectangle_area_perimeter/program && ./exercises/05_rectangle_area_perimeter/program --test
```

O arquivo `main.c` e o exercicio para resolver. O arquivo `solution.c` contem uma solucao comentada em PT-BR.
