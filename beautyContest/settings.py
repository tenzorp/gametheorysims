from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 1.00,
    'participation_fee': 0.00,
    'doc': "",
}

SESSION_CONFIGS = [
    {
       'name': 'beautyContest',
       'display_name': "Beauty Contest",
       'num_demo_participants': 3,
       'app_sequence': ['beautyContest'],
    },
]


LANGUAGE_CODE = 'en'

REAL_WORLD_CURRENCY_CODE = 'USD'
REAL_WORLD_CURRENCY_DECIMAL_PLACES = 3
POINTS_DECIMAL_PLACES = 3
USE_POINTS = True

ROOMS = [
    {
        'name': 'class',
        'display_name': 'Class',
    }
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = "<h1>Active Sessions</h1>"


SECRET_KEY = '23b=-4m+s(=9s+r#5vbql+d#o_44)f-ya7zq0%3esza_gn7icq'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
