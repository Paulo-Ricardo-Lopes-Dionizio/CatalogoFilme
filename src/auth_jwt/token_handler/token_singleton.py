from .token_creator import TokenCreator
token_creator = TokenCreator(
    token_key = 'secretKey',
    exp_time_min=30
)