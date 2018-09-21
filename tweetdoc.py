from sumy.nlp.tokenizers import Tokenizer

class word:
    word = ""
    def __init__(self,word):
        self.word = word

class sentence:
    content = ""
    words = []
    word_frequencies =[]
    tokens = ""
    tk = Tokenizer("english")
    fv = []
    def __init__(self,cont):
        self.content = cont
        self.tokens = cont.split()
        self.words = self.to_words(cont)
        for w in self.content.split():
            self.word_frequencies.append(word(w))

    def to_words(self,sent):
        return self.tk.to_words(sent)

class tweetdoc:
    sentences = []
    words = []
    documents ={}
    ct = 0
    def __init__(self):
        self.sentences=[]
        self.ct = 0
    def append(self,con):
        s = sentence(con)
        self.documents[self.ct] = s
        self.sentences.append(s)
        self.words.append(self.sentences[-1].words)

        self.ct = self.ct +1
