import os
import replicate
from dotenv import load_dotenv

load_dotenv()

output = replicate.run(
    "meta/llama-2-7b-chat",
    input={
        "prompt": "Explícame qué es gaming en cortas palabras.",
        "max_length": 200,
        "temperature": 0.7,
        "top_p": 0.9
    }
)

for item in output:
    print(item, end="")
