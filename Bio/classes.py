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
            raise Exception('molType={} must be one of {}'.format(molType,
                                                                  self.allowedMolTypes))
        # check that code is not already used in the same structure
        chain = structure.getChain(code)
        if chain:
            raise Exception('code={} already used'.format(code))

        self.structure = structure
        self.code = code
        self.molType = molType
        # add this chain to the Parent structure
        structure.chainDict[code] = self
        structure.chains.append(self)

    def delete(self):
        """(Chain) -> NoneType

        Remove this chain from the dictionary and list of chains of the Parent
        structure
        """
        del self.structure.chainDict[self.code]
        self.structure.chains.remove(self)


class Residue:
    """ A Residue class

    Represent individual chemical compounds linked into a molecule
    """


class Atom:
    """ A Atom class

    Represent atoms found in linked chemical compounds
    """


if __name__ == "__main__":
    import doctest
    doctest.testmod()
