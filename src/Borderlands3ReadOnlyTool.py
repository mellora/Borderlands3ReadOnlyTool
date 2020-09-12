from src.Tools import Borderlands3ReadOnlyTool

if __name__ == '__main__':
    test = Borderlands3ReadOnlyTool()
    for name in test.get_saves():
        print(name)
