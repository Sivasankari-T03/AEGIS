from algorithms.forward_chaining import forward_chain

facts = ["fever", "cough"]

result = forward_chain(facts)

print("Known Facts:")
print(facts)

print("\nInference Result:")
print(result)