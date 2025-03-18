import re

from hstest.stage_test import *
from hstest.test_case import TestCase

CheckResult.correct = lambda: CheckResult(True, '')
CheckResult.wrong = lambda feedback: CheckResult(False, feedback)


class ChattyBotTest(StageTest):
    def generate(self) -> List[TestCase]:
        return [
            TestCase(stdin="John", attach="John"),
            TestCase(stdin="Nick", attach="Nick")
        ]

    def check(self, reply: str, clue: Any) -> CheckResult:
        lines = reply.strip().splitlines()

        # Check if the output has exactly 4 lines
        if len(lines) != 4:
            return CheckResult.wrong(
                "Your program should output exactly 4 lines!\n" +
                f"Lines found: {len(lines)}\n"
                "Ensure you are not adding any extra lines or missing any\n" +
                "and that your program outputs the lines exactly as shown in the above example."
            )

        # Check if the first line matches the format `Hello! My name is {bot_name}.`
        if not re.match(r"^Hello! My name is .*\.$", lines[0]):
            return CheckResult.wrong(
                "The 1-st line of your output is NOT correct.\n" +
                "Your program incorrectly output as the 1-st line: " + lines[0] + "\n\n" +
                "The 1-st line should be: 'Hello! My name is {bot_name}.'"
            )

        # Check if the second line matches the format: `I was created in {birth_year}.`
        if not re.match(r"^I was created in \d{4}\.$", lines[1]):
            return CheckResult.wrong(
                "The 2-nd line of your output does NOT match the expected format or does NOT contain a valid year.\n" +
                "Your program incorrectly output as the 2-nd line: " + lines[1] + "\n\n" +
                "The 2-nd line should be: 'I was created in {birth_year}.' "
                "where {birth_year} is a four-digit number like 2023."
            )

        # Check if the third line matches the format: `Please, remind me of your name.`
        if lines[2] != "Please, remind me of your name.":
            return CheckResult.wrong(
                "The 3-rd line of your output is NOT correct.\n" +
                "Your program incorrectly output as the 3-rd line: " + lines[2] + "\n\n" +
                "The 3-rd line should be: 'Please, remind me of your name.'"
            )

        # Check if the fourth line matches the format `What a great name you have, {name}!`
        if not re.match(r"^What a great name you have, \w+!$", lines[3]):
            return CheckResult.wrong(
                "The 4-th line of your output is NOT correct.\n" +
                "Your program incorrectly output as the 4-th line: " + lines[3] + "\n\n" +
                "The 4-th line should be: 'What a great name you have, {name}!' "
                "where {name} is the name you input earlier."
            )

        return CheckResult.correct()


if __name__ == '__main__':
    ChattyBotTest().run_tests()
