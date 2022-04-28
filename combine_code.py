import pandas as pd

acros = pd.read_csv("glosses.csv")
out = []

ins = open("template.ins", "r").read()


dtx = open("template.dtx", "r").read()

code = open("template.sty", "r").read()

def underscorify(s):
    if "_" not in s:
        return s
    else:
        s = s.replace("_", "\\textsubscript{", 1)
        s = s.replace("_", "}")
        return s


for entry in acros.to_dict(orient="records"):
    out.append(
        "%%<package>\\DeclareAcronym{%s}{short=%s,long=%s,short-format=\\scshape}"
        % (
            entry["Abbreviation"].lower(),
            underscorify(entry["Abbreviation"]),
            entry["Meaning"],
        )
    )

with open("expex-acro.ins", "w") as f:
    f.write(ins)

with open("expex-acro.dtx", "w") as f:
    f.write(
        dtx.replace(
            "<<CODE_CONTENT>>", code
        ).replace("<<ABBREV_PLACEHOLDER>>", "\n".join(out))
    )
