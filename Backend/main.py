import openai
from fastapi import FastAPI



# Retrieve Enviornment Variables
openai.organization = 'org-dqJt85SuvQdcoF1tv94EqHdD'
openai.api_key = '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'

app = FastAPI()


@app.get("/")
async def root():
    try:
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=["this is test"])
        message_text = response["choices"][0]["message"]["content"]
        print(message_text)
    except Exception as e:
        print(e)
    return {"me": "This is me testing FAST API"}