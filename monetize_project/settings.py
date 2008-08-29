# Django settings for monetize_project project.

import os
ROOT_PATH = os.path.dirname(__file__)



MONETIZE_CONTEXT = {
    # Amazon Honor System
    'amazon_paypage':'url',

    # Amazon Affilliates (used for all others)
    'amazon_affiliates_id':'affiliates_id',

    # Amazon Affiliates: Custom Links
    'amazon_custom_link_title':'Look at the Kindle!',
    'amazon_custom_link_url':'http://www.amazon.com/etc/etc',

    # Amazon Affilliates: Omakase
    'amazon_omakase_width':'728',
    'amazon_omakase_height':'90',

    # Amazon Affiliates: Search
    'amazon_search_terms':"Django book",
    'amazon_search_title':"Search for Django books!",

    # Slicehost Referrals
    'slicehost_referral_id':'slicehost referal id',

    # Dreamhost Referrals
    'dreamhost_referral_code':'dreamhost referal id',

    # Google AdSense: Ad Unit
    'adsense_ad_unit_client':'ad unit client',
    'adsense_ad_unit_slot':'ad slot id',
    'adsense_ad_unit_width':'336',
    'adsense_ad_unit_height':'280',

    # Paypal
    'paypal_business':'email',
    'paypal_item_name':'name',
    'paypal_currency_code':'USD',
    'paypal_amount':None, # '5.00',
    'paypal_tax':'0',
    'paypal_lc':'US',
    'paypal_bn':'PP-DonationsBF',
    'paypal_image':'http://www.paypal.com/en_US/i/btn/btn_donate_LG.gif'
}

MONETIZE_TARGET = {
    'django':'django_monetize/amazon_search.html',
    'python':'django_monetize/paypal_donate.html',

}

MONETIZE_DEFAULT = 'django_monetize/slicehost_referral.html'

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = ''           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = ''             # Or path to database file if using sqlite3.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ''

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '#==th24xb_-*gpf-ovp@91cb+atycl-rlwc(jnim-j5erag^6t'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'monetize_project.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(ROOT_PATH, 'templates'),
)

INSTALLED_APPS = (
    'django_monetize',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
)
