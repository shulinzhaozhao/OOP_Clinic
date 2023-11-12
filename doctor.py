from patient import Patient  # Import the Patient class if not already imported

class Doctor:
    nextID = 1000  # Start from 1000 for the first doctor

    def __init__(self, myDoctorFName, myDoctorLName, myDoctorSpec=None):
        # Initialize the Doctor object with first name, last name, specialization, and default values
        self.__myDoctorFName = myDoctorFName  # First name of the doctor
        self.__myDoctorLName = myDoctorLName  # Last name of the doctor
        self.__myDoctorSpec = myDoctorSpec  # Specialization of the doctor
        self.__patients = []  # List of patients assigned to this doctor
        self.__consultations = []  # List of consultations for this doctor
        self.__myDoctorID = Doctor.nextID  # Assign a unique doctor ID
        # Increment the nextID for the next doctor
        Doctor.nextID += 1

    @property
    def doctor_id(self):
        return self.__myDoctorID  # Getter method for doctor ID

    @property
    def doctor_fname(self):
        return self.__myDoctorFName  # Getter method for doctor's first name

    @doctor_fname.setter
    def doctor_fname(self, fname):
        self.__myDoctorFName = fname  # Setter method for doctor's first name

    @property
    def doctor_lname(self):
        return self.__myDoctorLName  # Getter method for doctor's last name
    
    @doctor_lname.setter
    def doctor_lname(self, lname):
        self.__myDoctorLName = lname  # Setter method for doctor's last name
    
    @property
    def doctor_spec(self):
        return self.__myDoctorSpec  # Getter method for doctor's specialization
    
    @doctor_spec.setter
    def doctor_spec(self, spec):
        self.__myDoctorSpec = spec  # Setter method for doctor's specialization

    def get_patient_list(self):
        return self.__patients  # Getter method for the list of patients assigned to this doctor

    def add_consultation(self, consultation):
        self.__consultations.append(consultation)  # Add a consultation to the doctor's list

    def get_consultation_list(self):
        return self.__consultations  # Getter method for the list of consultations for this doctor

    def assign_doctor_to_patient(self, doctor, patient):
        self.__patients.append(patient)  # Add a patient to the list of patients assigned to this doctor
        patient.patient_doctor = self  # Assign this doctor to the patient

    def __str__(self):
        # Generate a string representation of the doctor object
        patient_list = ", ".join(
            [f"{patient.patient_fname} {patient.patient_lname}" for patient in self.__patients]
        )
        consultations_info = "\n".join(
            [
                f"Date: {consultation.date}, Reason: {consultation.reason}, Fee: {consultation.fee}"
                for consultation in self.__consultations
            ]
        )
        return (
            f"Doctor ID: {self.__myDoctorID}\n"
            f"Name: {self.__myDoctorFName} {self.__myDoctorLName}\n"
            f"Specialization: {self.__myDoctorSpec}\n"
            f"Patients: {patient_list}\n"
            f"Consultations:\n{consultations_info}"
        )
