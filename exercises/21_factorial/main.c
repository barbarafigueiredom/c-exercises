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

unsigned long long solve(int value) {
    unsigned long long fatorial = 1;

    for (int i = 1; i <= value; i++) {
        fatorial *= i;
    }

    return fatorial;
}

void run_tests(void) {
    TestCase cases[] = {
        {"0", "1"},
{"1", "1"},
{"2", "2"},
{"3", "6"},
{"4", "24"},
{"5", "120"},
{"6", "720"},
{"7", "5040"},
{"10", "3628800"},
{"12", "479001600"},
    };
    int total = (int)(sizeof(cases) / sizeof(cases[0]));

    for (int i = 0; i < total; i++) {
        int value = 0;
        char actual[64];

        sscanf(cases[i].input, "%d", &value);
        snprintf(actual, sizeof(actual), "%llu", solve(value));
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

    printf("%llu\n", solve(value));
    return 0;
}
