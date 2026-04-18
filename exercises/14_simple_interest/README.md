# 14 - Juros Simples

**Objetivo:** Leia capital, taxa anual e tempo, depois imprima o juros simples usando a formula capital * taxa * tempo / 100.

**Conceitos:** porcentagens, multiplicacao, divisao

**Entrada**
Tres numeros: capital taxa tempo.

**Saida**
Um numero com duas casas decimais.

**Exemplo de entrada**
```text
1000 5 2
```

**Exemplo de saida**
```text
100.00
```

**Como calcular**
O juros simples e calculado multiplicando capital, taxa e tempo, e depois dividindo por 100.
Formula: `(capital * taxa * tempo) / 100`.

**O que voce precisa fazer no codigo**
Na funcao `solve(double principal, double rate, double time)`, os tres valores ja chegam pelos parametros.
Voce deve calcular o juros simples e retornar o resultado com `return`.
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
gcc -Wall -Wextra -std=c11 ./exercises/14_simple_interest/main.c -o ./exercises/14_simple_interest/program && ./exercises/14_simple_interest/program --test
```

O arquivo `main.c` e o exercicio para resolver. O arquivo `solution.c` contem uma solucao comentada em PT-BR.
