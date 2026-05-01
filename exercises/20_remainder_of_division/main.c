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
    return a % b;
}

void run_tests(void) {
    TestCase cases[] = {
        {"10 3", "1"},
{"20 5", "0"},
{"7 2", "1"},
{"99 10", "9"},
{"100 6", "4"},
{"55 4", "3"},
{"81 8", "1"},
{"123 7", "4"},
{"1000 9", "1"},
{"42 11", "9"},
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
