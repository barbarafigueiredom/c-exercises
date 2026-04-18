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

double solve(double a, double b, double c) {

    return (a + b + c) / 3 ;
}

void run_tests(void) {
    TestCase cases[] = {
        {"1 2 3", "2.00"},
{"10 20 30", "20.00"},
{"5 5 5", "5.00"},
{"0 0 10", "3.33"},
{"2.5 3.5 4.5", "3.50"},
{"-5 5 10", "3.33"},
{"7 8.5 9", "8.17"},
{"100 50 25", "58.33"},
{"1.2 3.4 5.6", "3.40"},
{"9.9 0.1 5", "5.00"},
    };
    int total = (int)(sizeof(cases) / sizeof(cases[0]));

    for (int i = 0; i < total; i++) {
        double a = 0.0;
        double b = 0.0;
        double c = 0.0;
        char actual[64];

        sscanf(cases[i].input, "%lf %lf %lf", &a, &b, &c);
        snprintf(actual, sizeof(actual), "%.2f", solve(a, b, c));
        print_test_result(i + 1, cases[i].input, cases[i].expected, actual);
    }
}

int main(int argc, char *argv[]) {
    if (argc > 1 && strcmp(argv[1], "--test") == 0) {
        run_tests();
        return 0;
    }

    double a = 0.0;
    double b = 0.0;
    double c = 0.0;

    if (scanf("%lf %lf %lf", &a, &b, &c) != 3) {
        return 1;
    }

    printf("%.2f\n", solve(a, b, c));
    return 0;
}
