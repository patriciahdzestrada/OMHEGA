from molecular_loader import load_molecule
from chirality import get_chiral_centers

def test_lactic_acid():

    mol = load_molecule(
        "CC(O)C(=O)O"
    )

    centers = get_chiral_centers(mol)

    assert len(centers) == 1