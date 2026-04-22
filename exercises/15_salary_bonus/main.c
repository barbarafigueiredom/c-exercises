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

double solve(double amount, double percentage) {
   double porcentagem = (amount * percentage) / 100;
    return porcentagem + amount;
}

void run_tests(void) {
    TestCase cases[] = {
        {"1000 10", "1100.00"},
{"2500 5", "2625.00"},
{"3200 12.5", "3600.00"},
{"1500 0", "1500.00"},
{"999.99 8", "1079.99"},
{"5000 20", "6000.00"},
{"780 15", "897.00"},
{"2300 7.5", "2472.50"},
{"4100 3", "4223.00"},
{"1200 18", "1416.00"},
    };
    int total = (int)(sizeof(cases) / sizeof(cases[0]));

    for (int i = 0; i < total; i++) {
        double amount = 0.0;
        double percentage = 0.0;
        char actual[64];

        sscanf(cases[i].input, "%lf %lf", &amount, &percentage);
        snprintf(actual, sizeof(actual), "%.2f", solve(amount, percentage));
        print_test_result(i + 1, cases[i].input, cases[i].expected, actual);
    }
}

int main(int argc, char *argv[]) {
    if (argc > 1 && strcmp(argv[1], "--test") == 0) {
        run_tests();
        return 0;
    }

    double amount = 0.0;
    double percentage = 0.0;

    if (scanf("%lf %lf", &amount, &percentage) != 2) {
        return 1;
    }

    printf("%.2f\n", solve(amount, percentage));
    return 0;
}
