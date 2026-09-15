rules = [
    {
        "if": ["fever", "cough"],
        "then": "flu"
    },
    {
        "if": ["flu"],
        "then": "rest_and_medicine"
    },
    {
        "if": ["headache", "fever"],
        "then": "viral_infection"
    }
]

def forward_chain(facts):

    inferred = facts.copy()
    changed = True

    while changed:
        changed = False

        for rule in rules:

            if all(condition in inferred for condition in rule["if"]):

                if rule["then"] not in inferred:
                    inferred.append(rule["then"])
                    changed = True

    return inferred