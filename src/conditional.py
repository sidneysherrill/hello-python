def main():
    isCold = True
    isUnopened = False


    if not isUnopened: print('Throw it away')
    elif not isCold: print('Put in the fridge')
    elif not isCold & isUnopened: print('Drink it')
    else: print('Do not drink it')

if __name__ == "__main__": main()