


def esBisiesto(age):
    if age % 400 == 0:
        return True
    elif age % 100 != 0 and age % 4 == 0:
        return True
    else:
        return False
    

print(esBisiesto(2000))