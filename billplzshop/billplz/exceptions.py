"""
List of errors from Billplz
https://www.billplz.com/api#errors
"""

class BilplzException(Exception):
    default_message = ''

    def __init__(self, *args, **kwargs):
        if args or kwargs:
            super().__init__(*args, **kwargs)
        super().__init__(self.default_message)


class Unauthorized(BilplzException):
    """
    Invalid API key.
    """
    default_message = 'Invalid API key.'


class NotFound(BilplzException):
    """
    Specified resource could not be found.
    """
    default_message = 'Specified resource could not be found.'


class UnprocessableEntity(BilplzException):
    """
    Your passed parameter is invalid or resource could not be found.
    """
    default_message = 'Your passed parameter is invalid or resource could not \
                       be found.'


class TooManyRequests(BilplzException):
    """
    Reached rate limit.
    """
    default_message = 'Reached rate limit.'


class InternalServerError(BilplzException):
    """
    Internal Server Error -- We had a problem with our server. Try again later.
    """
    default_message = 'Internal Server Error -- We had a problem with our \
                       server. Try again later.'


class ServiceUnavailable(BilplzException):
    """
    We're temporarily offline for maintenance. Please try again later.
    """
    default_message = 'We\'re temporarily offline for maintenance. Please try \
                       again later.'
