# Projektmodell och spårbarhet

En sammanhängande Skill: technology-explanation. Monolitisk canonical instruktion valdes eftersom alla arbetslägen delar ansvar och målgrupp. Båda Knowledge-filer deklareras explicit; inga scripts eller assets. Detta undviker också en konflikt i motorn 1.6.33 där skill-contract.schema.json förbjuder resource_policy medan validate_generated_delivery.py kräver fältet för modular_skills. Ingen motorkod ändras.

Originalinstruktionen, samtliga avsnitt och exempel bevaras byte för byte i canonical/instructions.md. De redundanta källkopiorna avvecklades i steg 5; originalet finns i Git och verifieras via tests/baseline.json. Conversation starters och Knowledge bevaras byte för byte.

Fem mål är byggda och strukturellt verifierade i steg 4, men inte funktionellt verifierade. Custom GPT är historisk. Runtimeverktyg och användartillstånd krävs inte. Web är valfri. Ingen separat modellinstruktion.
