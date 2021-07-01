def main():
    list = [7, 8, 9]
    actualList = {
        0: 1,
        1: 8,
        3: 9
    }
    ford = {
        "year": 1999,
        "make": "Ford",
        "model": "ballsack"
    }
    for item in ford:
        print(f'{item}: {ford[item]}')

if __name__ == "__main__": main()