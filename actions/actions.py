# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import AllSlotsReset
from rasa_sdk.events import Restarted
from rasa_sdk.events import SlotSet
from .api_currency import currency
import datetime




class ActionCurrency(Action):
    '''Currency'''
    def name(self) -> Text:
        return "action_currency"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        try:
            my_country = tracker.get_slot("your_country")
            new_country = tracker.get_slot("new_country")
            amount = tracker.get_slot("amount")
            response =currency(my_country,new_country,amount)
        
            dispatcher.utter_message(response)

        except:
            dispatcher.utter_message("Please give me right information.")

        return [SlotSet('your_country',my_country),SlotSet('new_country',new_country),SlotSet('amount',amount)]


class ActionClear(Action):
    '''Reset All'''
    def name(self) -> Text:
        return "action_clear"

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return [AllSlotsReset()]

