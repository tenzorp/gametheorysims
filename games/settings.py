from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 1.00,
    'participation_fee': 0.00,
}

SESSION_CONFIGS = [
    {
        'name': 'beautyContest',
        'display_name': 'Beauty Contest',
        'num_demo_participants': 3,
        'app_sequence': ['beautyContest'],
    },
    {
        'name': 'prisoner',
        'display_name': "Prisoner's Dilemma",
        'num_demo_participants': 2,
        'app_sequence': ['prisoner'],
    },
    {
        'name': 'secondPrice',
        'display_name': 'Second Price Auction',
        'num_demo_participants': 2,
        'app_sequence': ['secondPrice'],
        'players_per_group': 3,
    },
    {
        'name': 'priceComp',
        'display_name': 'Price Competition',
        'num_demo_participants': 2,
        'app_sequence': ['priceComp']
    },
    {
        'name': 'frontrunner',
        'display_name': 'Frontrunner - Challenger',
        'num_demo_participants': 2,
        'app_sequence': ['frontrunner']
    },
    {
        'name': 'oneill',
        'display_name': "O'Neill Game",
        'num_demo_participants': 2,
        'app_sequence': ['oneill']
    },
    {
        'name': 'traveler',
        'display_name': "Traveler's Dilemma",
        'num_demo_participants': 2,
        'app_sequence': ['traveler']
    },
    {
        'name': 'minimum',
        'display_name': 'Minimum Effort Game',
        'num_demo_participants': 5,
        'app_sequence': ['minimum']
    },
    {
        'name': 'nct',
        'display_name': 'Non-credible Threat Game',
        'num_demo_participants': 2,
        'app_sequence': ['nct']
    },
]


LANGUAGE_CODE = 'en'

REAL_WORLD_CURRENCY_CODE = 'USD'
REAL_WORLD_CURRENCY_DECIMAL_PLACES = 2
USE_POINTS = False

ROOMS = [
    {
        'name': 'class',
        'display_name': 'Class',
    }
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = 'cv^w#tgt^!9@roz8uu(z%3lys64p^2=a*_%7xg(e#i^kxe%_#f'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
