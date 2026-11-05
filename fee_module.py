
#fee_module.py
def calculate_fee(training_days, fee_per_day):
    return training_days * fee_per_day


workshop_dict = {
    1: {"workshop_name": "Web Development Workshop", "training_days": 3, "fee_per_day": 120},
    2: {"workshop_name": "Mobile App Development Workshop", "training_days": 4, "fee_per_day": 150},
    3: {"workshop_name": "Data Analytics Workshop", "training_days": 5, "fee_per_day": 180}
}

class Participant:
    def __init__(self, participant_name, workshop_name, training_days, fee_per_day):
        self.participant_name = participant_name
        self.workshop_name = workshop_name
        self.training_days = training_days
        self.total_fee = calculate_fee(training_days, fee_per_day)
        self.category = "High Fee" if self.total_fee > 600 else "Normal Fee"

    def display_info(self):
        print(f"Participant Name : {self.participant_name}")
        print(f"Workshop Name    : {self.workshop_name}")
        print(f"Training Days    : {self.training_days}")
        print(f"Total Fee        : RM {self.total_fee:.2f}")
        print(f"Fee Category     : {self.category}")