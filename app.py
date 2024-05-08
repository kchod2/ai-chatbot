from llama_index.core import VectorStoreIndex, Settings, SimpleDirectoryReader, StorageContext, load_index_from_storage
from llama_index.llms.azure_openai import AzureOpenAI
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
import gradio
import os

os.environ["AZURE_OPENAI_API_KEY"] = 'xxxxxxxxxxxxxx'
#enter your API key here

Settings.llm = AzureOpenAI(
    azure_endpoint="https://i-homework.openai.azure.com",
    api_version="2024-02-15-preview",
    engine="i-homework",
    temperature=1.0,
    max_tokens=512)

Settings.embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-small-en-v1.5"
)

def construct_index(directory_path):
    docs = SimpleDirectoryReader(directory_path).load_data()

    index = VectorStoreIndex.from_documents(docs)
    
    #Directory in which the indexes will be stored
    index.storage_context.persist(persist_dir="indexes")

    return index

def chatbot(input_text):
    
    # rebuild storage context
    storage_context = StorageContext.from_defaults(persist_dir="indexes")
    
    #load indexes from directory using storage_context 
    query_engine = load_index_from_storage(storage_context).as_query_engine()
    
    response = query_engine.query(input_text)
    
    #returning the response
    return response.response

#Creating the web UIusing gradio
iface = gradio.Interface(fn=chatbot,
                     inputs=gradio.Textbox(lines=5, label="Enter your question here"),
                     outputs="text",
                     title="Custom-trained AI Chatbot")

#Constructing indexes based on the documents in traininData folder
#This can be skipped if you have already trained your app and need to re-run it
index = construct_index("trainingData")

#launching the web UI using gradio
iface.launch()
