This codebase explores the use of LLMs to find the key themes in sermon transcripts. As such, the metadata of these sermons can be enriched with first advantages seen in improved (pseuodo)semantic search within the app. 

# How to run this project
1. Create a `.env` file in your clone of this repository. Copy over the content of the `.env.example` file into it.
1. Fill in the API key for the model which you'd like to use. The Gemini API key can be gotten from [here](https://ai.google.dev/gemini-api/docs).
1. Test the mvp by running `python sermon_tags.py`. This returns three one-word themes for each sermon in `input_data`.
