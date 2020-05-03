
import IncidentClassifier

class AnimalClassifier(IncidentClassifier.IncidentClassifier):
    def __init__(self, incidentOccured, isAnimal):
        super().__init__(self, incidentOccured)
        self.isAnimal = isAnimal