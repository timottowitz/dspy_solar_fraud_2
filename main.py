import dspy
import os
from dotenv import load_dotenv
from client_data import get_john_doe_data
from knowledge_base import SOC_KNOWLEDGE_BASE
from pipeline import StatementOfClaimsPipeline
from simple_retriever import SimpleRetriever


def generate_statement_of_claims(client_data: dict) -> str:
    """Generate the Statement of Claims document for the given client data."""
    load_dotenv()
    if not os.getenv("OPENAI_API_KEY"):
        raise ValueError("OPENAI_API_KEY not found in .env file.")

    # Configure DSPy to use a powerful model like GPT-4 Turbo
    llm = dspy.LM(
        model="openai/gpt-4-turbo-preview", max_tokens=4096, model_type="chat"
    )

    # Configure a lightweight retriever over our in-memory knowledge base
    retriever = SimpleRetriever(SOC_KNOWLEDGE_BASE)

    dspy.settings.configure(lm=llm, rm=retriever)

    print("DSPy configured successfully.")

    soc_pipeline = StatementOfClaimsPipeline(retriever=retriever)

    return soc_pipeline(client_data=client_data)


def main():
    # --- Load Example Data ---
    client_case_data = get_john_doe_data()
    print(f"Loaded data for new case: {client_case_data['client_name']}")

    print("\nGenerating Statement of Claims... This may take a few minutes.")
    final_document = generate_statement_of_claims(client_case_data)

    # --- 4. Save and Display Output ---
    output_filename = f"Solar_SOC_{client_case_data['client_name'].replace(' ', '_')}.txt"
    with open(output_filename, "w", encoding="utf-8") as f:
        f.write(final_document)

    print("\n" + "="*50)
    print(f"✅ Generation complete. Document saved as '{output_filename}'")
    print("="*50 + "\n")
    print("--- DOCUMENT PREVIEW ---")
    print(final_document)


if __name__ == "__main__":
    main()
