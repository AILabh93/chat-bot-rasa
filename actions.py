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


class action_monhoc(Action):
    def name(self):
        return "action_monhoc"
    
    def run(self, dispatcher, tracker, domain):
        mon_hoc=tracker.latest_message['entities'][0]['value']
        print(mon_hoc)
        if mon_hoc=='khmt':
            dispatcher.utter_message(template='utter_khmt_monhoc')
        if mon_hoc=='ktpm':
            dispatcher.utter_message(template='utter_ktpm_monhoc')
        if mon_hoc == 'httt':
            dispatcher.utter_message(template='utter_httt_monhoc')
        if mon_hoc == 'cntt':
            dispatcher.utter_message(template='utter_cntt_monhoc')
        if mon_hoc == 'khdl':
            dispatcher.utter_message(template='utter_khdl_monhoc')
        
        return []

class action_kienthuccancokhiratruong(Action):
    def name(self):
        return "action_kienthuccancokhiratruong"
    
    def run(self, dispatcher, tracker, domain):
        mon_hoc=tracker.latest_message['entities'][0]['value']
        print(mon_hoc)
        if mon_hoc=='khmt':
            dispatcher.utter_message(template='utter_khmt_kienthuccancokhiratruong')
        if mon_hoc=='ktpm':
            dispatcher.utter_message(template='utter_ktpm_kienthuccancokhiratruong')
        if mon_hoc == 'httt':
            dispatcher.utter_message(template='utter_httt_kienthuccancokhiratruong')
        if mon_hoc == 'cntt':
            dispatcher.utter_message(template='utter_cntt_kienthuccancokhiratruong')
        if mon_hoc == 'khdl':
            dispatcher.utter_message(template='utter_khdl_kienthuccancokhiratruong')
        
        return []


class action_giangvien(Action):
    def name(self):
        return "action_giangvien"
    
    def run(self, dispatcher, tracker, domain):
        mon_hoc=tracker.latest_message['entities'][0]['value']
        print(mon_hoc)
        if mon_hoc=='khmt':
            dispatcher.utter_message(template='utter_khmt_giangvien')
        if mon_hoc=='ktpm':
            dispatcher.utter_message(template='utter_ktpm_giangvien')
        if mon_hoc == 'httt':
            dispatcher.utter_message(template='utter_httt_giangvien')
        if mon_hoc == 'cntt':
            dispatcher.utter_message(template='utter_cntt_giangvien')
        if mon_hoc == 'khdl':
            dispatcher.utter_message(template='utter_khdl_giangvien')
        
        return []


class action_ngonngu(Action):
    def name(self):
        return "action_ngonngu"
    
    def run(self, dispatcher, tracker, domain):
        mon_hoc=tracker.latest_message['entities'][0]['value']
        print(mon_hoc)
        if mon_hoc=='khmt':
            dispatcher.utter_message(template='utter_khmt_ngonngu')
        if mon_hoc=='ktpm':
            dispatcher.utter_message(template='utter_ktpm_ngonngu')
        if mon_hoc == 'httt':
            dispatcher.utter_message(template='utter_httt_ngonngu')
        if mon_hoc == 'cntt':
            dispatcher.utter_message(template='utter_cntt_ngonngu')
        if mon_hoc == 'khdl':
            dispatcher.utter_message(template='utter_khdl_ngonngu')
        
        return []



class action_laptrinh(Action):
    def name(self):
        return "action_laptrinh"
    
    def run(self, dispatcher, tracker, domain):
        mon_hoc=tracker.latest_message['entities'][0]['value']
        print(mon_hoc)
        if mon_hoc=='khmt':
            dispatcher.utter_message(template='utter_khmt_laptrinh')
        if mon_hoc=='ktpm':
            dispatcher.utter_message(template='utter_ktpm_laptrinh')
        if mon_hoc == 'httt':
            dispatcher.utter_message(template='utter_httt_laptrinh')
        if mon_hoc == 'cntt':
            dispatcher.utter_message(template='utter_cntt_laptrinh')
        if mon_hoc == 'khdl':
            dispatcher.utter_message(template='utter_khdl_laptrinh')
        
        return []
