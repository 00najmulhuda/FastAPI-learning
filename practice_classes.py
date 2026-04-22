class Lead:
    def __init__(self,name,company,budget):
        self.name = name
        self.company = company
        self.budget = budget
    
    def is_hot_lead(self):
        if self.budget > 50000:
            return f"{self.name}  is a hot lead"
        else:
            return f"{self.name} is  cold lead"

lead1 = Lead("Najmul","zomato",800000)
lead2 = Lead("huda","amazon",30000)
lead3 = Lead("noor","flipkart",100000)

print(lead1.name,lead1.company,lead1.budget,lead1.is_hot_lead())
print(lead2.name,lead2.company,lead2.budget,lead2.is_hot_lead())
print(lead3.name,lead3.company,lead3.budget,lead3.is_hot_lead())