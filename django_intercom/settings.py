from django.conf import settings

INTERCOM_APPID = getattr(settings, 'INTERCOM_APPID', None)
INTERCOM_SECURE_KEY = getattr(settings, 'INTERCOM_SECURE_KEY', None)
INTERCOM_ENABLE_INBOX = getattr(settings, 'INTERCOM_ENABLE_INBOX', True)
INTERCOM_ENABLE_INBOX_COUNTER = getattr(settings, 'INTERCOM_ENABLE_INBOX_COUNTER', True)
INTERCOM_INBOX_CSS_SELECTOR = getattr(settings, 'INTERCOM_INBOX_CSS_SELECTOR', '#Intercom')
INTERCOM_USER_DATA_CLASS = getattr(settings, 'INTERCOM_USER_DATA_CLASS', None)
INTERCOM_CUSTOM_DATA_CLASSES = getattr(settings, 'INTERCOM_CUSTOM_DATA_CLASSES', None)
INTERCOM_COMPANY_DATA_CLASS = getattr(settings, 'INTERCOM_COMPANY_DATA_CLASS', None)
INTERCOM_DISABLED = getattr(settings, 'INTERCOM_DISABLED', False)
INTERCOM_INCLUDE_USERID = getattr(settings, 'INTERCOM_INCLUDE_USERID', True)
INTERCOM_UNAUTHENTICATED_USER_EMAIL = getattr(settings, 'INTERCOM_UNAUTHENTICATED_USER_EMAIL', 'lead@example.com')
