# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


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

from rasa_sdk import Action
from rasa_sdk.events import SlotSet

class ActionRecipeDialog(Action):
   def name(self) -> Text:
      return "action_recipe_dialog"
   
   @staticmethod
   def required_slots(tracker):
      return [
         "url",
         "ingredientsorsteps"
         ]	  
   
   def submit(
      self,
      dispatcher: CollectingDispatcher,
      tracker: Tracker,
      domain: Dict[Text, Any]): #-> List[Dict]:
         #check what to return?
         return []		


	  
class ActionAskYouTube(Action):
   def name(self) -> Text:
      return "action_ask_youtube"

   def run(
      self,
      dispatcher: CollectingDispatcher,
      tracker: Tracker,
      domain: Dict[Text, Any]): #-> List[Dict[Text, Any]]:
         user_q = tracker.get_slot('question')
         result=getanswersfromyoutube(user_q)
         
         return [SlotSet("matches", result if result is not None else [])]
