from devices.fan import MAX_SPEED

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
    }
}
