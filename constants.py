CAT_ENDPOINT = 'https://api.thecatapi.com/v1/images/search'
DOG_ENDPOINT = 'https://api.thedogapi.com/v1/images/search'

MESSAGES: dict[str, str] = {
    'start': (
        "Hey, {}, I'm KittyBot!\n\n"
        'My goal is to run up your mood with the cutest kitties'
    ),
    'one_more': (
        'Get another one - /kitty\n'
        'Are you stuck? - /help'
    ),
    'help': 'Type /kitty or hit a button on the keyboard to get one',
    'bad_request': 'Nice try!',
    'main_api_error': 'Main API request error: {}',
}
