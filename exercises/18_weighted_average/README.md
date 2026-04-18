# 18 - Media Ponderada

**Objetivo:** Leia tres notas e seus pesos, depois imprima a media ponderada com duas casas decimais.

**Conceitos:** numeros de ponto flutuante, multiplicacao, divisao

**Entrada**
Seis numeros: nota1 peso1 nota2 peso2 nota3 peso3.

**Saida**
Um numero com duas casas decimais.

**Exemplo de entrada**
```text
7 2 8 3 9 5
```

**Exemplo de saida**
```text
8.30
```

**Como calcular**
Na media ponderada, cada nota e multiplicada pelo seu peso.
Depois some todos os resultados e divida pela soma dos pesos.
Formula: `(nota1*peso1 + nota2*peso2 + nota3*peso3) / (peso1 + peso2 + peso3)`.

**O que voce precisa fazer no codigo**
Na funcao `solve(...)`, todas as notas e pesos ja chegam pelos parametros.
Voce deve calcular a media ponderada e retornar um valor decimal com `return`.
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
gcc -Wall -Wextra -std=c11 ./exercises/18_weighted_average/main.c -o ./exercises/18_weighted_average/program && ./exercises/18_weighted_average/program --test
```

O arquivo `main.c` e o exercicio para resolver. O arquivo `solution.c` contem uma solucao comentada em PT-BR.
