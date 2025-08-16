class Patient:
    def __init__(self, name, age, disease):
        self.name = name
        self.age = age
        self.disease = disease

def search_patients_by_disease(patients, disease):
    # If patients are Patient objects
    if all(isinstance(p, Patient) for p in patients):
        return [p.name for p in patients if p.disease.lower() == disease.lower()]
    # If patients are dictionaries
    else:
        return [p["Name"] for p in patients if p["Disease"].lower() == disease.lower()]

# Input example - list of dictionaries
patients = [
    {"Name": "Alice", "Age": 30, "Disease": "Flu"},
    {"Name": "Bob", "Age": 45, "Disease": "Diabetes"},
    {"Name": "Charlie", "Age": 35, "Disease": "Flu"}
]

search_disease = "Flu"

# Search and output
matching_patients = search_patients_by_disease(patients, search_disease)
print(f"Patients with {search_disease}: {matching_patients}")
