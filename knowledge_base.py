# knowledge_base.py
import dspy

# We manually chunk the provided examples into a structured knowledge base.
# In a larger system, this could be automated and stored in a vector DB like ChromaDB.
SOC_KNOWLEDGE_BASE = [
    dspy.Example(
        content="""I. INTRODUCTION - This arbitration proceeding arises out of a predatory, deceptive, and fundamentally fraudulent solar panel financing scheme imposed upon Claimant, Ms. Marina Tellez—a medically disabled, low-income senior citizen living in Euless, Texas. The scheme was orchestrated by Respondents Texas Energy Resources Innovations LLC (“Texas Energy”), Sunlight Financial LLC (“Sunlight”), and Cross River Bank (“Cross River”), acting jointly to market, sell, and finance a grossly overpriced solar system under false pretenses.""",
        metadata={"doc_name": "Tellez_SOC", "section_title": "Introduction"}
    ).with_inputs("content"),
    dspy.Example(
        content="""V. BACKGROUND – CLAIMANT PROFILE - Karen Garcia and her husband, Jose Luna, are a working-class family living in Dallas. The couple built their home from the ground up in 2020 after years of saving. Their mortgage payments were manageable, and they were financially stable before entering into the solar agreement. At the time of the solar sale, their household income was modest and entirely dependent on Mr. Luna's labor. They were not shopping for solar panels. Rather, they were approached at home by Dynamic SLR sales representatives...""",
        metadata={"doc_name": "Garcia_SOC", "section_title": "Factual Background"}
    ).with_inputs("content"),
    dspy.Example(
        content="""IX. FILING OF FRAUDULENT LIEN - On September 1, 2021, GoodLeap filed a UCC-1 financing statement with the Texas Secretary of State. This lien falsely represents the solar panels and related hardware as personal property. Under Texas Civil Practice & Remedies Code § 12.002, it is unlawful to file a document that: 1. Is known to be false; 2. Is filed with the intent to cause harm; 3. Claims a property interest that does not exist. Here, the lien clouds title to the Garcias’ homestead and obstructs their ability to refinance or sell. It constitutes a fraudulent lien under Texas law.""",
        metadata={"doc_name": "Garcia_SOC", "section_title": "Fraudulent Lien"}
    ).with_inputs("content"),
    dspy.Example(
        content="""XI. LEGAL CAUSES OF ACTION - 1. Deceptive Trade Practices Act (Tex. Bus. & Com. Code § 17.41 et seq.) - Legal Elements: • Claimant is a consumer; • Respondents committed false, misleading, or deceptive acts; • The acts were a producing cause of damages. Application to Facts: Ms. Tellez qualifies as a consumer under the DTPA... Respondents misrepresented that the system would eliminate her energy bill; that the system would qualify her for automatic cost-reducing tax credits; and that the financing would be offset by savings. Each of these misrepresentations was material... Treble damages are available under § 17.50(b)(1) due to the knowing and intentional nature of these misrepresentations.""",
        metadata={"doc_name": "Tellez_SOC", "section_title": "Legal Cause of Action - DTPA"}
    ).with_inputs("content"),
    dspy.Example(
        content="""XI. LEGAL CAUSES OF ACTION - 3. Elder Fraud (Tex. Hum. Res. Code § 102.003; Tex. Bus. & Com. Code § 17.46(b)) - Texas law affords enhanced protections to elderly and disabled individuals. Ms. Tellez is both. Respondents targeted her with high-pressure sales tactics, knowing she was alone, physically frail, and dependent on others for assistance. The transaction was marked by concealment, exploitation, and coercion, rendering it abusive under elder protection statutes. The Texas DTPA allows enhanced penalties when the victim is an elderly consumer (over 60), which applies here.""",
        metadata={"doc_name": "Tellez_SOC", "section_title": "Legal Cause of Action - Elder Fraud"}
    ).with_inputs("content"),
    dspy.Example(
        content="""XII. PRAYER FOR RELIEF - Claimant respectfully requests the following relief: A. Rescission and Declaratory Relief - Cancel the solar loan contract; Order GoodLeap to remove the UCC lien; Declare that Claimant owes no further payment. B. Statutory Damages - $10,000 for the fraudulent lien; Treble damages under DTPA... C. Compensatory Damages... D. Exemplary Damages... E. Injunctive Relief...""",
        metadata={"doc_name": "Garcia_SOC", "section_title": "Prayer for Relief"}
    ).with_inputs("content"),
]
