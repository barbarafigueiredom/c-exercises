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

void solve(int number, char *output, size_t output_size) {
    // TODO: implemente a logica deste exercicio.
    (void)number;
    snprintf(output, output_size, "TODO");
}

void run_tests(void) {
    TestCase cases[] = {
        {"1", "1 x 1 = 1\n1 x 2 = 2\n1 x 3 = 3\n1 x 4 = 4\n1 x 5 = 5\n1 x 6 = 6\n1 x 7 = 7\n1 x 8 = 8\n1 x 9 = 9\n1 x 10 = 10"},
{"2", "2 x 1 = 2\n2 x 2 = 4\n2 x 3 = 6\n2 x 4 = 8\n2 x 5 = 10\n2 x 6 = 12\n2 x 7 = 14\n2 x 8 = 16\n2 x 9 = 18\n2 x 10 = 20"},
{"3", "3 x 1 = 3\n3 x 2 = 6\n3 x 3 = 9\n3 x 4 = 12\n3 x 5 = 15\n3 x 6 = 18\n3 x 7 = 21\n3 x 8 = 24\n3 x 9 = 27\n3 x 10 = 30"},
{"5", "5 x 1 = 5\n5 x 2 = 10\n5 x 3 = 15\n5 x 4 = 20\n5 x 5 = 25\n5 x 6 = 30\n5 x 7 = 35\n5 x 8 = 40\n5 x 9 = 45\n5 x 10 = 50"},
{"7", "7 x 1 = 7\n7 x 2 = 14\n7 x 3 = 21\n7 x 4 = 28\n7 x 5 = 35\n7 x 6 = 42\n7 x 7 = 49\n7 x 8 = 56\n7 x 9 = 63\n7 x 10 = 70"},
{"9", "9 x 1 = 9\n9 x 2 = 18\n9 x 3 = 27\n9 x 4 = 36\n9 x 5 = 45\n9 x 6 = 54\n9 x 7 = 63\n9 x 8 = 72\n9 x 9 = 81\n9 x 10 = 90"},
{"10", "10 x 1 = 10\n10 x 2 = 20\n10 x 3 = 30\n10 x 4 = 40\n10 x 5 = 50\n10 x 6 = 60\n10 x 7 = 70\n10 x 8 = 80\n10 x 9 = 90\n10 x 10 = 100"},
{"11", "11 x 1 = 11\n11 x 2 = 22\n11 x 3 = 33\n11 x 4 = 44\n11 x 5 = 55\n11 x 6 = 66\n11 x 7 = 77\n11 x 8 = 88\n11 x 9 = 99\n11 x 10 = 110"},
{"12", "12 x 1 = 12\n12 x 2 = 24\n12 x 3 = 36\n12 x 4 = 48\n12 x 5 = 60\n12 x 6 = 72\n12 x 7 = 84\n12 x 8 = 96\n12 x 9 = 108\n12 x 10 = 120"},
{"-4", "-4 x 1 = -4\n-4 x 2 = -8\n-4 x 3 = -12\n-4 x 4 = -16\n-4 x 5 = -20\n-4 x 6 = -24\n-4 x 7 = -28\n-4 x 8 = -32\n-4 x 9 = -36\n-4 x 10 = -40"},
    };
    int total = (int)(sizeof(cases) / sizeof(cases[0]));

    for (int i = 0; i < total; i++) {
        int number = 0;
        char actual[512];

        sscanf(cases[i].input, "%d", &number);
        solve(number, actual, sizeof(actual));
        print_test_result(i + 1, cases[i].input, cases[i].expected, actual);
    }
}

int main(int argc, char *argv[]) {
    if (argc > 1 && strcmp(argv[1], "--test") == 0) {
        run_tests();
        return 0;
    }

    int number = 0;
    char output[512];

    if (scanf("%d", &number) != 1) {
        return 1;
    }

    solve(number, output, sizeof(output));
    printf("%s\n", output);
    return 0;
}
