"""
Module 3: Verhaltensweisen und psychische Problemlagen
Weight: 15% (Note: Actual NBA weighting combines M2 & M3, then takes the higher score. We'll adjust calculation later if needed)
"""

module3 = {
    "name": "Modul 3: Verhaltensweisen und psychische Problemlagen",
    "weight": 0.15, # Placeholder weight, actual calculation might differ based on NBA rules
    "questions": [
        {
            "question": "3.1 Motorisch geprägte Verhaltensauffälligkeiten",
            "explanation": "Bewertet wird das Auftreten von körperlicher Unruhe, ziellosem Umherlaufen, Bewegungsstereotypien.",
            "options": [
                {"score": 0, "text": "Nie oder sehr selten", "option_explanation": "Verhalten tritt praktisch nicht auf."},
                {"score": 1, "text": "Selten (1-3 Mal pro Woche)", "option_explanation": "Verhalten tritt gelegentlich auf."},
                {"score": 3, "text": "Häufig (mehrmals pro Woche bis täglich)", "option_explanation": "Verhalten tritt regelmäßig auf."},
                {"score": 5, "text": "Täglich mehrmals", "option_explanation": "Verhalten tritt sehr häufig auf."}
                # Note: NBA uses scores 0, 1, 3, 5 for frequency in M3
            ]
        },
        {
            "question": "3.2 Nächtliche Unruhe",
            "explanation": "Bewertet wird nächtliches Umherirren, Aufstehen, Rufen oder andere Störungen der Nachtruhe.",
            "options": [
                {"score": 0, "text": "Nie oder sehr selten", "option_explanation": "Keine oder kaum nächtliche Unruhe."},
                {"score": 1, "text": "Selten (1-3 Mal pro Woche)", "option_explanation": "Nächtliche Unruhe tritt gelegentlich auf."},
                {"score": 3, "text": "Häufig (mehrmals pro Woche bis täglich)", "option_explanation": "Nächtliche Unruhe tritt regelmäßig auf."},
                {"score": 5, "text": "Täglich mehrmals", "option_explanation": "Nächtliche Unruhe tritt sehr häufig auf."}
            ]
        },
        {
            "question": "3.3 Selbstschädigendes und autoaggressives Verhalten",
            "explanation": "Bewertet wird Verhalten wie sich selbst schlagen, kratzen, beißen oder Kopf anschlagen.",
            "options": [
                {"score": 0, "text": "Nie oder sehr selten", "option_explanation": "Verhalten tritt praktisch nicht auf."},
                {"score": 1, "text": "Selten (1-3 Mal pro Woche)", "option_explanation": "Verhalten tritt gelegentlich auf."},
                {"score": 3, "text": "Häufig (mehrmals pro Woche bis täglich)", "option_explanation": "Verhalten tritt regelmäßig auf."},
                {"score": 5, "text": "Täglich mehrmals", "option_explanation": "Verhalten tritt sehr häufig auf."}
            ]
        },
        {
            "question": "3.4 Beschädigen von Gegenständen",
            "explanation": "Bewertet wird das Zerstören oder Beschädigen von Mobiliar, Kleidung oder anderen Gegenständen.",
            "options": [
                {"score": 0, "text": "Nie oder sehr selten", "option_explanation": "Verhalten tritt praktisch nicht auf."},
                {"score": 1, "text": "Selten (1-3 Mal pro Woche)", "option_explanation": "Verhalten tritt gelegentlich auf."},
                {"score": 3, "text": "Häufig (mehrmals pro Woche bis täglich)", "option_explanation": "Verhalten tritt regelmäßig auf."},
                {"score": 5, "text": "Täglich mehrmals", "option_explanation": "Verhalten tritt sehr häufig auf."}
            ]
        },
        {
            "question": "3.5 Physisch aggressives Verhalten gegenüber anderen Personen",
            "explanation": "Bewertet wird körperliche Aggression wie Schlagen, Treten, Beißen, Stoßen gegenüber anderen.",
            "options": [
                {"score": 0, "text": "Nie oder sehr selten", "option_explanation": "Verhalten tritt praktisch nicht auf."},
                {"score": 1, "text": "Selten (1-3 Mal pro Woche)", "option_explanation": "Verhalten tritt gelegentlich auf."},
                {"score": 3, "text": "Häufig (mehrmals pro Woche bis täglich)", "option_explanation": "Verhalten tritt regelmäßig auf."},
                {"score": 5, "text": "Täglich mehrmals", "option_explanation": "Verhalten tritt sehr häufig auf."}
            ]
        },
        {
            "question": "3.6 Verbale Aggression",
            "explanation": "Bewertet wird aggressives verbales Verhalten wie Beschimpfen, Schreien, Fluchen.",
            "options": [
                {"score": 0, "text": "Nie oder sehr selten", "option_explanation": "Verhalten tritt praktisch nicht auf."},
                {"score": 1, "text": "Selten (1-3 Mal pro Woche)", "option_explanation": "Verhalten tritt gelegentlich auf."},
                {"score": 3, "text": "Häufig (mehrmals pro Woche bis täglich)", "option_explanation": "Verhalten tritt regelmäßig auf."},
                {"score": 5, "text": "Täglich mehrmals", "option_explanation": "Verhalten tritt sehr häufig auf."}
            ]
        },
        {
            "question": "3.7 Andere pflegerelevante vokale Auffälligkeiten",
            "explanation": "Bewertet wird ständiges Rufen, Jammern, Klagen oder Stöhnen ohne direkten Bezug zu Schmerz oder Bedürfnis.",
             "options": [
                {"score": 0, "text": "Nie oder sehr selten", "option_explanation": "Verhalten tritt praktisch nicht auf."},
                {"score": 1, "text": "Selten (1-3 Mal pro Woche)", "option_explanation": "Verhalten tritt gelegentlich auf."},
                {"score": 3, "text": "Häufig (mehrmals pro Woche bis täglich)", "option_explanation": "Verhalten tritt regelmäßig auf."},
                {"score": 5, "text": "Täglich mehrmals", "option_explanation": "Verhalten tritt sehr häufig auf."}
            ]
        },
        {
            "question": "3.8 Abwehr von pflegerischen oder anderen unterstützenden Maßnahmen",
            "explanation": "Bewertet wird Widerstand oder Abwehr gegenüber notwendiger Hilfe bei Körperpflege, Essen, Mobilisation etc.",
             "options": [
                {"score": 0, "text": "Nie oder sehr selten", "option_explanation": "Keine oder kaum Abwehr."},
                {"score": 1, "text": "Selten (1-3 Mal pro Woche)", "option_explanation": "Gelegentliche Abwehr."},
                {"score": 3, "text": "Häufig (mehrmals pro Woche bis täglich)", "option_explanation": "Regelmäßige Abwehr."},
                {"score": 5, "text": "Täglich mehrmals", "option_explanation": "Sehr häufige oder ständige Abwehr."}
            ]
        },
        {
            "question": "3.9 Wahnvorstellungen",
            "explanation": "Bewertet wird das Äußern von unrealistischen, unkorrigierbaren Überzeugungen (z.B. Verfolgungswahn).",
             "options": [
                {"score": 0, "text": "Nie oder sehr selten", "option_explanation": "Keine Wahnvorstellungen."},
                {"score": 1, "text": "Selten (1-3 Mal pro Woche)", "option_explanation": "Gelegentliches Äußern von Wahnvorstellungen."},
                {"score": 3, "text": "Häufig (mehrmals pro Woche bis täglich)", "option_explanation": "Regelmäßiges Äußern von Wahnvorstellungen."},
                {"score": 5, "text": "Täglich mehrmals", "option_explanation": "Ständiges Vorhandensein von Wahnvorstellungen."}
            ]
        },
        {
            "question": "3.10 Ängste",
            "explanation": "Bewertet wird das Äußern oder Zeigen von Ängsten (z.B. Angst vor Alleinsein, Dunkelheit, bestimmten Situationen).",
             "options": [
                {"score": 0, "text": "Nie oder sehr selten", "option_explanation": "Keine oder kaum Ängste."},
                {"score": 1, "text": "Selten (1-3 Mal pro Woche)", "option_explanation": "Gelegentliche Ängste."},
                {"score": 3, "text": "Häufig (mehrmals pro Woche bis täglich)", "option_explanation": "Regelmäßige Ängste."},
                {"score": 5, "text": "Täglich mehrmals", "option_explanation": "Ständige oder sehr starke Ängste."}
            ]
        },
        {
            "question": "3.11 Antriebslosigkeit bei depressiver Stimmungslage",
            "explanation": "Bewertet wird mangelnder Antrieb oder Initiative, obwohl die Person körperlich dazu fähig wäre und aktiviert werden kann.",
             "options": [
                {"score": 0, "text": "Nie oder sehr selten", "option_explanation": "Keine Antriebslosigkeit."},
                {"score": 1, "text": "Selten (1-3 Mal pro Woche)", "option_explanation": "Gelegentliche Antriebslosigkeit."},
                {"score": 3, "text": "Häufig (mehrmals pro Woche bis täglich)", "option_explanation": "Regelmäßige Antriebslosigkeit."},
                {"score": 5, "text": "Täglich mehrmals", "option_explanation": "Ständige Antriebslosigkeit."}
            ]
        },
        {
            "question": "3.12 Sozial inadäquate Verhaltensweisen",
            "explanation": "Bewertet wird das Vorhandensein von Traurigkeit, Hoffnungslosigkeit, sozialem Rückzug.",
             "options": [
                {"score": 0, "text": "Nie oder sehr selten", "option_explanation": "Keine depressive Stimmung."},
                {"score": 1, "text": "Selten (1-3 Mal pro Woche)", "option_explanation": "Gelegentlich depressive Stimmung."},
                {"score": 3, "text": "Häufig (mehrmals pro Woche bis täglich)", "option_explanation": "Regelmäßig depressive Stimmung."},
                {"score": 5, "text": "Täglich mehrmals", "option_explanation": "Ständige oder sehr ausgeprägte depressive Stimmung."}
            ]
        },
        {
            "question": "3.13 Sonstige pflegerelevante inadäquate Handlungen",
            "explanation": "Bewertet wird sozial unangepasstes Verhalten wie Distanzlosigkeit, sexuell übergriffiges Verhalten, lautes Schimpfen in der Öffentlichkeit.",
             "options": [
                {"score": 0, "text": "Nie oder sehr selten", "option_explanation": "Verhalten tritt praktisch nicht auf."},
                {"score": 1, "text": "Selten (1-3 Mal pro Woche)", "option_explanation": "Verhalten tritt gelegentlich auf."},
                {"score": 3, "text": "Häufig (mehrmals pro Woche bis täglich)", "option_explanation": "Verhalten tritt regelmäßig auf."},
                {"score": 5, "text": "Täglich mehrmals", "option_explanation": "Verhalten tritt sehr häufig auf."}
            ]
        }
        # Add more questions as per your document if needed
    ]
}