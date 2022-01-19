def handle_errors(error, message):
    def dec(func):
        def handler_func(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                if isinstance(e, error):
                    print(message)
                else:
                    raise e
        return handler_func
    return dec


@handle_errors(ValueError, "Interrupt")
@handle_errors(RuntimeError, "RunTimeError")
def my_func():
    raise RuntimeError("Ich bin ein Fehler o.o")


my_func()
