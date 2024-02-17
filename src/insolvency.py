class Insolvency:
    def __init__(self, publication_date, reference_number, curt, name, residence):
        self.publication_date = publication_date
        self.reference_number = reference_number
        self.curt = curt
        self.name = name
        self.residence = residence

    def __str__(self):
        return f'{self.publication_date}, {self.reference_number}, {self.curt}, {self.name}, {self.residence}'

