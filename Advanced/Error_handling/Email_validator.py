# Email validator

class NameTooShortError(Exception):
    """ Less than or equal to 4. """
    pass


class MustContainAtSymbolError(Exception):
    """ No '@' in the email. """
    pass


class InvalidDomainError(Exception):
    """ Invalid domain. Valid domains are: .com, .bg, .net, .org"""
    pass


def validate(email):
    valid_domains = ['com', 'bg', 'net', 'org']
    try:
        if '@' not in email:
            raise MustContainAtSymbolError('Email must contain @')
        elif len(email[:email.index('@')]) <= 4:
            raise NameTooShortError('Name must be more than 4 characters')
        elif email[email.index('.')+1:] not in valid_domains:
            raise InvalidDomainError('Domain must be one of the following: .com, .bg, .org, .net')
        else:
            print("Email is valid")
    except MustContainAtSymbolError as err:
        print('MustContainAtSymbolError:', err)
    except NameTooShortError as err:
        print('NameTooShortError:', err)
    except InvalidDomainError as err:
        print('InvalidDomainError:', err)


validate(input())
# validate(input())
