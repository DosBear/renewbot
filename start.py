# -*- coding: utf-8 -*-
import os
import re
import sys
import config
import timeout
import logging
import mechanize
import telegrambot
import time
from logging.handlers import TimedRotatingFileHandler



def init():
    if (not os.path.exists(config.LOG_PATH)):    os.mkdir(config.LOG_PATH)
    handler = TimedRotatingFileHandler(os.path.join(config.LOG_PATH, config.LOG_FILE), when="midnight", interval=1)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    handler.suffix = "%Y%m%d"
    logging.getLogger().addHandler(handler)

    handler2 = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler2.setFormatter(formatter)
    handler2.suffix = "%Y%m%d"
    logging.getLogger().addHandler(handler2)


def IniProgInfo():
  with open(config.VERSION_PATH, 'r') as myfile:
    data=myfile.read()
  for prVer in config.SOFT_LIST:
    match= re.findall(prVer + config.MASK, data)
    if len(match)>0 :
       config.SOFT_LIST[prVer][1] = match[0]

#@timeout(30)
def getCTMServerResult():
    cnt = 0
    while True:
      try:
          br = mechanize.Browser()
          br.set_handle_robots(False)
          br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
          br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
          content = br.open(config.URL).read()
          return content
      except:
          logging.info( time.strftime("%d/%m/%Y %H:%M:%S") + " Exception in getCTMServerResult")
          content = ""
      cnt+=1
      if(content!="" or cnt>3): #try 3 times
        return content
    return content


def GetProgInfo():
    data = getCTMServerResult().decode("utf-8")
    with open(config.VERSION_PATH, "w") as text_file:
        text_file.write(data)
    for prVer in config.SOFT_LIST:
      match= re.findall(prVer + config.MASK, data)
      if len(match)>0 :
        if (config.SOFT_LIST[prVer][1] != match[0]):
          config.SOFT_LIST[prVer][1] = match[0]
          telegrambot.send_all(u"Вышла версия программы {0} {1}".format(config.SOFT_LIST[prVer][0], str(match[0])))

init()
IniProgInfo()

while(True):
    GetProgInfo();
    time.sleep(config.SLEEP_PERIOD)
