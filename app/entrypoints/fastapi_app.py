from typing import Union

from fastapi import FastAPI
from app.services import sentiment_analysis
from app.adapters import sentiment_analyzer

app = FastAPI()


@app.get("/")
def read_root():
    adapter: sentiment_analyzer.AbstractSentimentAnalyzer = sentiment_analyzer.FakeSentimentAnalyzer()
    return {"Hello": ""}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
