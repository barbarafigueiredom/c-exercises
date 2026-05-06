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
    int sum = 0;
    int a = 0;
    int b = 1;

    if (value == 0){
        return a;
    }

    if (value == 1){
        return b;
    }

        
    for (int i = 0; i < value; i++) {
        sum = a + b;
        a = b + sum;
        return sum;
    }

    return 0;
}

void run_tests(void) {
    TestCase cases[] = {
        {"0", "0"},
{"1", "1"},
{"2", "1"},
{"3", "2"},
{"4", "3"},
{"5", "5"},
{"6", "8"},
{"7", "13"},
{"10", "55"},
{"15", "610"},
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
