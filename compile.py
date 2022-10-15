import os
f = open("template.tex","r")
t = f.read()
f.close()

f = open("code.ptex","r")
c = f.read()
f.close()



c = c.replace("=>","$\Rightarrow$")
c = c.replace("Because","$\\because$")
c = c.replace("Therefore","$\\\\\\therefore$")
while 1:
    begin = c.find("{{")
    if begin==-1:
        break
    end = c.find("}}")
    cc = c[begin+2:end]

    cc = cc.replace(",","&")
    cc = cc.replace("\n",r"\\")

    cc = r"""\[
    \left[
    \begin{array}""" + cc + r"""\end{array}
    \right]
    \]"""
    cc = cc.replace(r"}\\","}")
    c = c[0:begin] + cc + c[end+2:]
f = open("tmp.tex","w")
c = f.write(t.replace("{{code here}}",c))
f.close()

os.system("pdflatex tmp.tex")