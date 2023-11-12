class Patient:
    nextID = 100  # Initialize nextID to 100

    def __init__(self, myPatientFName, myPatientLName):
        # Initialize the Patient object with first name, last name, and default values
        self.__myPatientID = Patient.nextID  # Assign a unique patient ID
        self.__myPatientFName = myPatientFName  # First name of the patient
        self.__myPatientLName = myPatientLName  # Last name of the patient
        self.__myDoctor = None  # The doctor assigned to this patient
        self.__consultations = []  # List of consultations for this patient

        # Increment the nextID for the next patient
        Patient.nextID += 1

    @property
    def patient_id(self):
        return self.__myPatientID  # Getter method for patient ID

    @property
    def patient_fname(self):
        return self.__myPatientFName  # Getter method for patient's first name

    @patient_fname.setter
    def patient_fname(self, fname):
        self.__myPatientFName = fname  # Setter method for patient's first name

    @property
    def patient_lname(self):
        return self.__myPatientLName  # Getter method for patient's last name

    @patient_lname.setter
    def patient_lname(self, lname):
        self.__myPatientLName = lname  # Setter method for patient's last name

    @property
    def patient_doctor(self):
        return self.__myDoctor  # Getter method for the assigned doctor

    @patient_doctor.setter
    def patient_doctor(self, doctor):
        self.__myDoctor = doctor  # Setter method for assigning a doctor to the patient

    def get_consultations(self):
        return self.__consultations  # Getter method for patient's consultations

    def add_consultation(self, consultation):
        if consultation not in self.__consultations:
            self.__consultations.append(consultation)  # Add a consultation to the patient's list

    def __str__(self):
        # Generate a string representation of the patient object
        doctor_name = (
            f"{self.__myDoctor.doctor_fname} {self.__myDoctor.doctor_lname}"
            if self.__myDoctor
            else "Not assigned"
        )

        consultations_info = "\n".join(
            [
                f"Date: {consultation.date}, Reason: {consultation.reason}, Fee: {consultation.fee}"
                for consultation in self.__consultations
            ]
        )

        return (
            f"Patient ID: {self.__myPatientID}\n"
            f"Name: {self.__myPatientFName} {self.__myPatientLName}\n"
            f"Assigned Doctor: {doctor_name}\n"
            f"Consultations:\n{consultations_info}"
        )
