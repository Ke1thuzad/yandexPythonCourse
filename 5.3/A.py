def error_handler():
    try:
        func()
    except ValueError:
        print('ValueError')
    except TypeError:
        print('TypeError')
    except SystemError:
        print('SystemError')
    else:
        print('No Exceptions')


error_handler()