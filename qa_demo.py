from promptify import Prompter , OpenAI , Pipeline
import os
from pprint import pprint

api_key = os.getenv('OPENAI_API_KEY')
model        = OpenAI(api_key) 
prompter     = Prompter('qa.jinja') 
pipe         = Pipeline(prompter , model)

context = "The rabbit-hole went straight on like a tunnel for some way, and then dipped suddenly down, so suddenly that Alice had not a moment to think about stopping herself before she found herself falling down a very deep well."

question = "what is the main problem with patient?" 

result = pipe.fit(
    context,
    domain="medical",
    question = question
    )

pprint(result)
