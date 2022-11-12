import os
import json5 as json


class portfolio:
    def __init__(self):
        self.DIR = os.path.dirname(os.path.realpath(__file__))
        self.file = os.path.join(self.DIR, 'portfolio.json')
        self.data = self.get_data(self.file)

    def get_data(self,file):
        try:
            with open(file,'r',encoding='utf-8') as f:
                return json.load(f)
        except:
            return []

    def set_data(self,data,file):
        with open(file,'w',encoding='utf-8') as f:
            json.dump(data,f,indent=4)

    def save(self):
        self.set_data(self.data,self.file)


def tag2icon(tag):
    i = {}
    i["icon"] = "mdi-square-rounded"
    i["tooltip"] = tag

    if tag == "Java":
        i["icon"] = "mdi-language-java"
    elif tag == "JavaScript":
        i["icon"] = "mdi-language-javascript"
    elif tag == "CSS":
        i["icon"] = "mdi-language-css3"
    elif tag == "Jupyter Notebook":
        i["icon"] = "mdi-circle"
        i["tooltip"] = "Jupyter Notebook/Lab"
    elif tag == "HTML":
        i["icon"] = "mdi-language-html5"
    elif tag == "Batchfile":
        i["icon"] = "mdi-console"
    elif tag == "PowerShell":
        i["icon"] = "mdi-powershell"
    elif tag == "PowerShell":
        i["icon"] = "mdi-powershell"
    elif tag == "TypeScript":
        i["icon"] = "mdi-language-typescript"
    elif tag == "C#":
        i["icon"] = "mdi-language-csharp"
    elif tag == "Shell":
        i["icon"] = "mdi-console"
    elif tag == "VBScript":
        i["icon"] = "mdi-script"
    elif tag == "Dart":
        i["icon"] = "mdi-bird"
        i["tooltip"] = "Flutter/Dart"
    elif tag == "GLSL":
        i["icon"] = "mdi-gradient-horizontal"
        i["tooltip"] = "GLSL/ShaderLab"
    elif tag == "ShaderLab":
        i["icon"] = "mdi-gradient-horizontal"
        i["tooltip"] = "GLSL/ShaderLab"
    elif tag == "Kotlin":
        i["icon"] = "mdi-language-kotlin"
    elif tag == "Swift":
        i["icon"] = "mdi-language-swift"
    elif tag == "alpha":
        i["icon"] = "mdi-alpha"
        i["tooltip"] = "alpha/abandoned"
    elif tag == "Python":
        i["icon"] = "mdi-language-python"

    return i

def name2description(name):
    desc = "sorry, i haven't writting a description yet."

    if name == "github-scraper":
        desc = "scrapes all my public github projects using python and selenium!"

    return desc


if __name__ == "__main__":

    import re

    pfo = portfolio()

    for p in pfo.data:

        # pc = re.sub(r'[^A-Za-z]+',',',str(p))
        # for w in re.split(',',pc):
        #     print(w)

        p["desc"] = name2description(p["name"])
        p["icons"] = []
        for t in p.get("tags"):
            p["icons"].append(tag2icon(t))
    
    # pfo.save()