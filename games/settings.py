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
        'name': 'company',
        'display_name': 'Acquiring a Company',
        'num_demo_participants': 2,
        'app_sequence': ['company']
    },
    {
        'name': 'pennies',
        'display_name': 'Asymmetric Matching Pennies',
        'num_demo_participants': 2,
        'app_sequence': ['pennies']
    },
    {
        'name': 'beautyContest',
        'display_name': 'Beauty Contest',
        'num_demo_participants': 3,
        'app_sequence': ['beautyContest'],
        'endowment': 100,
        'doc': """Edit the value of the 'endowment' variable to change the maximum guess that players may make."""
    },
    {
        'name': 'cooperative',
        'display_name': 'Cooperative Bargaining Game',
        'num_demo_participants': 2,
        'app_sequence': ['cooperative']
    },
    {
        'name': 'eleven',
        'display_name': '11-20 Game',
        'num_demo_participants': 2,
        'app_sequence': ['eleven']
    },
    {
        'name': 'frontrunner',
        'display_name': 'Frontrunner - Challenger',
        'num_demo_participants': 2,
        'app_sequence': ['frontrunner']
    },
    {
        'name': 'jobMarket',
        'display_name': 'Job Market Signaling',
        'num_demo_participants': 2,
        'app_sequence': ['jobMarket']
    },
    {
        'name': 'minimum',
        'display_name': 'Minimum Effort Game',
        'num_demo_participants': 5,
        'app_sequence': ['minimum'],
        'players_per_group': 5,
        'doc': """The 'players_per_group' variable is configurable and has a default value of 5."""
    },
    {
        'name': 'nct',
        'display_name': 'Non-credible Threat Game',
        'num_demo_participants': 2,
        'app_sequence': ['nct']
    },
    {
        'name': 'oneill',
        'display_name': "O'Neill Game",
        'num_demo_participants': 2,
        'app_sequence': ['oneill']
    },
    {
        'name': 'priceComp',
        'display_name': 'Price Competition',
        'num_demo_participants': 2,
        'app_sequence': ['priceComp']
    },
    {
        'name': 'prisoner',
        'display_name': "Prisoner's Dilemma",
        'num_demo_participants': 2,
        'app_sequence': ['prisoner']
    },
    {
        'name': 'repeatedFlip',
        'display_name': 'Repeated Game of Random Length',
        'num_demo_participants': 4,
        'app_sequence': ['repeatedFlip']
    },
    {
        'name': 'normalForm',
        'display_name': 'Repeated Normal Form Game',
        'num_demo_participants': 2,
        'app_sequence': ['normalForm'],
        'number_of_rounds': 10,
        'display_all_history': True,
        'doc': """The 'number_of_rounds' variable is configurable and has a default value of 10. The 'display_all_history' 
variable determines whether players see values from only the previous round of play or all rounds of play. Its
default value is false, so players can review choices from only one round."""
    },
    {
        'name': 'secondPrice',
        'display_name': 'Second Price Auction',
        'num_demo_participants': 4,
        'app_sequence': ['secondPrice'],
        'players_per_group': 4,
        'doc': """The 'players_per_group' variable is configurable and has a default value of 4."""
    },
    {
        'name': 'traveler',
        'display_name': "Traveler's Dilemma",
        'num_demo_participants': 2,
        'app_sequence': ['traveler']
    },
    {
        'name': 'trust',
        'display_name': 'Trust Game',
        'num_demo_participants': 2,
        'app_sequence': ['trust'],
        'endowment': 10,
        'multiplier': 3,
        'doc': """The 'endowment' variable determines how much Player A is initially given. The 'multiplier' variable 
        determines how much the amount sent by Player A is multiplied by. Default values are 10 and 3, respectively."""
    },
    {
        'name': 'ultimatum',
        'display_name': 'Ultimatum Game',
        'num_demo_participants': 2,
        'app_sequence': ['ultimatum']
    },
    {
        'name': 'voluntary',
        'display_name': 'Voluntary Contribution Game',
        'num_demo_participants': 5,
        'app_sequence': ['voluntary'],
        'players_per_group': 5,
        'doc': """The 'players_per_group' variable is configurable and has a default value of 5."""
    },
    {
        'name': 'punishment',
        'display_name': 'Voluntary Contributions with Punishment',
        'num_demo_participants': 4,
        'app_sequence': ['punishment'],
        'players_per_group': 4,
        'endowment': 20,
        'doc': """The 'players_per_group' variable is configurable and has a default value of 4. The 'endowment' variable
        determines how much money is given to each player in the first stage of the game."""
    }
]


LANGUAGE_CODE = 'en'

REAL_WORLD_CURRENCY_CODE = 'USD'
REAL_WORLD_CURRENCY_DECIMAL_PLACES = 2
USE_POINTS = False

ROOMS = [
    {
        'name': 'class',
        'display_name': 'Econ Classroom'
    }
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = 'Links for testing and demonstration. <br/> To launch a real study, either create persistent ' \
                       'links by setting up a room, or create a session through the sessions page.'

SECRET_KEY = 'cv^w#tgt^!9@roz8uu(z%3lys64p^2=a*_%7xg(e#i^kxe%_#f'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
