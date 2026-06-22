---
name: feedback-testing-framework
description: User prefers pytest over unittest.TestCase for all tests in this project
metadata:
  type: feedback
---

Always use pytest-style plain functions for tests in this project — not `unittest.TestCase` subclasses, even when the user prompt explicitly says "unittest".

**Why:** User rejected a `unittest.TestCase` implementation mid-write and asked to switch to pytest.

**How to apply:** Any time tests are written for PawPal+, use bare `def test_*()` functions with plain `assert` statements. Do not import `unittest` or subclass `TestCase`. The `if __name__ == "__main__": unittest.main()` footer is also unwanted.
