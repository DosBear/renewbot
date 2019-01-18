# -*- coding: utf-8 -*-
import os
import json
import config

with open('secrets.json', 'r') as f:
    SECRETS = json.load(f)

LOG_PATH = os.path.join(os.path.dirname(__file__), 'log')
LOG_FILE = 'renew.log'
VERSION_PATH = os.path.join(os.path.dirname(__file__),  'version.ini')
MASK = "=([0-9]+.[0-9]+)"
SLEEP_PERIOD = 60
URL = 'http://ftp.ctm.ru/ctm/Scripts/Versions.ini'
START_MESSAGE = "I'm just getting started"

SOFT_LIST= {
          'VEDPRICE':            [u'ВЭД-Контракт'   ,         ''  ],
          'REPORT':              [u'СТМ-Отчет'      ,         ''  ],
          'RAILINFO':            [u'Rail-Инфо'      ,         ''  ],
          'CONTROL':             [u'ВЭД-Контроль МП',         ''  ],
          'MONITOR_ED':          [u'Монитор ЭД'     ,         ''  ],
          'CONV2010':            [u'СТМ Конвертер'  ,         ''  ],
          'RailAddDues':         [u'Rail-Доп.сборы' ,         ''  ],
          'DCL':                 [u'ВЭД-Декларант'  ,         ''  ],
          'RAILTARIF':           [u'Rail-Тариф'     ,         ''  ],
          'TD':                  [u'Транспортные документы',  ''  ],
          'DCLPaymentDocs':      [u'Модуль платежей',         ''  ],
          'STS':                 [u'ВЭД-Склад',               ''  ],
          'FINANCE':             [u'СТМ-Финансы',             ''  ],
          'CSERVICE':            [u'СТМ-Сервис',              ''  ],
          'KPSPI':               [u'КПС ПИ',                  ''  ],
          'RAILTARIFRU':         [u'Rail-Тариф Россия',       ''  ],
          'PAYMENT':             [u'ВЭД-Платежи',             ''  ],
          'VED_INFO':            [u'ВЭД-Инфо',                ''  ],
          'ALPHABET':            [u'ВЭД-Алфавит',             ''  ],
          'RAILATLAS':           [u'Rail-Атлас',              ''  ],
          'CONTROLS32':          [u'ВЭД-Контроль',            ''  ],
          }
