import unittest
import os
from solution1678 import Solution


def main():
    os.system("clear")
    # input
    command = "G()(al)"
    output = "Goal"

    s = Solution()

    result = s.interpret(command)
    assert result == output, "no result equal ok"
    print("ok")


if __name__ == "__main__":
    main()
