import pandas as pd

from molecular_loader import load_molecule
from descriptors import num_chiral_centers


def main():

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

    results = []

    for _, row in df.iterrows():

        mol = load_molecule(
            row["smiles"]
        )

        centers = num_chiral_centers(mol)

        results.append({
            "name": row["name"],
            "smiles": row["smiles"],
            "chiral_centers": centers
        })

    result_df = pd.DataFrame(results)

    print(result_df)


if __name__ == "__main__":
    main()