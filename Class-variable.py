class Bank:
    bank_name="ABC Bank"

    @classmethod
    def change_bank_name(cls, name):
        old_name=cls.bank_name
        cls.bank_name=name
        print(f"Change name from {old_name} to {name}")

        
my_bank=Bank.change_bank_name("Askari Bank")