from rdkit import Chem


def load_molecule(smiles):

    mol = Chem.MolFromSmiles(smiles)

    if mol is None:
        raise ValueError(
            f"SMILES inválido: {smiles}"
        )

    return mol