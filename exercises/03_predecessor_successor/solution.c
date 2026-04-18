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

void solve(int number, int *first, int *second) {
    // O antecessor e uma unidade menor que o numero original.
    *first = number - 1;

    // O sucessor e uma unidade maior que o numero original.
    *second = number + 1;
}

void run_tests(void) {
    TestCase cases[] = {
        {"0", "-1 1"},
{"1", "0 2"},
{"-5", "-6 -4"},
{"10", "9 11"},
{"100", "99 101"},
{"-1", "-2 0"},
{"42", "41 43"},
{"999", "998 1000"},
{"-100", "-101 -99"},
{"7", "6 8"},
    };
    int total = (int)(sizeof(cases) / sizeof(cases[0]));

    for (int i = 0; i < total; i++) {
        int number = 0;
        int first = 0;
        int second = 0;
        char actual[64];

        sscanf(cases[i].input, "%d", &number);
        solve(number, &first, &second);
        snprintf(actual, sizeof(actual), "%d %d", first, second);
        print_test_result(i + 1, cases[i].input, cases[i].expected, actual);
    }
}

int main(int argc, char *argv[]) {
    if (argc > 1 && strcmp(argv[1], "--test") == 0) {
        run_tests();
        return 0;
    }

    int number = 0;
    int first = 0;
    int second = 0;

    if (scanf("%d", &number) != 1) {
        return 1;
    }

    solve(number, &first, &second);
    printf("%d %d\n", first, second);
    return 0;
}
