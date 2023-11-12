# Import the Doctor and Patient classes from their respective modules
from doctor import Doctor
from patient import Patient

class Consultation:
    def __init__(self, date, doctor, patient, reason, fee):
        # Initialize consultation attributes
        self.__myCDate = date  # Consultation date
        self.__myCDoctor = doctor  # Doctor associated with the consultation
        self.__myCPatient = patient  # Patient associated with the consultation
        self.__myCReason = reason  # Reason for the consultation
        self.__myFee = fee  # Consultation fee

    @property
    def doctor(self):
        return self.__myCDoctor  # Get the associated doctor

    @property
    def patient(self):
        return self.__myCPatient  # Get the associated patient

    @property
    def date(self):
        return self.__myCDate  # Get the consultation date

    @property
    def reason(self):
        return self.__myCReason  # Get the reason for the consultation

    @property
    def fee(self):
        return self.__myFee  # Get the consultation fee

    @fee.setter
    def fee(self, new_fee):
        self.__myFee = new_fee  # Set a new consultation fee

    def assign_doctor(self, doctor):
        # Assign a doctor to the consultation and add the consultation to the doctor's list
        self.__myCDoctor = doctor
        doctor.add_consultation(self)

    def __str__(self):
        # Generate a formatted string representation of the consultation
        return (
            f"Date: {self.__myCDate}\n"
            f"Doctor: {self.__myCDoctor.doctor_fname} {self.__myCDoctor.doctor_lname}\n"
            f"Patient: {self.__myCPatient.patient_fname} {self.__myCPatient.patient_lname}\n"
            f"Reason: {self.__myCReason}\n"
            f"Fee: {self.__myFee}\n"
        )
