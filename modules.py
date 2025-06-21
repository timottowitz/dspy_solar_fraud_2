# modules.py
import dspy
import signatures


class SectionGenerator(dspy.Module):
    def __init__(self):
        super().__init__()
        self.generate = dspy.ChainOfThought(signatures.GenerateSection)

    def forward(self, client_facts, context, section_title):
        return self.generate(
            client_facts=client_facts,
            context=context,
            section_title=section_title
        )


class LegalArgumentGenerator(dspy.Module):
    def __init__(self):
        super().__init__()
        self.generate = dspy.ChainOfThought(
            signatures.GenerateLegalCauseOfAction
        )

    def forward(self, client_facts, cause_of_action, example_argument):
        return self.generate(
            client_facts=client_facts,
            cause_of_action=cause_of_action,
            example_argument=example_argument
        )
