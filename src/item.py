from typing import KeysView


class Item:
    # * Hint: the name should be one word for ease in parsing later.
    name: str
    description: str

    def __init__(self, name: str, description: str):
        self.description = description
        self.name = name




listOfItems = {
    'gold': Item("Gold", """It's gold, it was in them hills, it is now here.
         With you.
        Enjoying you company."""),
    'money': Item("Money", """Fiat currency."""),
    'goop': Item("Goop", """Gwyenth paltrow's own Goop.
        The company, instantiated.
        This is not her yonic excretions. """),
    'vaporizer': Item("Vaporizer", """Don't let lambda see you use this on camera.
        Sweet nicotine.""")
}

#alias to item keys
#unneeded i suppose... still find it weird to ask if i ==e when i is not clearly the keys... i do not like python
#static typing and explicitness are crucicial... brb learning Rust.
itemKeys: KeysView[str] = listOfItems.keys()


def isItem(e):
        for i in listOfItems:
            if i == e:
                return True
            else:
                return False


testEntry = "vaporizer"
if (isItem(testEntry)):
    print(listOfItems[testEntry].name)
else:
    print(f"test entry = {testEntry} is not in itemList")
