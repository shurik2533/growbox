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
    }
}
