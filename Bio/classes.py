#!/Users/BadWiard/anaconda3/envs/py36/bin/python
class Structure:
    """" The Structure class

    A structure represents a group of polymer molecules
    Structure is a parent class to Chain. One Structure may have many Chains.
    But one structure has only one Chain with a given code. That is,
    (structure, code) is an unique identifier of a Chain.
    """

    def __init__(self, name, conformation=0, pdbIds=None):
        """(Structure, str, int, str) -> NoneType
        >>> structure = Structure('Chromosome Regulator', 0, '1A12')
        >>> structure.name
        'Chromosome Regulator'
        >>> structure.conformation
        0
        >>> structure.pdbIds
        '1A12'
        """

        if not name:
            raise Exception('name must be set to non-empty string')
        self.name = name
        self.conformation = conformation
        self.pdbIds = pdbIds

        self.chains = []  # For the children (list)
        self.chainDict = {}  # For the children (dictionary)

    def delete(self):
        """ (Structure) -> NoneType

        To delete the structure, delete all of its chains
        """
        for chain in self.chains:
            chain.delete()

    def getChain(self, code):
        """(Structure, str) -> Chain

        Return Chain with code code if it is in self.chains
        """
        return self.chainDict.get(code)  # None if code is not in chainDict


class Chain:
    """ A Chain class

    Represent one polymer molecule
    Chain is a child class of Structure. Each Child has only one Structure
    """

    allowedMolTypes = ('protein', 'DNA', 'RNA')

    def __init__(self, structure, code, molType='protein'):
        """(Chain, Structure, str, str) -> NoneType

        Construct a Chain defined uniquely by structure and code
        """

        if not code:
            raise Exception('code must be set to non-empty string')
        if molType not in self.allowedMolTypes:
            raise Exception('molType={} must be one of {}'.
                            format(molType, self.allowedMolTypes))
        # check that code is not already used in the same structure
        chain = structure.getChain(code)  # None if code is not in the structure
        if chain:
            raise Exception('code={} already used'.format(code))

        self.structure = structure
        self.code = code
        self.molType = molType
        # add this chain to the Parent structure dict and list

        self.resDict = {}  # For the children (dict)
        self.residues = []  # For the children (list)

        structure.chainDict[code] = self
        structure.chains.append(self)

    def delete(self):
        """(Chain) -> NoneType

        Remove this chain from the dictionary and list of chains of the Parent
        structure
        """

        for residue in self.residues:
            residue.delete()  # This is a method of residue

        del self.structure.chainDict[self.code]
        self.structure.chains.remove(self)

    def getResidue(self, seqId):
        """(Chain str) -> Residue

        Return a residue with seqId
        """

        return self.resDict.get(seqId)

    def getAtoms(self):
        """(Chain) -> list

        Return all atoms from all residues in self
        """

        atoms = []
        for residue in self.residues:
            atoms.extend(residue.atoms)
        return atoms


class Residue:
    """ A Residue class, Child class of Chain

    Represent individual chemical compounds linked into a molecule
    """

    def __init__(self, chain, seqId, code=None):
        """(Residue, Chain, str, str) -> NoneType

        Construct a residue, defined uniquely by its chain and seqId
        """

        if not seqId:
            raise Exception('seqId must be a non-empty string')

        residue = self.chain.getResidue(seqId)
        if residue:
            raise Exception('{} already used'.format(seqId))

        self.chain = chain
        self.seqId = seqId
        self.code = code

        self.atomDict = {}  # Children (dict)
        self.atoms = []  # Children (list)
        chain.resDict[seqId] = self  # Parent' link
        chain.residues.append(self)  # Parent's link

    def delete(self):
        """(Residue) -> NoneType

        Delete all atoms in the residue
        """

        for atom in self.atoms:
            atom.delete()
        del self.chain.resDict[self.seqId]
        self.chain.residues.remove(self)

    def getAtom(self, name):
        """(Residue, str) -> Atom
        """

        return self.atomDict.get(name)


class Atom:
    """ A Atom class, Child class of Residue

    Represent atoms found in linked chemical compounds
    """


if __name__ == "__main__":
    import doctest
    doctest.testmod()
