""" 
from datasets import load_dataset
dataset = load_dataset("snli")
example = dataset["train"][0]
print(example)
print(dataset["train"].features["label"])

from datasets import load_dataset
dataset = load_dataset("ag_news",split="train")
example = dataset[20]
print(example)

from promptsource.templates import DatasetTemplates , Template 
ag_news_prompt = DatasetTemplates('ag_news')
prompt = ag_news_prompt["classify_question_first"]
"""

from datasets import load_dataset
from promptsource.templates import DatasetTemplates

dataset = load_dataset("ag_news", split="train")
example = dataset[1]

ag_news_prompts = DatasetTemplates('ag_news')
prompt_key = "classify_question_first"
prompt = ag_news_prompts[prompt_key]
result = prompt.apply(example)

print("INPUT: ", result[0])
print("TARGET: ", result[1])
