import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from ClinicController import Clinic
from datetime import date
from tkcalendar import DateEntry

class ClinicGUI():
    def __init__(self, clinic):
        self.clinic = clinic
        self.window = tk.Tk()
        self.window.title("Wellness Clinic")
        self.window.geometry('760x500+50+50')
        self.window.resizable(False, False)

        # Create a style for ttk widgets to customize appearance
        style = ttk.Style()
        style.configure("TLabel", padding=(10, 5))
        style.configure("TButton", padding=(10, 5))
        style.configure("TEntry", padding=(5, 5))

        # Set a different theme for ttk widgets
        style.theme_use('clam')  # Choose a theme that suits your preference

        # Create main frame
        self.main_frame = ttk.Frame(self.window)
        self.main_frame.pack(padx=20, pady=20, expand=True, fill='both')

        # Create frames for patients, doctors, and consultations
        self.patient_frame = ttk.Frame(self.main_frame)
        self.patient_frame.pack(side=tk.LEFT, padx=10, pady=10)

        self.doctor_frame = ttk.Frame(self.main_frame)
        self.doctor_frame.pack(side=tk.LEFT, padx=10, pady=10)

        self.consultation_frame = ttk.Frame(self.main_frame)
        self.consultation_frame.pack(side=tk.TOP, padx=10, pady=20)
        # Create a new frame for additional functionalities
        self.extra_frame = ttk.Frame(self.window)
        self.extra_frame.pack(padx=20, pady=10, expand=True, fill='both', side='bottom')

        self.button_frame = ttk.Frame(self.window)
        self.button_frame.pack(padx=20, pady=10, expand=True, fill='both')

        # Labels and input fields for patients, doctors, and consultations
        self.patient_label = ttk.Label(self.patient_frame, text="Select Patient:")
        self.patient_label.pack()

        self.patient_listbox = tk.Listbox(
            self.patient_frame, selectmode=tk.SINGLE, exportselection=0)
        self.patient_listbox.pack()

        self.doctor_label = ttk.Label(self.doctor_frame, text="Select Doctor:")
        self.doctor_label.pack()

        self.doctor_listbox = tk.Listbox(
            self.doctor_frame, selectmode=tk.SINGLE, exportselection=0, height=10, width=30)
        self.doctor_listbox.pack()

        self.consultation_label = ttk.Label(self.consultation_frame, text="Consultation Details:")
        self.consultation_label.pack()

        self.date_label = ttk.Label(self.consultation_frame, text="Date (Double click):")
        self.date_label.pack()

        # Set the mindate to today's date
        self.date_entry = DateEntry(self.consultation_frame, date_pattern='yyyy-mm-dd', mindate=date.today())
        self.date_entry.pack()

        self.reason_label = ttk.Label(self.consultation_frame, text="Reason:")
        self.reason_label.pack()
        self.reason_entry = ttk.Entry(self.consultation_frame)
        self.reason_entry.pack()

        self.fee_label = ttk.Label(self.consultation_frame, text="Fee($):")
        self.fee_label.pack()
        self.fee_entry = ttk.Entry(self.consultation_frame)
        self.fee_entry.pack()

        # Buttons for additional functionalities
        self.patient_info_button = ttk.Button(
            self.extra_frame, text="Patient Information", command=self.show_patient_info)
        self.patient_info_button.pack(side='left', padx=20, pady=5)

        self.doctor_info_button = ttk.Button(
            self.extra_frame, text="Doctor Information", command=self.show_doctor_info)
        self.doctor_info_button.pack(side='left', padx=80, pady=5)

        self.exit_button = ttk.Button(
            self.extra_frame, text="Exit", command=self.exit_app)
        self.exit_button.pack(side='right', padx=50, pady=5)

        self.consultation_report_button = ttk.Button(
            self.button_frame, text="Consultation Report", command=self.show_consultation_report)
        self.consultation_report_button.pack(side='right', padx=80, pady=5)

        self.add_consultation_button = ttk.Button(
            self.consultation_frame, text="Add Consultation", command=self.add_consultation)
        self.add_consultation_button.pack(side='left', padx=40, pady=40)

        self.assign_button = ttk.Button(
            self.button_frame, text="Assign Doctor", command=self.assign_doctor)
        self.assign_button.pack(side='left', padx=140, pady=10)

        # Populate patient and doctor lists
        self.populate_patient_list()
        self.populate_doctor_list()

        # Search input fields and buttons for doctors and patients
        self.doctor_search_label = ttk.Label(self.doctor_frame, text="Search Doctor:")
        self.doctor_search_label.pack()

        self.doctor_search_entry = ttk.Entry(self.doctor_frame)
        self.doctor_search_entry.pack()

        self.patient_search_label = ttk.Label(self.patient_frame, text="Search Patient:")
        self.patient_search_label.pack()

        self.patient_search_entry = ttk.Entry(self.patient_frame)
        self.patient_search_entry.pack()

        self.doctor_search_button = ttk.Button(
            self.doctor_frame, text="Search", command=self.search_doctor)
        self.doctor_search_button.pack()

        self.patient_search_button = ttk.Button(
            self.patient_frame, text="Search", command=self.search_patient)
        self.patient_search_button.pack()

    def search_doctor(self):
        # Search for doctors based on input criteria
        search_criteria = self.doctor_search_entry.get().lower()
        matching_doctors = self.clinic.search_doctors(search_criteria)
        self.update_doctor_listbox(matching_doctors)

    def search_patient(self):
        # Search for patients based on input criteria
        search_criteria = self.patient_search_entry.get().lower()
        matching_patients = self.clinic.search_patients(search_criteria)
        self.update_patient_listbox(matching_patients)

    def update_doctor_listbox(self, doctor_list):
        # Update the doctor listbox
        self.doctor_listbox.delete(0, tk.END)  # Clear the listbox
        for doctor_info in doctor_list:
            self.doctor_listbox.insert(tk.END, doctor_info)

    def update_patient_listbox(self, patient_list):
        # Update the patient listbox
        self.patient_listbox.delete(0, tk.END)  # Clear the listbox
        for patient_info in patient_list:
            self.patient_listbox.insert(tk.END, patient_info)

    def populate_patient_list(self):
        # Populate the patient listbox with all patients
        patients = self.clinic.get_all_patients()
        for patient in patients:
            self.patient_listbox.insert(
                tk.END, f"{patient.patient_id} - {patient.patient_fname} {patient.patient_lname}")

    def populate_doctor_list(self):
        # Populate the doctor listbox with all doctors
        doctors = self.clinic.get_all_doctors()
        for doctor in doctors:
            self.doctor_listbox.insert(
                tk.END, f"{doctor.doctor_id} -  {doctor.doctor_fname} {doctor.doctor_lname} ({doctor.doctor_spec})")

    def assign_doctor(self):
        # Assign a doctor to a selected patient
        selected_patient_indices = self.patient_listbox.curselection()
        selected_doctor_indices = self.doctor_listbox.curselection()

        if selected_patient_indices and selected_doctor_indices:
            for patient_index in selected_patient_indices:
                patient_id = self.patient_listbox.get(patient_index).split(" - ")[0]

                for doctor_index in selected_doctor_indices:
                    doctor_id = self.doctor_listbox.get(doctor_index).split(" - ")[0]
                    result = self.clinic.assign_doctor(patient_id, doctor_id)
                    showinfo("Result", result)
        else:
            showinfo("Error", "Please select a patient and a doctor.")

    def add_consultation(self):
        # Add a consultation for selected patients and doctors
        selected_patient_indices = self.patient_listbox.curselection()
        selected_doctor_indices = self.doctor_listbox.curselection()
        date = self.date_entry.get_date() 
        reason = self.reason_entry.get()
        fee = self.fee_entry.get()
        validation_result = self.clinic.validate_consultation(date, selected_patient_indices, selected_doctor_indices, reason, fee)
        if validation_result:
            showinfo("Error", validation_result)
            return

        for patient_index in selected_patient_indices:
            patient_id = self.patient_listbox.get(patient_index).split(" - ")[0]

            for doctor_index in selected_doctor_indices:
                doctor_id = self.doctor_listbox.get(doctor_index).split(" - ")[0]
                result = self.clinic.add_consultation_to_patient(patient_id, doctor_id, date, reason, fee)
            showinfo("Result", result)

    def show_doctor_info(self):
        # Display information about a selected doctor
        selected_doctor_index = self.doctor_listbox.curselection()

        if selected_doctor_index:
            doctor_id = self.doctor_listbox.get(selected_doctor_index[0]).split(" - ")[0]
            doctor_info=self.clinic.get_doctor_info(doctor_id)
            showinfo("Doctor Information", doctor_info)
        else:
            showinfo("Error", "Please select a doctor.")

    def show_patient_info(self):
        # Display information about a selected patient
        selected_patient_index = self.patient_listbox.curselection()
        
        if selected_patient_index:
            patient_id = self.patient_listbox.get(selected_patient_index[0]).split(" - ")[0]
            patient_info = self.clinic.get_patient_info(patient_id)
            showinfo("Patient Information", patient_info)
        else:
            showinfo("Error", "Please select a patient.")

    def show_consultation_report(self):
        # Display the consultation report
        consultation_report = self.clinic.generate_consultation_report()
        report_window = tk.Toplevel(self.window)
        report_window.title("Consultation Report")
        report_text = tk.Text(report_window)
        report_text.pack()
        report_text.insert(tk.END, consultation_report)
        report_text.config(state=tk.DISABLED)  # Make the text widget read-only
   
    def run(self):
        # Run the main GUI loop
        self.window.mainloop()

    def exit_app(self):
        # Exit the application
        self.window.destroy()

def main():
    clinic = Clinic()  # Create a Clinic instance here
    clinic.load_patients_from_file("Patient.txt")
    clinic.load_doctors_from_file("Doctor.txt")
    app = ClinicGUI(clinic)
    app.run()

if __name__ == "__main__":
    main()
