from deep_translator import GoogleTranslator

class Translation:

    def printer(self,inp_text ,trans_text):
        print(f"given text: {inp_text} -> translated text : {trans_text}")

    def Main(self):

        while True:

            inp = input("Enter the Text :")

            if inp.lower()  == "exit":
                print("Exitingggggg")
                return 

            translation = GoogleTranslator(source='auto', target='ko').translate(str(inp))
            self.printer(inp,translation)


if __name__ == "__main__":

    t = Translation()
    t.Main()


