 # -*- coding: utf-8 -*-
from mattermost_bot.bot import respond_to, listen_to
import os
import time
import getpass
import re

@respond_to('MittagessenNun')
@listen_to('MittagessenNun')
def mittagessen_aufruf(message):
    pass

mittagessen_aufruf.__doc__ = "KIT CN: Zeigt Speiseplan an und macht Umfrage, wer zum Mittagessen mitkommt"


@respond_to('MittagessenUm (.*)')
@listen_to('MittagessenUm (.*)')
def mittagessen_um(message, uhrzeit):
    pass

mittagessen_um.__doc__ = "KIT CN: Umfrage, wer zu einer bestimmten Zeit zum Mittagessen mitkommt."

@respond_to('SpeiseplanAnzeigen')
@listen_to('SpeiseplanAnzeigen')
def mittagessen_speiseplan(message):
    pass

mittagessen_speiseplan.__doc__ = u"KIT CN: Zeigt Speiseplan für einzelnen Benutzer an"

