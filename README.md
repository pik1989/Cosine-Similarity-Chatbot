# End to End DS Project

**Project Title:** Cosine Similarity based Chatbot

This project is a simple chatbot that uses cosine similarity for question answering. It performs tokenization and stopword removal on the user's input, then matches the input to a pre-defined list of questions using cosine similarity. If a match is found, the corresponding answer is returned to the user. If no match is found, the chatbot responds with "We can't answer this".

#### Getting Started

These instructions will help you get the project up and running on your local machine for development and testing purposes.

##### Prerequisites

You will need the following packages to run the project - 

* Python 3.x
* nltk
* numpy

##### Installing

Use the following command to install the necessary packages:

```
pip install nltk numpy
```

##### Running the program

1. Clone the repository to your local machine
2. Navigate to the project directory
3. Run the following command to start the chatbot -

    ```
    python app.py
    ```

#### How it works

The chatbot employs cosine similarity to find the best match for the user's input. The pre-defined list of questions and their corresponding answers are present in the `test.csv` file, which is loaded into memory when the program starts. When the user enters a question, the following steps are performed:

1. Tokenization - The user's input is tokenized, which means it is split into individual words or tokens.
2. Stopword removal - Stopwords are words like "is", "the", "a", etc. which do not carry any significant meaning in the sentence. They are removed to reduce the noise in the text.
3. Cosine similarity - The cosine similarity between the user's input and each question in the data set is calculated. The question with the highest cosine similarity score is chosen as the match for the user's input.
4. Response - If a match is found, the corresponding answer is returned to the user. If no match is found, the chatbot responds with "We can't answer this".

![image](https://github.com/pik1989/Cosine-Similarity-Chatbot/assets/34673684/ead0a0cc-b64c-4dd4-9753-4a89aebe9494)

#### Future improvements

The current version of the chatbot is a simple prototype. There are several avenues for improvement, such as - 

1. Using more advanced algorithms for matching the user's input to the pre-defined questions.
2. Integrating natural language processing (NLP) techniques for better understanding of the user's input.
3. Implementing a feedback system for users to rate the relevance of the answers provided by the chatbot.
4. Call the chatGPT (Open AI APIs) to get a relevant answer that is not present in the Q&A dataset.
   
#### Future Scope

![image](https://github.com/pik1989/Cosine-Similarity-Chatbot/assets/34673684/daa0de37-1588-4efd-805e-a3706b46ef2d)
