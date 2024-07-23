from llama_index.core.base.llms.types import ChatMessage, MessageRole
from llama_index.core.prompts.base import ChatPromptTemplate
from jinja2 import Environment, FileSystemLoader
from llama_index.vector_stores.milvus import MilvusVectorStore
from llama_index.core import VectorStoreIndex , get_response_synthesizer
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.core.query_engine import RetrieverQueryEngine
import os
collection_name = os.getenv('COLLECTION_NAME')
uri = os.getenv('URI')

env = Environment(loader=FileSystemLoader(""))
template = env.get_template("rag_template.txt")
test_template = env.get_template("test.txt")

system_message = ChatMessage(
    content=template.render(),
    role=MessageRole.SYSTEM,
  )
text_qa_template_message = [
    system_message,
    ChatMessage(
    content=(
      "Context information is below.\n"
      "---------------------\n"
      "{context_str}\n"
      "---------------------\n"
      "Given the context information and not prior knowledge, "
      "answer the query.\n"
      "Query: {query_str}\n"
      "Answer: "      
    ),
    role=MessageRole.USER,
  )
  ]
text_qa_prompt_template = ChatPromptTemplate(message_templates=text_qa_template_message)
response_synthesizer = get_response_synthesizer(
    text_qa_template= text_qa_prompt_template  
    )
vector_store = MilvusVectorStore(collection_name=collection_name, dim=1536, overwrite=False, uri=uri)
index = VectorStoreIndex.from_vector_store(vector_store)
retriever = VectorIndexRetriever(index=index,similarity_top_k=2)
retriever_engine = RetrieverQueryEngine(
        retriever=retriever,
        response_synthesizer=response_synthesizer
)

retriever_response = retriever_engine.query("Explain me about Data-Ingestion ?")
print(retriever_response)

'''
def display_prompt_dict(prompts_dict):
  for k, p in prompts_dict.items():
    # Print prompt key and text label
    print(f"**Prompt Key**: {k}")
    print(f"**Text:** ")
    
    print(p.get_template())
    print("\n")
retriever_response = retriever_engine.get_prompts()
prompt = display_prompt_dict(retriever_response)
'''