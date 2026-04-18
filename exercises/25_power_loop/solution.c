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

int solve(int a, int b) {
    // Qualquer numero elevado a zero resulta em 1.
    int result = 1;

    // Multiplique pela base a quantidade de vezes indicada pelo expoente.
    for (int i = 0; i < b; i++) {
        result *= a;
    }

    // Retorne o resultado final da potencia.
    return result;
}

void run_tests(void) {
    TestCase cases[] = {
        {"2 0", "1"},
{"2 1", "2"},
{"2 5", "32"},
{"3 4", "81"},
{"5 3", "125"},
{"10 2", "100"},
{"7 1", "7"},
{"1 9", "1"},
{"0 5", "0"},
{"4 4", "256"},
    };
    int total = (int)(sizeof(cases) / sizeof(cases[0]));

    for (int i = 0; i < total; i++) {
        int a = 0;
        int b = 0;
        char actual[64];

        sscanf(cases[i].input, "%d %d", &a, &b);
        snprintf(actual, sizeof(actual), "%d", solve(a, b));
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

    if (scanf("%d %d", &a, &b) != 2) {
        return 1;
    }

    printf("%d\n", solve(a, b));
    return 0;
}
