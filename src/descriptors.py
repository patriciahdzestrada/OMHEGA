from chirality import get_chiral_centers


def num_chiral_centers(mol):

    centers = get_chiral_centers(mol)

    return len(centers)