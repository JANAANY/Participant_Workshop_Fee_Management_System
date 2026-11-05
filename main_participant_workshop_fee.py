# main_workshop.py
import streamlit
import fee_module

def main():
    participants_list = []
    streamlit.title("=== PARTICIPANT WORKSHOP FEE MANAGEMENT SYSTEM ===")
    
    num = int(streamlit.number_input("Enter number of participants to register:", min_value=1, step=1))
    
    for i in range(num):
        streamlit.write(f"\nParticipant {i+1}:")
        name = streamlit.text_input("Enter participant name:", key=f"name_{i}")
        streamlit.write("1 - Web Development Workshop (3 days, RM 120/day)")
        streamlit.write("2 - Mobile App Development Workshop (4 days, RM 150/day)")
        streamlit.write("3 - Data Analytics Workshop (5 days, RM 180/day)")
        
        choice = int(streamlit.number_input("Enter workshop choice (1/2/3): ", min_value=1, max_value=3, step=1))
        
        w_info = fee_module.workshop_dict[choice]
        p = fee_module.Participant(name, w_info["workshop_name"], w_info["training_days"], w_info["fee_per_day"])
        participants_list.append(p)
        
    streamlit.write("\n=== RECORD SUMMARY ===")
    for p in participants_list:
        p.display_info()

if __name__ == "__main__":
    main()
