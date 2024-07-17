# What is NER in NLP ?

from promptify import Prompter,OpenAI, Pipeline
import os
sentence     =  """Ideas for Startups by Paul Graham  Page 2 of 8 The initial idea is just a starting point-- not a blueprint, but a question. It might help if they were \\nexpressed that way. Instead of saying that your idea is to make a collaborative, web-based spreadsheet, say: could one make a collaborative, web-based spreadsheet? A few grammatical tweaks, and a woefully incomplete idea becomes a promising question to explore.  There's a real difference, because an assertion provokes objections in a way a question doesn't. If \\nyou say: I'm going to build a web-based spreadsheet, then critics-- the most dangerous of which \\nare in your own head-- will immediately reply that you'd be competing with Microsoft, that you couldn't give people the kind of UI they expect, that users wouldn't want to have their data on your servers, and so on.  A question doesn't seem so challenging. It becomes: let's try making a web-based spreadsheet and see how far we get. And everyone knows that if you tried this you'd be able to make something useful. Maybe what you'd end up with wouldn't even be a spreadsheet. Maybe it would be some kind of new spreadsheet-like collaboration tool that doesn't even have a name yet. You wouldn't have thought of something like that except by implementing your way toward it. \\n \\nTreating a startup idea as a question changes what you're looking for. If an idea is a blueprint, it has to be right. But if it's a question, it can be wrong, so long as it's wrong in a way that leads to more ideas.  One valuable way for an idea to be wrong is to be only a partial solution. When someone's working on a problem that seems too big, I always ask: is there some way to bite off some subset of the problem, then gradually expand from there? That will generally work unless you get trapped on a local maximum, like 1980s-style AI, or C.  \\nUpwind \\n \\nSo far, we've reduced the problem from thinking of a million dollar idea to thinking of a mistaken question. That doesn't seem so hard, does it?  To generate such questions you need two things: to be familiar with promising new technologies, and to have the right kind of friends."""
                
api_key = os.getenv('OPENAI_API_KEY')

model        = OpenAI(api_key) 
prompter     = Prompter('ner.jinja') 
pipe         = Pipeline(prompter , model)


result = pipe.fit(sentence, domain="Learning Assistant", labels=None)
print(result)
