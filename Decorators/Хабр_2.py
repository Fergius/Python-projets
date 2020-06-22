def talk():
    # Внутри определение функции "talk" мы можем определить другую
    def whisper(word="да"):
        return word.lower() +"...";
    print(whisper())


print(talk())