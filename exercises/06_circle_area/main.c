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
        {"0", "0.00"},
{"1", "3.14"},
{"2", "12.57"},
{"2.5", "19.63"},
{"3", "28.27"},
{"4.2", "55.42"},
{"5", "78.54"},
{"7.1", "158.37"},
{"10", "314.16"},
{"12.3", "475.29"},
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
