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

void solve(int width, int height, int *area, int *perimeter) {
    // TODO: implemente a logica deste exercicio.
    (void)width;
    (void)height;
    (void)area;
    (void)perimeter;
}

void run_tests(void) {
    TestCase cases[] = {
        {"1 1", "1 4"},
{"2 3", "6 10"},
{"5 10", "50 30"},
{"7 4", "28 22"},
{"9 9", "81 36"},
{"12 5", "60 34"},
{"15 2", "30 34"},
{"8 6", "48 28"},
{"20 1", "20 42"},
{"11 13", "143 48"},
    };
    int total = (int)(sizeof(cases) / sizeof(cases[0]));

    for (int i = 0; i < total; i++) {
        int width = 0;
        int height = 0;
        int area = 0;
        int perimeter = 0;
        char actual[64];

        sscanf(cases[i].input, "%d %d", &width, &height);
        solve(width, height, &area, &perimeter);
        snprintf(actual, sizeof(actual), "%d %d", area, perimeter);
        print_test_result(i + 1, cases[i].input, cases[i].expected, actual);
    }
}

int main(int argc, char *argv[]) {
    if (argc > 1 && strcmp(argv[1], "--test") == 0) {
        run_tests();
        return 0;
    }

    int width = 0;
    int height = 0;
    int area = 0;
    int perimeter = 0;

    if (scanf("%d %d", &width, &height) != 2) {
        return 1;
    }

    solve(width, height, &area, &perimeter);
    printf("%d %d\n", area, perimeter);
    return 0;
}
