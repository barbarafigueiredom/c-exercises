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

const char *solve(int value) {
    // TODO: implemente a logica deste exercicio.
    (void)value;
    return "TODO";
}

void run_tests(void) {
    TestCase cases[] = {
        {"-5", "NEGATIVE"},
{"0", "ZERO"},
{"7", "POSITIVE"},
{"-1", "NEGATIVE"},
{"1", "POSITIVE"},
{"100", "POSITIVE"},
{"-100", "NEGATIVE"},
{"999", "POSITIVE"},
{"-42", "NEGATIVE"},
{"5", "POSITIVE"},
    };
    int total = (int)(sizeof(cases) / sizeof(cases[0]));

    for (int i = 0; i < total; i++) {
        int value = 0;
        char actual[64];

        sscanf(cases[i].input, "%d", &value);
        snprintf(actual, sizeof(actual), "%s", solve(value));
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

    printf("%s\n", solve(value));
    return 0;
}
