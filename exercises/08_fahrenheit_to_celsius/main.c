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
    // TODO: implemente a logica deste exercicio.
    (void)value;
    return 0.0;
}

void run_tests(void) {
    TestCase cases[] = {
        {"32", "0.00"},
{"50", "10.00"},
{"77", "25.00"},
{"98.6", "37.00"},
{"212", "100.00"},
{"-40", "-40.00"},
{"59.9", "15.50"},
{"13.1", "-10.50"},
{"41", "5.00"},
{"107.96", "42.20"},
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
