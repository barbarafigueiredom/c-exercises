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

int solve(int a, int b, int c) {
    // Comece assumindo que o primeiro numero e o maior.
    int greatest = a;

    // Troque se o segundo numero for maior.
    if (b > greatest) {
        greatest = b;
    }

    // Troque novamente se o terceiro numero for maior que o atual.
    if (c > greatest) {
        greatest = c;
    }

    // Retorne o maior numero encontrado.
    return greatest;
}

void run_tests(void) {
    TestCase cases[] = {
        {"1 2 3", "3"},
{"10 5 8", "10"},
{"-1 -2 -3", "-1"},
{"7 7 2", "7"},
{"0 0 0", "0"},
{"100 50 150", "150"},
{"9 12 11", "12"},
{"-5 20 3", "20"},
{"42 24 36", "42"},
{"500 1000 750", "1000"},
    };
    int total = (int)(sizeof(cases) / sizeof(cases[0]));

    for (int i = 0; i < total; i++) {
        int a = 0;
        int b = 0;
        int c = 0;
        char actual[64];

        sscanf(cases[i].input, "%d %d %d", &a, &b, &c);
        snprintf(actual, sizeof(actual), "%d", solve(a, b, c));
        print_test_result(i + 1, cases[i].input, cases[i].expected, actual);
    }
}

int main(int argc, char *argv[]) {
    if (argc > 1 && strcmp(argv[1], "--test") == 0) {
        run_tests();
        return 0;
    }

    int a = 0;
    int b = 0;
    int c = 0;

    if (scanf("%d %d %d", &a, &b, &c) != 3) {
        return 1;
    }

    printf("%d\n", solve(a, b, c));
    return 0;
}
