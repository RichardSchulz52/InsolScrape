class Insolvency:
    def __init__(self, reference_number, publication_date, curt, name, residence):
        self.reference_number = reference_number
        self.publication_date = publication_date
        self.curt = curt
        self.name = name
        self.residence = residence

    def __str__(self):
        return f'{self.publication_date}, {self.reference_number}, {self.curt}, {self.name}, {self.residence}'

