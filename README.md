# chatbot
**AI-based chat app trained with custom data**

This is a simple instance of ChatGPT trained with custom data (drug-related pdf files), operated via a web UI, with additional limitations imposed to make it stay focused on a topic. 

Based on the solution: https://medium.com/@sushwanth.n/how-to-train-chatgpt-with-your-custom-data-and-create-your-own-chatbot-6d525fc7f20f
Updated to account for changes in functions/classes in more recent versions of some libraries

# Dependent libraries:

Use this command to install the dependent libraries that will be used to train chatGPT on custom data.

*pip install -r requirements.txt*

+ Azureopenai — Azure OpenAI python library
+ llama-index — LlamaIndex data framework for the LLM application
+ pypdf — The open source python library that will be used to read the pdf files to train the AI chatbot on
+ gradio — Gradio.app is a simple way to create a web UI to demonstrate the application

## Getting the API key from Azure OpenAI:

If you do not have an Azure API key, sign up here:
https://azure.microsoft.com/en-us/products/ai-services/openai-service

This app makes use of the free option.

## Running the app:

Navigate to the main catalog "ai-chatbot". Use this command in console to start the app.

*python app.py*

It will take some time to read the pdf files, index them and learn. In order for the chatbot to be focused on a given topic, the contents of the pdf files will be used as "context" for the prompt. The files' content will be converted into embeddings in order to reduce complexity, as free usage only supports requests up to about 8000 tokens. When the process is finished, you will see two new sub-folders created in the main directory. “Indexes” is the catalog that has all the indexes based on the data in the “trainingData”. The flagged responses will be saved in the “flagged” catalog. Wait until you see the url where you can test your trained chat model:

(http://127.0.0.1:7860/)

Open the link in your browser. You will see a simple chat UI with a window to enter your prompts / questions on the left side. The answers from the chatbot will appear on the right side. The app needs to keep running in the background in order for the chat UI to work.

When the chatbot encounters a question on a different topic, it will decline to answer. Whenever it mentions "context", it refers to the custom data it was trained on (pdf files in the trainingData catalog).

You can try to improve the quality of answers by tinkering with the model's parameters in Settings.llm. In this example, temperature (the parameter that controls randomness) was maxed out, as it visibly improved information retrieval.
