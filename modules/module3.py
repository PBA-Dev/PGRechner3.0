"""
Module 3: Verhaltensweisen und psychische Problemlagen
Weight: 15% (Note: Actual NBA weighting combines M2 & M3, then takes the higher score. We'll adjust calculation later if needed)
"""

module3 = {
    "name": "Modul 3: Verhaltensweisen und psychische Problemlagen",
    "weight": 0.15, # Placeholder weight, actual calculation might differ based on NBA rules
    "questions": [
        {
            "text": "3.1 Motorisch geprägte Verhaltensauffälligkeiten",
            "explanation": "Dieses Kriterium fasst verschiedene Verhaltensweisen zusammen. Dazu gehören vor allem das (scheinbar) ziellose Umhergehen in der Wohnung oder der Einrichtung und der Versuch desorientierter Personen, ohne Begleitung die Wohnung, Einrichtung zu verlassen oder Orte aufzusuchen, die für diese Person unzugänglich sein sollten, zum Beispiel Treppenhaus, Zimmer anderer Bewohner.  Ebenso zu berücksichtigen ist allgemeine Rastlosigkeit in Form von ständigem Aufstehen und Hinsetzen oder Hin- und Herrutschen auf dem Sitzplatz oder im und aus dem Bett. ",
            "options": [
                {"score": 0, "text": "Nie oder sehr selten", "option_explanation": "Verhalten tritt praktisch nicht auf."},
                {"score": 1, "text": "Selten (1-3 Mal pro Woche)", "option_explanation": "Verhalten tritt gelegentlich auf."},
                {"score": 3, "text": "Häufig (mehrmals pro Woche bis täglich)", "option_explanation": "Verhalten tritt regelmäßig auf."},
                {"score": 5, "text": "Täglich mehrmals", "option_explanation": "Verhalten tritt sehr häufig auf."}
            ]
        },
        {
            "text": "3.2 Nächtliche Unruhe",
            "explanation": "Gemeint sind hier nächtliches Umherirren oder nächtliche Unruhephasen bis hin zur Umkehr des Tag-Nacht-Rhythmus im Sinne von aktiv sein in der Nacht und schlafen während des Tages.  Zu bewerten ist, wie häufig Anlass für personelle Unterstützung zur Beruhigung und gegebenenfalls wieder ins Bett bringen besteht.  Schlafstörungen wie Einschlafschwierigkeiten am Abend oder Wachphasen während der Nacht sind nicht zu werten.  Andere nächtliche Hilfen, zum Beispiel Hilfen zur Orientierung, Aufstehen, zu Bett bringen, Hilfe bei nächtlichen Toilettengängen, körperbezogene Pflegemaßnahmen oder Lagerungen sind nur unter F 4.6.2;  Ruhen und Schlafen, Medikamentengabe und andere angeordnete Maßnahmen aus dem Modul 5 sind nur dort zu bewerten. ",
            "options": [
                {"score": 0, "text": "Nie oder sehr selten", "option_explanation": "Keine oder kaum nächtliche Unruhe."},
                {"score": 1, "text": "Selten (1-3 Mal pro Woche)", "option_explanation": "Nächtliche Unruhe tritt gelegentlich auf."},
                {"score": 3, "text": "Häufig (mehrmals pro Woche bis täglich)", "option_explanation": "Nächtliche Unruhe tritt regelmäßig auf."},
                {"score": 5, "text": "Täglich mehrmals", "option_explanation": "Nächtliche Unruhe tritt sehr häufig auf."}
            ]
        },
        {
            "text": "3.3 Selbstschädigendes und autoaggressives Verhalten",
            "explanation": "Selbstschädigendes und autoaggressives Verhalten kann zum Beispiel darin bestehen, sich selbst durch Gegenstände zu verletzen, ungenießbare Substanzen zu essen und zu trinken, sich selbst zu schlagen und sich selbst mit den Fingernägeln oder Zähnen zu verletzen. ",
            "options": [
                {"score": 0, "text": "Nie oder sehr selten", "option_explanation": "Verhalten tritt praktisch nicht auf."},
                {"score": 1, "text": "Selten (1-3 Mal pro Woche)", "option_explanation": "Verhalten tritt gelegentlich auf."},
                {"score": 3, "text": "Häufig (mehrmals pro Woche bis täglich)", "option_explanation": "Verhalten tritt regelmäßig auf."},
                {"score": 5, "text": "Täglich mehrmals", "option_explanation": "Verhalten tritt sehr häufig auf."}
            ]
        },
        {
            "text": "3.4 Beschädigen von Gegenständen",
            "explanation": "Gemeint sind hier aggressive auf Gegenstände gerichtete Handlungen wie Gegenstände wegstoßen oder wegschieben, gegen Gegenstände schlagen, das Zerstören von Dingen sowie das Treten nach Gegenständen. ",
            "options": [
                {"score": 0, "text": "Nie oder sehr selten", "option_explanation": "Verhalten tritt praktisch nicht auf."},
                {"score": 1, "text": "Selten (1-3 Mal pro Woche)", "option_explanation": "Verhalten tritt gelegentlich auf."},
                {"score": 3, "text": "Häufig (mehrmals pro Woche bis täglich)", "option_explanation": "Verhalten tritt regelmäßig auf."},
                {"score": 5, "text": "Täglich mehrmals", "option_explanation": "Verhalten tritt sehr häufig auf."}
            ]
        },
        {
            "text": "3.5 Physisch aggressives Verhalten gegenüber anderen Personen",
            "explanation": "Physisch aggressives Verhalten gegenüber anderen Personen kann zum Beispiel darin bestehen, nach Personen zu schlagen oder zu treten, andere mit Zähnen oder Fingernägeln zu verletzen, andere zu stoßen oder wegzudrängen, oder in Verletzungsversuchen gegenüber anderen Personen mit Gegenständen. ",
            "options": [
                {"score": 0, "text": "Nie oder sehr selten", "option_explanation": "Verhalten tritt praktisch nicht auf."},
                {"score": 1, "text": "Selten (1-3 Mal pro Woche)", "option_explanation": "Verhalten tritt gelegentlich auf."},
                {"score": 3, "text": "Häufig (mehrmals pro Woche bis täglich)", "option_explanation": "Verhalten tritt regelmäßig auf."},
                {"score": 5, "text": "Täglich mehrmals", "option_explanation": "Verhalten tritt sehr häufig auf."}
            ]
        },
        {
            "text": "3.6 Verbale Aggression",
            "explanation": "Verbale Aggression kann sich zum Beispiel in verbalen Beschimpfungen oder in der Bedrohung anderer Personen ausdrücken. ",
            "options": [
                {"score": 0, "text": "Nie oder sehr selten", "option_explanation": "Verhalten tritt praktisch nicht auf."},
                {"score": 1, "text": "Selten (1-3 Mal pro Woche)", "option_explanation": "Verhalten tritt gelegentlich auf."},
                {"score": 3, "text": "Häufig (mehrmals pro Woche bis täglich)", "option_explanation": "Verhalten tritt regelmäßig auf."},
                {"score": 5, "text": "Täglich mehrmals", "option_explanation": "Verhalten tritt sehr häufig auf."}
            ]
        },
        {
            "text": "3.7 Andere pflegerelevante vokale Auffälligkeiten",
            "explanation": "Andere pflegerelevante vokale Auffälligkeiten können sein: Lautes Rufen, Schreien, Klagen ohne nachvollziehbaren Grund, vor sich hin schimpfen, fluchen, seltsame Laute von sich geben, ständiges Wiederholen von Sätzen und Fragen. ",
            "options": [
                {"score": 0, "text": "Nie oder sehr selten", "option_explanation": "Verhalten tritt praktisch nicht auf."},
                {"score": 1, "text": "Selten (1-3 Mal pro Woche)", "option_explanation": "Verhalten tritt gelegentlich auf."},
                {"score": 3, "text": "Häufig (mehrmals pro Woche bis täglich)", "option_explanation": "Verhalten tritt regelmäßig auf."},
                {"score": 5, "text": "Täglich mehrmals", "option_explanation": "Verhalten tritt sehr häufig auf."}
            ]
        },
        {
            "text": "3.8 Abwehr von pflegerischen oder anderen unterstützenden Maßnahmen",
            "explanation": "Hier ist die Abwehr von Unterstützung, zum Beispiel bei der Körperpflege, die Verweigerung der Nahrungsaufnahme, der Medikamenteneinnahme oder anderer notwendiger Verrichtungen sowie die Manipulation an Vorrichtungen wie zum Beispiel an Kathetern, Infusionen oder Sondenernährung gemeint.  Dazu gehört nicht die willentliche (selbstbestimmte) Ablehnung bestimmter Maßnahmen. ",
            "options": [
                {"score": 0, "text": "Nie oder sehr selten", "option_explanation": "Keine oder kaum Abwehr."},
                {"score": 1, "text": "Selten (1-3 Mal pro Woche)", "option_explanation": "Gelegentliche Abwehr."},
                {"score": 3, "text": "Häufig (mehrmals pro Woche bis täglich)", "option_explanation": "Regelmäßige Abwehr."},
                {"score": 5, "text": "Täglich mehrmals", "option_explanation": "Sehr häufige oder ständige Abwehr."}
            ]
        },
        {
            "text": "3.9 Wahnvorstellungen",
            "explanation": "Wahnvorstellungen beziehen sich zum Beispiel auf die Vorstellung, mit Verstorbenen oder imaginären Personen in Kontakt zu stehen, oder auf die Vorstellung, verfolgt, bedroht oder bestohlen zu werden. ",
            "options": [
                {"score": 0, "text": "Nie oder sehr selten", "option_explanation": "Keine Wahnvorstellungen."},
                {"score": 1, "text": "Selten (1-3 Mal pro Woche)", "option_explanation": "Gelegentliches Äußern von Wahnvorstellungen."},
                {"score": 3, "text": "Häufig (mehrmals pro Woche bis täglich)", "option_explanation": "Regelmäßiges Äußern von Wahnvorstellungen."},
                {"score": 5, "text": "Täglich mehrmals", "option_explanation": "Ständiges Vorhandensein von Wahnvorstellungen."}
            ]
        },
        {
            "text": "3.10 Ängste",
            "explanation": "Es geht hier um ausgeprägte Ängste, die wiederkehrend sind und als bedrohlich erlebt werden.  Die Person hat keine eigene Möglichkeit/Strategie zur Bewältigung und Überwindung der Angst.  Die Angst führt zu erheblichen psychischen oder körperlichen Beschwerden, einem hohen Leidensdruck und Beeinträchtigungen in der Bewältigung des Alltags.  Ängste lassen sich nicht nur bei Angststörungen finden, sondern auch bei anderen psychischen Störungen wie zum Beispiel bei Schizophrenie und Depression.  Darüber hinaus können ausgeprägte Ängste im Sinne dieses Kriteriums auch durch rein somatische Krankheiten wie onkologische Erkrankungen verursacht werden.  Das Herstellen einer angstfreien Atmosphäre durch bloße Anwesenheit einer weiteren Person (ohne deren aktive personelle Unterstützung) wird hier nicht bewertet. ",
            "options": [
                {"score": 0, "text": "Nie oder sehr selten", "option_explanation": "Keine oder kaum Ängste."},
                {"score": 1, "text": "Selten (1-3 Mal pro Woche)", "option_explanation": "Gelegentliche Ängste."},
                {"score": 3, "text": "Häufig (mehrmals pro Woche bis täglich)", "option_explanation": "Regelmäßige Ängste."},
                {"score": 5, "text": "Täglich mehrmals", "option_explanation": "Ständige oder sehr starke Ängste."}
            ]
        },
        {
            "text": "3.11 Antriebslosigkeit bei depressiver Stimmungslage",
            "explanation": "Antriebsstörungen wie Antriebschwäche, Antriebsmangel oder Antriebsarmut können Vorstufen der Antriebslosigkeit sein.  Die Antriebslosigkeit stellt eine sehr schwere Form der Antriebsstörung dar.  Die depressive Stimmungslage äußert sich insbesondere durch Hoffnungslosigkeit, Niedergeschlagenheit oder Verzweiflung.  Es kann sich aber beispielsweise auch durch ein Gefühl der Gefühllosigkeit mit fehlender emotionaler Schwingungsfähigkeit zeigen, so dass weder Freude noch Trauer empfunden werden können.  Antriebslosigkeit bei depressiver Stimmungslage zeigt sich zum Beispiel daran, dass die Person kaum Interesse an der Umgebung hat, kaum Eigeninitiative aufbringt und eine aufwendige Motivierung durch andere benötigt, um etwas zu tun.  Hier ist nicht gemeint, dass Menschen mit rein kognitiven Beeinträchtigungen, zum Beispiel bei Demenz, Impulse benötigen, um eine Handlung zu beginnen oder fortzuführen. ",
            "options": [
                {"score": 0, "text": "Nie oder sehr selten", "option_explanation": "Keine Antriebslosigkeit."},
                {"score": 1, "text": "Selten (1-3 Mal pro Woche)", "option_explanation": "Gelegentliche Antriebslosigkeit."},
                {"score": 3, "text": "Häufig (mehrmals pro Woche bis täglich)", "option_explanation": "Regelmäßige Antriebslosigkeit."},
                {"score": 5, "text": "Täglich mehrmals", "option_explanation": "Ständige Antriebslosigkeit."}
            ]
        },
        {
            "text": "3.12 Sozial inadäquate Verhaltensweisen",
            "explanation": "Sozial inadäquate Verhaltensweisen sind zum Beispiel distanzloses Verhalten, auffälliges Einfordern von Aufmerksamkeit, sich vor anderen in unpassenden Situationen entkleiden, unangemessenes Greifen nach Personen oder unangemessene körperliche oder verbale sexuelle Annäherungsversuche. ",
            "options": [
                {"score": 0, "text": "Nie oder sehr selten", "option_explanation": "Keine depressive Stimmung."},
                {"score": 1, "text": "Selten (1-3 Mal pro Woche)", "option_explanation": "Gelegentlich depressive Stimmung."},
                {"score": 3, "text": "Häufig (mehrmals pro Woche bis täglich)", "option_explanation": "Regelmäßig depressive Stimmung."},
                {"score": 5, "text": "Täglich mehrmals", "option_explanation": "Ständige oder sehr ausgeprägte depressive Stimmung."}
            ]
        },
        {
            "text": "3.13 Sonstige pflegerelevante inadäquate Handlungen",
            "explanation": "Sonstige pflegerelevante inadäquate Handlungen sind zum Beispiel Nesteln an der Kleidung, ständiges Wiederholen der gleichen Handlung (Stereotypien), planlose Aktivitäten, Verstecken oder Horten von Gegenständen, Kotschmieren, Urinieren in die Wohnung. ",
            "options": [
                {"score": 0, "text": "Nie oder sehr selten", "option_explanation": "Verhalten tritt praktisch nicht auf."},
                {"score": 1, "text": "Selten (1-3 Mal pro Woche)", "option_explanation": "Verhalten tritt gelegentlich auf."},
                {"score": 3, "text": "Häufig (mehrmals pro Woche bis täglich)", "option_explanation": "Verhalten tritt regelmäßig auf."},
                {"score": 5, "text": "Täglich mehrmals", "option_explanation": "Verhalten tritt sehr häufig auf."}
            ]
        }
    ]
}