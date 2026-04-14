from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="Healthcare JARVIS Multi-Agent", version="1.0.0")

class Symptom(BaseModel):
    symptom: str
    duration: str
    severity: int  # 1-10

class PatientIntake(BaseModel):
    patient_id: str
    age: int
    symptoms: List[Symptom]
    voice_transcript: Optional[str] = None

class DiagnosisReport(BaseModel):
    patient_id: str
    risk_level: str
    possible_conditions: List[str]
    recommendations: List[str]
    doctor_summary: str
    urgency: str

CONDITION_MAP = {
    "fièvre": ["grippe", "infection bactérienne", "COVID-19"],
    "toux": ["bronchite", "pneumonie", "COVID-19"],
    "douleur": ["inflammation", "trauma", "infection"],
    "fatigue": ["anémie", "thyroïde", "burnout"],
    "essoufflement": ["asthme", "cardiopathie", "pneumonie"],
}

@app.post("/intake", response_model=dict)
def patient_intake(patient: PatientIntake):
    return {"patient_id": patient.patient_id, "status": "intake_complete", "symptoms_count": len(patient.symptoms)}

@app.post("/diagnose", response_model=DiagnosisReport)
def diagnose(patient: PatientIntake):
    conditions = []
    for s in patient.symptoms:
        for key, vals in CONDITION_MAP.items():
            if key in s.symptom.lower():
                conditions.extend(vals)
    conditions = list(set(conditions)) or ["Consultation approfondie requise"]
    max_severity = max((s.severity for s in patient.symptoms), default=0)
    urgency = "URGENT" if max_severity >= 8 else "MODERE" if max_severity >= 5 else "FAIBLE"
    risk = "HIGH" if urgency == "URGENT" else "MEDIUM" if urgency == "MODERE" else "LOW"
    summary = f"Patient {patient.age}ans. {len(patient.symptoms)} symptômes. Sévérité max: {max_severity}/10. Conditions possibles: {', '.join(conditions[:3])}."
    return DiagnosisReport(
        patient_id=patient.patient_id,
        risk_level=risk,
        possible_conditions=conditions[:5],
        recommendations=["Consulter un médecin", "Repos recommandé", "Hydratation"],
        doctor_summary=summary,
        urgency=urgency
    )

@app.get("/health")
def health():
    return {"status": "ok", "agents": ["intake", "diagnosis", "report"]}
