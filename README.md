# Exercicios Basicos de C

Este workspace contem 25 exercicios basicos de C para serem resolvidos no VS Code.

Cada pasta de exercicio contem:
- `README.md` com o enunciado em PT-BR.
- `main.c` com a funcao `solve(...)` preparada para completar.
- `solution.c` com uma solucao comentada em PT-BR.
- Uma chave `--test` que imprime 10 entradas predefinidas, saidas esperadas, saidas atuais e status de aprovacao.

Os arquivos `main.c` compilam imediatamente, mas as implementacoes de `solve(...)` estao propositalmente incompletas. Espere testes falhando ate resolver cada exercicio.

## Estrutura

```text
exercises/
  01_sum_two_numbers/
    README.md
    main.c
    solution.c
  ...
```

## Como usar no VS Code

Abra qualquer arquivo `main.c` e use as tasks inclusas:
- `Build Current C File`
- `Run Current C File`
- `Run Current File Tests`

Tambem e possivel compilar manualmente:

```bash
gcc -Wall -Wextra -std=c11 exercises/01_sum_two_numbers/main.c -o exercises/01_sum_two_numbers/program
./exercises/01_sum_two_numbers/program --test
```

Para testar a solucao comentada de um exercicio:

```bash
gcc -Wall -Wextra -std=c11 exercises/01_sum_two_numbers/solution.c -o exercises/01_sum_two_numbers/solution
./exercises/01_sum_two_numbers/solution --test
```

## Exercicios

### 01 - Soma de Dois Numeros

**Pasta:** `exercises/01_sum_two_numbers`

**Objetivo:** Leia dois inteiros e imprima a soma entre eles.

**Entrada:** Dois inteiros separados por espaco.

**Saida:** Um inteiro: a soma.

**Exemplo de entrada**
```text
7 5
```

**Exemplo de saida**
```text
12
```

### 02 - Subtracao de Dois Numeros

**Pasta:** `exercises/02_subtract_two_numbers`

**Objetivo:** Leia dois inteiros e imprima o resultado do primeiro menos o segundo.

**Entrada:** Dois inteiros separados por espaco.

**Saida:** Um inteiro: o resultado da subtracao.

**Exemplo de entrada**
```text
9 4
```

**Exemplo de saida**
```text
5
```

### 03 - Antecessor e Sucessor

**Pasta:** `exercises/03_predecessor_successor`

**Objetivo:** Leia um inteiro e imprima seu antecessor e seu sucessor.

**Entrada:** Um inteiro.

**Saida:** Dois inteiros separados por espaco: antecessor sucessor.

**Exemplo de entrada**
```text
10
```

**Exemplo de saida**
```text
9 11
```

### 04 - Media de Tres Numeros

**Pasta:** `exercises/04_average_of_three`

**Objetivo:** Leia tres numeros e imprima a media aritmetica com duas casas decimais.

**Entrada:** Tres numeros separados por espacos.

**Saida:** Um numero com duas casas decimais.

**Exemplo de entrada**
```text
4 5 6
```

**Exemplo de saida**
```text
5.00
```

### 05 - Area e Perimetro de um Retangulo

**Pasta:** `exercises/05_rectangle_area_perimeter`

**Objetivo:** Leia a largura e a altura de um retangulo e imprima sua area e seu perimetro.

**Entrada:** Dois inteiros: largura e altura.

**Saida:** Dois inteiros separados por espaco: area perimetro.

**Exemplo de entrada**
```text
5 3
```

**Exemplo de saida**
```text
15 16
```

### 06 - Area do Circulo

**Pasta:** `exercises/06_circle_area`

**Objetivo:** Leia o raio de um circulo e imprima sua area usando PI = 3.14159.

**Entrada:** Um numero: o raio.

**Saida:** Um numero com duas casas decimais.

**Exemplo de entrada**
```text
2
```

**Exemplo de saida**
```text
12.57
```

### 07 - Celsius para Fahrenheit

**Pasta:** `exercises/07_celsius_to_fahrenheit`

**Objetivo:** Leia uma temperatura em Celsius e converta para Fahrenheit.

**Entrada:** Um numero: a temperatura em Celsius.

**Saida:** Um numero com duas casas decimais.

**Exemplo de entrada**
```text
25
```

**Exemplo de saida**
```text
77.00
```

### 08 - Fahrenheit para Celsius

**Pasta:** `exercises/08_fahrenheit_to_celsius`

**Objetivo:** Leia uma temperatura em Fahrenheit e converta para Celsius.

**Entrada:** Um numero: a temperatura em Fahrenheit.

**Saida:** Um numero com duas casas decimais.

**Exemplo de entrada**
```text
77
```

**Exemplo de saida**
```text
25.00
```

### 09 - Segundos para Horas, Minutos e Segundos

**Pasta:** `exercises/09_seconds_to_hms`

**Objetivo:** Leia um total de segundos e converta para horas, minutos e segundos.

**Entrada:** Um inteiro: total de segundos.

**Saida:** Tres inteiros separados por espaco: horas minutos segundos.

**Exemplo de entrada**
```text
3661
```

**Exemplo de saida**
```text
1 1 1
```

### 10 - Par ou Impar

**Pasta:** `exercises/10_even_or_odd`

**Objetivo:** Leia um inteiro e imprima EVEN se ele for par ou ODD se ele for impar.

**Entrada:** Um inteiro.

**Saida:** A palavra EVEN ou ODD.

**Exemplo de entrada**
```text
7
```

**Exemplo de saida**
```text
ODD
```

### 11 - Sinal de um Numero

**Pasta:** `exercises/11_sign_of_number`

**Objetivo:** Leia um inteiro e imprima POSITIVE, NEGATIVE ou ZERO.

**Entrada:** Um inteiro.

**Saida:** Uma destas palavras: POSITIVE, NEGATIVE, ZERO.

**Exemplo de entrada**
```text
-8
```

**Exemplo de saida**
```text
NEGATIVE
```

### 12 - Maior entre Dois Numeros

**Pasta:** `exercises/12_greater_of_two`

**Objetivo:** Leia dois inteiros e imprima o maior deles. Se forem iguais, imprima esse valor.

**Entrada:** Dois inteiros separados por espaco.

**Saida:** Um inteiro.

**Exemplo de entrada**
```text
12 7
```

**Exemplo de saida**
```text
12
```

### 13 - Maior entre Tres Numeros

**Pasta:** `exercises/13_greatest_of_three`

**Objetivo:** Leia tres inteiros e imprima o maior valor.

**Entrada:** Tres inteiros separados por espacos.

**Saida:** Um inteiro.

**Exemplo de entrada**
```text
3 9 4
```

**Exemplo de saida**
```text
9
```

### 14 - Juros Simples

**Pasta:** `exercises/14_simple_interest`

**Objetivo:** Leia capital, taxa anual e tempo, depois imprima o juros simples usando a formula capital * taxa * tempo / 100.

**Entrada:** Tres numeros: capital taxa tempo.

**Saida:** Um numero com duas casas decimais.

**Exemplo de entrada**
```text
1000 5 2
```

**Exemplo de saida**
```text
100.00
```

### 15 - Salario com Bonus

**Pasta:** `exercises/15_salary_bonus`

**Objetivo:** Leia um salario base e uma porcentagem de bonus, depois imprima o salario final apos aplicar o bonus.

**Entrada:** Dois numeros: salario porcentagem_do_bonus.

**Saida:** Um numero com duas casas decimais.

**Exemplo de entrada**
```text
2000 10
```

**Exemplo de saida**
```text
2200.00
```

### 16 - Preco com Desconto

**Pasta:** `exercises/16_discount_price`

**Objetivo:** Leia o preco original e uma porcentagem de desconto, depois imprima o preco final apos o desconto.

**Entrada:** Dois numeros: preco porcentagem_de_desconto.

**Saida:** Um numero com duas casas decimais.

**Exemplo de entrada**
```text
80 25
```

**Exemplo de saida**
```text
60.00
```

### 17 - Tabuada

**Pasta:** `exercises/17_multiplication_table`

**Objetivo:** Leia um inteiro e imprima sua tabuada de 1 ate 10, uma linha por resultado.

**Entrada:** Um inteiro.

**Saida:** Dez linhas no formato number x i = result.

**Exemplo de entrada**
```text
3
```

**Exemplo de saida**
```text
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 5 = 15
3 x 6 = 18
3 x 7 = 21
3 x 8 = 24
3 x 9 = 27
3 x 10 = 30
```

### 18 - Media Ponderada

**Pasta:** `exercises/18_weighted_average`

**Objetivo:** Leia tres notas e seus pesos, depois imprima a media ponderada com duas casas decimais.

**Entrada:** Seis numeros: nota1 peso1 nota2 peso2 nota3 peso3.

**Saida:** Um numero com duas casas decimais.

**Exemplo de entrada**
```text
7 2 8 3 9 5
```

**Exemplo de saida**
```text
8.30
```

### 19 - Troca de Dois Numeros

**Pasta:** `exercises/19_swap_two_numbers`

**Objetivo:** Leia dois inteiros e imprima os dois em ordem invertida.

**Entrada:** Dois inteiros separados por espaco.

**Saida:** Dois inteiros separados por espaco: segundo primeiro.

**Exemplo de entrada**
```text
4 9
```

**Exemplo de saida**
```text
9 4
```

### 20 - Resto da Divisao

**Pasta:** `exercises/20_remainder_of_division`

**Objetivo:** Leia dois inteiros e imprima o resto da divisao do primeiro pelo segundo.

**Entrada:** Dois inteiros separados por espaco. Nos testes, o segundo valor nunca sera zero.

**Saida:** Um inteiro: o resto.

**Exemplo de entrada**
```text
10 3
```

**Exemplo de saida**
```text
1
```

### 21 - Fatorial

**Pasta:** `exercises/21_factorial`

**Objetivo:** Leia um inteiro nao negativo n e imprima n!.

**Entrada:** Um inteiro n, onde n e nao negativo.

**Saida:** Um inteiro: o fatorial de n.

**Exemplo de entrada**
```text
5
```

**Exemplo de saida**
```text
120
```

### 22 - Numero de Fibonacci

**Pasta:** `exercises/22_fibonacci`

**Objetivo:** Leia um inteiro n e imprima o enesimo numero de Fibonacci, considerando F(0) = 0 e F(1) = 1.

**Entrada:** Um inteiro n, onde n e nao negativo.

**Saida:** Um inteiro: o enesimo numero de Fibonacci.

**Exemplo de entrada**
```text
7
```

**Exemplo de saida**
```text
13
```

### 23 - Soma de 1 ate N

**Pasta:** `exercises/23_sum_1_to_n`

**Objetivo:** Leia um inteiro positivo n e imprima a soma de todos os inteiros de 1 ate n.

**Entrada:** Um inteiro positivo n.

**Saida:** Um inteiro: a soma de 1 ate n.

**Exemplo de entrada**
```text
5
```

**Exemplo de saida**
```text
15
```

### 24 - Contar Digitos

**Pasta:** `exercises/24_count_digits`

**Objetivo:** Leia um inteiro nao negativo e imprima quantos digitos ele possui. O numero 0 possui 1 digito.

**Entrada:** Um inteiro nao negativo.

**Saida:** Um inteiro: a quantidade de digitos.

**Exemplo de entrada**
```text
4502
```

**Exemplo de saida**
```text
4
```

### 25 - Potencia Inteira

**Pasta:** `exercises/25_power_loop`

**Objetivo:** Leia um inteiro base e um inteiro nao negativo expoente, depois imprima base elevada a expoente usando um laco.

**Entrada:** Dois inteiros separados por espaco: base expoente.

**Saida:** Um inteiro: base^expoente.

**Exemplo de entrada**
```text
2 5
```

**Exemplo de saida**
```text
32
```

## Executar todos os testes

```bash
./run_all_tests.sh
```
