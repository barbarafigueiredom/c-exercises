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

void solve(int total_seconds, int *hours, int *minutes, int *seconds) {    
    *hours = total_seconds / 3600;
    int rest_hours = total_seconds % 3600;
    *minutes = rest_hours / 60;
    *seconds = rest_hours % 60;
}

void run_tests(void) {
    TestCase cases[] = {
        {"0", "0 0 0"},
{"59", "0 0 59"},
{"60", "0 1 0"},
{"61", "0 1 1"},
{"3599", "0 59 59"},
{"3600", "1 0 0"},
{"3661", "1 1 1"},
{"7325", "2 2 5"},
{"86399", "23 59 59"},
{"10000", "2 46 40"},
    };
    int total = (int)(sizeof(cases) / sizeof(cases[0]));

    for (int i = 0; i < total; i++) {
        int total_seconds = 0;
        int hours = 0;
        int minutes = 0;
        int seconds = 0;
        char actual[64];

        sscanf(cases[i].input, "%d", &total_seconds);
        solve(total_seconds, &hours, &minutes, &seconds);
        snprintf(actual, sizeof(actual), "%d %d %d", hours, minutes, seconds);
        print_test_result(i + 1, cases[i].input, cases[i].expected, actual);
    }
}

int main(int argc, char *argv[]) {
    if (argc > 1 && strcmp(argv[1], "--test") == 0) {
        run_tests();
        return 0;
    }

    int total_seconds = 0;
    int hours = 0;
    int minutes = 0;
    int seconds = 0;

    if (scanf("%d", &total_seconds) != 1) {
        return 1;
    }

    solve(total_seconds, &hours, &minutes, &seconds);
    printf("%d %d %d\n", hours, minutes, seconds);
    return 0;
}
