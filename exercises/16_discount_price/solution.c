#include <stdio.h>
#include <string.h>

typedef struct {
    const char *input;
    const char *expected;
} TestCase;

void print_test_result(int index, const char *input, const char *expected, const char *actual) {
    printf("Test %d\n", index);
    printf("Input: %s\n", input);
    printf("Expected:\n%s\n", expected);
    printf("Actual:\n%s\n", actual);
    printf("Status: %s\n\n", strcmp(expected, actual) == 0 ? "PASS" : "FAIL");
}

double solve(double amount, double percentage) {
    // Calcule quanto dinheiro sera retirado do preco original.
    double discount_value = amount * percentage / 100.0;

    // Subtraia o desconto do preco original.
    double final_price = amount - discount_value;

    // Retorne o preco com desconto.
    return final_price;
}

void run_tests(void) {
    TestCase cases[] = {
        {"100 10", "90.00"},
{"250 5", "237.50"},
{"399.90 12", "351.91"},
{"1500 0", "1500.00"},
{"999.99 8", "919.99"},
{"80 25", "60.00"},
{"45.50 10", "40.95"},
{"230 7.5", "212.75"},
{"4100 3", "3977.00"},
{"1200 18", "984.00"},
    };
    int total = (int)(sizeof(cases) / sizeof(cases[0]));

    for (int i = 0; i < total; i++) {
        double amount = 0.0;
        double percentage = 0.0;
        char actual[64];

        sscanf(cases[i].input, "%lf %lf", &amount, &percentage);
        snprintf(actual, sizeof(actual), "%.2f", solve(amount, percentage));
        print_test_result(i + 1, cases[i].input, cases[i].expected, actual);
    }
}

int main(int argc, char *argv[]) {
    if (argc > 1 && strcmp(argv[1], "--test") == 0) {
        run_tests();
        return 0;
    }

    double amount = 0.0;
    double percentage = 0.0;

    if (scanf("%lf %lf", &amount, &percentage) != 2) {
        return 1;
    }

    printf("%.2f\n", solve(amount, percentage));
    return 0;
}
