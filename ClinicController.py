# Import the Doctor, Patient, and Consultation classes from their respective modules
from doctor import Doctor
from patient import Patient
from consultation import Consultation

class Clinic:
    def __init__(self):
        # Initialize a Clinic object with empty lists for doctors, patients, and consultations
        self.__doctors = []  # List to store doctor objects
        self.__patients = []  # List to store patient objects
        self.__consultations = []  # List to store consultation objects
    
    # Properties to access the lists of doctors, patients, and consultations
    @property
    def doctors(self):
        return self.__doctors

    @property
    def patients(self):
        return self.__patients

    @property
    def consultations(self):
        return self.__consultations
    
    # Setter for the doctors list (not recommended as it directly modifies the list)
    @doctors.setter
    def doctors(self, value):
        self.__doctors = value
    
    # Method to add a patient to the clinic
    def add_patient(self, patient):
        self.__patients.append(patient)

    # Method to add a doctor to the clinic
    def add_doctor(self, doctor):
        self.__doctors.append(doctor)
    
    # Method to add a consultation to the clinic
    def add_consultation(self, consultation):
        self.__consultations.append(consultation)

    # Methods to retrieve lists of doctors, patients, and consultations
    def get_all_doctors(self):
        return self.__doctors

    def get_all_patients(self):
        return self.__patients

    def get_all_consultations(self):
        return self.__consultations

    # Method to add a consultation to a patient
    def add_consultation_to_patient(self, patient_id, doctor_id, date, reason, fee):
        # Find the patient and doctor based on their IDs
        patient = self.find_patient_by_id(patient_id)
        doctor = self.find_doctor_by_id(doctor_id)

        # Check if all required consultation details are provided
        if not date or not reason or not fee:
            return "Please fill in all consultation details."
            
        if patient:
            # Check if the patient is already assigned a doctor
            if not patient.patient_doctor:
                return "Please assign a doctor to this patient first."
            
            if doctor:
                # Create a new consultation and add it to both doctor and patient
                consultation = Consultation(date, doctor, patient, reason, fee)
                doctor.add_consultation(consultation)
                patient.add_consultation(consultation)
                return "Consultation added."
            else:
                return "Doctor not found."
        else:
            return "Patient not found."

    # Method to assign a doctor to a patient
    def assign_doctor(self, patient_id, doctor_id):
        # Find the patient and doctor based on their IDs
        patient = self.find_patient_by_id(patient_id)
        doctor = self.find_doctor_by_id(doctor_id)

        if patient and doctor:
            # Check if the patient is already assigned a doctor
            if patient.patient_doctor is not None:
                return f"{patient.patient_fname} {patient.patient_lname} is already assigned to {patient.patient_doctor.doctor_fname} {patient.patient_doctor.doctor_lname}"

            try:
                # Assign the doctor to the patient using a new method
                doctor.assign_doctor_to_patient(doctor, patient)
                return f"Assigned {doctor.doctor_fname} {doctor.doctor_lname} to {patient.patient_fname} {patient.patient_lname}"
            except ValueError as e:
                return str(e)
        else:
            return "Patient or doctor not found."

    # Method to retrieve information about a patient
    def get_patient_info(self, patient_id):
        patient = self.find_patient_by_id(patient_id)
        
        if patient:
            # Generate patient information, including assigned doctor and consultations
            patient_info = f"Patient ID: {patient.patient_id}\n"
            patient_info += f"Name: {patient.patient_fname} {patient.patient_lname}\n"
            
            if patient.patient_doctor:
                patient_info += f"Doctor: {patient.patient_doctor.doctor_fname} {patient.patient_doctor.doctor_lname}\n"
            else:
                patient_info += "Doctor: Not assigned\n"
            
            total_fees = 0
            consultation_info = "Consultations:\n"
            for consultation in patient.get_consultations():
                total_fees += float(consultation.fee)
                consultation_info += f"Date: {consultation.date}\n"
                consultation_info += f"Reason: {consultation.reason}\n"
                consultation_info += f"Fee($): {consultation.fee}\n\n"
            
            patient_info += consultation_info
            patient_info += f"Total Fees($) Due: {total_fees}"
            
            return patient_info
        else:
            return "Patient not found."

    # Method to retrieve information about a doctor
    def get_doctor_info(self, doctor_id): 
        doctor = self.find_doctor_by_id(doctor_id)

        if doctor:
            # Generate doctor information, including patients and consultations
            doctor_info = f"Doctor ID: {doctor.doctor_id}\n"
            doctor_info += f"Name: {doctor.doctor_fname} {doctor.doctor_lname}\n"
            doctor_info += f"Specialization: {doctor.doctor_spec}\n"
            
            if doctor.get_patient_list():
                doctor_info += "\nList of Patients:\n"
                for patient in doctor.get_patient_list():
                    doctor_info += f"Patient ID: {patient.patient_id}, Name: {patient.patient_fname} {patient.patient_lname}\n"
            
            if doctor.get_consultation_list():
                doctor_info += "\nList of Consultations with Patients:\n"
                for consultation in doctor.get_consultation_list():
                    doctor_info += f"Date: {consultation.date}, Reason: {consultation.reason}, Patient: {consultation.patient.patient_fname} {consultation.patient.patient_lname}, Fee($): {consultation.fee}\n"
            
            return doctor_info
        else:
            print("Error: Doctor not found.")  # For demonstration, printing to console.         

    # Method to find a patient by their ID
    def find_patient_by_id(self, patient_id):
        for patient in self.get_all_patients():
            if str(patient.patient_id) == patient_id:
                return patient
        return None

    # Method to find a doctor by their ID
    def find_doctor_by_id(self, doctor_id):
        for doctor in self.get_all_doctors():
            if str(doctor.doctor_id) == doctor_id:
                return doctor
        return None
    
    # Method to load patients from a file
    def load_patients_from_file(self, filename):
        with open(filename, "r") as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                if line:
                    patient_info = line.split(",")
                    myPatientFName = patient_info[0]
                    myPatientLName = patient_info[1]
                    patient = Patient(myPatientFName, myPatientLName)
                    self.add_patient(patient)

    # Method to load doctors from a file
    def load_doctors_from_file(self, filename):
        with open(filename, "r") as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                if line:
                    doctor_info = line.split(",")
                    myDoctorFName = doctor_info[0]
                    myDoctorLName = doctor_info[1]
                    myDoctorSpec = doctor_info[2]
                    doctor= Doctor( myDoctorFName, myDoctorLName,myDoctorSpec)
                    self.add_doctor(doctor)

    # Method to generate a consultation report
    def generate_consultation_report(self):
        consultation_report = "Consultation report for Wellness Clinic:\n\n"
        total_fees = 0

        consultations = []

        # Collect all consultations from doctors
        for doctor in self.get_all_doctors():
            consultations.extend(doctor.get_consultation_list())

        # Sort consultations based on dates
        sorted_consultations = sorted(consultations, key=lambda consultation: consultation.date)

        for consultation in sorted_consultations:
            doctor = consultation.doctor
            patient = consultation.patient
            consultation_report += f"Doctor: {doctor.doctor_fname} {doctor.doctor_lname}\n"
            consultation_report += f"Date: {consultation.date}, Reason: {consultation.reason}, Patient: {patient.patient_fname} {patient.patient_lname}, Fee($): {consultation.fee}\n"
            total_fees += float(consultation.fee)
            consultation_report += "\n"

        consultation_report += f"\nTotal Fees($): {total_fees}"
        return consultation_report

    # Method to search for doctors based on search criteria
    def search_doctors(self, search_criteria):
        matching_doctors = []
        for doctor in self.get_all_doctors():
            doctor_info = f"{doctor.doctor_id} - {doctor.doctor_fname} {doctor.doctor_lname} ({doctor.doctor_spec})"
            if search_criteria in doctor_info.lower():
                matching_doctors.append(doctor_info)
        return matching_doctors

    # Method to search for patients based on search criteria
    def search_patients(self, search_criteria):
        matching_patients = []
        for patient in self.get_all_patients():
            patient_info = f"{patient.patient_id} - {patient.patient_fname} {patient.patient_lname}"
            if search_criteria in patient_info.lower():
                matching_patients.append(patient_info)
        return matching_patients
    
    # Method to validate consultation details
    def validate_consultation(self, date, selected_patient_indices, selected_doctor_indices, reason, fee):
        # Validate the date field
        if not date:
            return "Please select a date."

        # Validate that a patient and a doctor are selected
        if not selected_patient_indices:
            return "Please select a patient."
        if not selected_doctor_indices:
            return "Please select a doctor."

        # Validate the reason field
        if not reason:
            return "Please provide a reason for the consultation."

        # Validate the fee field (assuming it should be a positive number)
        if not fee:
            return "Please provide a consultation fee."
        try:
            fee = float(fee)
            if fee <= 0:
                return "Consultation fee must be a positive number."
        except ValueError:
            return "Invalid consultation fee. Please enter a valid number."

        # If no errors, return None
        return None

    def __str__(self):
        # Generate a string representation of the clinic object
        clinic_info = "Clinic Information:\n"
        clinic_info += f"Number of Doctors: {len(self.__doctors)}\n"
        clinic_info += f"Number of Patients: {len(self.__patients)}\n"
        clinic_info += f"Number of Consultations: {len(self.__consultations)}\n"
        return clinic_info
