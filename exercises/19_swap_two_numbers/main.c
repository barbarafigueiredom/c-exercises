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

void solve(int first_input, int second_input, int *first_output, int *second_output) {
    // TODO: implemente a logica deste exercicio.
    (void)first_input;
    (void)second_input;
    (void)first_output;
    (void)second_output;
}

void run_tests(void) {
    TestCase cases[] = {
        {"1 2", "2 1"},
{"5 10", "10 5"},
{"-3 7", "7 -3"},
{"0 0", "0 0"},
{"100 50", "50 100"},
{"-10 -20", "-20 -10"},
{"42 24", "24 42"},
{"999 1", "1 999"},
{"8 -8", "-8 8"},
{"123 456", "456 123"},
    };
    int total = (int)(sizeof(cases) / sizeof(cases[0]));

    for (int i = 0; i < total; i++) {
        int first_input = 0;
        int second_input = 0;
        int first_output = 0;
        int second_output = 0;
        char actual[64];

        sscanf(cases[i].input, "%d %d", &first_input, &second_input);
        solve(first_input, second_input, &first_output, &second_output);
        snprintf(actual, sizeof(actual), "%d %d", first_output, second_output);
        print_test_result(i + 1, cases[i].input, cases[i].expected, actual);
    }
}

int main(int argc, char *argv[]) {
    if (argc > 1 && strcmp(argv[1], "--test") == 0) {
        run_tests();
        return 0;
    }

    int first_input = 0;
    int second_input = 0;
    int first_output = 0;
    int second_output = 0;

    if (scanf("%d %d", &first_input, &second_input) != 2) {
        return 1;
    }

    solve(first_input, second_input, &first_output, &second_output);
    printf("%d %d\n", first_output, second_output);
    return 0;
}
