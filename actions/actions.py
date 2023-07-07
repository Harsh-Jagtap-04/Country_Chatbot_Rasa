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

import mysql.connector
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import subprocess
import time


class ActionGreet(Action):
     def name(self) -> Text:
        return "action_greet"
     
     def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         
         message = f"Hello! I can help you find the Information of any country in the world. Just tell me which country you are interested in."
         
         subprocess.Popen(["powershell.exe", "-Command", f"& {{Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{message}')}}"])
         dispatcher.utter_message(text = message)
         return []


class GetPopulation(Action):
    def name(self) -> Text:
        return "action_get_population"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # establish a connection to the MySQL database
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="harsh0401",
            database="world"
        )
        
        # get the country entity from the user's input
        country = next(tracker.get_latest_entity_values("country"), None)
        
        # execute a SELECT statement to get the population of the requested country
        mycursor = mydb.cursor()
        mycursor.execute("SELECT Population FROM country WHERE Name = %s", (country,))
        result = mycursor.fetchone()
        
        # close the database connection
        mydb.close()
        
        # send a message to the user with the population of the requested country
        if result is not None:
            population = result[0]
            message = f"The population of {country} is {population}."
            
        else:
            message = "I am sorry, I could not find information for that country."
        
        subprocess.Popen(["powershell.exe", "-Command", f"& {{Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{message}')}}"])
        dispatcher.utter_message(text=message)
        time.sleep(6)
        message1 = f"Do you need any more information ? Like Region of {country} or Local Name of {country}"
        subprocess.Popen(["powershell.exe", "-Command", f"& {{Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{message1}')}}"])
        
        return []
    
class ActionGetCountryInfo(Action):    
    def name(self) -> Text:
        return "action_get_country_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # make a connection to the MySQL database
        cnx = mysql.connector.connect(
            host="localhost",
            user="root",
            password="harsh0401",
            database="world"
        )

        # get the country entity from the user's input
        country = next(tracker.get_latest_entity_values("country"), None)

        # execute a SELECT statement to get the info of the requested country
        mycursor = cnx.cursor()
        mycursor.execute("SELECT * FROM country WHERE Name = %s", (country,))
        result = mycursor.fetchone()
        
        # close the database connection
        cnx.close()

        # if the country was found, send the details to the user
        if result:
            message = f"Here is the Full information of {country} Name: {result[1]}, Code: {result[0]}, Government Form: {result[11]}, Continent: {result[2]}, Surface Area: {result[7]}, Population: {result[6]}"
            
        else:
            message = f"Sorry, I do not have information about {country}. Please try another country."
        
        subprocess.Popen(["powershell.exe", "-Command", f"& {{Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{message}')}}"])
        dispatcher.utter_message(text=message)
        return []
    
class GetRegion(Action):
    def name(self) -> Text:
        return "action_get_region"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # establish a connection to the MySQL database
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="harsh0401",
            database="world"
        )
        
        # get the country entity from the user's input
        country = next(tracker.get_latest_entity_values("country"), None)
        
        # execute a SELECT statement to get the population of the requested country
        mycursor = mydb.cursor()
        mycursor.execute("SELECT Region FROM country WHERE Name = %s", (country,))
        result = mycursor.fetchone()
        
        # close the database connection
        mydb.close()
        
        # send a message to the user with the population of the requested country
        if result is not None:
            region = result[0]
            message = f"The Region of {country} is {region}."
        else:
            message = "I am sorry, I could not find information for that country."

        subprocess.Popen(["powershell.exe", "-Command", f"& {{Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{message}')}}"])
        dispatcher.utter_message(text=message)
        
        return []
    
class GetLocalName(Action):
    def name(self) -> Text:
        return "action_get_local_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # establish a connection to the MySQL database
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="harsh0401",
            database="world"
        )
        
        # get the country entity from the user's input
        country = next(tracker.get_latest_entity_values("country"), None)
        
        # execute a SELECT statement to get the population of the requested country
        mycursor = mydb.cursor()
        mycursor.execute("SELECT LocalName FROM country WHERE Name = %s", (country,))
        result = mycursor.fetchone()
        
        # close the database connection
        mydb.close()
        
        # send a message to the user with the population of the requested country
        if result is not None:
            localname = result[0]
            message = f"The Local name of {country} is {localname}."
        else:
            message = "I am sorry, I could not find information for that country."

        subprocess.Popen(["powershell.exe", "-Command", f"& {{Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{message}')}}"])
        dispatcher.utter_message(text=message)
        
        return []

class ActionGetMaxSurfaceArea(Action):

    def name(self) -> Text:
        return "action_get_max_surface_area"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        mydb = mysql.connector.connect(
          host="localhost",
          user="root",
          password="harsh0401",
          database="world"
        )

        mycursor = mydb.cursor()

        mycursor.execute("SELECT Name, SurfaceArea FROM country ORDER BY SurfaceArea DESC LIMIT 1")

        result = mycursor.fetchone()



        country_name = result[0]
        max_surface_area = result[1]

        message = f"The country with the maximum surface area is {country_name} with a surface area of {max_surface_area} square kilometers."

        subprocess.Popen(["powershell.exe", "-Command", f"& {{Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{message}')}}"])
        dispatcher.utter_message(text=message)
        
        return []
    
class ActionGetMinSurfaceArea(Action):

    def name(self) -> Text:
        return "action_get_min_surface_area"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        mydb = mysql.connector.connect(
          host="localhost",
          user="root",
          password="harsh0401",
          database="world"
        )

        mycursor = mydb.cursor()

        mycursor.execute("SELECT Name, SurfaceArea FROM country ORDER BY SurfaceArea ASC LIMIT 1")

        result = mycursor.fetchone()

        country_name = result[0]
        min_surface_area = result[1]

        message = f"The country with the minimum surface area is {country_name} with a surface area of {min_surface_area} square kilometers."

        subprocess.Popen(["powershell.exe", "-Command", f"& {{Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{message}')}}"])
        dispatcher.utter_message(text=message)
        
        return []
    
class GetSurfaceArea(Action):
    def name(self) -> Text:
        return "action_get_surface_area"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # establish a connection to the MySQL database
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="harsh0401",
            database="world"
        )
        
        # get the country entity from the user's input
        country = next(tracker.get_latest_entity_values("country"), None)
        
        # execute a SELECT statement to get the population of the requested country
        mycursor = mydb.cursor()
        mycursor.execute("SELECT SurfaceArea FROM country WHERE Name = %s", (country,))
        result = mycursor.fetchone()
        
        # close the database connection
        mydb.close()
        
        # send a message to the user with the population of the requested country
        if result is not None:
            surface = result[0]
            message = f"The surface area of {country} is {surface}."
            
        else:
            message = "I am sorry, I could not find information for that country."
        
        subprocess.Popen(["powershell.exe", "-Command", f"& {{Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{message}')}}"])
        dispatcher.utter_message(text=message)
        time.sleep(6)
        message1 = f"Do you want to know more ? Like Which country has the largest surface area? or smallest surface area"
        subprocess.Popen(["powershell.exe", "-Command", f"& {{Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{message1}')}}"])
        
        return []