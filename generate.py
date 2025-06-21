import sys
import json
from main import generate_statement_of_claims

if __name__ == "__main__":
    client_data = json.load(sys.stdin)
    document = generate_statement_of_claims(client_data)
    print(document)
