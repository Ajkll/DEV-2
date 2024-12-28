class Plateau:
    def __init__(self, nbr_case=15, cases_speciales=None):
        self.nbr_case = nbr_case
        self.cases = [f"Case {i}" for i  in range(nbr_case)]
        self.cases_speciales = cases_speciales if cases_speciales else {}

    def est_case_valide(self, case):
        return  0 <= case < self.nbr_case

    def obtenir_effet_case(self, case):
        return self.cases_speciales.get(case, None)

    def afficher_cases(self):
        return self.cases

    def __str__(self):
        description = []
        for i in range(self.nbr_case):
            case_info = f"Case {i}"
            if i in self.cases_speciales:
                case_info += f" ({self.cases_speciales[i]})"
            description.append(case_info)
        return "\n".join(description)
