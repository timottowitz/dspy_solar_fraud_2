# pipeline.py
import dspy
from modules import SectionGenerator, LegalArgumentGenerator

class StatementOfClaimsPipeline(dspy.Module):
    def __init__(self, retriever):
        super().__init__()
        self.retriever = retriever
        self.section_generator = SectionGenerator()
        self.legal_argument_generator = LegalArgumentGenerator()

    def forward(self, client_data):
        # --- 1. Consolidate Client Facts for Context ---
        client_facts_summary = "\n".join(f"- {k}: {v}" for k, v in client_data.items())
        
        # --- 2. Generate Sections using RAG ---
        
        # Introduction
        intro_context = self.retriever("Drafting a compelling introduction for a solar fraud case.", k=1)[0].long_text
        introduction = self.section_generator(client_facts=client_facts_summary, context=intro_context, section_title="Introduction")
        
        # Factual Background (combining several parts)
        background_context = self.retriever("Drafting a detailed factual background and claimant profile for a solar arbitration.", k=1)[0].long_text
        factual_background = self.section_generator(client_facts=client_facts_summary, context=background_context, section_title="Background, Claimant Profile, Sales Process, and Installation Defects")

        # Fraudulent Lien
        lien_context = self.retriever("How to argue a fraudulent lien was filed under Texas law in a solar case.", k=1)[0].long_text
        fraudulent_lien = self.section_generator(client_facts=client_facts_summary, context=lien_context, section_title="Filing of Fraudulent Lien")

        # --- 3. Generate Legal Causes of Action (Looping with RAG) ---
        legal_arguments = []
        causes_of_action = ["Deceptive Trade Practices Act (DTPA)", "Elder Fraud", "Filing of Fraudulent Lien"]
        
        for cause in causes_of_action:
            print(f"Drafting legal argument for: {cause}...")
            # Retrieve a specific example for *this* cause of action
            example_argument = self.retriever(f"Model legal argument for {cause} in a solar financing fraud case.", k=1)[0].long_text
            
            # Generate the new argument using the retrieved example
            argument = self.legal_argument_generator(
                client_facts=f"Factual Background:\n{factual_background.section_text}\n\nClient Data:\n{client_facts_summary}",
                cause_of_action=cause,
                example_argument=example_argument
            )
            legal_arguments.append(f"### {cause.upper()}\n\n{argument.legal_argument}")
        
        # Prayer for Relief
        prayer_context = self.retriever("Drafting the prayer for relief section, asking for rescission, damages, and fees.", k=1)[0].long_text
        prayer_for_relief = self.section_generator(client_facts=client_facts_summary, context=prayer_context, section_title="Prayer for Relief")

        # --- 4. Assemble the Final Document ---
        final_document = f"""STATEMENT OF CLAIMS
Before JAMS Arbitration – {client_data['client_name']} v. {client_data['financing_institution_name']}

I. INTRODUCTION
{introduction.section_text}

II. PARTIES
(This section can be generated similarly or templated)

... (Sections III-IV can be templated or generated) ...

V-VII. FACTUAL BACKGROUND
{factual_background.section_text}

IX. FILING OF FRAUDULENT LIEN
{fraudulent_lien.section_text}

XI. LEGAL CAUSES OF ACTION
{"\n\n".join(legal_arguments)}

XII. PRAYER FOR RELIEF
{prayer_for_relief.section_text}

Respectfully submitted,
Charles Bennett
Attorney for Claimant
"""
        return final_document
