from mattermost_bot.bot import respond_to


@respond_to('LHCPage1')
def lhc_pageone_reply(message):
    attachments = [{
        'fallback': 'https://vistar-capture.web.cern.ch/vistar-capture/lhc1.png',
        'author_name': 'CERN',
        'author_link': 'https://op-webtools.web.cern.ch/vistar/vistars.php',
        'image_url': 'https://vistar-capture.web.cern.ch/vistar-capture/lhc1.png',
        'text': '',
        'color': '#59afe1'
    }]
    message.reply_webapi(
        'LHCPage1', attachments,
        username='Mattermostbot',
        icon_url='https://goo.gl/OF4DBq',
    )
lhc_pageone_reply.__doc__ = "Shows LHC Page1"

@respond_to('LHCOperation')
def lhc_operation_reply(message):
    attachments = [{
        'fallback': 'https://vistar-capture.web.cern.ch/vistar-capture/lhc3.png',
        'author_name': 'CERN',
        'author_link': 'https://op-webtools.web.cern.ch/vistar/vistars.php',
        'image_url': 'https://vistar-capture.web.cern.ch/vistar-capture/lhc3.png',
        'text': '',
        'color': '#59afe1'
    }]
    message.reply_webapi(
        'LHC Operation page', attachments,
        username='Mattermostbot',
        icon_url='https://goo.gl/OF4DBq',
    )

lhc_operation_reply.__doc__ = "Shows LHC Operation page"


@respond_to('LHCCoordination')
def lhc_coordination_reply(message):
    attachments = [{
        'fallback': 'https://vistar-capture.web.cern.ch/vistar-capture/lhccoord.png',
        'author_name': 'CERN',
        'author_link': 'https://op-webtools.web.cern.ch/vistar/vistars.php',
        'image_url': 'https://vistar-capture.web.cern.ch/vistar-capture/lhccoord.png',
        'text': '',
        'color': '#59afe1'
    }]
    message.reply_webapi(
        'LHC Coordination page', attachments,
        username='Mattermostbot',
        icon_url='https://goo.gl/OF4DBq',
    )

lhc_coordination_reply.__doc__ = "Shows LHC Coordination page"


@respond_to('LHCCMS')
def lhc_cms_reply(message):
    attachments = [{
        'fallback': 'https://cmspage1.web.cern.ch/cmspage1/data/page1.png',
        'author_name': 'CMS',
        'author_link': 'https://cmspage1.web.cern.ch',
        'image_url': 'https://cmspage1.web.cern.ch/cmspage1/data/page1.png',
        'text': '',
        'color': '#59afe1'
    }]
    message.reply_webapi(
        'LHC CMS page1', attachments,
        username='Mattermostbot',
        icon_url='https://goo.gl/OF4DBq',
    )

lhc_cms_reply.__doc__ = "Shows LHC CMS page"
