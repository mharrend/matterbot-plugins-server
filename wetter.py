 # -*- coding: utf-8 -*-
from mattermost_bot.bot import respond_to, listen_to
import os
import pymsgbox
import time
import getpass
import re
import pyowm


@respond_to('WetterAktuellAnzeigen')
@listen_to('WetterAktuellAnzeigen')
def wetter_aktuell(message):
    # Wichtig, damit nur der ausfuehrende User die Antwort angezeigt bekommt
    if message.get_username() == getpass.getuser():
	owm = pyowm.OWM('dc9b24b06636a7fd46717bc4edef9b89')
	observation = owm.weather_at_place('Eggenstein-Leopoldshafen,de')
	w = observation.get_weather()
	message.reply('Wetter von %s' % w.get_reference_time(timeformat='iso'))
	temperature = w.get_temperature('celsius')
        message.reply('Aktuelle Temperatur {0}°C, Minimum Temperatur {1}°C, Maximum Temperatur {2}°C'.format(temperature['temp'],temperature['temp_min'],temperature['temp_max']))

wetter_aktuell.__doc__ = u"Zeigt aktuelles Wetter für KIT CN an"

@respond_to('WetterVorhersageAnzeigen')
@listen_to('WetterVorhersageAnzeigen')
def wetter_vorhersage(message):
    # Wichtig, damit nur der ausfuehrende User die Antwort angezeigt bekommt
    if message.get_username() == getpass.getuser():
        owm = pyowm.OWM('dc9b24b06636a7fd46717bc4edef9b89')
	fc = owm.daily_forecast('Eggenstein-Leopoldshafen,de', limit=3)
	f= fc.get_forecast()
        message.reply('Wettervorhersage von %s' % f.get_reception_time(timeformat='iso'))
	for weather in f:
		temperature = weather.get_temperature('celsius')
		message.reply('Vorhersage für {0}:\n Wetteraussicht {1}\n Temperaturverlauf morgens {2}°C, mittags {3}°C, abends {4}°C, nachts {5}°C'.format(
		weather.get_reference_time('iso'), weather.get_detailed_status(), temperature['morn'], temperature['day'], temperature['eve'], temperature['night']))

wetter_vorhersage.__doc__ = u"Zeigt Wettervorhersage für KIT CN an"

