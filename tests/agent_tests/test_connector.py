import os
import unittest

from agent.agent_connector import extract_code, get_api_keys


class ConnectorTests(unittest.TestCase):
    def test_extract_code_removes_markdown_fence(self):
        self.assertEqual(extract_code("```python\nvalue = 1\n```"), "value = 1\n")

    def test_multiple_api_keys_are_read_without_logging_values(self):
        previous = os.environ.get("LLM_API_KEYS")
        try:
            os.environ["LLM_API_KEYS"] = "first, second"
            self.assertEqual(get_api_keys(), ["first", "second"])
        finally:
            if previous is None:
                os.environ.pop("LLM_API_KEYS", None)
            else:
                os.environ["LLM_API_KEYS"] = previous


if __name__ == "__main__":
    unittest.main()