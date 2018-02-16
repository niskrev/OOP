# from Ch 23 of Data science from scratch

class Table:
    """
    mimics table in SQL 
    columns: a list
    """
    def __init__(self, columns):
        self.columns = columns
        self.rows = []

    def __repr__(self):
        """
        pretty representation of the table, columns then rows
        :return: 
        """
        return str(self.columns) + "\n" + "\n".join(map(str, self.rows))

    def insert(self, row_values):
        if len(row_values) != len(self.columns):
            raise TypeError("wrong number of elements")
        row_dict = dict(zip(self.columns, row_values))
        self.rows.append(row_dict)
