Ce projet automatise une valorisation DCF (Discounted Cash Flow) à partir d’un fichier Excel.
Il calcule automatiquement les Free Cash Flows actualisés, la valeur terminale, l’Enterprise Value (EV) et l’Equity Value, comme dans un modèle utilisé en Private Equity ou Corporate Finance.

🚀 Fonctionnalités

Importation des données financières (Excel) avec Pandas

Actualisation des Free Cash Flows sur plusieurs années

Calcul du WACC, de la valeur terminale, de l’EV et de l’Equity Value

🧮 Méthodes financières utilisées

Actualisation des flux :
PV = Cash Flow / (1 + WACC)^t

Valeur terminale :
Terminal Value = FCF_final × (1 + g) / (WACC − g)

Enterprise Value :
EV = Somme des flux actualisés + Valeur terminale actualisée

Equity Value :
Equity = EV − Dette nette

🛠 Technologies

Python • Pandas • NumPy

✨ Auteur

Sofia Kammoune
