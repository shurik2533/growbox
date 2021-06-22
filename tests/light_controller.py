import sys
from unittest import mock
from unittest.mock import call
import fake_rpi
from freezegun import freeze_time

from config import config
from config.config import MODES

sys.modules['RPi'] = fake_rpi.RPi     # Fake RPi
sys.modules['RPi.GPIO'] = fake_rpi.RPi.GPIO # Fake GPIO
config.MODE = MODES['vegetation']

from controllers.light_controller import LightController
from controllers import light_controller
from state import STATE

STATE['thermometer']['top'] = 24
STATE['thermometer']['bottom'] = 24


@freeze_time("2021-05-23 20:00")
def test_both_starts_greater_on():
    light_controller.DAY_STARTS_AT = '19:00'
    light_controller.DAY_ENDS_AT = '07:00'
    light_controller.LIGHT_MODE = 'both'

    with mock.patch('devices.relay.on') as mocked_method:
        lc = LightController(STATE)
        lc.control()
        expected = [call(8), call(25)]
        called = mocked_method.call_args_list
        assert expected == called

    assert STATE['light']['1'] == 'ON'
    assert STATE['light']['2'] == 'ON'


@freeze_time("2021-05-23 20:00")
def test_one_starts_greater_on():
    light_controller.DAY_STARTS_AT = '19:00'
    light_controller.DAY_ENDS_AT = '07:00'
    light_controller.LIGHT_MODE = 'one'

    with mock.patch('devices.relay.on') as mocked_method:
        lc = LightController(STATE)
        lc.control()
        expected = [call(8)]
        called = mocked_method.call_args_list
        assert expected == called

    assert STATE['light']['1'] == 'ON'
    assert STATE['light']['2'] == 'OFF'


@freeze_time("2021-05-23 08:00")
def test_both_starts_less_on():
    light_controller.DAY_STARTS_AT = '07:00'
    light_controller.DAY_ENDS_AT = '19:00'
    light_controller.LIGHT_MODE = 'both'

    with mock.patch('devices.relay.on') as mocked_method:
        lc = LightController(STATE)
        lc.control()
        expected = [call(8), call(25)]
        called = mocked_method.call_args_list
        assert expected == called

    assert STATE['light']['1'] == 'ON'
    assert STATE['light']['2'] == 'ON'


@freeze_time("2021-05-23 08:00")
def test_one_starts_less_on():
    light_controller.DAY_STARTS_AT = '07:00'
    light_controller.DAY_ENDS_AT = '19:00'
    light_controller.LIGHT_MODE = 'one'

    with mock.patch('devices.relay.on') as mocked_method:
        lc = LightController(STATE)
        lc.control()
        expected = [call(8)]
        called = mocked_method.call_args_list
        assert expected == called

    assert STATE['light']['1'] == 'ON'
    assert STATE['light']['2'] == 'OFF'


@freeze_time("2021-05-23 10:00")
def test_both_starts_greater_off():
    light_controller.DAY_STARTS_AT = '19:00'
    light_controller.DAY_ENDS_AT = '07:00'
    light_controller.LIGHT_MODE = 'both'

    with mock.patch('devices.relay.off') as mocked_method:
        lc = LightController(STATE)
        lc.control()
        expected = [call(8), call(25)]
        called = mocked_method.call_args_list
        assert expected == called

    assert STATE['light']['1'] == 'OFF'
    assert STATE['light']['2'] == 'OFF'


@freeze_time("2021-05-23 10:00")
def test_one_starts_greater_off():
    light_controller.DAY_STARTS_AT = '19:00'
    light_controller.DAY_ENDS_AT = '07:00'
    light_controller.LIGHT_MODE = 'one'

    with mock.patch('devices.relay.off') as mocked_method:
        lc = LightController(STATE)
        lc.control()
        expected = [call(8), call(25)]
        called = mocked_method.call_args_list
        assert expected == called

    assert STATE['light']['1'] == 'OFF'
    assert STATE['light']['2'] == 'OFF'


@freeze_time("2021-05-23 22:00")
def test_both_starts_less_off():
    light_controller.DAY_STARTS_AT = '07:00'
    light_controller.DAY_ENDS_AT = '19:00'
    light_controller.LIGHT_MODE = 'both'

    with mock.patch('devices.relay.off') as mocked_method:
        lc = LightController(STATE)
        lc.control()
        expected = [call(8), call(25)]
        called = mocked_method.call_args_list
        assert expected == called

    assert STATE['light']['1'] == 'OFF'
    assert STATE['light']['2'] == 'OFF'


@freeze_time("2021-05-23 23:00")
def test_one_starts_less_off():
    light_controller.DAY_STARTS_AT = '07:00'
    light_controller.DAY_ENDS_AT = '19:00'
    light_controller.LIGHT_MODE = 'one'

    with mock.patch('devices.relay.off') as mocked_method:
        lc = LightController(STATE)
        lc.control()
        expected = [call(8), call(25)]
        called = mocked_method.call_args_list
        assert expected == called

    assert STATE['light']['1'] == 'OFF'
    assert STATE['light']['2'] == 'OFF'


@freeze_time("2021-05-23 08:00")
def test_max_temperature():
    light_controller.DAY_STARTS_AT = '07:00'
    light_controller.DAY_ENDS_AT = '19:00'
    light_controller.LIGHT_MODE = 'both'
    STATE['thermometer']['top'] = 30
    STATE['thermometer']['bottom'] = 34

    with mock.patch('devices.relay.off') as mocked_method:
        lc = LightController(STATE)
        lc.control()
        expected = [call(8), call(25)]
        called = mocked_method.call_args_list
        assert expected == called

    assert STATE['light']['1'] == 'OFF'
    assert STATE['light']['2'] == 'OFF'
