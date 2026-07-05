from decision.decision_engine import calculate
from decision.recommendation import generate


class DecisionService:

    def process(self, report):

        report = calculate(report)

        report = generate(report)

        return report