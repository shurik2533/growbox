import joblib as joblib

from devices.fan import MAX_SPEED
from datetime import datetime

STATE_PATH = 'state.joblib'

STATE = {
    'fan': {
        'top': MAX_SPEED,
        'bottom': MAX_SPEED
    },
    'thermometer': {
        'top': None,
        'bottom': None,
        'external': None
    },
    'light': {
        '1': 'OFF',
        '2': 'OFF'
    },
    'humidity': {
        'humidity': None,
        'temperature': None
    },
    'co2': {
        'co2': None,
        'temperature': None
    },
    'soil_moisture': {
        'top': None,
        'bottom': None
    },
    'last_watering_time': {
        'top': datetime.now(),
        'bottom': datetime.now()
    },
    'heat': None
}


try:
    _state = joblib.load(STATE_PATH)
    STATE['last_watering_time'] = _state['last_watering_time']
    STATE['light'] = _state['light']
    STATE['heat'] = _state['heat']
except FileNotFoundError:
    pass
