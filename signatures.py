# signatures.py
import dspy

class GenerateSection(dspy.Signature):
    """Generate a specific section of a legal Statement of Claims, following the provided context and client facts."""
    
    context = dspy.InputField(desc="Relevant examples and instructions from model legal documents.")
    client_facts = dspy.InputField(desc="A summary of all facts for the current client's case.")
    section_title = dspy.InputField(desc="The title of the section to be generated (e.g., 'Introduction', 'Filing of Fraudulent Lien').")
    
    section_text = dspy.OutputField(desc="The fully drafted text for the specified section, written in a persuasive, clear, and professional legal tone.", prefix="Draft:")

class GenerateLegalCauseOfAction(dspy.Signature):
    """Generate a detailed legal cause of action argument for a Statement of Claims.
    
    Instructions:
    1.  Thoroughly analyze the provided `example_argument` to understand the structure, tone, and legal citations for this cause of action.
    2.  State the legal elements for the `cause_of_action`.
    3.  Meticulously apply the specific `client_facts` to each legal element.
    4.  Construct a detailed, persuasive argument of at least 250 words explaining why each element is met.
    5.  DO NOT name the installer as a respondent, but mention their role in the scheme. The respondent is the financing company.
    """
    
    example_argument = dspy.InputField(desc="A model argument for this specific cause of action from a past successful case.")
    client_facts = dspy.InputField(desc="The complete factual summary of the current client's case.")
    cause_of_action = dspy.InputField(desc="The legal cause of action to be argued (e.g., 'DTPA', 'Fraudulent Lien').")

    legal_argument = dspy.OutputField(desc="The fully drafted, detailed legal argument for this cause of action.", prefix="Argument:")
