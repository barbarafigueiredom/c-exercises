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
    if (a >= b){
        return a; 
    }
    return b;
}

void run_tests(void) {
    TestCase cases[] = {
        {"5 3", "5"},
{"10 10", "10"},
{"-1 -5", "-1"},
{"7 20", "20"},
{"0 8", "8"},
{"100 99", "100"},
{"-10 10", "10"},
{"42 24", "42"},
{"500 1000", "1000"},
{"-3 -3", "-3"},
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
