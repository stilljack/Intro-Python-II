import textwrap
# textwrap impl, send it text, it'll wrap and print it for ya
# edit this function to alter text wrap settings or do any other final processing on text,
# could be expanded concatanate multiple strs or whatever

tw = textwrap
class shared_func(object):


    lastType = ""

    def textwrapIMPL(self,text: str):
        final = tw.wrap(text, 80)

        for t in final:
            print(t)
            self.lastType=t

    def getLast(self):
        return self.lastType



sf = shared_func()
