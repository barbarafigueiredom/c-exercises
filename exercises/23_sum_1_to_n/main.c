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
    // TODO: implemente a logica deste exercicio.
    (void)value;
    return 0;
}

void run_tests(void) {
    TestCase cases[] = {
        {"1", "1"},
{"2", "3"},
{"3", "6"},
{"4", "10"},
{"5", "15"},
{"10", "55"},
{"20", "210"},
{"50", "1275"},
{"100", "5050"},
{"25", "325"},
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
