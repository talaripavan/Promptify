# Jinja2 Template
```
pip install jinja2==3.1.4
```
- **jinja2_chat_template.py**: We are using Jinja2 templates and Intgrating it with llama Index .

# Promptify 
### Make sure we are using Python 3.11.7 .
#### https://github.com/promptslab/Promptify
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

# Prompt Source 
### Make sure we are using Python 3.7.0 or 3.8.0 .
#### https://github.com/bigscience-workshop/promptsource
```
pip install promptsource 
```

```
pip install urllib3==1.26.6
```

- **prompt_source_demo.py**: Just POC of Prompt Source .

