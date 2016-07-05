 # -*- coding: utf-8 -*-
from mattermost_bot.bot import respond_to, listen_to

from calendarBot.calendarBotSettings import *
from calendarBot.calendarApi import *


@respond_to('KalenderHinzufuegen (.*) (.*)')
@listen_to('KalenderHinzufuegen (.*) (.*)')
def kalender_hinzufuegen(message, calendarName, calendarGroup):
    successful, res = createNewCalendar(calendarName, calendarGroup)
    if not successful:
        message.reply('Failure occurred: {0}'.format(res))
    else:
        message.reply('Successful: {0}'.format(res))

kalender_hinzufuegen.__doc__ = u"Fügt einen Kalender hinzu, Erster Eintrag: Kalendername, Zweiter Eintrag: Gruppe, in die die Events gepostet werden sollen"


@respond_to('EventHinzufuegen' +' ' + r'(\b\S+\b)' + ' ' + r'(\b\S+\b)' + ' ' +r'(\d{1,2}[.]\d{1,2}[.]\d{4}\s+\d{1,2}[:]\d{1,2})' + ' ' + r'(\d{1,2}[.]\d{1,2}[.]\d{4}\s+\d{1,2}[:]\d{1,2})' + r'(.*)', re.DOTALL)
@listen_to('EventHinzufuegen' +' ' + r'(\b\S+\b)' + ' ' + r'(\b\S+\b)' + ' ' +r'(\d{1,2}[.]\d{1,2}[.]\d{4}\s+\d{1,2}[:]\d{1,2})' + ' ' + r'(\d{1,2}[.]\d{1,2}[.]\d{4}\s+\d{1,2}[:]\d{1,2})' + r'(.*)', re.DOTALL)
def event_hinzufuegen(message, calendarName, eventName, eventStartDate, eventEndDate, eventDescription):
    successful, res = addEvent (calendarName, eventName, eventDescription, eventStartDate, eventEndDate)
    if not successful:
        message.reply('Failure occurred: {0}'.format(res))
    else:
        message.reply('Successful: {0}'.format(res))
        message.reply('Event was created:\n CalendarName: {0}\n eventName: {1}\n eventStartDate: {2}\n eventEndDate: {3}\n eventDescription: {4}'.format(calendarName, eventName, eventStartDate, eventEndDate, eventDescription))


event_hinzufuegen.__doc__ = u"Fuegt ein Event in den jeweiligen Kalender ein. Syntax EventHinzufuegen calendarName EventName 01.06.2016 12:00 01.06.2016 13:00 optionale Beschreibung"

@respond_to('AgendaHeuteAnzeigen' + r'(.*)', re.DOTALL)
@listen_to('AgendaHeuteAnzeigen' + r'(.*)', re.DOTALL)
def agenda_heute_anzeigen(message, calendarName):
    successful, res = showAgenda(calendarName)
    if not successful:
        message.reply('Failure occurred: {0}'.format(res))
    else:
        message.reply('Successful: {0} events found'.format(len(res)))
        for item in res:
            message.reply('EventName: {0}\n EventBeschreibung: {1}\n EventStart: {2}\n EventEnd: {3}\n EventLocation: {4}\n EventCategory: {5}\n\n'.format(item.subject, html2text.html2text(item.body), item.start.astimezone(EWSTimeZone.timezone('Europe/Copenhagen')), item.end.astimezone(EWSTimeZone.timezone('Europe/Copenhagen')), item.location, item.categories))


agenda_heute_anzeigen.__doc__ = u"Zeigt die heutige Agenda an. Falls kein Kalender angegeben wird, werden Ereignisse in allen Kalendern angezeigt. Syntax AgendaHeuteAnzeigen ttHgeneral"




@respond_to('AgendaAnzeigen' + r'(.*)' + ' '  +r'(\d{1,2}[.]\d{1,2}[.]\d{4})' + ' ' + r'(\d{1,2}[.]\d{1,2}[.]\d{4})', re.DOTALL)
@listen_to('AgendaAnzeigen' + r'(.*)', re.DOTALL)
def agenda_anzeigen(message, calendarName, startDate, endDate):
    successful, res = showAgenda(calendarName, startDate, endDate)
    if not successful:
        message.reply('Failure occurred: {0}'.format(res))
    else:
        message.reply('Successful: {0} events found'.format(len(res)))
        for item in res:
            message.reply('EventName: {0}\n EventBeschreibung: {1}\n EventStart: {2}\n EventEnd: {3}\n EventLocation: {4}\n EventCategory: {5}\n\n'.format(item.subject, html2text.html2text(item.body), item.start.astimezone(EWSTimeZone.timezone('Europe/Copenhagen')), item.end.astimezone(EWSTimeZone.timezone('Europe/Copenhagen')), item.location, item.categories))


agenda_anzeigen.__doc__ = u"Zeigt die Agenda für die jeweilige Zeitspanne an. Falls kein Kalender angegeben wird, werden Ereignisse in allen Kalendern angezeigt. Syntax AgendaAnzeigen ttHgeneral 01.06.2016 01.06.2016"


@respond_to('AgendaAnzeigen' + r'(.*)' + ' '  +r'(\d{1,2}[.]\d{1,2}[.]\d{4}\s+\d{1,2}[:]\d{1,2})' + ' ' + r'(\d{1,2}[.]\d{1,2}[.]\d{4}\s+\d{1,2}[:]\d{1,2})', re.DOTALL)
@listen_to('AgendaAnzeigen' + r'(.*)', re.DOTALL)
def agenda_anzeigen(message, calendarName, startDate, endDate):
    successful, res = showAgenda(calendarName, startDate, endDate)
    if not successful:
        message.reply('Failure occurred: {0}'.format(res))
    else:
        message.reply('Successful: {0} events found'.format(len(res)))
        for item in res:
            message.reply('EventName: {0}\n EventBeschreibung: {1}\n EventStart: {2}\n EventEnd: {3}\n EventLocation: {4}\n EventCategory: {5}\n\n'.format(item.subject, html2text.html2text(item.body), item.start.astimezone(EWSTimeZone.timezone('Europe/Copenhagen')), item.end.astimezone(EWSTimeZone.timezone('Europe/Copenhagen')), item.location, item.categories))


agenda_anzeigen.__doc__ = u"Zeigt die Agenda für die jeweilige Zeitspanne an. Falls kein Kalender angegeben wird, werden Ereignisse in allen Kalendern angezeigt. Syntax AgendaAnzeigen ttHgeneral 01.06.2016 15:00 01.06.2016 16:00"
