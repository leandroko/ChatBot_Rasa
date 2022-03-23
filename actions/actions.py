# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []



from typing import Any, Text, Dict, List
from pandas.core.indexes.base import Index

from rasa_sdk.events import SlotSet
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import pandas as pd
import os
import datetime as dt
import string

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class action_receber_nome(Action):
    
    def name(self) -> Text:
        return "action_receber_nome"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        text = tracker.latest_message['text']
        dispatcher.utter_message(text=f"Irei lembrar de seu nome {text}! Em que posso ajudar?")
        return [SlotSet("nome", text)]
    
    
class action_dizer_nome(Action):
    
    def name(self) -> Text:
        return "action_dizer_nome"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        name = tracker.get_slot("nome")
        if not name:
            dispatcher.utter_message(text="Ainda não sei o seu nome, como você se chama?")
        else:
            dispatcher.utter_message(text=f"Seu nome é {name}!")
        return []



class action_listar_unidades(Action):
    
    def name(self) -> Text:
        return "action_listar_unidades"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        cidade = tracker.get_slot("cidade")
        
        cidade = cidade.lower()
        
        cidade2 = string.capwords(cidade)
        
        df = pd.read_csv(BASE_DIR + '\\unidadesaude.csv', sep=';')
        df = df.dropna()
        dfpr = df[df['ESTADO'] == 'PR']
        dfpr = dfpr[dfpr['CIDADE'].str.lower() == cidade]
        resultado = dfpr.reset_index(drop=True).head(5)
         
        dispatcher.utter_message(text=f"Segue 5 unidades de saúde para a cidade de {cidade2}: \n {resultado}!")
        
        return []