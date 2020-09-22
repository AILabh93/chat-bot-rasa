# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"
from typing import Any, Text, Dict, List, Union
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import UserUtteranceReverted

from bs4 import BeautifulSoup
import requests
import lxml
import bs4
import gc



class action_get_luong(Action):
    def name(self):
        return 'action_luong'
    def run(self,dispatcher, tracker, domain):
        soup = BeautifulSoup (open("data.html", encoding="utf8"), features="lxml")
        divs = soup.select("div.bk-lesson-content > p")
        dispatcher.utter_message(divs[11].get_text())
        dispatcher.utter_message(image=str('https://vncoder.vn//upload/img/post/images/post/2020_04/Khoa%20h%E1%BB%8Dc%20m%C3%A1y%20t%C3%ADnh%202.png'))
        return []



def createButton():
    temp_button_lst = []

    temp_button_lst.append({
        "type": "postback",
        "title": "Khoa học máy tính",
        "payload": "khmt"
    })

    temp_button_lst.append({
        "type": "postback",
        "title": "Kĩ thuật phần mềm",
        "payload": "ktpm"
    })

    temp_button_lst.append({
        "type": "postback",
        "title": "Công nghệ thông tin",
        "payload": "cntt"
    })

    return temp_button_lst


class action_but(Action):
    def name(self):
        return 'action_but'
    def run(self,dispatcher, tracker, domain):
        but=createButton()

        but1={
        "type": "postback",
        "title": "Hệ thống thông tin",
        "payload": "httt"
        }
        
        but2={
        "type": "postback",
        "title": "Khoa học dữ liệu",
        "payload": "khdl"
        }
        dispatcher.utter_message(text="Bạn cần tư vấn gì", buttons=but)
        dispatcher.utter_message(text="Nữa nè :)", buttons=[but1, but2])

        return []

class action_unknown(Action):
    def name(self):
        return "action_unknown"
    
    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(text='Xin lỗi mình chưa hiểu ý bạn')
        but =  createButton()
        
        but1={
        "type": "postback",
        "title": "Hệ thống thông tin",
        "payload": "httt"
        }
        
        but2={
        "type": "postback",
        "title": "Khoa học dữ liệu",
        "payload": "khdl"
        }
        dispatcher.utter_message(text="Bạn có thể chọn các chuyên ngành sau", buttons=but)
        dispatcher.utter_message(text="Nữa nè <3", buttons=[but1, but2])
                
        return []

class action_tuvan(Action):
    def name(self):
        return "action_tuvan"
    
    def run(self, dispatcher, tracker, domain):
        mon_hoc=tracker.latest_message['entities'][0]['value']
        print(mon_hoc)
        if mon_hoc=='khmt':
            dispatcher.utter_message(template='utter_tuvan_khmt')
        if mon_hoc=='ktpm':
            dispatcher.utter_message(template='utter_tuvan_ktpm')
        if mon_hoc == 'httt':
            dispatcher.utter_message(template='utter_tuvan_httt')
        if mon_hoc == 'cntt':
            dispatcher.utter_message(template='utter_tuvan_cntt')
        if mon_hoc == 'khdl':
            dispatcher.utter_message(template='utter_tuvan_khdl')
        
        return []

class action_vieclam(Action):
    def name(self):
        return "action_vieclam"
    
    def run(self, dispatcher, tracker, domain):
        mon_hoc=tracker.latest_message['entities'][0]['value']
        print(mon_hoc)
        if mon_hoc=='khmt':
            dispatcher.utter_message(template='utter_khmt_vieclam')
        if mon_hoc=='ktpm':
            dispatcher.utter_message(template='utter_ktpm_vieclam')
        if mon_hoc == 'httt':
            dispatcher.utter_message(template='utter_httt_vieclam')
        if mon_hoc == 'cntt':
            dispatcher.utter_message(template='utter_cntt_vieclam')
        if mon_hoc == 'khdl':
            dispatcher.utter_message(template='utter_khdl_vieclam')
        
        return []

class action_tilesvratruong(Action):
    def name(self):
        return "action_tilesvratruong"
    
    def run(self, dispatcher, tracker, domain):
        mon_hoc=tracker.latest_message['entities'][0]['value']
        print(mon_hoc)
        if mon_hoc=='khmt':
            dispatcher.utter_message(template='utter_khmt_tilesvratruong')
        if mon_hoc=='ktpm':
            dispatcher.utter_message(template='utter_ktpm_tilesvratruong')
        if mon_hoc == 'httt':
            dispatcher.utter_message(template='utter_httt_tilesvratruong')
        if mon_hoc == 'cntt':
            dispatcher.utter_message(template='utter_cntt_tilesvratruong')
        if mon_hoc == 'khdl':
            dispatcher.utter_message(template='utter_khdl_tilesvratruong')
        
        return []

class action_canhtranh(Action):
    def name(self):
        return "action_canhtranh"
    
    def run(self, dispatcher, tracker, domain):
        mon_hoc=tracker.latest_message['entities'][0]['value']
        print(mon_hoc)
        if mon_hoc=='khmt':
            dispatcher.utter_message(template='utter_khmt_canhtranh')
        if mon_hoc=='ktpm':
            dispatcher.utter_message(template='utter_ktpm_canhtranh')
        if mon_hoc == 'httt':
            dispatcher.utter_message(template='utter_httt_canhtranh')
        if mon_hoc == 'cntt':
            dispatcher.utter_message(template='utter_cntt_canhtranh')
        if mon_hoc == 'khdl':
            dispatcher.utter_message(template='utter_khdl_canhtranh')
        
        return []
    
class action_tailieu(Action):
    def name(self):
        return "action_tailieu"
    
    def run(self, dispatcher, tracker, domain):
        mon_hoc=tracker.latest_message['entities'][0]['value']
        print(mon_hoc)
        if mon_hoc=='khmt':
            dispatcher.utter_message(template='utter_khmt_tailieu')
        if mon_hoc=='ktpm':
            dispatcher.utter_message(template='utter_ktpm_tailieu')
        if mon_hoc == 'httt':
            dispatcher.utter_message(template='utter_httt_tailieu')
        if mon_hoc == 'cntt':
            dispatcher.utter_message(template='utter_cntt_tailieu')
        if mon_hoc == 'khdl':
            dispatcher.utter_message(template='utter_khdl_tailieu')
        
        return []
    
class action_dinhhuongsai(Action):
    def name(self):
        return "action_dinhhuongsai"
    
    def run(self, dispatcher, tracker, domain):
        mon_hoc=tracker.latest_message['entities'][0]['value']
        print(mon_hoc)
        if mon_hoc=='khmt':
            dispatcher.utter_message(template='utter_khmt_dinhhuongsai')
        if mon_hoc=='ktpm':
            dispatcher.utter_message(template='utter_ktpm_dinhhuongsai')
        if mon_hoc == 'httt':
            dispatcher.utter_message(template='utter_httt_dinhhuongsai')
        if mon_hoc == 'cntt':
            dispatcher.utter_message(template='utter_cntt_dinhhuongsai')
        if mon_hoc == 'khdl':
            dispatcher.utter_message(template='utter_khdl_dinhhuongsai')
        
        return []

class action_ungdung(Action):
    def name(self):
        return "action_ungdung"
    
    def run(self, dispatcher, tracker, domain):
        mon_hoc=tracker.latest_message['entities'][0]['value']
        print(mon_hoc)
        if mon_hoc=='khmt':
            dispatcher.utter_message(template='utter_khmt_ungdung')
        if mon_hoc=='ktpm':
            dispatcher.utter_message(template='utter_ktpm_ungdung')
        if mon_hoc == 'httt':
            dispatcher.utter_message(template='utter_httt_ungdung')
        if mon_hoc == 'cntt':
            dispatcher.utter_message(template='utter_cntt_ungdung')
        if mon_hoc == 'khdl':
            dispatcher.utter_message(template='utter_khdl_ungdung')
        
        return []


class action_linhvuc(Action):
    def name(self):
        return "action_linhvuc"
    
    def run(self, dispatcher, tracker, domain):
        mon_hoc=tracker.latest_message['entities'][0]['value']
        print(mon_hoc)
        if mon_hoc=='khmt':
            dispatcher.utter_message(template='utter_khmt_linhvuc')
        if mon_hoc=='ktpm':
            dispatcher.utter_message(template='utter_ktpm_linhvuc')
        if mon_hoc == 'httt':
            dispatcher.utter_message(template='utter_httt_linhvuc')
        if mon_hoc == 'cntt':
            dispatcher.utter_message(template='utter_cntt_linhvuc')
        if mon_hoc == 'khdl':
            dispatcher.utter_message(template='utter_khdl_linhvuc')
        
        return []