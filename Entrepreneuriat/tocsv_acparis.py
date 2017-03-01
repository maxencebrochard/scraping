

import os
import pandas as pd


path = os.path.realpath('./acparis')
#path = path + "/members_url_instit_loc_exp.json.try1"

path = path + "/acparis.json"

df = pd.read_json(path)

df.to_csv("acparis.csv",encoding="UTF-8", sep=";", index=None)
