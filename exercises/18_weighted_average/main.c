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

double solve(double grade1, double weight1, double grade2, double weight2, double grade3, double weight3) {
    // TODO: implemente a logica deste exercicio.
    (void)grade1;
    (void)weight1;
    (void)grade2;
    (void)weight2;
    (void)grade3;
    (void)weight3;
    return 0.0;
}

void run_tests(void) {
    TestCase cases[] = {
        {"7 2 8 3 9 5", "8.30"},
{"10 1 10 1 10 1", "10.00"},
{"5 1 6 1 7 1", "6.00"},
{"4.5 2 7.5 3 8 5", "7.15"},
{"0 2 10 3 5 5", "5.50"},
{"9 4 8 3 7 3", "8.10"},
{"6.5 2 7.5 2 8.5 6", "7.90"},
{"3 5 4 2 10 3", "5.30"},
{"1.2 1 3.4 2 5.6 3", "4.13"},
{"8 5 9 2 10 3", "8.80"},
    };
    int total = (int)(sizeof(cases) / sizeof(cases[0]));

    for (int i = 0; i < total; i++) {
        double grade1 = 0.0;
        double weight1 = 0.0;
        double grade2 = 0.0;
        double weight2 = 0.0;
        double grade3 = 0.0;
        double weight3 = 0.0;
        char actual[64];

        sscanf(
            cases[i].input,
            "%lf %lf %lf %lf %lf %lf",
            &grade1,
            &weight1,
            &grade2,
            &weight2,
            &grade3,
            &weight3
        );
        snprintf(actual, sizeof(actual), "%.2f", solve(grade1, weight1, grade2, weight2, grade3, weight3));
        print_test_result(i + 1, cases[i].input, cases[i].expected, actual);
    }
}

int main(int argc, char *argv[]) {
    if (argc > 1 && strcmp(argv[1], "--test") == 0) {
        run_tests();
        return 0;
    }

    double grade1 = 0.0;
    double weight1 = 0.0;
    double grade2 = 0.0;
    double weight2 = 0.0;
    double grade3 = 0.0;
    double weight3 = 0.0;

    if (scanf("%lf %lf %lf %lf %lf %lf", &grade1, &weight1, &grade2, &weight2, &grade3, &weight3) != 6) {
        return 1;
    }

    printf("%.2f\n", solve(grade1, weight1, grade2, weight2, grade3, weight3));
    return 0;
}
