'''
以如下的json文件输入
[
    {
        attr:"姓名",
        value:[
            "张","李","王二麻子"
    ]},
    {
        attr:"年龄",
        value:[
            "18","50","36"
    ]},
    {
        attr:"身高",
        value:[
            "179","158","169"
    ]}
]
'''
import json
import os
import glob
class JSONtoLatexTable:
    Maxrow=10
    def __init__(self, jsonPath, outputPath):
        self.jsonFile = json.load(open(jsonPath,'r',encoding="utf8"))
        self.outputPath = outputPath
        self.head = "\\begin{table}[htbp]\n"
        self.alignment = "\t\\centering\n"
        self.caption = "\t\\caption{}\n"
        self.label = ""
        self.table = ""
        self.tail = "\\end{table}\n"

    def tableBlock(self, start,alignment,width=Maxrow):
        table=""
        tableHead="\t\\begin{tabular}{"+alignment*(width+1)+"}\n"
        tableTail="\t\t\\hline\n\t\\end{tabular}\n"
        for rows in self.jsonFile:
            tableRows = "\t\t\\hline\n\t\t"+rows["attr"]
            for v in rows["value"][start:start+width]:
                tableRows += ('&'+v.__str__())
            tableRows += "\\\\\n"
            table += tableRows
        return tableHead+table+tableTail

    def CreatTable(self,alignment='c'):
        width = len(self.jsonFile[0]["value"])
        table=""
        if width>self.Maxrow:
            blockNum = width//self.Maxrow
            lastBlockWidth = width%self.Maxrow
            for block in range(0,blockNum):
                table+=self.tableBlock(block*self.Maxrow,alignment)

            if(lastBlockWidth>0):
                table+=self.tableBlock(width*blockNum,alignment,lastBlockWidth)
        else:
            table+=self.tableBlock(0,alignment,width)
        self.table = table

    def setCaption(caption):
        self.caption = "\t\\caption{"+caption+"}\n"

    def setLabel(self, label):
        self.label = "\t\\label{"+label+"}\n"
    
    def setAlignment(self, alignment):
        self.alignment = "\t\\"+alignment+"\n"

    def Generate(self):
        fd = open(self.outputPath,'w', encoding="utf8")
        fd.write(self.head+self.alignment+self.caption+self.label+self.table+self.tail)
        fd.close()

P = JSONtoLatexTable("./data.json","./outputTest.txt")
P.CreatTable()
P.setCaption("一个合适的解")
P.Generate()

