from __future__ import annotations

import json
from pathlib import Path
from textwrap import dedent


ROOT = Path(__file__).resolve().parents[1]
EXERCISES_DIR = ROOT / "exercises"


def c_string(value: str) -> str:
    escaped = value.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n")
    return f'"{escaped}"'


def render_cases(cases: list[tuple[str, str]]) -> str:
    lines = [f"        {{{c_string(input_text)}, {c_string(expected_text)}}}," for input_text, expected_text in cases]
    return "\n".join(lines)


def indent_block(text: str, spaces: int = 12) -> str:
    prefix = " " * spaces
    return "\n".join(prefix + line if line else "" for line in dedent(text).strip().splitlines())


def render_scaffold(text: str) -> str:
    return indent_block(text)


def render_solution(meta: dict, fallback: str) -> str:
    return indent_block(PT_BR_SOLUTIONS.get(meta["slug"], fallback))


def common_header() -> str:
    return dedent(
        """\
        #include <stdio.h>
        #include <string.h>

        typedef struct {
            const char *input;
            const char *expected;
        } TestCase;

        void print_test_result(int index, const char *input, const char *expected, const char *actual) {
            printf("Test %d\\n", index);
            printf("Input: %s\\n", input);
            printf("Expected:\\n%s\\n", expected);
            printf("Actual:\\n%s\\n", actual);
            printf("Status: %s\\n\\n", strcmp(expected, actual) == 0 ? "PASS" : "FAIL");
        }

        """
    )


def source_int_binary(meta: dict, solved: bool = False) -> str:
    body = render_solution(
        meta,
        """
        // TODO: implemente a logica deste exercicio.
        (void)a;
        (void)b;
        return 0;
        """,
    ) if solved else render_scaffold(
        """
        // TODO: implemente a logica deste exercicio.
        (void)a;
        (void)b;
        return 0;
        """
    )
    return common_header() + dedent(
        f"""\
        int solve(int a, int b) {{
{body}
        }}

        void run_tests(void) {{
            TestCase cases[] = {{
        {render_cases(meta["cases"])}
            }};
            int total = (int)(sizeof(cases) / sizeof(cases[0]));

            for (int i = 0; i < total; i++) {{
                int a = 0;
                int b = 0;
                char actual[64];

                sscanf(cases[i].input, "%d %d", &a, &b);
                snprintf(actual, sizeof(actual), "{meta["printf_format"]}", solve(a, b));
                print_test_result(i + 1, cases[i].input, cases[i].expected, actual);
            }}
        }}

        int main(int argc, char *argv[]) {{
            if (argc > 1 && strcmp(argv[1], "--test") == 0) {{
                run_tests();
                return 0;
            }}

            int a = 0;
            int b = 0;

            if (scanf("%d %d", &a, &b) != 2) {{
                return 1;
            }}

            printf("{meta["printf_format"]}\\n", solve(a, b));
            return 0;
        }}
        """
    )


def source_unary_pair(meta: dict, solved: bool = False) -> str:
    body = render_solution(
        meta,
        """
        // TODO: implemente a logica deste exercicio.
        (void)number;
        (void)first;
        (void)second;
        """,
    ) if solved else render_scaffold(
        """
        // TODO: implemente a logica deste exercicio.
        (void)number;
        (void)first;
        (void)second;
        """
    )
    return common_header() + dedent(
        f"""\
        void solve(int number, int *first, int *second) {{
{body}
        }}

        void run_tests(void) {{
            TestCase cases[] = {{
        {render_cases(meta["cases"])}
            }};
            int total = (int)(sizeof(cases) / sizeof(cases[0]));

            for (int i = 0; i < total; i++) {{
                int number = 0;
                int first = 0;
                int second = 0;
                char actual[64];

                sscanf(cases[i].input, "%d", &number);
                solve(number, &first, &second);
                snprintf(actual, sizeof(actual), "{meta["printf_format"]}", first, second);
                print_test_result(i + 1, cases[i].input, cases[i].expected, actual);
            }}
        }}

        int main(int argc, char *argv[]) {{
            if (argc > 1 && strcmp(argv[1], "--test") == 0) {{
                run_tests();
                return 0;
            }}

            int number = 0;
            int first = 0;
            int second = 0;

            if (scanf("%d", &number) != 1) {{
                return 1;
            }}

            solve(number, &first, &second);
            printf("{meta["printf_format"]}\\n", first, second);
            return 0;
        }}
        """
    )


def source_average_of_three(meta: dict, solved: bool = False) -> str:
    body = render_solution(
        meta,
        """
        // TODO: implemente a logica deste exercicio.
        (void)a;
        (void)b;
        (void)c;
        return 0.0;
        """,
    ) if solved else render_scaffold(
        """
        // TODO: implemente a logica deste exercicio.
        (void)a;
        (void)b;
        (void)c;
        return 0.0;
        """
    )
    return common_header() + dedent(
        f"""\
        double solve(double a, double b, double c) {{
{body}
        }}

        void run_tests(void) {{
            TestCase cases[] = {{
        {render_cases(meta["cases"])}
            }};
            int total = (int)(sizeof(cases) / sizeof(cases[0]));

            for (int i = 0; i < total; i++) {{
                double a = 0.0;
                double b = 0.0;
                double c = 0.0;
                char actual[64];

                sscanf(cases[i].input, "%lf %lf %lf", &a, &b, &c);
                snprintf(actual, sizeof(actual), "%.2f", solve(a, b, c));
                print_test_result(i + 1, cases[i].input, cases[i].expected, actual);
            }}
        }}

        int main(int argc, char *argv[]) {{
            if (argc > 1 && strcmp(argv[1], "--test") == 0) {{
                run_tests();
                return 0;
            }}

            double a = 0.0;
            double b = 0.0;
            double c = 0.0;

            if (scanf("%lf %lf %lf", &a, &b, &c) != 3) {{
                return 1;
            }}

            printf("%.2f\\n", solve(a, b, c));
            return 0;
        }}
        """
    )


def source_int_ternary(meta: dict, solved: bool = False) -> str:
    body = render_solution(
        meta,
        """
        // TODO: implemente a logica deste exercicio.
        (void)a;
        (void)b;
        (void)c;
        return 0;
        """,
    ) if solved else render_scaffold(
        """
        // TODO: implemente a logica deste exercicio.
        (void)a;
        (void)b;
        (void)c;
        return 0;
        """
    )
    return common_header() + dedent(
        f"""\
        int solve(int a, int b, int c) {{
{body}
        }}

        void run_tests(void) {{
            TestCase cases[] = {{
        {render_cases(meta["cases"])}
            }};
            int total = (int)(sizeof(cases) / sizeof(cases[0]));

            for (int i = 0; i < total; i++) {{
                int a = 0;
                int b = 0;
                int c = 0;
                char actual[64];

                sscanf(cases[i].input, "%d %d %d", &a, &b, &c);
                snprintf(actual, sizeof(actual), "%d", solve(a, b, c));
                print_test_result(i + 1, cases[i].input, cases[i].expected, actual);
            }}
        }}

        int main(int argc, char *argv[]) {{
            if (argc > 1 && strcmp(argv[1], "--test") == 0) {{
                run_tests();
                return 0;
            }}

            int a = 0;
            int b = 0;
            int c = 0;

            if (scanf("%d %d %d", &a, &b, &c) != 3) {{
                return 1;
            }}

            printf("%d\\n", solve(a, b, c));
            return 0;
        }}
        """
    )


def source_int_pair_from_binary(meta: dict, solved: bool = False) -> str:
    body = render_solution(
        meta,
        """
        // TODO: implemente a logica deste exercicio.
        (void)first_input;
        (void)second_input;
        (void)first_output;
        (void)second_output;
        """,
    ) if solved else render_scaffold(
        """
        // TODO: implemente a logica deste exercicio.
        (void)first_input;
        (void)second_input;
        (void)first_output;
        (void)second_output;
        """
    )
    return common_header() + dedent(
        f"""\
        void solve(int first_input, int second_input, int *first_output, int *second_output) {{
{body}
        }}

        void run_tests(void) {{
            TestCase cases[] = {{
        {render_cases(meta["cases"])}
            }};
            int total = (int)(sizeof(cases) / sizeof(cases[0]));

            for (int i = 0; i < total; i++) {{
                int first_input = 0;
                int second_input = 0;
                int first_output = 0;
                int second_output = 0;
                char actual[64];

                sscanf(cases[i].input, "%d %d", &first_input, &second_input);
                solve(first_input, second_input, &first_output, &second_output);
                snprintf(actual, sizeof(actual), "{meta["printf_format"]}", first_output, second_output);
                print_test_result(i + 1, cases[i].input, cases[i].expected, actual);
            }}
        }}

        int main(int argc, char *argv[]) {{
            if (argc > 1 && strcmp(argv[1], "--test") == 0) {{
                run_tests();
                return 0;
            }}

            int first_input = 0;
            int second_input = 0;
            int first_output = 0;
            int second_output = 0;

            if (scanf("%d %d", &first_input, &second_input) != 2) {{
                return 1;
            }}

            solve(first_input, second_input, &first_output, &second_output);
            printf("{meta["printf_format"]}\\n", first_output, second_output);
            return 0;
        }}
        """
    )


def source_rectangle(meta: dict, solved: bool = False) -> str:
    body = render_solution(
        meta,
        """
        // TODO: implemente a logica deste exercicio.
        (void)width;
        (void)height;
        (void)area;
        (void)perimeter;
        """,
    ) if solved else render_scaffold(
        """
        // TODO: implemente a logica deste exercicio.
        (void)width;
        (void)height;
        (void)area;
        (void)perimeter;
        """
    )
    return common_header() + dedent(
        f"""\
        void solve(int width, int height, int *area, int *perimeter) {{
{body}
        }}

        void run_tests(void) {{
            TestCase cases[] = {{
        {render_cases(meta["cases"])}
            }};
            int total = (int)(sizeof(cases) / sizeof(cases[0]));

            for (int i = 0; i < total; i++) {{
                int width = 0;
                int height = 0;
                int area = 0;
                int perimeter = 0;
                char actual[64];

                sscanf(cases[i].input, "%d %d", &width, &height);
                solve(width, height, &area, &perimeter);
                snprintf(actual, sizeof(actual), "%d %d", area, perimeter);
                print_test_result(i + 1, cases[i].input, cases[i].expected, actual);
            }}
        }}

        int main(int argc, char *argv[]) {{
            if (argc > 1 && strcmp(argv[1], "--test") == 0) {{
                run_tests();
                return 0;
            }}

            int width = 0;
            int height = 0;
            int area = 0;
            int perimeter = 0;

            if (scanf("%d %d", &width, &height) != 2) {{
                return 1;
            }}

            solve(width, height, &area, &perimeter);
            printf("%d %d\\n", area, perimeter);
            return 0;
        }}
        """
    )


def source_double_unary(meta: dict, solved: bool = False) -> str:
    body = render_solution(
        meta,
        """
        // TODO: implemente a logica deste exercicio.
        (void)value;
        return 0.0;
        """,
    ) if solved else render_scaffold(
        """
        // TODO: implemente a logica deste exercicio.
        (void)value;
        return 0.0;
        """
    )
    return common_header() + dedent(
        f"""\
        double solve(double value) {{
{body}
        }}

        void run_tests(void) {{
            TestCase cases[] = {{
        {render_cases(meta["cases"])}
            }};
            int total = (int)(sizeof(cases) / sizeof(cases[0]));

            for (int i = 0; i < total; i++) {{
                double value = 0.0;
                char actual[64];

                sscanf(cases[i].input, "%lf", &value);
                snprintf(actual, sizeof(actual), "%.2f", solve(value));
                print_test_result(i + 1, cases[i].input, cases[i].expected, actual);
            }}
        }}

        int main(int argc, char *argv[]) {{
            if (argc > 1 && strcmp(argv[1], "--test") == 0) {{
                run_tests();
                return 0;
            }}

            double value = 0.0;

            if (scanf("%lf", &value) != 1) {{
                return 1;
            }}

            printf("%.2f\\n", solve(value));
            return 0;
        }}
        """
    )


def source_seconds_to_hms(meta: dict, solved: bool = False) -> str:
    body = render_solution(
        meta,
        """
        // TODO: implemente a logica deste exercicio.
        (void)total_seconds;
        (void)hours;
        (void)minutes;
        (void)seconds;
        """,
    ) if solved else render_scaffold(
        """
        // TODO: implemente a logica deste exercicio.
        (void)total_seconds;
        (void)hours;
        (void)minutes;
        (void)seconds;
        """
    )
    return common_header() + dedent(
        f"""\
        void solve(int total_seconds, int *hours, int *minutes, int *seconds) {{
{body}
        }}

        void run_tests(void) {{
            TestCase cases[] = {{
        {render_cases(meta["cases"])}
            }};
            int total = (int)(sizeof(cases) / sizeof(cases[0]));

            for (int i = 0; i < total; i++) {{
                int total_seconds = 0;
                int hours = 0;
                int minutes = 0;
                int seconds = 0;
                char actual[64];

                sscanf(cases[i].input, "%d", &total_seconds);
                solve(total_seconds, &hours, &minutes, &seconds);
                snprintf(actual, sizeof(actual), "%d %d %d", hours, minutes, seconds);
                print_test_result(i + 1, cases[i].input, cases[i].expected, actual);
            }}
        }}

        int main(int argc, char *argv[]) {{
            if (argc > 1 && strcmp(argv[1], "--test") == 0) {{
                run_tests();
                return 0;
            }}

            int total_seconds = 0;
            int hours = 0;
            int minutes = 0;
            int seconds = 0;

            if (scanf("%d", &total_seconds) != 1) {{
                return 1;
            }}

            solve(total_seconds, &hours, &minutes, &seconds);
            printf("%d %d %d\\n", hours, minutes, seconds);
            return 0;
        }}
        """
    )


def source_text_from_int(meta: dict, solved: bool = False) -> str:
    body = render_solution(
        meta,
        """
        // TODO: implemente a logica deste exercicio.
        (void)value;
        return "TODO";
        """,
    ) if solved else render_scaffold(
        """
        // TODO: implemente a logica deste exercicio.
        (void)value;
        return "TODO";
        """
    )
    return common_header() + dedent(
        f"""\
        const char *solve(int value) {{
{body}
        }}

        void run_tests(void) {{
            TestCase cases[] = {{
        {render_cases(meta["cases"])}
            }};
            int total = (int)(sizeof(cases) / sizeof(cases[0]));

            for (int i = 0; i < total; i++) {{
                int value = 0;
                char actual[64];

                sscanf(cases[i].input, "%d", &value);
                snprintf(actual, sizeof(actual), "%s", solve(value));
                print_test_result(i + 1, cases[i].input, cases[i].expected, actual);
            }}
        }}

        int main(int argc, char *argv[]) {{
            if (argc > 1 && strcmp(argv[1], "--test") == 0) {{
                run_tests();
                return 0;
            }}

            int value = 0;

            if (scanf("%d", &value) != 1) {{
                return 1;
            }}

            printf("%s\\n", solve(value));
            return 0;
        }}
        """
    )


def source_binary_percentage(meta: dict, solved: bool = False) -> str:
    body = render_solution(
        meta,
        """
        // TODO: implemente a logica deste exercicio.
        (void)amount;
        (void)percentage;
        return 0.0;
        """,
    ) if solved else render_scaffold(
        """
        // TODO: implemente a logica deste exercicio.
        (void)amount;
        (void)percentage;
        return 0.0;
        """
    )
    return common_header() + dedent(
        f"""\
        double solve(double amount, double percentage) {{
{body}
        }}

        void run_tests(void) {{
            TestCase cases[] = {{
        {render_cases(meta["cases"])}
            }};
            int total = (int)(sizeof(cases) / sizeof(cases[0]));

            for (int i = 0; i < total; i++) {{
                double amount = 0.0;
                double percentage = 0.0;
                char actual[64];

                sscanf(cases[i].input, "%lf %lf", &amount, &percentage);
                snprintf(actual, sizeof(actual), "%.2f", solve(amount, percentage));
                print_test_result(i + 1, cases[i].input, cases[i].expected, actual);
            }}
        }}

        int main(int argc, char *argv[]) {{
            if (argc > 1 && strcmp(argv[1], "--test") == 0) {{
                run_tests();
                return 0;
            }}

            double amount = 0.0;
            double percentage = 0.0;

            if (scanf("%lf %lf", &amount, &percentage) != 2) {{
                return 1;
            }}

            printf("%.2f\\n", solve(amount, percentage));
            return 0;
        }}
        """
    )


def source_simple_interest(meta: dict, solved: bool = False) -> str:
    body = render_solution(
        meta,
        """
        // TODO: implemente a logica deste exercicio.
        (void)principal;
        (void)rate;
        (void)time;
        return 0.0;
        """,
    ) if solved else render_scaffold(
        """
        // TODO: implemente a logica deste exercicio.
        (void)principal;
        (void)rate;
        (void)time;
        return 0.0;
        """
    )
    return common_header() + dedent(
        f"""\
        double solve(double principal, double rate, double time) {{
{body}
        }}

        void run_tests(void) {{
            TestCase cases[] = {{
        {render_cases(meta["cases"])}
            }};
            int total = (int)(sizeof(cases) / sizeof(cases[0]));

            for (int i = 0; i < total; i++) {{
                double principal = 0.0;
                double rate = 0.0;
                double time = 0.0;
                char actual[64];

                sscanf(cases[i].input, "%lf %lf %lf", &principal, &rate, &time);
                snprintf(actual, sizeof(actual), "%.2f", solve(principal, rate, time));
                print_test_result(i + 1, cases[i].input, cases[i].expected, actual);
            }}
        }}

        int main(int argc, char *argv[]) {{
            if (argc > 1 && strcmp(argv[1], "--test") == 0) {{
                run_tests();
                return 0;
            }}

            double principal = 0.0;
            double rate = 0.0;
            double time = 0.0;

            if (scanf("%lf %lf %lf", &principal, &rate, &time) != 3) {{
                return 1;
            }}

            printf("%.2f\\n", solve(principal, rate, time));
            return 0;
        }}
        """
    )


def source_table(meta: dict, solved: bool = False) -> str:
    body = render_solution(
        meta,
        """
        // TODO: implemente a logica deste exercicio.
        (void)number;
        snprintf(output, output_size, "TODO");
        """,
    ) if solved else render_scaffold(
        """
        // TODO: implemente a logica deste exercicio.
        (void)number;
        snprintf(output, output_size, "TODO");
        """
    )
    return common_header() + dedent(
        f"""\
        void solve(int number, char *output, size_t output_size) {{
{body}
        }}

        void run_tests(void) {{
            TestCase cases[] = {{
        {render_cases(meta["cases"])}
            }};
            int total = (int)(sizeof(cases) / sizeof(cases[0]));

            for (int i = 0; i < total; i++) {{
                int number = 0;
                char actual[512];

                sscanf(cases[i].input, "%d", &number);
                solve(number, actual, sizeof(actual));
                print_test_result(i + 1, cases[i].input, cases[i].expected, actual);
            }}
        }}

        int main(int argc, char *argv[]) {{
            if (argc > 1 && strcmp(argv[1], "--test") == 0) {{
                run_tests();
                return 0;
            }}

            int number = 0;
            char output[512];

            if (scanf("%d", &number) != 1) {{
                return 1;
            }}

            solve(number, output, sizeof(output));
            printf("%s\\n", output);
            return 0;
        }}
        """
    )


def source_weighted_average(meta: dict, solved: bool = False) -> str:
    body = render_solution(
        meta,
        """
        // TODO: implemente a logica deste exercicio.
        (void)grade1;
        (void)weight1;
        (void)grade2;
        (void)weight2;
        (void)grade3;
        (void)weight3;
        return 0.0;
        """,
    ) if solved else render_scaffold(
        """
        // TODO: implemente a logica deste exercicio.
        (void)grade1;
        (void)weight1;
        (void)grade2;
        (void)weight2;
        (void)grade3;
        (void)weight3;
        return 0.0;
        """
    )
    return common_header() + dedent(
        f"""\
        double solve(double grade1, double weight1, double grade2, double weight2, double grade3, double weight3) {{
{body}
        }}

        void run_tests(void) {{
            TestCase cases[] = {{
        {render_cases(meta["cases"])}
            }};
            int total = (int)(sizeof(cases) / sizeof(cases[0]));

            for (int i = 0; i < total; i++) {{
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
            }}
        }}

        int main(int argc, char *argv[]) {{
            if (argc > 1 && strcmp(argv[1], "--test") == 0) {{
                run_tests();
                return 0;
            }}

            double grade1 = 0.0;
            double weight1 = 0.0;
            double grade2 = 0.0;
            double weight2 = 0.0;
            double grade3 = 0.0;
            double weight3 = 0.0;

            if (scanf("%lf %lf %lf %lf %lf %lf", &grade1, &weight1, &grade2, &weight2, &grade3, &weight3) != 6) {{
                return 1;
            }}

            printf("%.2f\\n", solve(grade1, weight1, grade2, weight2, grade3, weight3));
            return 0;
        }}
        """
    )


def source_unary_int(meta: dict, solved: bool = False) -> str:
    body = render_solution(
        meta,
        """
        // TODO: implemente a logica deste exercicio.
        (void)value;
        return 0;
        """,
    ) if solved else render_scaffold(
        """
        // TODO: implemente a logica deste exercicio.
        (void)value;
        return 0;
        """
    )
    return common_header() + dedent(
        f"""\
        int solve(int value) {{
{body}
        }}

        void run_tests(void) {{
            TestCase cases[] = {{
        {render_cases(meta["cases"])}
            }};
            int total = (int)(sizeof(cases) / sizeof(cases[0]));

            for (int i = 0; i < total; i++) {{
                int value = 0;
                char actual[64];

                sscanf(cases[i].input, "%d", &value);
                snprintf(actual, sizeof(actual), "%d", solve(value));
                print_test_result(i + 1, cases[i].input, cases[i].expected, actual);
            }}
        }}

        int main(int argc, char *argv[]) {{
            if (argc > 1 && strcmp(argv[1], "--test") == 0) {{
                run_tests();
                return 0;
            }}

            int value = 0;

            if (scanf("%d", &value) != 1) {{
                return 1;
            }}

            printf("%d\\n", solve(value));
            return 0;
        }}
        """
    )


def source_unary_ull(meta: dict, solved: bool = False) -> str:
    body = render_solution(
        meta,
        """
        // TODO: implemente a logica deste exercicio.
        (void)value;
        return 0ULL;
        """,
    ) if solved else render_scaffold(
        """
        // TODO: implemente a logica deste exercicio.
        (void)value;
        return 0ULL;
        """
    )
    return common_header() + dedent(
        f"""\
        unsigned long long solve(int value) {{
{body}
        }}

        void run_tests(void) {{
            TestCase cases[] = {{
        {render_cases(meta["cases"])}
            }};
            int total = (int)(sizeof(cases) / sizeof(cases[0]));

            for (int i = 0; i < total; i++) {{
                int value = 0;
                char actual[64];

                sscanf(cases[i].input, "%d", &value);
                snprintf(actual, sizeof(actual), "%llu", solve(value));
                print_test_result(i + 1, cases[i].input, cases[i].expected, actual);
            }}
        }}

        int main(int argc, char *argv[]) {{
            if (argc > 1 && strcmp(argv[1], "--test") == 0) {{
                run_tests();
                return 0;
            }}

            int value = 0;

            if (scanf("%d", &value) != 1) {{
                return 1;
            }}

            printf("%llu\\n", solve(value));
            return 0;
        }}
        """
    )


PT_BR_SOLUTIONS = {
    "01_sum_two_numbers": """
    // Some os dois numeros e guarde o resultado em uma nova variavel.
    int sum = a + b;

    // Devolva a resposta final para a funcao principal.
    return sum;
    """,
    "02_subtract_two_numbers": """
    // Subtraia o segundo numero do primeiro.
    int difference = a - b;

    // Retorne o resultado da subtracao.
    return difference;
    """,
    "03_predecessor_successor": """
    // O antecessor e uma unidade menor que o numero original.
    *first = number - 1;

    // O sucessor e uma unidade maior que o numero original.
    *second = number + 1;
    """,
    "04_average_of_three": """
    // Primeiro some os tres valores.
    double sum = a + b + c;

    // Depois divida por 3.0 para manter o resultado como decimal.
    double average = sum / 3.0;

    // Retorne a media final.
    return average;
    """,
    "05_rectangle_area_perimeter": """
    // A area e largura multiplicada pela altura.
    *area = width * height;

    // O perimetro e a soma dos quatro lados.
    *perimeter = 2 * width + 2 * height;
    """,
    "06_circle_area": """
    // Guarde PI em uma constante para deixar a formula mais clara.
    const double pi = 3.14159;

    // A area do circulo e PI vezes o raio ao quadrado.
    double area = pi * value * value;

    // Retorne a area calculada.
    return area;
    """,
    "07_celsius_to_fahrenheit": """
    // Multiplique Celsius por 9.
    double scaled = value * 9.0;

    // Divida por 5 para completar a fracao 9/5.
    double converted = scaled / 5.0;

    // Some 32 para mudar da escala Celsius para Fahrenheit.
    double fahrenheit = converted + 32.0;

    // Retorne a temperatura convertida.
    return fahrenheit;
    """,
    "08_fahrenheit_to_celsius": """
    // Subtraia 32 primeiro porque Fahrenheit comeca 32 graus acima de Celsius.
    double adjusted = value - 32.0;

    // Multiplique por 5 e divida por 9 para converter a escala.
    double celsius = adjusted * 5.0 / 9.0;

    // Retorne a temperatura convertida.
    return celsius;
    """,
    "09_seconds_to_hms": """
    // As horas inteiras aparecem ao dividir por 3600.
    *hours = total_seconds / 3600;

    // Os segundos restantes sao o que sobra depois de tirar as horas.
    int remaining_seconds = total_seconds % 3600;

    // Os minutos inteiros saem dos segundos restantes.
    *minutes = remaining_seconds / 60;

    // Os ultimos segundos restantes completam a resposta.
    *seconds = remaining_seconds % 60;
    """,
    "10_even_or_odd": """
    // Quando o resto da divisao por 2 e 0, o numero e par.
    if (value % 2 == 0) {
        return "EVEN";
    }

    // Caso contrario, o numero e impar.
    return "ODD";
    """,
    "11_sign_of_number": """
    // Verifique se o numero e maior que zero.
    if (value > 0) {
        return "POSITIVE";
    }

    // Verifique se o numero e menor que zero.
    if (value < 0) {
        return "NEGATIVE";
    }

    // Se nao for maior nem menor, entao ele e zero.
    return "ZERO";
    """,
    "12_greater_of_two": """
    // Se o primeiro valor for maior ou igual ao segundo, mantenha ele.
    if (a >= b) {
        return a;
    }

    // Caso contrario, o segundo valor e o maior.
    return b;
    """,
    "13_greatest_of_three": """
    // Comece assumindo que o primeiro numero e o maior.
    int greatest = a;

    // Troque se o segundo numero for maior.
    if (b > greatest) {
        greatest = b;
    }

    // Troque novamente se o terceiro numero for maior que o atual.
    if (c > greatest) {
        greatest = c;
    }

    // Retorne o maior numero encontrado.
    return greatest;
    """,
    "14_simple_interest": """
    // Multiplique capital, taxa e tempo seguindo a formula.
    double raw_interest = principal * rate * time;

    // Divida por 100 porque a taxa foi informada em porcentagem.
    double interest = raw_interest / 100.0;

    // Retorne o valor do juros simples.
    return interest;
    """,
    "15_salary_bonus": """
    // Calcule quanto dinheiro o bonus adiciona ao salario.
    double bonus_value = amount * percentage / 100.0;

    // Some o bonus ao salario original.
    double final_salary = amount + bonus_value;

    // Retorne o novo salario.
    return final_salary;
    """,
    "16_discount_price": """
    // Calcule quanto dinheiro sera retirado do preco original.
    double discount_value = amount * percentage / 100.0;

    // Subtraia o desconto do preco original.
    double final_price = amount - discount_value;

    // Retorne o preco com desconto.
    return final_price;
    """,
    "17_multiplication_table": """
    // Guarde a posicao onde o proximo texto sera escrito dentro da string.
    size_t used = 0;

    // Repita de 1 ate 10 para montar a tabuada inteira.
    for (int i = 1; i <= 10; i++) {
        // Calcule o resultado da multiplicacao da linha atual.
        int result = number * i;

        // Adicione uma linha ao buffer de saida.
        int written = snprintf(
            output + used,
            output_size - used,
            i == 1 ? "%d x %d = %d" : "\\n%d x %d = %d",
            number,
            i,
            result
        );

        // Avance a posicao de escrita para a proxima linha.
        used += (size_t)written;
    }
    """,
    "18_weighted_average": """
    // Multiplique cada nota pelo seu peso.
    double weighted_sum =
        grade1 * weight1 +
        grade2 * weight2 +
        grade3 * weight3;

    // Some os pesos para saber o peso total.
    double total_weight = weight1 + weight2 + weight3;

    // Divida a soma ponderada pelo peso total.
    double average = weighted_sum / total_weight;

    // Retorne a media ponderada.
    return average;
    """,
    "19_swap_two_numbers": """
    // Coloque o segundo valor de entrada na primeira saida.
    *first_output = second_input;

    // Coloque o primeiro valor de entrada na segunda saida.
    *second_output = first_input;
    """,
    "20_remainder_of_division": """
    // O operador de resto mostra o que sobra depois da divisao.
    int remainder = a % b;

    // Retorne o resto.
    return remainder;
    """,
    "21_factorial": """
    // Comece com 1 porque multiplicar por 1 nao altera o resultado.
    unsigned long long factorial = 1ULL;

    // Multiplique todos os numeros de 1 ate o valor informado.
    for (int i = 1; i <= value; i++) {
        factorial *= (unsigned long long)i;
    }

    // Retorne o fatorial.
    return factorial;
    """,
    "22_fibonacci": """
    // Trate diretamente os dois primeiros numeros de Fibonacci.
    if (value == 0) {
        return 0;
    }
    if (value == 1) {
        return 1;
    }

    // Comece em F(0) e F(1).
    int previous = 0;
    int current = 1;

    // Monte a sequencia ate chegar na posicao pedida.
    for (int i = 2; i <= value; i++) {
        int next = previous + current;
        previous = current;
        current = next;
    }

    // Agora a variavel current guarda F(value).
    return current;
    """,
    "23_sum_1_to_n": """
    // Comece o acumulador em zero.
    int sum = 0;

    // Some todos os inteiros de 1 ate o valor informado.
    for (int i = 1; i <= value; i++) {
        sum += i;
    }

    // Retorne a soma total.
    return sum;
    """,
    "24_count_digits": """
    // O numero 0 e um caso especial porque ele ainda possui um digito.
    if (value == 0) {
        return 1;
    }

    // Conte quantas vezes conseguimos remover o ultimo digito.
    int digits = 0;
    int current = value;

    while (current > 0) {
        digits++;
        current /= 10;
    }

    // Retorne a quantidade de digitos contada.
    return digits;
    """,
    "25_power_loop": """
    // Qualquer numero elevado a zero resulta em 1.
    int result = 1;

    // Multiplique pela base a quantidade de vezes indicada pelo expoente.
    for (int i = 0; i < b; i++) {
        result *= a;
    }

    // Retorne o resultado final da potencia.
    return result;
    """,
}


PATTERN_BUILDERS = {
    "int_binary": source_int_binary,
    "unary_pair": source_unary_pair,
    "average_of_three": source_average_of_three,
    "int_ternary": source_int_ternary,
    "unary_int": source_unary_int,
    "unary_ull": source_unary_ull,
    "rectangle": source_rectangle,
    "double_unary": source_double_unary,
    "seconds_to_hms": source_seconds_to_hms,
    "text_from_int": source_text_from_int,
    "simple_interest": source_simple_interest,
    "binary_percentage": source_binary_percentage,
    "multiplication_table": source_table,
    "weighted_average": source_weighted_average,
    "int_pair_from_binary": source_int_pair_from_binary,
}


EXERCISES = [
    {
        "slug": "01_sum_two_numbers",
        "title": "01 - Sum Two Numbers",
        "concepts": "reading integers, addition, formatted output",
        "statement": "Read two integers and print their sum.",
        "input_format": "Two integers separated by a space.",
        "output_format": "One integer: the sum.",
        "example_input": "7 5",
        "example_output": "12",
        "pattern": "int_binary",
        "todo": "return the sum of a and b.",
        "printf_format": "%d",
        "cases": [
            ("0 0", "0"),
            ("2 3", "5"),
            ("10 15", "25"),
            ("-5 7", "2"),
            ("100 200", "300"),
            ("-10 -20", "-30"),
            ("999 1", "1000"),
            ("42 -42", "0"),
            ("123 456", "579"),
            ("-100 50", "-50"),
        ],
    },
    {
        "slug": "02_subtract_two_numbers",
        "title": "02 - Subtract Two Numbers",
        "concepts": "reading integers, subtraction, formatted output",
        "statement": "Read two integers and print the result of the first minus the second.",
        "input_format": "Two integers separated by a space.",
        "output_format": "One integer: the subtraction result.",
        "example_input": "9 4",
        "example_output": "5",
        "pattern": "int_binary",
        "todo": "return the result of a minus b.",
        "printf_format": "%d",
        "cases": [
            ("5 3", "2"),
            ("10 10", "0"),
            ("0 7", "-7"),
            ("-5 -2", "-3"),
            ("100 25", "75"),
            ("3 9", "-6"),
            ("50 -10", "60"),
            ("-8 5", "-13"),
            ("999 1", "998"),
            ("1 999", "-998"),
        ],
    },
    {
        "slug": "03_predecessor_successor",
        "title": "03 - Predecessor and Successor",
        "concepts": "integers, addition, subtraction",
        "statement": "Read an integer and print its predecessor and successor.",
        "input_format": "One integer.",
        "output_format": "Two integers separated by a space: predecessor successor.",
        "example_input": "10",
        "example_output": "9 11",
        "pattern": "unary_pair",
        "todo": "set first to the predecessor of number and second to the successor of number.",
        "printf_format": "%d %d",
        "cases": [
            ("0", "-1 1"),
            ("1", "0 2"),
            ("-5", "-6 -4"),
            ("10", "9 11"),
            ("100", "99 101"),
            ("-1", "-2 0"),
            ("42", "41 43"),
            ("999", "998 1000"),
            ("-100", "-101 -99"),
            ("7", "6 8"),
        ],
    },
    {
        "slug": "04_average_of_three",
        "title": "04 - Average of Three Numbers",
        "concepts": "floating-point numbers, addition, division",
        "statement": "Read three numbers and print their arithmetic average with two decimal places.",
        "input_format": "Three numbers separated by spaces.",
        "output_format": "One number with two decimal places.",
        "example_input": "4 5 6",
        "example_output": "5.00",
        "pattern": "average_of_three",
        "todo": "return the arithmetic average of a, b, and c.",
        "cases": [
            ("1 2 3", "2.00"),
            ("10 20 30", "20.00"),
            ("5 5 5", "5.00"),
            ("0 0 10", "3.33"),
            ("2.5 3.5 4.5", "3.50"),
            ("-5 5 10", "3.33"),
            ("7 8.5 9", "8.17"),
            ("100 50 25", "58.33"),
            ("1.2 3.4 5.6", "3.40"),
            ("9.9 0.1 5", "5.00"),
        ],
    },
    {
        "slug": "05_rectangle_area_perimeter",
        "title": "05 - Rectangle Area and Perimeter",
        "concepts": "multiplication, addition, geometry basics",
        "statement": "Read the width and height of a rectangle and print its area and perimeter.",
        "input_format": "Two integers: width and height.",
        "output_format": "Two integers separated by a space: area perimeter.",
        "example_input": "5 3",
        "example_output": "15 16",
        "pattern": "rectangle",
        "todo": "set area to width multiplied by height and perimeter to two times width plus two times height.",
        "cases": [
            ("1 1", "1 4"),
            ("2 3", "6 10"),
            ("5 10", "50 30"),
            ("7 4", "28 22"),
            ("9 9", "81 36"),
            ("12 5", "60 34"),
            ("15 2", "30 34"),
            ("8 6", "48 28"),
            ("20 1", "20 42"),
            ("11 13", "143 48"),
        ],
    },
    {
        "slug": "06_circle_area",
        "title": "06 - Circle Area",
        "concepts": "floating-point numbers, multiplication, constants",
        "statement": "Read the radius of a circle and print its area using PI = 3.14159.",
        "input_format": "One number: the radius.",
        "output_format": "One number with two decimal places.",
        "example_input": "2",
        "example_output": "12.57",
        "pattern": "double_unary",
        "todo": "return the area of the circle using PI = 3.14159.",
        "cases": [
            ("0", "0.00"),
            ("1", "3.14"),
            ("2", "12.57"),
            ("2.5", "19.63"),
            ("3", "28.27"),
            ("4.2", "55.42"),
            ("5", "78.54"),
            ("7.1", "158.37"),
            ("10", "314.16"),
            ("12.3", "475.29"),
        ],
    },
    {
        "slug": "07_celsius_to_fahrenheit",
        "title": "07 - Celsius to Fahrenheit",
        "concepts": "unit conversion, multiplication, division, addition",
        "statement": "Read a temperature in Celsius and convert it to Fahrenheit.",
        "input_format": "One number: the temperature in Celsius.",
        "output_format": "One number with two decimal places.",
        "example_input": "25",
        "example_output": "77.00",
        "pattern": "double_unary",
        "todo": "return the Fahrenheit temperature equivalent to value in Celsius.",
        "cases": [
            ("0", "32.00"),
            ("10", "50.00"),
            ("25", "77.00"),
            ("37", "98.60"),
            ("100", "212.00"),
            ("-40", "-40.00"),
            ("15.5", "59.90"),
            ("-10.5", "13.10"),
            ("5", "41.00"),
            ("42.2", "107.96"),
        ],
    },
    {
        "slug": "08_fahrenheit_to_celsius",
        "title": "08 - Fahrenheit to Celsius",
        "concepts": "unit conversion, subtraction, multiplication, division",
        "statement": "Read a temperature in Fahrenheit and convert it to Celsius.",
        "input_format": "One number: the temperature in Fahrenheit.",
        "output_format": "One number with two decimal places.",
        "example_input": "77",
        "example_output": "25.00",
        "pattern": "double_unary",
        "todo": "return the Celsius temperature equivalent to value in Fahrenheit.",
        "cases": [
            ("32", "0.00"),
            ("50", "10.00"),
            ("77", "25.00"),
            ("98.6", "37.00"),
            ("212", "100.00"),
            ("-40", "-40.00"),
            ("59.9", "15.50"),
            ("13.1", "-10.50"),
            ("41", "5.00"),
            ("107.96", "42.20"),
        ],
    },
    {
        "slug": "09_seconds_to_hms",
        "title": "09 - Seconds to Hours, Minutes, and Seconds",
        "concepts": "integer division, remainder, decomposition",
        "statement": "Read a total number of seconds and convert it to hours, minutes, and seconds.",
        "input_format": "One integer: total seconds.",
        "output_format": "Three integers separated by spaces: hours minutes seconds.",
        "example_input": "3661",
        "example_output": "1 1 1",
        "pattern": "seconds_to_hms",
        "todo": "convert total_seconds into whole hours, remaining minutes, and remaining seconds.",
        "cases": [
            ("0", "0 0 0"),
            ("59", "0 0 59"),
            ("60", "0 1 0"),
            ("61", "0 1 1"),
            ("3599", "0 59 59"),
            ("3600", "1 0 0"),
            ("3661", "1 1 1"),
            ("7325", "2 2 5"),
            ("86399", "23 59 59"),
            ("10000", "2 46 40"),
        ],
    },
    {
        "slug": "10_even_or_odd",
        "title": "10 - Even or Odd",
        "concepts": "conditions, remainder operator",
        "statement": "Read an integer and print EVEN if it is even, or ODD if it is odd.",
        "input_format": "One integer.",
        "output_format": "The word EVEN or ODD.",
        "example_input": "7",
        "example_output": "ODD",
        "pattern": "text_from_int",
        "todo": 'return "EVEN" when value is even, otherwise return "ODD".',
        "cases": [
            ("0", "EVEN"),
            ("1", "ODD"),
            ("2", "EVEN"),
            ("7", "ODD"),
            ("-4", "EVEN"),
            ("-9", "ODD"),
            ("42", "EVEN"),
            ("99", "ODD"),
            ("100", "EVEN"),
            ("-101", "ODD"),
        ],
    },
    {
        "slug": "11_sign_of_number",
        "title": "11 - Sign of a Number",
        "concepts": "conditions, comparisons",
        "statement": "Read an integer and print POSITIVE, NEGATIVE, or ZERO.",
        "input_format": "One integer.",
        "output_format": "One of these words: POSITIVE, NEGATIVE, ZERO.",
        "example_input": "-8",
        "example_output": "NEGATIVE",
        "pattern": "text_from_int",
        "todo": 'return "POSITIVE", "NEGATIVE", or "ZERO" according to the sign of value.',
        "cases": [
            ("-5", "NEGATIVE"),
            ("0", "ZERO"),
            ("7", "POSITIVE"),
            ("-1", "NEGATIVE"),
            ("1", "POSITIVE"),
            ("100", "POSITIVE"),
            ("-100", "NEGATIVE"),
            ("999", "POSITIVE"),
            ("-42", "NEGATIVE"),
            ("5", "POSITIVE"),
        ],
    },
    {
        "slug": "12_greater_of_two",
        "title": "12 - Greater of Two Numbers",
        "concepts": "conditions, comparisons",
        "statement": "Read two integers and print the greater one. If they are equal, print that value.",
        "input_format": "Two integers separated by a space.",
        "output_format": "One integer.",
        "example_input": "12 7",
        "example_output": "12",
        "pattern": "int_binary",
        "todo": "return the greater value between a and b. If they are equal, return either one.",
        "printf_format": "%d",
        "cases": [
            ("5 3", "5"),
            ("10 10", "10"),
            ("-1 -5", "-1"),
            ("7 20", "20"),
            ("0 8", "8"),
            ("100 99", "100"),
            ("-10 10", "10"),
            ("42 24", "42"),
            ("500 1000", "1000"),
            ("-3 -3", "-3"),
        ],
    },
    {
        "slug": "13_greatest_of_three",
        "title": "13 - Greatest of Three Numbers",
        "concepts": "conditions, comparisons",
        "statement": "Read three integers and print the greatest value.",
        "input_format": "Three integers separated by spaces.",
        "output_format": "One integer.",
        "example_input": "3 9 4",
        "example_output": "9",
        "pattern": "int_ternary",
        "todo": "return the greatest value among a, b, and c.",
        "cases": [
            ("1 2 3", "3"),
            ("10 5 8", "10"),
            ("-1 -2 -3", "-1"),
            ("7 7 2", "7"),
            ("0 0 0", "0"),
            ("100 50 150", "150"),
            ("9 12 11", "12"),
            ("-5 20 3", "20"),
            ("42 24 36", "42"),
            ("500 1000 750", "1000"),
        ],
    },
    {
        "slug": "14_simple_interest",
        "title": "14 - Simple Interest",
        "concepts": "percentages, multiplication, division",
        "statement": "Read principal, annual rate, and time, then print the simple interest using the formula principal * rate * time / 100.",
        "input_format": "Three numbers: principal rate time.",
        "output_format": "One number with two decimal places.",
        "example_input": "1000 5 2",
        "example_output": "100.00",
        "pattern": "simple_interest",
        "todo": "return the simple interest calculated from principal, rate, and time.",
        "cases": [
            ("1000 5 2", "100.00"),
            ("1500 10 1", "150.00"),
            ("200 3 4", "24.00"),
            ("5000 7.5 3", "1125.00"),
            ("750 12 2", "180.00"),
            ("100 1 1", "1.00"),
            ("3500 8 0.5", "140.00"),
            ("999.99 6 1", "60.00"),
            ("250 2.5 8", "50.00"),
            ("4200 4 5", "840.00"),
        ],
    },
    {
        "slug": "15_salary_bonus",
        "title": "15 - Salary Bonus",
        "concepts": "percentages, addition",
        "statement": "Read a base salary and a bonus percentage, then print the final salary after applying the bonus.",
        "input_format": "Two numbers: salary bonus_percentage.",
        "output_format": "One number with two decimal places.",
        "example_input": "2000 10",
        "example_output": "2200.00",
        "pattern": "binary_percentage",
        "todo": "return the salary after increasing amount by percentage percent.",
        "cases": [
            ("1000 10", "1100.00"),
            ("2500 5", "2625.00"),
            ("3200 12.5", "3600.00"),
            ("1500 0", "1500.00"),
            ("999.99 8", "1079.99"),
            ("5000 20", "6000.00"),
            ("780 15", "897.00"),
            ("2300 7.5", "2472.50"),
            ("4100 3", "4223.00"),
            ("1200 18", "1416.00"),
        ],
    },
    {
        "slug": "16_discount_price",
        "title": "16 - Discount Price",
        "concepts": "percentages, subtraction",
        "statement": "Read the original price and a discount percentage, then print the final price after the discount.",
        "input_format": "Two numbers: price discount_percentage.",
        "output_format": "One number with two decimal places.",
        "example_input": "80 25",
        "example_output": "60.00",
        "pattern": "binary_percentage",
        "todo": "return the price after decreasing amount by percentage percent.",
        "cases": [
            ("100 10", "90.00"),
            ("250 5", "237.50"),
            ("399.90 12", "351.91"),
            ("1500 0", "1500.00"),
            ("999.99 8", "919.99"),
            ("80 25", "60.00"),
            ("45.50 10", "40.95"),
            ("230 7.5", "212.75"),
            ("4100 3", "3977.00"),
            ("1200 18", "984.00"),
        ],
    },
    {
        "slug": "17_multiplication_table",
        "title": "17 - Multiplication Table",
        "concepts": "loops, multiplication, formatted output",
        "statement": "Read an integer and print its multiplication table from 1 to 10, one line per result.",
        "input_format": "One integer.",
        "output_format": "Ten lines in the format number x i = result.",
        "example_input": "3",
        "example_output": "3 x 1 = 3\n3 x 2 = 6\n3 x 3 = 9\n3 x 4 = 12\n3 x 5 = 15\n3 x 6 = 18\n3 x 7 = 21\n3 x 8 = 24\n3 x 9 = 27\n3 x 10 = 30",
        "pattern": "multiplication_table",
        "todo": "write the multiplication table from 1 to 10 into output.",
        "cases": [
            ("1", "1 x 1 = 1\n1 x 2 = 2\n1 x 3 = 3\n1 x 4 = 4\n1 x 5 = 5\n1 x 6 = 6\n1 x 7 = 7\n1 x 8 = 8\n1 x 9 = 9\n1 x 10 = 10"),
            ("2", "2 x 1 = 2\n2 x 2 = 4\n2 x 3 = 6\n2 x 4 = 8\n2 x 5 = 10\n2 x 6 = 12\n2 x 7 = 14\n2 x 8 = 16\n2 x 9 = 18\n2 x 10 = 20"),
            ("3", "3 x 1 = 3\n3 x 2 = 6\n3 x 3 = 9\n3 x 4 = 12\n3 x 5 = 15\n3 x 6 = 18\n3 x 7 = 21\n3 x 8 = 24\n3 x 9 = 27\n3 x 10 = 30"),
            ("5", "5 x 1 = 5\n5 x 2 = 10\n5 x 3 = 15\n5 x 4 = 20\n5 x 5 = 25\n5 x 6 = 30\n5 x 7 = 35\n5 x 8 = 40\n5 x 9 = 45\n5 x 10 = 50"),
            ("7", "7 x 1 = 7\n7 x 2 = 14\n7 x 3 = 21\n7 x 4 = 28\n7 x 5 = 35\n7 x 6 = 42\n7 x 7 = 49\n7 x 8 = 56\n7 x 9 = 63\n7 x 10 = 70"),
            ("9", "9 x 1 = 9\n9 x 2 = 18\n9 x 3 = 27\n9 x 4 = 36\n9 x 5 = 45\n9 x 6 = 54\n9 x 7 = 63\n9 x 8 = 72\n9 x 9 = 81\n9 x 10 = 90"),
            ("10", "10 x 1 = 10\n10 x 2 = 20\n10 x 3 = 30\n10 x 4 = 40\n10 x 5 = 50\n10 x 6 = 60\n10 x 7 = 70\n10 x 8 = 80\n10 x 9 = 90\n10 x 10 = 100"),
            ("11", "11 x 1 = 11\n11 x 2 = 22\n11 x 3 = 33\n11 x 4 = 44\n11 x 5 = 55\n11 x 6 = 66\n11 x 7 = 77\n11 x 8 = 88\n11 x 9 = 99\n11 x 10 = 110"),
            ("12", "12 x 1 = 12\n12 x 2 = 24\n12 x 3 = 36\n12 x 4 = 48\n12 x 5 = 60\n12 x 6 = 72\n12 x 7 = 84\n12 x 8 = 96\n12 x 9 = 108\n12 x 10 = 120"),
            ("-4", "-4 x 1 = -4\n-4 x 2 = -8\n-4 x 3 = -12\n-4 x 4 = -16\n-4 x 5 = -20\n-4 x 6 = -24\n-4 x 7 = -28\n-4 x 8 = -32\n-4 x 9 = -36\n-4 x 10 = -40"),
        ],
    },
    {
        "slug": "18_weighted_average",
        "title": "18 - Weighted Average",
        "concepts": "floating-point numbers, multiplication, division",
        "statement": "Read three grades and their weights, then print the weighted average with two decimal places.",
        "input_format": "Six numbers: grade1 weight1 grade2 weight2 grade3 weight3.",
        "output_format": "One number with two decimal places.",
        "example_input": "7 2 8 3 9 5",
        "example_output": "8.30",
        "pattern": "weighted_average",
        "todo": "return the weighted average of the three grades.",
        "cases": [
            ("7 2 8 3 9 5", "8.30"),
            ("10 1 10 1 10 1", "10.00"),
            ("5 1 6 1 7 1", "6.00"),
            ("4.5 2 7.5 3 8 5", "7.15"),
            ("0 2 10 3 5 5", "5.50"),
            ("9 4 8 3 7 3", "8.10"),
            ("6.5 2 7.5 2 8.5 6", "7.90"),
            ("3 5 4 2 10 3", "5.30"),
            ("1.2 1 3.4 2 5.6 3", "4.13"),
            ("8 5 9 2 10 3", "8.80"),
        ],
    },
    {
        "slug": "19_swap_two_numbers",
        "title": "19 - Swap Two Numbers",
        "concepts": "variables, assignments",
        "statement": "Read two integers and print them in the opposite order.",
        "input_format": "Two integers separated by a space.",
        "output_format": "Two integers separated by a space: second first.",
        "example_input": "4 9",
        "example_output": "9 4",
        "pattern": "int_pair_from_binary",
        "todo": "set first_output to second_input and second_output to first_input.",
        "printf_format": "%d %d",
        "cases": [
            ("1 2", "2 1"),
            ("5 10", "10 5"),
            ("-3 7", "7 -3"),
            ("0 0", "0 0"),
            ("100 50", "50 100"),
            ("-10 -20", "-20 -10"),
            ("42 24", "24 42"),
            ("999 1", "1 999"),
            ("8 -8", "-8 8"),
            ("123 456", "456 123"),
        ],
    },
    {
        "slug": "20_remainder_of_division",
        "title": "20 - Remainder of Division",
        "concepts": "integer division, remainder operator",
        "statement": "Read two integers and print the remainder of the first divided by the second.",
        "input_format": "Two integers separated by a space. The second value is never zero in the tests.",
        "output_format": "One integer: the remainder.",
        "example_input": "10 3",
        "example_output": "1",
        "pattern": "int_binary",
        "todo": "return the remainder of a divided by b.",
        "printf_format": "%d",
        "cases": [
            ("10 3", "1"),
            ("20 5", "0"),
            ("7 2", "1"),
            ("99 10", "9"),
            ("100 6", "4"),
            ("55 4", "3"),
            ("81 8", "1"),
            ("123 7", "4"),
            ("1000 9", "1"),
            ("42 11", "9"),
        ],
    },
    {
        "slug": "21_factorial",
        "title": "21 - Factorial",
        "concepts": "loops, multiplication, accumulation",
        "statement": "Read a non-negative integer n and print n!.",
        "input_format": "One integer n, where n is non-negative.",
        "output_format": "One integer: the factorial of n.",
        "example_input": "5",
        "example_output": "120",
        "pattern": "unary_ull",
        "todo": "use a loop to calculate the factorial of value.",
        "cases": [
            ("0", "1"),
            ("1", "1"),
            ("2", "2"),
            ("3", "6"),
            ("4", "24"),
            ("5", "120"),
            ("6", "720"),
            ("7", "5040"),
            ("10", "3628800"),
            ("12", "479001600"),
        ],
    },
    {
        "slug": "22_fibonacci",
        "title": "22 - Fibonacci Number",
        "concepts": "loops, sequence generation, variables",
        "statement": "Read an integer n and print the nth Fibonacci number, considering F(0) = 0 and F(1) = 1.",
        "input_format": "One integer n, where n is non-negative.",
        "output_format": "One integer: the nth Fibonacci number.",
        "example_input": "7",
        "example_output": "13",
        "pattern": "unary_int",
        "todo": "use a loop to return the nth Fibonacci number.",
        "cases": [
            ("0", "0"),
            ("1", "1"),
            ("2", "1"),
            ("3", "2"),
            ("4", "3"),
            ("5", "5"),
            ("6", "8"),
            ("7", "13"),
            ("10", "55"),
            ("15", "610"),
        ],
    },
    {
        "slug": "23_sum_1_to_n",
        "title": "23 - Sum From 1 to N",
        "concepts": "loops, accumulation, integers",
        "statement": "Read a positive integer n and print the sum of all integers from 1 to n.",
        "input_format": "One positive integer n.",
        "output_format": "One integer: the sum from 1 to n.",
        "example_input": "5",
        "example_output": "15",
        "pattern": "unary_int",
        "todo": "use a loop to sum all integers from 1 to value.",
        "cases": [
            ("1", "1"),
            ("2", "3"),
            ("3", "6"),
            ("4", "10"),
            ("5", "15"),
            ("10", "55"),
            ("20", "210"),
            ("50", "1275"),
            ("100", "5050"),
            ("25", "325"),
        ],
    },
    {
        "slug": "24_count_digits",
        "title": "24 - Count Digits",
        "concepts": "loops, integer division, conditions",
        "statement": "Read a non-negative integer and print how many digits it has. The number 0 has 1 digit.",
        "input_format": "One non-negative integer.",
        "output_format": "One integer: the number of digits.",
        "example_input": "4502",
        "example_output": "4",
        "pattern": "unary_int",
        "todo": "use a loop to count how many digits value has.",
        "cases": [
            ("0", "1"),
            ("7", "1"),
            ("10", "2"),
            ("99", "2"),
            ("100", "3"),
            ("4502", "4"),
            ("99999", "5"),
            ("123456", "6"),
            ("1000000", "7"),
            ("2147483647", "10"),
        ],
    },
    {
        "slug": "25_power_loop",
        "title": "25 - Integer Power",
        "concepts": "loops, multiplication, repeated operations",
        "statement": "Read an integer base and a non-negative integer exponent, then print base raised to exponent using a loop.",
        "input_format": "Two integers separated by a space: base exponent.",
        "output_format": "One integer: base^exponent.",
        "example_input": "2 5",
        "example_output": "32",
        "pattern": "int_binary",
        "todo": "use a loop to return a raised to the power of b.",
        "printf_format": "%d",
        "cases": [
            ("2 0", "1"),
            ("2 1", "2"),
            ("2 5", "32"),
            ("3 4", "81"),
            ("5 3", "125"),
            ("10 2", "100"),
            ("7 1", "7"),
            ("1 9", "1"),
            ("0 5", "0"),
            ("4 4", "256"),
        ],
    },
]


PT_BR_DESCRIPTIONS = {
    "01_sum_two_numbers": {
        "title": "01 - Soma de Dois Numeros",
        "goal": "Leia dois inteiros e imprima a soma entre eles.",
        "concepts": "leitura de inteiros, adicao, saida formatada",
        "input": "Dois inteiros separados por espaco.",
        "output": "Um inteiro: a soma.",
        "example_input": "7 5",
        "example_output": "12",
    },
    "02_subtract_two_numbers": {
        "title": "02 - Subtracao de Dois Numeros",
        "goal": "Leia dois inteiros e imprima o resultado do primeiro menos o segundo.",
        "concepts": "leitura de inteiros, subtracao, saida formatada",
        "input": "Dois inteiros separados por espaco.",
        "output": "Um inteiro: o resultado da subtracao.",
        "example_input": "9 4",
        "example_output": "5",
    },
    "03_predecessor_successor": {
        "title": "03 - Antecessor e Sucessor",
        "goal": "Leia um inteiro e imprima seu antecessor e seu sucessor.",
        "concepts": "inteiros, adicao, subtracao",
        "input": "Um inteiro.",
        "output": "Dois inteiros separados por espaco: antecessor sucessor.",
        "example_input": "10",
        "example_output": "9 11",
    },
    "04_average_of_three": {
        "title": "04 - Media de Tres Numeros",
        "goal": "Leia tres numeros e imprima a media aritmetica com duas casas decimais.",
        "concepts": "numeros de ponto flutuante, adicao, divisao",
        "input": "Tres numeros separados por espacos.",
        "output": "Um numero com duas casas decimais.",
        "example_input": "4 5 6",
        "example_output": "5.00",
    },
    "05_rectangle_area_perimeter": {
        "title": "05 - Area e Perimetro de um Retangulo",
        "goal": "Leia a largura e a altura de um retangulo e imprima sua area e seu perimetro.",
        "concepts": "multiplicacao, adicao, geometria basica",
        "input": "Dois inteiros: largura e altura.",
        "output": "Dois inteiros separados por espaco: area perimetro.",
        "example_input": "5 3",
        "example_output": "15 16",
    },
    "06_circle_area": {
        "title": "06 - Area do Circulo",
        "goal": "Leia o raio de um circulo e imprima sua area usando PI = 3.14159.",
        "concepts": "numeros de ponto flutuante, multiplicacao, constantes",
        "input": "Um numero: o raio.",
        "output": "Um numero com duas casas decimais.",
        "example_input": "2",
        "example_output": "12.57",
    },
    "07_celsius_to_fahrenheit": {
        "title": "07 - Celsius para Fahrenheit",
        "goal": "Leia uma temperatura em Celsius e converta para Fahrenheit.",
        "concepts": "conversao de unidades, multiplicacao, divisao, adicao",
        "input": "Um numero: a temperatura em Celsius.",
        "output": "Um numero com duas casas decimais.",
        "example_input": "25",
        "example_output": "77.00",
    },
    "08_fahrenheit_to_celsius": {
        "title": "08 - Fahrenheit para Celsius",
        "goal": "Leia uma temperatura em Fahrenheit e converta para Celsius.",
        "concepts": "conversao de unidades, subtracao, multiplicacao, divisao",
        "input": "Um numero: a temperatura em Fahrenheit.",
        "output": "Um numero com duas casas decimais.",
        "example_input": "77",
        "example_output": "25.00",
    },
    "09_seconds_to_hms": {
        "title": "09 - Segundos para Horas, Minutos e Segundos",
        "goal": "Leia um total de segundos e converta para horas, minutos e segundos.",
        "concepts": "divisao inteira, resto, decomposicao",
        "input": "Um inteiro: total de segundos.",
        "output": "Tres inteiros separados por espaco: horas minutos segundos.",
        "example_input": "3661",
        "example_output": "1 1 1",
    },
    "10_even_or_odd": {
        "title": "10 - Par ou Impar",
        "goal": "Leia um inteiro e imprima EVEN se ele for par ou ODD se ele for impar.",
        "concepts": "condicionais, operador de resto",
        "input": "Um inteiro.",
        "output": "A palavra EVEN ou ODD.",
        "example_input": "7",
        "example_output": "ODD",
    },
    "11_sign_of_number": {
        "title": "11 - Sinal de um Numero",
        "goal": "Leia um inteiro e imprima POSITIVE, NEGATIVE ou ZERO.",
        "concepts": "condicionais, comparacoes",
        "input": "Um inteiro.",
        "output": "Uma destas palavras: POSITIVE, NEGATIVE, ZERO.",
        "example_input": "-8",
        "example_output": "NEGATIVE",
    },
    "12_greater_of_two": {
        "title": "12 - Maior entre Dois Numeros",
        "goal": "Leia dois inteiros e imprima o maior deles. Se forem iguais, imprima esse valor.",
        "concepts": "condicionais, comparacoes",
        "input": "Dois inteiros separados por espaco.",
        "output": "Um inteiro.",
        "example_input": "12 7",
        "example_output": "12",
    },
    "13_greatest_of_three": {
        "title": "13 - Maior entre Tres Numeros",
        "goal": "Leia tres inteiros e imprima o maior valor.",
        "concepts": "condicionais, comparacoes",
        "input": "Tres inteiros separados por espacos.",
        "output": "Um inteiro.",
        "example_input": "3 9 4",
        "example_output": "9",
    },
    "14_simple_interest": {
        "title": "14 - Juros Simples",
        "goal": "Leia capital, taxa anual e tempo, depois imprima o juros simples usando a formula capital * taxa * tempo / 100.",
        "concepts": "porcentagens, multiplicacao, divisao",
        "input": "Tres numeros: capital taxa tempo.",
        "output": "Um numero com duas casas decimais.",
        "example_input": "1000 5 2",
        "example_output": "100.00",
    },
    "15_salary_bonus": {
        "title": "15 - Salario com Bonus",
        "goal": "Leia um salario base e uma porcentagem de bonus, depois imprima o salario final apos aplicar o bonus.",
        "concepts": "porcentagens, adicao",
        "input": "Dois numeros: salario porcentagem_do_bonus.",
        "output": "Um numero com duas casas decimais.",
        "example_input": "2000 10",
        "example_output": "2200.00",
    },
    "16_discount_price": {
        "title": "16 - Preco com Desconto",
        "goal": "Leia o preco original e uma porcentagem de desconto, depois imprima o preco final apos o desconto.",
        "concepts": "porcentagens, subtracao",
        "input": "Dois numeros: preco porcentagem_de_desconto.",
        "output": "Um numero com duas casas decimais.",
        "example_input": "80 25",
        "example_output": "60.00",
    },
    "17_multiplication_table": {
        "title": "17 - Tabuada",
        "goal": "Leia um inteiro e imprima sua tabuada de 1 ate 10, uma linha por resultado.",
        "concepts": "lacos, multiplicacao, saida formatada",
        "input": "Um inteiro.",
        "output": "Dez linhas no formato number x i = result.",
        "example_input": "3",
        "example_output": "3 x 1 = 3\n3 x 2 = 6\n3 x 3 = 9\n3 x 4 = 12\n3 x 5 = 15\n3 x 6 = 18\n3 x 7 = 21\n3 x 8 = 24\n3 x 9 = 27\n3 x 10 = 30",
    },
    "18_weighted_average": {
        "title": "18 - Media Ponderada",
        "goal": "Leia tres notas e seus pesos, depois imprima a media ponderada com duas casas decimais.",
        "concepts": "numeros de ponto flutuante, multiplicacao, divisao",
        "input": "Seis numeros: nota1 peso1 nota2 peso2 nota3 peso3.",
        "output": "Um numero com duas casas decimais.",
        "example_input": "7 2 8 3 9 5",
        "example_output": "8.30",
    },
    "19_swap_two_numbers": {
        "title": "19 - Troca de Dois Numeros",
        "goal": "Leia dois inteiros e imprima os dois em ordem invertida.",
        "concepts": "variaveis, atribuicoes",
        "input": "Dois inteiros separados por espaco.",
        "output": "Dois inteiros separados por espaco: segundo primeiro.",
        "example_input": "4 9",
        "example_output": "9 4",
    },
    "20_remainder_of_division": {
        "title": "20 - Resto da Divisao",
        "goal": "Leia dois inteiros e imprima o resto da divisao do primeiro pelo segundo.",
        "concepts": "divisao inteira, operador de resto",
        "input": "Dois inteiros separados por espaco. Nos testes, o segundo valor nunca sera zero.",
        "output": "Um inteiro: o resto.",
        "example_input": "10 3",
        "example_output": "1",
    },
    "21_factorial": {
        "title": "21 - Fatorial",
        "goal": "Leia um inteiro nao negativo n e imprima n!.",
        "concepts": "lacos, multiplicacao, acumulacao",
        "input": "Um inteiro n, onde n e nao negativo.",
        "output": "Um inteiro: o fatorial de n.",
        "example_input": "5",
        "example_output": "120",
    },
    "22_fibonacci": {
        "title": "22 - Numero de Fibonacci",
        "goal": "Leia um inteiro n e imprima o enesimo numero de Fibonacci, considerando F(0) = 0 e F(1) = 1.",
        "concepts": "lacos, geracao de sequencia, variaveis",
        "input": "Um inteiro n, onde n e nao negativo.",
        "output": "Um inteiro: o enesimo numero de Fibonacci.",
        "example_input": "7",
        "example_output": "13",
    },
    "23_sum_1_to_n": {
        "title": "23 - Soma de 1 ate N",
        "goal": "Leia um inteiro positivo n e imprima a soma de todos os inteiros de 1 ate n.",
        "concepts": "lacos, acumulacao, inteiros",
        "input": "Um inteiro positivo n.",
        "output": "Um inteiro: a soma de 1 ate n.",
        "example_input": "5",
        "example_output": "15",
    },
    "24_count_digits": {
        "title": "24 - Contar Digitos",
        "goal": "Leia um inteiro nao negativo e imprima quantos digitos ele possui. O numero 0 possui 1 digito.",
        "concepts": "lacos, divisao inteira, condicionais",
        "input": "Um inteiro nao negativo.",
        "output": "Um inteiro: a quantidade de digitos.",
        "example_input": "4502",
        "example_output": "4",
    },
    "25_power_loop": {
        "title": "25 - Potencia Inteira",
        "goal": "Leia um inteiro base e um inteiro nao negativo expoente, depois imprima base elevada a expoente usando um laco.",
        "concepts": "lacos, multiplicacao, operacoes repetidas",
        "input": "Dois inteiros separados por espaco: base expoente.",
        "output": "Um inteiro: base^expoente.",
        "example_input": "2 5",
        "example_output": "32",
    },
}


def render_exercise_readme(meta: dict) -> str:
    return dedent(
        f"""\
        # {meta["title"]}

        **Goal:** {meta["statement"]}

        **Concepts:** {meta["concepts"]}

        **Input**
        {meta["input_format"]}

        **Output**
        {meta["output_format"]}

        **Example input**
        ```text
        {meta["example_input"]}
        ```

        **Example output**
        ```text
        {meta["example_output"]}
        ```

        **How to work on it**
        1. Open `main.c`.
        2. Complete the `solve(...)` function.
        3. Compile with `gcc -Wall -Wextra -std=c11 main.c -o program`.
        4. Run normally with `./program`.
        5. Run the predefined checks with `./program --test`.

        The starter code compiles immediately, but the default `TODO` implementation is incomplete, so the tests will fail until you solve the exercise.
        """
    )


def render_exercise_readme_pt_br(meta: dict) -> str:
    item = PT_BR_DESCRIPTIONS[meta["slug"]]
    exercise_path = f"./exercises/{meta['slug']}"
    implementation_by_pattern = {
        "int_binary": [
            "Na funcao `solve(int a, int b)`, os dois valores de entrada ja chegam prontos pelos parametros `a` e `b`.",
            "Voce deve calcular o resultado pedido no enunciado e retornar um unico valor inteiro com `return`.",
        ],
        "unary_pair": [
            "Na funcao `solve(int number, int *first, int *second)`, o valor de entrada chega pelo parametro `number`.",
            "Voce deve colocar as duas respostas nas variaveis apontadas por `first` e `second`.",
            "Use `*first = ...;` e `*second = ...;` para guardar os resultados.",
        ],
        "average_of_three": [
            "Na funcao `solve(double a, double b, double c)`, os tres valores de entrada ja chegam pelos parametros.",
            "Voce deve calcular o resultado pedido e retornar um valor decimal com `return`.",
            "Voce nao precisa formatar a quantidade de casas decimais dentro de `solve(...)`.",
            "O `main(...)` deste exercicio ja imprime a resposta com duas casas decimais para voce.",
        ],
        "int_ternary": [
            "Na funcao `solve(int a, int b, int c)`, os tres valores de entrada ja chegam pelos parametros.",
            "Voce deve calcular o resultado pedido e retornar um unico valor inteiro com `return`.",
        ],
        "int_pair_from_binary": [
            "Na funcao `solve(int first_input, int second_input, int *first_output, int *second_output)`, os dois valores de entrada chegam pelos dois primeiros parametros.",
            "Voce deve guardar as duas respostas nas variaveis apontadas por `first_output` e `second_output`.",
            "Use `*first_output = ...;` e `*second_output = ...;`.",
        ],
        "rectangle": [
            "Na funcao `solve(int width, int height, int *area, int *perimeter)`, a largura e a altura chegam pelos parametros `width` e `height`.",
            "Voce deve guardar a area em `*area` e o perimetro em `*perimeter`.",
        ],
        "double_unary": [
            "Na funcao `solve(double value)`, o valor de entrada ja chega pelo parametro `value`.",
            "Voce deve calcular o resultado pedido e retornar um valor decimal com `return`.",
            "Voce nao precisa formatar a quantidade de casas decimais dentro de `solve(...)`.",
            "O `main(...)` deste exercicio ja imprime a resposta com duas casas decimais para voce.",
        ],
        "seconds_to_hms": [
            "Na funcao `solve(int total_seconds, int *hours, int *minutes, int *seconds)`, o total de segundos chega em `total_seconds`.",
            "Voce deve separar a resposta e guardar cada parte em `*hours`, `*minutes` e `*seconds`.",
        ],
        "text_from_int": [
            "Na funcao `solve(int value)`, o numero de entrada ja chega pelo parametro `value`.",
            "Voce deve retornar uma string com a resposta, como `\"EVEN\"`, `\"ODD\"`, `\"POSITIVE\"`, `\"NEGATIVE\"` ou `\"ZERO\"`.",
        ],
        "binary_percentage": [
            "Na funcao `solve(double amount, double percentage)`, os valores de entrada ja chegam pelos parametros.",
            "Voce deve calcular o resultado pedido e retornar um valor decimal com `return`.",
            "Voce nao precisa formatar a quantidade de casas decimais dentro de `solve(...)`.",
            "O `main(...)` deste exercicio ja imprime a resposta com duas casas decimais para voce.",
        ],
        "simple_interest": [
            "Na funcao `solve(double principal, double rate, double time)`, os tres valores ja chegam pelos parametros.",
            "Voce deve calcular o juros simples e retornar o resultado com `return`.",
            "Voce nao precisa formatar a quantidade de casas decimais dentro de `solve(...)`.",
            "O `main(...)` deste exercicio ja imprime a resposta com duas casas decimais para voce.",
        ],
        "multiplication_table": [
            "Na funcao `solve(int number, char *output, size_t output_size)`, o numero da tabuada chega em `number`.",
            "Voce deve montar o texto da resposta dentro de `output`, respeitando o tamanho maximo informado por `output_size`.",
            "A resposta final deve ficar pronta para ser impressa exatamente como os testes esperam.",
        ],
        "weighted_average": [
            "Na funcao `solve(...)`, todas as notas e pesos ja chegam pelos parametros.",
            "Voce deve calcular a media ponderada e retornar um valor decimal com `return`.",
            "Voce nao precisa formatar a quantidade de casas decimais dentro de `solve(...)`.",
            "O `main(...)` deste exercicio ja imprime a resposta com duas casas decimais para voce.",
        ],
        "unary_int": [
            "Na funcao `solve(int value)`, o valor de entrada ja chega pelo parametro `value`.",
            "Voce deve calcular o resultado pedido e retornar um unico valor inteiro com `return`.",
        ],
        "unary_ull": [
            "Na funcao `solve(int value)`, o valor de entrada ja chega pelo parametro `value`.",
            "Voce deve calcular o resultado pedido e retornar um valor inteiro usando `return`.",
        ],
    }
    formula_by_slug = {
        "04_average_of_three": [
            "A media aritmetica de tres numeros e calculada somando os tres valores e dividindo o total por 3.",
            "Formula: `(a + b + c) / 3`.",
        ],
        "05_rectangle_area_perimeter": [
            "A area de um retangulo e calculada multiplicando largura por altura.",
            "Formula da area: `largura * altura`.",
            "O perimetro de um retangulo e a soma de todos os lados.",
            "Formula do perimetro: `2 * largura + 2 * altura`.",
        ],
        "06_circle_area": [
            "A area do circulo e calculada multiplicando PI pelo raio ao quadrado.",
            "Neste exercicio, use `PI = 3.14159`.",
            "Formula: `PI * raio * raio`.",
        ],
        "07_celsius_to_fahrenheit": [
            "Para transformar Celsius em Fahrenheit, multiplique a temperatura por 9, divida por 5 e depois some 32.",
            "Formula: `(C * 9 / 5) + 32`.",
        ],
        "08_fahrenheit_to_celsius": [
            "Para transformar Fahrenheit em Celsius, subtraia 32 da temperatura, multiplique por 5 e divida por 9.",
            "Formula: `(F - 32) * 5 / 9`.",
        ],
        "09_seconds_to_hms": [
            "Para separar segundos em horas, minutos e segundos, primeiro descubra quantas horas cabem no total.",
            "Depois use o resto para descobrir os minutos e o que sobrar sera a quantidade final de segundos.",
        ],
        "14_simple_interest": [
            "O juros simples e calculado multiplicando capital, taxa e tempo, e depois dividindo por 100.",
            "Formula: `(capital * taxa * tempo) / 100`.",
        ],
        "15_salary_bonus": [
            "Para calcular o bonus, pegue a porcentagem do salario base e depois some esse valor ao salario original.",
            "Formula do bonus: `salario * porcentagem / 100`.",
            "Formula final: `salario + bonus`.",
        ],
        "16_discount_price": [
            "Para calcular o desconto, pegue a porcentagem do preco original e depois subtraia esse valor do preco inicial.",
            "Formula do desconto: `preco * porcentagem / 100`.",
            "Formula final: `preco - desconto`.",
        ],
        "18_weighted_average": [
            "Na media ponderada, cada nota e multiplicada pelo seu peso.",
            "Depois some todos os resultados e divida pela soma dos pesos.",
            "Formula: `(nota1*peso1 + nota2*peso2 + nota3*peso3) / (peso1 + peso2 + peso3)`.",
        ],
        "20_remainder_of_division": [
            "O resto da divisao e o valor que sobra depois de dividir um numero pelo outro.",
            "Em C, isso pode ser calculado com o operador `%`.",
        ],
        "21_factorial": [
            "O fatorial de um numero e calculado multiplicando esse numero por todos os inteiros positivos menores que ele ate chegar em 1.",
            "Exemplo: `5! = 5 * 4 * 3 * 2 * 1`.",
        ],
        "22_fibonacci": [
            "Na sequencia de Fibonacci, cada numero novo e a soma dos dois anteriores.",
            "Comeco da sequencia: `0, 1, 1, 2, 3, 5, 8...`.",
        ],
        "23_sum_1_to_n": [
            "Voce deve somar todos os inteiros de 1 ate `n`.",
            "Exemplo: se `n = 5`, entao a soma e `1 + 2 + 3 + 4 + 5 = 15`.",
        ],
        "24_count_digits": [
            "Para contar os digitos de um numero inteiro, voce pode dividir o numero por 10 varias vezes ate ele chegar a 0.",
            "Cada divisao remove o ultimo digito e aumenta a contagem em 1.",
        ],
        "25_power_loop": [
            "Uma potencia inteira pode ser calculada multiplicando a base por ela mesma varias vezes.",
            "Exemplo: `2^5 = 2 * 2 * 2 * 2 * 2`.",
        ],
    }
    implementation_lines = implementation_by_pattern[meta["pattern"]]
    lines = [
        f"# {item['title']}",
        "",
        f"**Objetivo:** {item['goal']}",
        "",
        f"**Conceitos:** {item['concepts']}",
        "",
        "**Entrada**",
        item["input"],
        "",
        "**Saida**",
        item["output"],
        "",
        "**Exemplo de entrada**",
        "```text",
        item["example_input"],
        "```",
        "",
        "**Exemplo de saida**",
        "```text",
        item["example_output"],
        "```",
        "",
    ]
    if meta["slug"] in formula_by_slug:
        lines.extend([
            "**Como calcular**",
            *formula_by_slug[meta["slug"]],
            "",
        ])
    lines.extend([
        "**O que voce precisa fazer no codigo**",
    ])
    lines.extend(implementation_lines)
    lines.extend([
        "",
        "**Como resolver**",
        "1. Abra `main.c`.",
        "2. Complete a funcao `solve(...)`.",
        "3. Compile com `gcc -Wall -Wextra -std=c11 main.c -o program`.",
        "4. Rode as verificacoes predefinidas com `./program --test`.",
        "5. Se quiser consultar a resposta comentada, abra `solution.c`.",
        "",
        "**Comando unico a partir da pasta raiz do projeto**",
        "```bash",
        f"gcc -Wall -Wextra -std=c11 {exercise_path}/main.c -o {exercise_path}/program && {exercise_path}/program --test",
        "```",
        "",
        "O arquivo `main.c` e o exercicio para resolver. O arquivo `solution.c` contem uma solucao comentada em PT-BR.",
    ])
    return "\n".join(lines) + "\n"


def render_root_readme(exercises: list[dict]) -> str:
    lines = [
        "# C Beginner Exercises",
        "",
        "This workspace contains 20 beginner-friendly C exercises designed to be solved in VS Code.",
        "",
        "Each exercise folder contains:",
        "- `README.md` with the problem statement.",
        "- `main.c` with a scaffolded `solve(...)` function.",
        "- A `--test` switch that prints 10 predefined inputs, expected outputs, actual outputs, and pass/fail status.",
        "",
        "The scaffolds compile out of the box, but the `solve(...)` implementations are intentionally unfinished. Expect failing tests until each exercise is solved.",
        "",
        "## Structure",
        "",
        "```text",
        "exercises/",
        "  01_sum_two_numbers/",
        "    README.md",
        "    main.c",
        "  ...",
        "```",
        "",
        "## Working in VS Code",
        "",
        "Open any `main.c` file and use the included VS Code tasks:",
        "- `Build Current C File`",
        "- `Run Current C File`",
        "- `Run Current File Tests`",
        "",
        "You can also compile manually:",
        "",
        "```bash",
        "gcc -Wall -Wextra -std=c11 exercises/01_sum_two_numbers/main.c -o exercises/01_sum_two_numbers/program",
        "./exercises/01_sum_two_numbers/program --test",
        "```",
        "",
        "## Exercise List",
        "",
    ]

    for meta in exercises:
        lines.append(f"- `{meta['slug']}`: {meta['title']}")

    lines.extend(
        [
            "",
            "## Run Every Exercise Test",
            "",
            "```bash",
            "./run_all_tests.sh",
            "```",
        ]
    )

    return "\n".join(lines) + "\n"


def render_root_readme_pt_br(exercises: list[dict]) -> str:
    lines = [
        "# Exercicios Basicos de C",
        "",
        f"Este workspace contem {len(exercises)} exercicios basicos de C para serem resolvidos no VS Code.",
        "",
        "Cada pasta de exercicio contem:",
        "- `README.md` com o enunciado em PT-BR.",
        "- `main.c` com a funcao `solve(...)` preparada para completar.",
        "- `solution.c` com uma solucao comentada em PT-BR.",
        "- Uma chave `--test` que imprime 10 entradas predefinidas, saidas esperadas, saidas atuais e status de aprovacao.",
        "",
        "Os arquivos `main.c` compilam imediatamente, mas as implementacoes de `solve(...)` estao propositalmente incompletas. Espere testes falhando ate resolver cada exercicio.",
        "",
        "## Estrutura",
        "",
        "```text",
        "exercises/",
        "  01_sum_two_numbers/",
        "    README.md",
        "    main.c",
        "    solution.c",
        "  ...",
        "```",
        "",
        "## Como usar no VS Code",
        "",
        "Abra qualquer arquivo `main.c` e use as tasks inclusas:",
        "- `Build Current C File`",
        "- `Run Current C File`",
        "- `Run Current File Tests`",
        "",
        "Tambem e possivel compilar manualmente:",
        "",
        "```bash",
        "gcc -Wall -Wextra -std=c11 exercises/01_sum_two_numbers/main.c -o exercises/01_sum_two_numbers/program",
        "./exercises/01_sum_two_numbers/program --test",
        "```",
        "",
        "Para testar a solucao comentada de um exercicio:",
        "",
        "```bash",
        "gcc -Wall -Wextra -std=c11 exercises/01_sum_two_numbers/solution.c -o exercises/01_sum_two_numbers/solution",
        "./exercises/01_sum_two_numbers/solution --test",
        "```",
        "",
        "## Exercicios",
        "",
    ]

    for meta in exercises:
        item = PT_BR_DESCRIPTIONS[meta["slug"]]
        lines.extend(
            [
                f"### {item['title']}",
                "",
                f"**Pasta:** `exercises/{meta['slug']}`",
                "",
                f"**Objetivo:** {item['goal']}",
                "",
                f"**Entrada:** {item['input']}",
                "",
                f"**Saida:** {item['output']}",
                "",
                "**Exemplo de entrada**",
                "```text",
                item["example_input"],
                "```",
                "",
                "**Exemplo de saida**",
                "```text",
                item["example_output"],
                "```",
                "",
            ]
        )

    lines.extend(
        [
            "## Executar todos os testes",
            "",
            "```bash",
            "./run_all_tests.sh",
            "```",
        ]
    )

    return "\n".join(lines) + "\n"


def render_tasks_json() -> str:
    tasks = {
        "version": "2.0.0",
        "tasks": [
            {
                "label": "Build Current C File",
                "type": "shell",
                "command": "gcc",
                "args": [
                    "-Wall",
                    "-Wextra",
                    "-std=c11",
                    "${file}",
                    "-o",
                    "${fileDirname}/program",
                ],
                "group": {"kind": "build", "isDefault": True},
                "problemMatcher": ["$gcc"],
            },
            {
                "label": "Run Current C File",
                "type": "shell",
                "command": "${fileDirname}/program",
                "dependsOn": "Build Current C File",
            },
            {
                "label": "Run Current File Tests",
                "type": "shell",
                "command": "${fileDirname}/program",
                "args": ["--test"],
                "dependsOn": "Build Current C File",
            },
        ],
    }
    return json.dumps(tasks, indent=2) + "\n"


def render_run_all_tests() -> str:
    return dedent(
        """\
        #!/usr/bin/env bash
        set -euo pipefail

        ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
        BUILD_DIR="${ROOT_DIR}/.build"

        mkdir -p "${BUILD_DIR}"

        for source_file in "${ROOT_DIR}"/exercises/*/solution.c; do
          exercise_dir="$(dirname "${source_file}")"
          exercise_name="$(basename "${exercise_dir}")"
          binary_path="${BUILD_DIR}/${exercise_name}"

          echo "== ${exercise_name} =="
          gcc -Wall -Wextra -std=c11 "${source_file}" -o "${binary_path}"
          "${binary_path}" --test
        done
        """
    )


def render_gitignore() -> str:
    return dedent(
        """\
        .build/
        exercises/**/program
        """
    )


def main() -> None:
    EXERCISES_DIR.mkdir(parents=True, exist_ok=True)

    for meta in EXERCISES:
        exercise_dir = EXERCISES_DIR / meta["slug"]
        exercise_dir.mkdir(parents=True, exist_ok=True)

        readme_path = exercise_dir / "README.md"
        source_path = exercise_dir / "main.c"
        solution_path = exercise_dir / "solution.c"

        builder = PATTERN_BUILDERS[meta["pattern"]]
        readme_path.write_text(render_exercise_readme_pt_br(meta), encoding="utf-8")
        source_path.write_text(builder(meta, solved=False), encoding="utf-8")
        solution_path.write_text(builder(meta, solved=True), encoding="utf-8")

    (ROOT / "README.md").write_text(render_root_readme_pt_br(EXERCISES), encoding="utf-8")
    (ROOT / ".vscode").mkdir(parents=True, exist_ok=True)
    (ROOT / ".vscode" / "tasks.json").write_text(render_tasks_json(), encoding="utf-8")
    (ROOT / "run_all_tests.sh").write_text(render_run_all_tests(), encoding="utf-8")
    (ROOT / ".gitignore").write_text(render_gitignore(), encoding="utf-8")


if __name__ == "__main__":
    main()
