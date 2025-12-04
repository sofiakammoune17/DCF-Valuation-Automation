# -*- coding: utf-8 -*-
"""
Created on Wed May 21 13:37:32 2025

@author: GROUP STORE 237
"""

import pandas as pd

fichier = r'C:\Valorisation_DCF.xlsx'

df_flux = pd.read_excel(fichier, sheet_name="Flux Financiers")
df_params = pd.read_excel(fichier, sheet_name="Paramètres")

cash_flows = df_flux["Cash Flow"].dropna().values
ebitdas = df_flux["EBITDA"].dropna().values
revenus = df_flux["Chiffre d'Affaires"].dropna().values

parametres = dict(zip(df_params["Paramètre"], df_params["Valeur"]))
g = float(parametres["Taux de croissance à l'infini (g%)"]) / 100
r = float(parametres["Taux d'actualisation (r%)"]) / 100
dette = float(parametres["Dette nette"])

dcf = sum([cf / ((1 + r) ** (i + 1)) for i, cf in enumerate(cash_flows)])

vt = (cash_flows[-1] * (1 + g)) / (r - g)
vt_actualisee = vt / ((1 + r) ** 5)

ve = dcf + vt_actualisee

valeur_nette = ve - dette

print("===== RÉSULTATS DE LA VALORISATION DCF =====")
print(f"Valeur actuelle des cash flows sur 5 ans : {round(dcf, 2)}")
print(f"Valeur terminale actualisée : {round(vt_actualisee, 2)}")
print(f"Valeur de l’entreprise (EV) : {round(ve, 2)}")
print(f"Valeur nette de l’entreprise (Equity Value) : {round(valeur_nette, 2)}")
