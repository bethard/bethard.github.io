import re
import sys

keywords_to_trim = [
    "conference talk",
    "demo paper",
    "shared task paper",
    "workshop paper",
]
keywords_regex = rf'(?:{"|".join(keywords_to_trim)})'

text = sys.stdin.read()

text = re.sub(rf',\s*{keywords_regex}|{keywords_regex}(,?\s*)', '', text)

sys.stdout.write(text)
