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

double solve(double value) {
    // Multiplique Celsius por 9.
    double scaled = value * 9.0;

    // Divida por 5 para completar a fracao 9/5.
    double converted = scaled / 5.0;

    // Some 32 para mudar da escala Celsius para Fahrenheit.
    double fahrenheit = converted + 32.0;

    // Retorne a temperatura convertida.
    return fahrenheit;
}

void run_tests(void) {
    TestCase cases[] = {
        {"0", "32.00"},
{"10", "50.00"},
{"25", "77.00"},
{"37", "98.60"},
{"100", "212.00"},
{"-40", "-40.00"},
{"15.5", "59.90"},
{"-10.5", "13.10"},
{"5", "41.00"},
{"42.2", "107.96"},
    };
    int total = (int)(sizeof(cases) / sizeof(cases[0]));

    for (int i = 0; i < total; i++) {
        double value = 0.0;
        char actual[64];

        sscanf(cases[i].input, "%lf", &value);
        snprintf(actual, sizeof(actual), "%.2f", solve(value));
        print_test_result(i + 1, cases[i].input, cases[i].expected, actual);
    }
}

int main(int argc, char *argv[]) {
    if (argc > 1 && strcmp(argv[1], "--test") == 0) {
        run_tests();
        return 0;
    }

    double value = 0.0;

    if (scanf("%lf", &value) != 1) {
        return 1;
    }

    printf("%.2f\n", solve(value));
    return 0;
}
