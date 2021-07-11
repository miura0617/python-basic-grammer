import logging
import logging.handlers

import config

smtp_host = 'smtp.live.com'
smtp_port = 587

from_email = 'xxx@hotmail.com'
from_email = config.from_email
to_email = 'xxx@hotmail.com'
to_email = config.to_email
username = 'xxx@hotmail.com'
username = config.username
password = 'fasefasfasdfa'
password = config.password

logger = logging.getLogger('email')
logger.setLevel(logging.CRITICAL)

logger.addHandler(logging.handlers.SMTPHandler(
    (smtp_host, stmp_port), from_email, to_email,
    subject='Admin test log',
    credentials=(username, password),
    secure=(None, None, None),
    timeout=20
))

logger.info('test')
logger.critical('critical')

