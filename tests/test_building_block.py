import os
import numpy as np
import rdkit.Chem.AllChem as rdkit
import stk
import pickle

if not os.path.exists('building_block_tests_output'):
    os.mkdir('building_block_tests_output')


def test_init(amine2):
    assert len(amine2.func_groups) == 2
    assert amine2.func_groups[0].info.name == 'amine'
    assert len(amine2.atoms) == 5
    assert len(amine2.bonds) == 4


def test_bonder_centroids(tmp_aldehyde3):
    shape = (3, tmp_aldehyde3.mol.GetNumAtoms())
    tmp_aldehyde3.set_position_from_matrix(np.zeros(shape))

    for i, centroid in enumerate(tmp_aldehyde3.bonder_centroids()):
        assert len(centroid) == 3
        assert sum(centroid) < 1e-5
    assert i == 2


def test_bonder_plane():
    assert False


def test_bonder_plane_normal():
    assert False


def test_bonder_distances():
    assert False


def test_bonder_direction_vectors(tmp_aldehyde3):
    pos_mat = tmp_aldehyde3.position_matrix()
    # Set the coordinate of each bonder to the id of the fg.
    for fg in tmp_aldehyde3.func_groups:
        for bonder in fg.bonder_ids:
            pos_mat[:, bonder] = [fg.id, fg.id, fg.id]
    tmp_aldehyde3.set_position_from_matrix(pos_mat)

    dir_vectors = tmp_aldehyde3.bonder_direction_vectors()
    for i, (id1, id2, v) in enumerate(dir_vectors):
        # Calculate the expected direction vector based on ids.
        d = stk.normalize_vector(np.array([id2]*3) - np.array([id1]*3))
        assert np.allclose(d, v, atol=1e-8)
    assert i == 2


def test_centroid_centroid_direction_vector(aldehyde3):
    c1 = aldehyde3.bonder_centroid()
    c2 = aldehyde3.centroid()
    assert np.allclose(stk.normalize_vector(c2-c1),
                       aldehyde3.centroid_centroid_dir_vector(),
                       atol=1e-8)


def test_functional_groups(amine2):
    info = amine2.func_groups[0].info
    func_grp_mol = rdkit.MolFromSmarts(info.fg_smarts)
    fg_atoms = amine2.mol.GetSubstructMatches(func_grp_mol)
    for fg in amine2.functional_groups([info.name]):
        assert any(ids == fg.atom_ids for ids in fg_atoms)


def test_json_init(tmp_amine2):
    path = os.path.join('building_block_tests_output', 'mol.json')

    tmp_amine2.test_attr1 = 'something'
    tmp_amine2.test_attr2 = 12
    tmp_amine2.test_attr3 = ['12', 'something', 21]
    include_attrs = ['test_attr1', 'test_attr2', 'test_attr3']

    tmp_amine2.dump(path, include_attrs)
    mol2 = stk.Molecule.load(path)

    assert isinstance(tmp_amine2.file, str)
    assert tmp_amine2 is not mol2
    assert tmp_amine2.atom_props == tmp_amine2.atom_props
    assert mol2.func_groups == tmp_amine2.func_groups

    assert tmp_amine2.test_attr1 == mol2.test_attr1
    assert tmp_amine2.test_attr2 == mol2.test_attr2
    assert tmp_amine2.test_attr3 == mol2.test_attr3


def test_caching():
    # This test is in a try block because pytest runs with
    # molecule cache turned off. If this test fails, the finally
    # clause ensures that the cache remains off so other tests are
    # not affected by unexpected cache problems.
    try:
        stk.OPTIONS['cache'] = True
        mol = stk.BuildingBlock.smiles_init('NCCCN', ['amine'])
        mol2 = stk.BuildingBlock.smiles_init('NCCCN', ['amine'])
        assert mol is mol2

        mol3 = stk.BuildingBlock.smiles_init('NCCCN', ['aldehyde'])
        assert mol3 is not mol

        stk.OPTIONS['cache'] = False
        mol4 = stk.BuildingBlock.smiles_init('NCCCN', ['amine'])
        stk.OPTIONS['cache'] = True
        assert mol is not mol4

    except Exception:
        raise

    finally:
        stk.OPTIONS['cache'] = False


def test_shift_fgs(amine4):
    ids = [10, 20, 30, 40]
    shifted = amine4.shift_fgs(ids, 32)

    for i, (fg1, fg2) in enumerate(zip(amine4.func_groups, shifted)):
        assert fg1 is not fg2
        assert fg2.id == ids[i]

        for a1, a2 in zip(fg1.atom_ids, fg2.atom_ids):
            assert a1 + 32 == a2

        for a1, a2 in zip(fg1.bonder_ids, fg2.bonder_ids):
            assert a1 + 32 == a2

        for a1, a2 in zip(fg1.deleter_ids, fg2.deleter_ids):
            assert a1 + 32 == a2


def test_pickle(amine2):
    result = pickle.loads(pickle.dumps(amine2))
    assert result.same(amine2)
