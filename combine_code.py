import pandas as pd

other = pd.read_csv("other.csv")
leipzig = pd.read_csv("leipzig.csv")

ACRO_VERSION = 3


ins = open("template.ins", "r").read()

dtx = open(f"template{ACRO_VERSION}.dtx", "r").read()

code = open(f"template{ACRO_VERSION}.sty", "r").read()


def underscorify(s):
    if "_" not in s:
        return s
    else:
        s = s.replace("_", "\\textsubscript{", 1)
        s = s.replace("_", "}")
        return s


def acro3gl(entry):
    return (
        "\\DeclareAcronym{%s}{short=%s,long=%s,short-format=\\scshape}"
        % (
            entry["Abbreviation"].lower().replace("_", ""),
            underscorify(entry["Abbreviation"]),
            entry["Meaning"].replace(" ", "~"),
        )
    )


def acro2gl(entry):
    return (
        "\\DeclareAcronym{%s}{short=%s,long=%s,short-format=\\scshape,class=gloss}"
        % (
            entry["Abbreviation"].lower().replace("_", ""),
            underscorify(entry["Abbreviation"]),
            entry["Meaning"],
        )
    )


leipzig_glosses = []
other_glosses = []
for entry in leipzig.to_dict(orient="records"):
    if ACRO_VERSION == 3:
        leipzig_glosses.append(acro3gl(entry))
    else:
        leipzig_glosses.append(acro2gl(entry))
for entry in other.to_dict(orient="records"):
    if ACRO_VERSION == 3:
        other_glosses.append(acro3gl(entry))
    else:
        other_glosses.append(acro2gl(entry))

with open("expex-acro.ins", "w") as f:
    f.write(ins)

with open("expex-acro.dtx", "w") as f:
    f.write(
        dtx.replace("<<CODE_CONTENT>>", code)
        .replace("<<ABBREV_PLACEHOLDER>>", "\n".join(other_glosses))
        .replace("<<LEIPZIG_PLACEHOLDER>>", "\n".join(leipzig_glosses))
    )
