# main_workshop.py
import fee_module

def main():
    participants_list = []
    print("=== PARTICIPANT WORKSHOP FEE MANAGEMENT SYSTEM ===")
    
    num = int(input("Enter number of participants to register: "))
    
    for i in range(num):
        print(f"\nParticipant {i+1}:")
        name = input("Enter participant name: ")
        print("1 - Web Development Workshop (3 days, RM 120/day)")
        print("2 - Mobile App Development Workshop (4 days, RM 150/day)")
        print("3 - Data Analytics Workshop (5 days, RM 180/day)")
        
        choice = int(input("Enter workshop choice (1/2/3): "))
        
        w_info = fee_module.workshop_dict[choice]
        p = fee_module.Participant(name, w_info["workshop_name"], w_info["training_days"], w_info["fee_per_day"])
        participants_list.append(p)
        
    print("\n=== RECORD SUMMARY ===")
    for p in participants_list:
        p.display_info()

if __name__ == "__main__":
    main()