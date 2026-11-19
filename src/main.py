import pandas as pd

from molecular_loader import load_molecule
from descriptors import num_chiral_centers

data = {
    "name": [
        "Acido lactico",
        "Acido propanoico"
    ],
    "smiles": [
        "CC(O)C(=O)O",
        "CCC(=O)O"
    ]
}

df = pd.DataFrame(data)

for _, row in df.iterrows():

    mol = load_molecule(
        row["smiles"]
    )

    print(
        row["name"],
        num_chiral_centers(mol)
    )