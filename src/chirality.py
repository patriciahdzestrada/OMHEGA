from rdkit import Chem


def get_chiral_centers(mol):

    return Chem.FindMolChiralCenters(
        mol,
        includeUnassigned=True
    )