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
# class ActionSetFaqSlot(Action):
#     """Returns the chitchat utterance dependent on the intent"""

#     def name(self) -> Text:
#         return "action_set_faq_slot"

#     def run(
#         self,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any],
#     ) -> List[EventType]:
#         full_intent = (
#             tracker.latest_message.get("response_selector", {})
#             .get("faq", {})
#             .get("full_retrieval_intent")
#         )
#         if full_intent:
#             topic = full_intent.split("/")[1]
#         else:
#             topic = None

#         return [SlotSet("faq", topic)]
