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

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from requests.auth import HTTPBasicAuth
import requests
import json
import urllib3
import urllib.parse
import time
import os

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class GetAction(Action):
    def name(self) -> Text:
        return "action_get_incidents"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        url = "https://coe.servicedesk.inspirisys.org:8090/api/v3/requests?TECHNICIAN_KEY=B21C907A-C903-465E-8A8A-BB8C4D63D549"
        print("Hello........")
        headers = {"Content-Type": "application/json"}
        req = requests.get(url, data=json.dumps({"list_info": {"row_count": 20, "start_index": 1,
                                                               "sort_field": "subject", "sort_order": "asc",
                                                               "get_total_count": True,
                                                               "search_fields": {"subject": "", "priority.name": ""}}}),
                           headers=headers, verify=False)
        print(req.content)
        print(req.status_code)
        dispatcher.utter_message(req.content)
        return []


class ArchiveFile(Action):
    def name(self) -> Text:
        return "action_archive_incidents"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        with open(os.path.dirname(os.path.abspath(__file__))+'/InputJSON/ArchiveFile.json', 'r') as myfile:
            data = myfile.read()
            email_value = tracker.get_slot("username")
            print("EmailID++++++++++++++" + email_value)
            sent_json = data.replace("EMAILID", email_value)
            print(sent_json)
            datavalue = urllib.parse.quote(sent_json)
            url = "https://coe.servicedesk.inspirisys.org:8090/api/v3/requests?TECHNICIAN_KEY=B21C907A-C903-465E-8A8A-BB8C4D63D549&input_data="+datavalue
            headers = {"Content-Type": "application/json"}
            print("create_ticket_for_outlook_newfile")
            req = requests.post(url, headers=headers, verify=False, timeout=180)
            result = req.json().get('response_status')
            if result['status_code'] == 2000:
                getid = req.json().get('request')
                ticketid = getid['id']
                print("Ticket Created Successfully and ticket No-" + ticketid)
                dispatcher.utter_message(text="Ticket Created Successfully and ticket number is " + ticketid)
            else:
                print("Not created")
                dispatcher.utter_message(text="Please try after some time for ticket creation")
            return []


class RecoverEmail(Action):
    def name(self) -> Text:
        return "action_recoveremail_incidents"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        with open(os.path.dirname(os.path.abspath(__file__)) + '/InputJSON/RecoverEmail.json', 'r') as myfile:
            data = myfile.read()
            email_value = tracker.get_slot("username")
            print("EmailID++++++++++++++" + email_value)
            sent_json = data.replace("EMAILID", email_value)
            print(sent_json)
            datavalue = urllib.parse.quote(sent_json)
            url = "https://coe.servicedesk.inspirisys.org:8090/api/v3/requests?TECHNICIAN_KEY=B21C907A-C903-465E-8A8A-BB8C4D63D549&input_data=" + datavalue
            headers = {"Content-Type": "application/json"}
            print("create_ticket_for_outlook_recovery")
            req = requests.post(url, headers=headers, verify=False, timeout=180)
            result = req.json().get('response_status')
            if result['status_code'] == 2000:
                getid = req.json().get('request')
                ticketid = getid['id']
                print("Ticket Created Successfully and ticket No-" + ticketid)
                dispatcher.utter_message(text="Ticket Created Successfully and ticket number is " + ticketid)
            else:
                print("Not created")
                dispatcher.utter_message(text="Please try after some time for ticket creation")
            return []


class PrinterIssue(Action):
    def name(self) -> Text:
        return "action_printer_incidents"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        with open(os.path.dirname(os.path.abspath(__file__))+'/InputJSON/Printerissue.json', 'r') as myfile:
            data = myfile.read()
            email_value = tracker.get_slot("username")
            print("EmailID++++++++++++++" + email_value)
            sent_json = data.replace("EMAILID", email_value)
            print(sent_json)
            datavalue = urllib.parse.quote(sent_json)
            url = "https://coe.servicedesk.inspirisys.org:8090/api/v3/requests?TECHNICIAN_KEY=B21C907A-C903-465E-8A8A-BB8C4D63D549&input_data="+datavalue
            headers = {"Content-Type": "application/json"}
            print("create_ticket_for_printer_queue")
            req = requests.post(url, headers=headers, verify=False, timeout=180)
            result = req.json().get('response_status')
            if result['status_code'] == 2000:
                getid = req.json().get('request')
                ticketid = getid['id']
                print("Ticket Created Successfully and ticket No-" + ticketid)
                dispatcher.utter_message(text="Ticket Created Successfully and ticket number is " + ticketid)
            else:
                print("Not created")
                dispatcher.utter_message(text="Please try after some time for ticket creation")
            return []

class CleanUpExplorer(Action):
    def name(self) -> Text:
        return "action_cleanup_incidents"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        with open(os.path.dirname(os.path.abspath(__file__))+'/InputJSON/CleanUpExplorer.json', 'r') as myfile:
            data = myfile.read()
            email_value = tracker.get_slot("username")
            print("EmailID++++++++++++++" + email_value)
            sent_json = data.replace("EMAILID", email_value)
            print(sent_json)
            datavalue = urllib.parse.quote(sent_json)
            url = "https://coe.servicedesk.inspirisys.org:8090/api/v3/requests?TECHNICIAN_KEY=B21C907A-C903-465E-8A8A-BB8C4D63D549&input_data="+datavalue
            headers = {"Content-Type": "application/json"}
            print("create_ticket_for_internet_explorer_clean")
            req = requests.post(url, headers=headers, verify=False, timeout=180)
            result = req.json().get('response_status')
            if result['status_code'] == 2000:
                getid = req.json().get('request')
                ticketid = getid['id']
                print("Ticket Created Successfully and ticket No-" + ticketid)
                dispatcher.utter_message(text="Ticket Created Successfully and ticket number is " + ticketid)
            else:
                print("Not created")
                dispatcher.utter_message(text="Please try after some time for ticket creation")
            return []


class Popup(Action):
    def name(self) -> Text:
        return "action_popup_incidents"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        with open(os.path.dirname(os.path.abspath(__file__))+'/InputJSON/PopUpExplorer.json', 'r') as myfile:
            data = myfile.read()
            email_value = tracker.get_slot("username")
            print("EmailID++++++++++++++" + email_value)
            sent_json = data.replace("EMAILID", email_value)
            print(sent_json)
            datavalue = urllib.parse.quote(sent_json)
            url = "https://coe.servicedesk.inspirisys.org:8090/api/v3/requests?TECHNICIAN_KEY=B21C907A-C903-465E-8A8A-BB8C4D63D549&input_data="+datavalue
            headers = {"Content-Type": "application/json"}
            print("create_ticket_for_internet_explorer_popup")
            req = requests.post(url, headers=headers, verify=False, timeout=180)
            result = req.json().get('response_status')
            if result['status_code'] == 2000:
                getid = req.json().get('request')
                ticketid = getid['id']
                print("Ticket Created Successfully and ticket No-" + ticketid)
                dispatcher.utter_message(text="Ticket Created Successfully and ticket number is " + ticketid)
            else:
                print("Not created")
                dispatcher.utter_message(text="Please try after some time for ticket creation")
            return []


class AdobeReader(Action):
    def name(self) -> Text:
        return "action_adobe_incidents"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        with open(os.path.dirname(os.path.abspath(__file__))+'/InputJSON/AdobeReaderExplorer.json', 'r') as myfile:
            data = myfile.read()
            email_value = tracker.get_slot("username")
            print("EmailID++++++++++++++" + email_value)
            sent_json = data.replace("EMAILID", email_value)
            print(sent_json)
            datavalue = urllib.parse.quote(sent_json)
            url = "https://coe.servicedesk.inspirisys.org:8090/api/v3/requests?TECHNICIAN_KEY=B21C907A-C903-465E-8A8A-BB8C4D63D549&input_data="+datavalue
            headers = {"Content-Type": "application/json"}
            print("create_ticket_for_internet_explorer_PDF")
            req = requests.post(url, headers=headers, verify=False, timeout=180)
            result = req.json().get('response_status')
            if result['status_code'] == 2000:
                getid = req.json().get('request')
                ticketid = getid['id']
                print("Ticket Created Successfully and ticket No-"+ticketid)
                dispatcher.utter_message(text="Ticket Created Successfully and ticket number is "+ticketid)
            else:
                print("Not created")
                dispatcher.utter_message(text="There was some problem while creating the ticket. Please try after some time..")
            return []


class CleanTemp(Action):
    def name(self) -> Text:
        return "action_cleantemp_incidents"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        with open(os.path.dirname(os.path.abspath(__file__))+'/InputJSON/CleanTempMobility.json', 'r') as myfile:
            data = myfile.read()
            email_value = tracker.get_slot("username")
            print("EmailID++++++++++++++" + email_value)
            sent_json = data.replace("EMAILID", email_value)
            print(sent_json)
            datavalue = urllib.parse.quote(sent_json)
            url = "https://coe.servicedesk.inspirisys.org:8090/api/v3/requests?TECHNICIAN_KEY=B21C907A-C903-465E-8A8A-BB8C4D63D549&input_data="+datavalue
            headers = {"Content-Type": "application/json"}
            print("create_ticket_for_mobility")
            req = requests.post(url, headers=headers, verify=False, timeout=180)
            result = req.json().get('response_status')
            if result['status_code'] == 2000:
                getid = req.json().get('request')
                ticketid = getid['id']
                print("Ticket Created Successfully and ticket No-" + ticketid)
                dispatcher.utter_message(text="Ticket Created Successfully and ticket number is " + ticketid)
            else:
                print("Not created")
                dispatcher.utter_message(text="Please try after some time for ticket creation")
            return []


class CDriveSpace(Action):
    def name(self) -> Text:
        return "action_cdrivespace_incidents"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        with open(os.path.dirname(os.path.abspath(__file__))+'/InputJSON/DriveSpace.json', 'r') as myfile:
            data = myfile.read()
            email_value = tracker.get_slot("username")
            print("EmailID++++++++++++++" + email_value)
            sent_json = data.replace("EMAILID", email_value)
            print(sent_json)
            datavalue = urllib.parse.quote(sent_json)
            url = "https://coe.servicedesk.inspirisys.org:8090/api/v3/requests?TECHNICIAN_KEY=B21C907A-C903-465E-8A8A-BB8C4D63D549&input_data="+datavalue
            headers = {"Content-Type": "application/json"}
            print("create_ticket_for_Temp_file_C")
            req = requests.post(url, headers=headers, verify=False, timeout=180)
            result = req.json().get('response_status')
            if result['status_code'] == 2000:
                getid = req.json().get('request')
                ticketid = getid['id']
                print("Ticket Created Successfully and ticket No-" + ticketid)
                dispatcher.utter_message(text="Ticket Created Successfully and ticket number is " + ticketid)
            else:
                print("Not created")
                dispatcher.utter_message(text="Please try after some time for ticket creation")
            return []


class JavaSolution(Action):
    def name(self) -> Text:
        return "action_javasolution_incidents"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        with open(os.path.dirname(os.path.abspath(__file__))+'/InputJSON/JavaSolution.json', 'r') as myfile:
            data = myfile.read()
            email_value = tracker.get_slot("username")
            print("EmailID++++++++++++++" + email_value)
            sent_json = data.replace("EMAILID", email_value)
            print(sent_json)
            datavalue = urllib.parse.quote(sent_json)
            url = "https://coe.servicedesk.inspirisys.org:8090/api/v3/requests?TECHNICIAN_KEY=B21C907A-C903-465E-8A8A-BB8C4D63D549&input_data="+datavalue
            headers = {"Content-Type": "application/json"}
            print("create_ticket_for_java_solution")
            req = requests.post(url, headers=headers, verify=False, timeout=180)
            result = req.json().get('response_status')
            if result['status_code'] == 2000:
                getid = req.json().get('request')
                ticketid = getid['id']
                print("Ticket Created Successfully and ticket No-" + ticketid)
                dispatcher.utter_message(text="Ticket Created Successfully and ticket number is " + ticketid)
            else:
                print("Not created")
                dispatcher.utter_message(text="Please try after some time for ticket creation")
            return []
