from molecular_loader import load_molecule
from descriptors import num_chiral_centers

def test_num_chiral_centers():

    mol = load_molecule(
        "CC(O)C(=O)O"
    )

    assert num_chiral_centers(mol) == 1