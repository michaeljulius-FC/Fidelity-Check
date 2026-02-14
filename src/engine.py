import time
import sys

# UI Colors for Presentation
BOLD, RED, GREEN, YELLOW, BLUE, END = '\033[1m', '\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[0m'

def run_fidelity_check():
    print(f"{BLUE}{BOLD}>>> FIDELITY-CHECK v1.2: INTEGRATED ADVOCACY ENGINE{END}")
    print(f"{BLUE}CALIBRATED FOR: DELAWARE SECONDARY IEP STANDARDS{END}")
    time.sleep(1)
    
    # --- LAYER 1: DATA INGESTION (THE REALITY) ---
    print(f"\n{BOLD}STEP 1: INGESTING PERFORMANCE DATA...{END}")
    time.sleep(1)
    # Data pulled from 'IEP Redact Master-OB2425.pdf' and PowerSchool simulation
    student_data = {
        "Name": "O'Bryant Jr.",
        "Grade": "09",
        "English_Grade": 56,
        "Attendance_Rate": "82%",
        "Placement": "Setting C (Behavioral ILC)"
    }
    print(f"   {GREEN}✓ Student Profile: {student_data['Name']} (Grade {student_data['Grade']}){END}")
    print(f"   {GREEN}✓ PowerSchool English 9 Grade: {student_data['English_Grade']}%{END}")
    print(f"   {GREEN}✓ Current Placement: {student_data['Placement']}{END}")

    # --- LAYER 2: THE FIDELITY GAP (GRADE TO GOAL) ---
    print(f"\n{BOLD}STEP 2: ANALYZING GRADE-TO-GOAL FIDELITY...{END}")
    time.sleep(1.5)
    
    iep_goal_accuracy = 72 # From Page 3 of the IEP
    
    if student_data['English_Grade'] < iep_goal_accuracy:
        print(f"\n{RED}{BOLD}🚩 CRITICAL GAP DETECTED: PERFORMANCE VS. PROGRESS{END}")
        print(f"{RED}   The school reports {iep_goal_accuracy}% progress on Reading Goals,{END}")
        print(f"{RED}   but the student has a {student_data['English_Grade']}% failing grade in English 9.{END}")
        print(f"   {BOLD}ANALYSIS:{END} The Specially Designed Instruction (SDI) is not effective.")
    
    # --- LAYER 3: RED FLAGS & INCONSISTENCIES (WORD TWISTER) ---
    print(f"\n{BOLD}STEP 3: SCANNING FOR DOCUMENT INCONSISTENCIES...{END}")
    time.sleep(1.2)
    
    flags = [
        ("JARGON FLAG", "SDI (Specially Designed Instruction)", "Is the 60 min/week service actually happening?"),
        ("CAREER FLAG", "Military/Security Career", "Isolated ILC placement conflicts with social readiness needs."),
        ("SERVICE FLAG", "Attendance Impact", "IEP notes frequent absences; check if services are being made up.")
    ]

    for type, term, twist in flags:
        print(f"   {YELLOW}Checking {term}...{END}")
        time.sleep(0.7)
        print(f"   {YELLOW}🚩 {type}:{END} {twist}")

    # --- LAYER 4: THE TWISTED QUESTIONS ---
    print(f"\n{BOLD}STEP 4: GENERATING COLLABORATIVE ADVOCACY BRIEFING...{END}")
    time.sleep(1.5)
    
    print(f"\n{GREEN}{BOLD}>>> AUDIT COMPLETE. 1-PAGE SHIELD GENERATED.{END}")
    print(f"{BOLD}KEY QUESTION FOR TEAM:{END} 'If my child is hitting 72% of his IEP goals,")
    print("why is he failing the actual class? Where is the breakdown in Fidelity?'")

if __name__ == "__main__":
    run_fidelity_check()
