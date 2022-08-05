
def normalize(arg):
    try: 
        if (len(arg) == 0):
            return arg
        elif arg[0] == '"' and arg[-1] == '"':
            return arg[1:-1]
        else:
            return int(arg)

    except ValueError as e:
        raise Exception("Failed to parse argument -- " +
                        "use \"\" for string arguments.")
    except Exception as e:
        raise e

