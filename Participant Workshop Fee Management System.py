def calculate_fee(training_days, fee_per_day):
    """Calculates and returns the total workshop fee."""
    return training_days * fee_per_day

# Dictionary storing workshop name, training days, and fee per day
workshop_dict = {
    1: {
        "workshop_name": "Web Development Workshop",
        "training_days": 3,
        "fee_per_day": 120
    },
    2: {
        "workshop_name": "Mobile App Development Workshop",
        "training_days": 4,
        "fee_per_day": 150
    },
    3: {
        "workshop_name": "Data Analytics Workshop",
        "training_days": 5,
        "fee_per_day": 180
    }
}

class Participant:
    def __init__(self,participant_name, workshop_name, training_days, fee_per_day):
        self.participant_name = participant_name
        self.workshop_name = workshop_name
        self.training_days = training_days
        self.fee_per_day = fee_per_day
        self.total_fee = training_days * fee_per_day
        
        # Fee category determination
        if self.total_fee > 600:
            self.category = "High Fee"
        else:
            self.category = "Normal Fee"
        
        
def display_info(self):
        print(f"Participant Name : {self.participant_name}")
        print(f"Workshop Name    : {self.workshop_name}")
        print(f"Training Days    : {self.training_days}")
        print(f"Total Fee        : RM {self.total_fee:.2f}")
        print(f"Fee Category     : {self.category}")
        print("-" * 40)

