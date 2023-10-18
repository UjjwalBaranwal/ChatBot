# # This files contains your custom actions which can be used to run
# # custom Python code.
# #
# # See this guide on how to implement these action:
# # https://rasa.com/docs/rasa/custom-actions


# # This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List

from typing import Any, Coroutine, Dict, List, Text
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.interfaces import Tracker
from rasa_sdk.types import DomainDict

import webbrowser


GS_classroom = {
    1: "GS-1 doesn't exist",
    2: "GS-2 doesn't exist",
    3: "when you enter in the GS building from GS gate then next to GS-4 you can get GS-3",
    4: "when you enter in the GS building from GS gate then then the first room GS-4",
    5: "GS-5",
    6: "GS-6",
    7: "GS-7",
    8: "GS-8",
}

SEW_classroom = {
    1: "SEW-1",
    2: "SEW-2",
    3: "SEW-3",
    4: "SEW-4",
    5: "SEW-5",
    6: "SEW-6",
    7: "SEW-7",
    8: "SEW-8",
    9: "SEW-9",
    0: "SEW-10",
}


class ActionTellWhereToGoInGS(Action):
    def name(self) -> Text:
        return "way_to_GS"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict) -> Coroutine[Any, Any, List[Dict[Text, Any]]]:
        # currLoc=tracker.get_slot("Location")
        currLoc = next(tracker.get_latest_entity_values("Location_GS"), None)
        msg = f"{GS_classroom[int(currLoc[-1])]}"
        dispatcher.utter_message(text=msg)

        return []


class ActionTellWhereToGoInSEW(Action):
    def name(self) -> Text:
        return "way_to_SEW"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict) -> Coroutine[Any, Any, List[Dict[Text, Any]]]:
        # currLoc=tracker.get_slot("Location")
        currLoc = next(tracker.get_latest_entity_values("Location_SEW"), None)
        msg = f"{SEW_classroom[int(currLoc[-1])]}"
        dispatcher.utter_message(text=msg)

        return []
# class ActionFacilitySearch(Action):
#     def name(self) -> Text:
#         return "facility_search"
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         facility = tracker.get_slot("facility_type")
#         address = "go to teliarganj near bikaner"
#         dispatcher.utter_message("Here is the address of the {}:{}".format(facility, address))
#         return [SlotSet("address", address)]


class ActionOpenPdf(Action):
    def name(self) -> Text:
        return "open_map"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict) -> Coroutine[Any, Any, List[Dict[Text, Any]]]:
        return super().run(dispatcher, tracker, domain)
    url = 'http://www.mnnit.ac.in/images/institute/master_plan.pdf'
    webbrowser.open(url, new=2)  # open in new tab
