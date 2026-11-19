from molecular_loader import load_molecule

def test_valid_smiles():

    mol = load_molecule(
        "CC(O)C(=O)O"
    )

    assert mol is not None