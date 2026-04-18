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

int solve(int value) {
    // O numero 0 e um caso especial porque ele ainda possui um digito.
    if (value == 0) {
        return 1;
    }

    // Conte quantas vezes conseguimos remover o ultimo digito.
    int digits = 0;
    int current = value;

    while (current > 0) {
        digits++;
        current /= 10;
    }

    // Retorne a quantidade de digitos contada.
    return digits;
}

void run_tests(void) {
    TestCase cases[] = {
        {"0", "1"},
{"7", "1"},
{"10", "2"},
{"99", "2"},
{"100", "3"},
{"4502", "4"},
{"99999", "5"},
{"123456", "6"},
{"1000000", "7"},
{"2147483647", "10"},
    };
    int total = (int)(sizeof(cases) / sizeof(cases[0]));

    for (int i = 0; i < total; i++) {
        int value = 0;
        char actual[64];

        sscanf(cases[i].input, "%d", &value);
        snprintf(actual, sizeof(actual), "%d", solve(value));
        print_test_result(i + 1, cases[i].input, cases[i].expected, actual);
    }
}

int main(int argc, char *argv[]) {
    if (argc > 1 && strcmp(argv[1], "--test") == 0) {
        run_tests();
        return 0;
    }

    int value = 0;

    if (scanf("%d", &value) != 1) {
        return 1;
    }

    printf("%d\n", solve(value));
    return 0;
}
