# Promptify https://github.com/promptslab/Promptify
### Make sure we are using Python 3.11.7 .
Experimenting with Promptify for our Agent.
```
pip install promptify
```
- **demo.py**: Using the 'ner.jinja' template, we can classify text into various entities. This process is a crucial part of Natural Language Processing (NLP) known as Named Entity Recognition (NER).

What is Named Entity Recognition (NER)?
Named Entity Recognition (NER) is a subtask of information extraction that seeks to locate and classify named entities mentioned in unstructured text into predefined categories such as the names of persons, organizations,etc.

- **explain_demo.py**: Using the 'explain.jinja' template , we can summarize the entire sentences.

- **get_prompt_templates.py**: This code utilizes the `promptify` library to generate prompts based on a specified template. The `generate_promptify_prompt` function creates a prompt using the 'qa.jinja' template, context, question, model name, and domain, and prints the resulting prompt.

- **qa_demo.py**:  A question-answering template that generates answers from the given context.

# Prompt Source https://github.com/bigscience-workshop/promptsource
