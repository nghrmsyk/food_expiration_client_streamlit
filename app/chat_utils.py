import requests
import json
from pydantic import BaseModel
from typing import List
import streamlit as st
import config

class Ingredient(BaseModel):
    食材: str
    期限種類: str
    期限: str

class Ingredients(BaseModel):
    食材リスト : List[Ingredient]
    目的: str


class DishProposer():
    def __init__(self):
        self.server_url = "http://" + config.server_ip + "/propose_dish/"
    
    def proposal(self,ingredients):
        response = self.upload(ingredients)
        return response

    def upload(self, data):
        """食材リストをアップロードするメソッド

        Returns:
            dict: サーバーからの応答データ。エラーが発生した場合はNone
        """

        response = requests.post(self.server_url, 
                                    data=json.dumps(data.dict()),
                                    headers = {'Content-Type': 'application/json'} 
        )
        response_data = response.json()
        return response_data
