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

listcn=['khmt']

class action_luong(Action):
    def name(self):
        return 'action_luong'
    def run(self,dispatcher, tracker, domain):
        mon_hoc=listcn[-1]
        if len(tracker.latest_message['entities'])>0:
            mon_hoc=tracker.latest_message['entities'][0]['value']
            listcn.append(mon_hoc)
        dispatcher.utter_message(template='utter_'+mon_hoc+'_luong')
        if mon_hoc=='khdl':
            dispatcher.utter_message(image=str('https://nordiccoder.com/app/uploads/2020/01/Screenshot-at-Jan-10-14-56-18.png'))
        elif mon_hoc=='cntt':
            dispatcher.utter_message(image=str('https://btec.fpt.edu.vn/wp-content/uploads/2019/07/2-1.jpg'))
        elif mon_hoc=='ktpm':
            dispatcher.utter_message(image=str('https://easyuni.com/media/uploads/2019/06/21/software-engineer-salary-worldwide-201920190226.png'))
        elif mon_hoc=='khmt':
            dispatcher.utter_message(image=str('https://media.bitdegree.org/storage/media/images/2020/01/computer-science-salary-entry-300x259.png'))
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
        print(listcn[-1])
        mon_hoc=tracker.latest_message['entities'][0]['value']
        listcn.append(mon_hoc)
        dispatcher.utter_message(template='utter_tuvan_'+mon_hoc)
        return []

class action_vieclam(Action):
    def name(self):
        return "action_vieclam"
    
    def run(self, dispatcher, tracker, domain):
        print(listcn[-1])
        mon_hoc=listcn[-1]
        if len(tracker.latest_message['entities'])>0:
            mon_hoc=tracker.latest_message['entities'][0]['value']
            listcn.append(mon_hoc)
        dispatcher.utter_message(template='utter_'+mon_hoc+'_vieclam')
        return []

class action_tilesvratruong(Action):
    def name(self):
        return "action_tilesvratruong"
    
    def run(self, dispatcher, tracker, domain):
        mon_hoc=listcn[-1]
        if len(tracker.latest_message['entities'])>0:
            mon_hoc=tracker.latest_message['entities'][0]['value']
            listcn.append(mon_hoc)
        dispatcher.utter_message(template='utter_'+mon_hoc+'_tilesvratruong')
        return []

class action_canhtranh(Action):
    def name(self):
        return "action_canhtranh"
    def run(self, dispatcher, tracker, domain):
        mon_hoc=listcn[-1]
        if len(tracker.latest_message['entities'])>0:
            mon_hoc=tracker.latest_message['entities'][0]['value']
            listcn.append(mon_hoc)
        dispatcher.utter_message(template='utter_'+mon_hoc+'_canhtranh')
        return []
    
    
class action_tailieu(Action):
    def name(self):
        return "action_tailieu"
    
    def run(self, dispatcher, tracker, domain):
        mon_hoc=listcn[-1]
        if len(tracker.latest_message['entities'])>0:
            mon_hoc=tracker.latest_message['entities'][0]['value']
            listcn.append(mon_hoc)
        dispatcher.utter_message(template='utter_'+mon_hoc+'_tailieu')
        return []

    
class action_dinhhuongsai(Action):
    def name(self):
        return "action_dinhhuongsai"
    
    def run(self, dispatcher, tracker, domain):
        mon_hoc=listcn[-1]
        if len(tracker.latest_message['entities'])>0:
            mon_hoc=tracker.latest_message['entities'][0]['value']
            listcn.append(mon_hoc)
        dispatcher.utter_message(template='utter_'+mon_hoc+'_dinhhuongsai')
        return []

class action_ungdung(Action):
    def name(self):
        return "action_ungdung"
    
    def run(self, dispatcher, tracker, domain):
        mon_hoc=listcn[-1]
        if len(tracker.latest_message['entities'])>0:
            mon_hoc=tracker.latest_message['entities'][0]['value']
            listcn.append(mon_hoc)
        dispatcher.utter_message(template='utter_'+mon_hoc+'_ungdung')
        return []


class action_linhvuc(Action):
    def name(self):
        return "action_linhvuc"
    
    def run(self, dispatcher, tracker, domain):
        mon_hoc=listcn[-1]
        if len(tracker.latest_message['entities'])>0:
            mon_hoc=tracker.latest_message['entities'][0]['value']
            listcn.append(mon_hoc)
        dispatcher.utter_message(template='utter_'+mon_hoc+'_linhvuc')
        return []

class action_monhoc(Action):
    def name(self):
        return "action_monhoc"
    def run(self, dispatcher, tracker, domain):
        mon_hoc=listcn[-1]
        if len(tracker.latest_message['entities'])>0:
            mon_hoc=tracker.latest_message['entities'][0]['value']
            listcn.append(mon_hoc)
        dispatcher.utter_message(template='utter_khmt_'+mon_hoc)
        return []

class action_kienthuccancokhiratruong(Action):
    def name(self):
        return "action_kienthuccancokhiratruong"
    
    def run(self, dispatcher, tracker, domain):
        mon_hoc=listcn[-1]
        if len(tracker.latest_message['entities'])>0:
            mon_hoc=tracker.latest_message['entities'][0]['value']
            listcn.append(mon_hoc)
        dispatcher.utter_message(template='utter_khmt_'+mon_hoc)        
        return []


class action_giangvien(Action):
    def name(self):
        return "action_giangvien"
    
    def run(self, dispatcher, tracker, domain):
        mon_hoc=listcn[-1]
        if len(tracker.latest_message['entities'])>0:
            mon_hoc=tracker.latest_message['entities'][0]['value']
            listcn.append(mon_hoc)
        dispatcher.utter_message(template='utter_'+mon_hoc+'_giangvien')
        return []


class action_ngonngu(Action):
    def name(self):
        return "action_ngonngu"
    
    def run(self, dispatcher, tracker, domain):
        mon_hoc=listcn[-1]
        if len(tracker.latest_message['entities'])>0:
            mon_hoc=tracker.latest_message['entities'][0]['value']
            listcn.append(mon_hoc)
        dispatcher.utter_message(template='utter_'+mon_hoc+'_ngonngu')
        return []


class action_laptrinh(Action):
    def name(self):
        return "action_laptrinh"
    
    def run(self, dispatcher, tracker, domain):
        mon_hoc=listcn[-1]
        if len(tracker.latest_message['entities'])>0:
            mon_hoc=tracker.latest_message['entities'][0]['value']
            listcn.append(mon_hoc)
        dispatcher.utter_message(template='utter_'+mon_hoc+'_laptrinh')
        return []