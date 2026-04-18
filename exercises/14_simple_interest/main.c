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

double solve(double principal, double rate, double time) {
    // TODO: implemente a logica deste exercicio.
    (void)principal;
    (void)rate;
    (void)time;
    return 0.0;
}

void run_tests(void) {
    TestCase cases[] = {
        {"1000 5 2", "100.00"},
{"1500 10 1", "150.00"},
{"200 3 4", "24.00"},
{"5000 7.5 3", "1125.00"},
{"750 12 2", "180.00"},
{"100 1 1", "1.00"},
{"3500 8 0.5", "140.00"},
{"999.99 6 1", "60.00"},
{"250 2.5 8", "50.00"},
{"4200 4 5", "840.00"},
    };
    int total = (int)(sizeof(cases) / sizeof(cases[0]));

    for (int i = 0; i < total; i++) {
        double principal = 0.0;
        double rate = 0.0;
        double time = 0.0;
        char actual[64];

        sscanf(cases[i].input, "%lf %lf %lf", &principal, &rate, &time);
        snprintf(actual, sizeof(actual), "%.2f", solve(principal, rate, time));
        print_test_result(i + 1, cases[i].input, cases[i].expected, actual);
    }
}

int main(int argc, char *argv[]) {
    if (argc > 1 && strcmp(argv[1], "--test") == 0) {
        run_tests();
        return 0;
    }

    double principal = 0.0;
    double rate = 0.0;
    double time = 0.0;

    if (scanf("%lf %lf %lf", &principal, &rate, &time) != 3) {
        return 1;
    }

    printf("%.2f\n", solve(principal, rate, time));
    return 0;
}
