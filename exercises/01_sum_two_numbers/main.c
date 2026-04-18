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
    // TODO: implemente a logica deste exercicio.
    (void)a;
    (void)b;
    return 0;
}

void run_tests(void) {
    TestCase cases[] = {
        {"0 0", "0"},
{"2 3", "5"},
{"10 15", "25"},
{"-5 7", "2"},
{"100 200", "300"},
{"-10 -20", "-30"},
{"999 1", "1000"},
{"42 -42", "0"},
{"123 456", "579"},
{"-100 50", "-50"},
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
