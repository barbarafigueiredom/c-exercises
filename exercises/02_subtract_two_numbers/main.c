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
    int sub = a - b;
    
    return sub;
}

void run_tests(void) {
    TestCase cases[] = {
        {"5 3", "2"},
{"10 10", "0"},
{"0 7", "-7"},
{"-5 -2", "-3"},
{"100 25", "75"},
{"3 9", "-6"},
{"50 -10", "60"},
{"-8 5", "-13"},
{"999 1", "998"},
{"1 999", "-998"},
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
