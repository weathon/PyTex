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
c = c.replace("## ","\\subsection")
c = c.replace("# ","\\section")
while 1:
    begin = c.find("{{(")
    if begin==-1:
        break
    end = c.find("}}")
    cc = c[begin+3:end]

    cc = cc.replace(",","&")
    cc = cc.replace("\n",r"\\")

    cc = r"""\[
    \left[
    \begin{array}""" + cc + r"""\end{array}
    \right]
    \]"""
    cc = cc.replace(r"}\\","}")
    c = c[0:begin] + cc + c[end+2:]


while 1:
    begin = c.find("{{")
    if begin==-1:
        break
    end = c.find("}}")
    cc = c[begin+2:end]

    cc = cc.replace(",","&")
    cc = cc.replace("\n",r"\\")

    cc = r"""
    \begin{bmatrix}""" + cc + r"""\end{bmatrix}
    """
    cc = cc.replace(r"}\\","}")
    c = c[0:begin] + cc + c[end+2:]
f = open("tmp.tex","w")
c = f.write(t.replace("{{code here}}",c))
f.close()

os.system("pdflatex tmp.tex")