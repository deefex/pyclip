def generate_counterstring(desired_marker, desired_length):
    counterstring = ''

    while desired_length > 0:
        appendage = desired_marker + str(desired_length)[::-1]
        if len(appendage) > desired_length:
            appendage = appendage[:desired_length]
        counterstring = counterstring + appendage
        desired_length -= len(appendage)

    return counterstring[::-1]
