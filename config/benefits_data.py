# config/benefits_data.py

# Structure:
# pflegegrad_benefits = {
#     <pflegegrad_number>: {
#         "period_1": { # e.g., Jan 1 - Jun 30, 2025
#             "date_range": "01.01.2025 - 30.06.2025",
#             "leistungen": [
#                 {"name": "Benefit Name", "value": "Amount/Description"},
#                 # ... more benefits ...
#             ]
#         },
#         "period_2": { # e.g., Jul 1, 2025 onwards
#             "date_range": "ab 01.07.2025",
#             "leistungen": [
#                 {"name": "Benefit Name", "value": "Amount/Description"},
#                 # ... more benefits ...
#             ]
#         }
#     },
#     # ... other pflegegrade ...
# }

pflegegrad_benefits = {
    0: { # Kein Pflegegrad - You might want to define specific text or leave empty
        "period_1": {"date_range": "01.01.2025 - 30.06.2025", "leistungen": [{"name": "Kein Anspruch auf reguläre Pflegeleistungen", "value": ""}]},
        "period_2": {"date_range": "ab 01.07.2025", "leistungen": [{"name": "Kein Anspruch auf reguläre Pflegeleistungen", "value": ""}]},
    },
    1: {  # Pflegegrad 1
        "period_1": {
            "date_range": "01.01.2025 - 30.06.2025",
            "leistungen": [
                {"name": "Pflegesachleistungen (§ 36 SGB XI)", "value": "Entlastungsbetrag § 45b kann verwendet werden."},
                {"name": "Pflegegeld (§ 37 SGB XI)", "value": "0 €"},
                {"name": "Teilstationäre Pflege (§ 41 SGB XI)", "value": "Entlastungsbetrag § 45b kann verwendet werden."},
                {"name": "Verhinderungspflege (§ 39 SGB XI)", "value": "0 € pro Kalenderjahr (bis zu 6 Wochen*)", "note": "*8 Wochen bei Pflegegrad 4 oder 5 bis vollendetes 25. Lebensjahr"},
                {"name": "Verhinderungspflege (Erhöhung aus nicht genutzten Mitteln der Kurzzeitpflege)", "value": "0 € pro Kalenderjahr"},
                {"name": "Kurzzeitpflege (§ 42 SGB XI)", "value": "Entlastungsbetrag § 45b kann verwendet werden."},
                {"name": "Kurzzeitpflege (Erhöhung aus nicht genutzten Mitteln der Verhinderungspflege)", "value": "0 € pro Kalenderjahr"},
                {"name": "Entlastungsbetrag (§ 45b SGB XI)", "value": "131 € pro Monat"},
                {"name": "Wohngruppenzuschlag (§ 38a SGB XI)", "value": "224 € pro Monat"},
                {"name": "Pflegehilfsmittel (nicht zum Verbrauch, z.B. Pflegebett)", "value": "Anspruch besteht"},
                {"name": "Pflegehilfsmittel (zum Verbrauch, z.B. Desinfektionsmittel)", "value": "42 € pro Monat"},
                {"name": "Zuschuss zu wohnumfeldverbessernden Maßnahmen (§ 40 SGB XI)", "value": "4.180 € pro Maßnahme"},
                {"name": "Beratungseinsatz (§ 37 Abs. 3 SGB XI)", "value": "Kostenlos", "details": "Einsatz kann halbjährlich abgerufen werden"},
                {"name": "Beratung durch Pflegestützpunkte und anerkannte Pflegeberater (§§ 7a, 7b SGB XI)", "value": "Anspruch besteht"},
                {"name": "Vollstationäre Pflege (§ 43 SGB XI)", "value": "131 € Zuschuss"},
                {"name": "Zusätzliche Betreuung im Pflegeheim (§ 43b SGB XI)", "value": "Kostenlos", "details": "sofern vom Pflegeheim angeboten"},
            ]
        },
        "period_2": {
            "date_range": "ab 01.07.2025",
            "leistungen": [
                {"name": "Pflegesachleistungen (§ 36 SGB XI)", "value": "Entlastungsbetrag § 45b kann verwendet werden."},
                {"name": "Pflegegeld (§ 37 SGB XI)", "value": "0 €"},
                {"name": "Teilstationäre Pflege (§ 41 SGB XI)", "value": "Entlastungsbetrag § 45b kann verwendet werden."},
                # For Pflegegrad 1, even after 01.07.2025, Verhinderungspflege and Kurzzeitpflege remain 0€ 
                # or use Entlastungsbetrag, so no "Gemeinsamer Jahresbetrag" entry with a value here, 
                # as the combined amount explicitly states 3539 EUR, which doesn't apply to PG1 directly.
                {"name": "Verhinderungspflege (§ 39 SGB XI)", "value": "0 € pro Kalenderjahr (bis zu 8 Wochen)", "note": "Wichtig: Bereits im 1. Halbjahr 2025 genutzte Leistungsbeträge werden im Jahr 2025 auf den Gemeinsamen Jahresbetrag angerechnet. (Für Pflegegrad 1 weiterhin 0€, keine direkte Erhöhung durch gemeinsame Betrachtung)"},
                {"name": "Kurzzeitpflege (§ 42 SGB XI)", "value": "Entlastungsbetrag § 45b kann verwendet werden.", "note": "Wichtig: Bereits im 1. Halbjahr 2025 genutzte Leistungsbeträge werden im Jahr 2025 auf den Gemeinsamen Jahresbetrag angerechnet."},
                {"name": "Entlastungsbetrag (§ 45b SGB XI)", "value": "131 € pro Monat"},
                {"name": "Wohngruppenzuschlag (§ 38a SGB XI)", "value": "224 € pro Monat"},
                {"name": "Pflegehilfsmittel (nicht zum Verbrauch, z.B. Pflegebett)", "value": "Anspruch besteht"},
                {"name": "Pflegehilfsmittel (zum Verbrauch, z.B. Desinfektionsmittel)", "value": "42 € pro Monat"},
                {"name": "Zuschuss zu wohnumfeldverbessernden Maßnahmen (§ 40 SGB XI)", "value": "4.180 € pro Maßnahme"},
                {"name": "Beratungseinsatz (§ 37 Abs. 3 SGB XI)", "value": "Kostenlos", "details": "Einsatz kann halbjährlich abgerufen werden"},
                {"name": "Beratung durch Pflegestützpunkte und anerkannte Pflegeberater (§§ 7a, 7b SGB XI)", "value": "Anspruch besteht"},
                {"name": "Vollstationäre Pflege (§ 43 SGB XI)", "value": "131 € Zuschuss"},
                {"name": "Zusätzliche Betreuung im Pflegeheim (§ 43b SGB XI)", "value": "Kostenlos", "details": "sofern vom Pflegeheim angeboten"},
            ]
        }
    },
    2: {  # Pflegegrad 2
        "period_1": {
            "date_range": "01.01.2025 - 30.06.2025",
            "leistungen": [
                {"name": "Pflegesachleistungen (§ 36 SGB XI)", "value": "796 € pro Monat"},
                {"name": "Pflegegeld (§ 37 SGB XI)", "value": "347 € pro Monat"},
                {"name": "Teilstationäre Pflege (§ 41 SGB XI)", "value": "721 € pro Monat"},
                {"name": "Verhinderungspflege (§ 39 SGB XI)", "value": "1.685 € pro Kalenderjahr (bis zu 6 Wochen*)", "note": "*8 Wochen bei Pflegegrad 4 oder 5 bis vollendetes 25. Lebensjahr"},
                {"name": "Verhinderungspflege (Erhöhung aus nicht genutzten Mitteln der Kurzzeitpflege)", "value": "843 € pro Kalenderjahr"},
                {"name": "Kurzzeitpflege (§ 42 SGB XI)", "value": "1.854 € pro Kalenderjahr (bis zu 8 Wochen)"},
                {"name": "Kurzzeitpflege (Erhöhung aus nicht genutzten Mitteln der Verhinderungspflege)", "value": "1.685 € pro Kalenderjahr"},
                {"name": "Entlastungsbetrag (§ 45b SGB XI)", "value": "131 € pro Monat"},
                {"name": "Wohngruppenzuschlag (§ 38a SGB XI)", "value": "224 € pro Monat"},
                {"name": "Pflegehilfsmittel (nicht zum Verbrauch, z.B. Pflegebett)", "value": "Anspruch besteht"},
                {"name": "Pflegehilfsmittel (zum Verbrauch, z.B. Desinfektionsmittel)", "value": "42 € pro Monat"},
                {"name": "Zuschuss zu wohnumfeldverbessernden Maßnahmen (§ 40 SGB XI)", "value": "4.180 € pro Maßnahme"},
                {"name": "Beratungseinsatz (§ 37 Abs. 3 SGB XI)", "value": "Kostenlos", "details": "Bei Pflegegeldbezug 1x pro Halbjahr Pflicht. Bei Bezug von ausschließlich Pflegesachleistung 1x pro Halbjahr auf Wunsch."},
                {"name": "Beratung durch Pflegestützpunkte und anerkannte Pflegeberater (§§ 7a, 7b SGB XI)", "value": "Anspruch besteht"},
                {"name": "Vollstationäre Pflege (§ 43 SGB XI)", "value": "805 € pro Monat", "details": "plus Zuschuss zum Eigenanteil an den pflegebedingten Aufwendungen in Höhe von: 15 % vom 1. bis 12. Monat, 30 % vom 13. bis 24. Monat, 50 % vom 25. bis 36. Monat, 75 % ab dem 37. Monat des Heimaufenthalts"},
                {"name": "Zusätzliche Betreuung im Pflegeheim (§ 43b SGB XI)", "value": "Kostenlos", "details": "sofern vom Pflegeheim angeboten"},
            ]
        },
        "period_2": {
            "date_range": "ab 01.07.2025",
            "leistungen": [
                {"name": "Pflegesachleistungen (§ 36 SGB XI)", "value": "796 € pro Monat"},
                {"name": "Pflegegeld (§ 37 SGB XI)", "value": "347 € pro Monat"},
                {"name": "Teilstationäre Pflege (§ 41 SGB XI)", "value": "721 € pro Monat"},
                {"name": "Gemeinsamer Jahresbetrag für Verhinderungs- und/oder Kurzzeitpflege", "value": "3.539 € pro Kalenderjahr (bis zu 8 Wochen)", "note": "Wichtig: Bereits im 1. Halbjahr 2025 genutzte Leistungsbeträge werden im Jahr 2025 auf den Gemeinsamen Jahresbetrag angerechnet."},
                {"name": "Entlastungsbetrag (§ 45b SGB XI)", "value": "131 € pro Monat"},
                {"name": "Wohngruppenzuschlag (§ 38a SGB XI)", "value": "224 € pro Monat"},
                {"name": "Pflegehilfsmittel (nicht zum Verbrauch, z.B. Pflegebett)", "value": "Anspruch besteht"},
                {"name": "Pflegehilfsmittel (zum Verbrauch, z.B. Desinfektionsmittel)", "value": "42 € pro Monat"},
                {"name": "Zuschuss zu wohnumfeldverbessernden Maßnahmen (§ 40 SGB XI)", "value": "4.180 € pro Maßnahme"},
                {"name": "Beratungseinsatz (§ 37 Abs. 3 SGB XI)", "value": "Kostenlos", "details": "Bei Pflegegeldbezug 1x pro Halbjahr Pflicht. Bei Bezug von ausschließlich Pflegesachleistung 1x pro Halbjahr auf Wunsch."},
                {"name": "Beratung durch Pflegestützpunkte und anerkannte Pflegeberater (§§ 7a, 7b SGB XI)", "value": "Anspruch besteht"},
                {"name": "Vollstationäre Pflege (§ 43 SGB XI)", "value": "805 € pro Monat", "details": "plus Zuschuss zum Eigenanteil an den pflegebedingten Aufwendungen in Höhe von: 15 % vom 1. bis 12. Monat, 30 % vom 13. bis 24. Monat, 50 % vom 25. bis 36. Monat, 75 % ab dem 37. Monat des Heimaufenthalts"},
                {"name": "Zusätzliche Betreuung im Pflegeheim (§ 43b SGB XI)", "value": "Kostenlos", "details": "sofern vom Pflegeheim angeboten"},
            ]
        }
    },
    3: {  # Pflegegrad 3
        "period_1": {
            "date_range": "01.01.2025 - 30.06.2025",
            "leistungen": [
                {"name": "Pflegesachleistungen (§ 36 SGB XI)", "value": "1.497 € pro Monat"},
                {"name": "Pflegegeld (§ 37 SGB XI)", "value": "599 € pro Monat"},
                {"name": "Teilstationäre Pflege (§ 41 SGB XI)", "value": "1.357 € pro Monat"},
                {"name": "Verhinderungspflege (§ 39 SGB XI)", "value": "1.685 € pro Kalenderjahr (bis zu 6 Wochen*)", "note": "*8 Wochen bei Pflegegrad 4 oder 5 bis vollendetes 25. Lebensjahr"},
                {"name": "Verhinderungspflege (Erhöhung aus nicht genutzten Mitteln der Kurzzeitpflege)", "value": "843 € pro Kalenderjahr"},
                {"name": "Kurzzeitpflege (§ 42 SGB XI)", "value": "1.854 € pro Kalenderjahr (bis zu 8 Wochen)"},
                {"name": "Kurzzeitpflege (Erhöhung aus nicht genutzten Mitteln der Verhinderungspflege)", "value": "1.685 € pro Kalenderjahr"},
                {"name": "Entlastungsbetrag (§ 45b SGB XI)", "value": "131 € pro Monat"},
                {"name": "Wohngruppenzuschlag (§ 38a SGB XI)", "value": "224 € pro Monat"},
                {"name": "Pflegehilfsmittel (nicht zum Verbrauch, z.B. Pflegebett)", "value": "Anspruch besteht"},
                {"name": "Pflegehilfsmittel (zum Verbrauch, z.B. Desinfektionsmittel)", "value": "42 € pro Monat"},
                {"name": "Zuschuss zu wohnumfeldverbessernden Maßnahmen (§ 40 SGB XI)", "value": "4.180 € pro Maßnahme"},
                {"name": "Beratungseinsatz (§ 37 Abs. 3 SGB XI)", "value": "Kostenlos", "details": "Bei Bezug von Pflegegeld 1x pro Halbjahr Pflicht. Bei Bezug von ausschließlich Pflegesachleistung 1x pro Halbjahr auf Wunsch."},
                {"name": "Beratung durch Pflegestützpunkte und anerkannte Pflegeberater (§§ 7a, 7b SGB XI)", "value": "Anspruch besteht"},
                {"name": "Vollstationäre Pflege (§ 43 SGB XI)", "value": "1.319 € pro Monat", "details": "plus Zuschuss zum Eigenanteil an den pflegebedingten Aufwendungen in Höhe von: 15 % vom 1. bis 12. Monat, 30 % vom 13. bis 24. Monat, 50 % vom 25. bis 36. Monat, 75 % ab dem 37. Monat des Heimaufenthalts"},
                {"name": "Zusätzliche Betreuung im Pflegeheim (§ 43b SGB XI)", "value": "Kostenlos", "details": "sofern vom Pflegeheim angeboten"},
            ]
        },
        "period_2": {
            "date_range": "ab 01.07.2025",
            "leistungen": [
                {"name": "Pflegesachleistungen (§ 36 SGB XI)", "value": "1.497 € pro Monat"},
                {"name": "Pflegegeld (§ 37 SGB XI)", "value": "599 € pro Monat"},
                {"name": "Teilstationäre Pflege (§ 41 SGB XI)", "value": "1.357 € pro Monat"},
                {"name": "Gemeinsamer Jahresbetrag für Verhinderungs- und/oder Kurzzeitpflege", "value": "3.539 € pro Kalenderjahr (bis zu 8 Wochen)", "note": "Wichtig: Bereits im 1. Halbjahr 2025 genutzte Leistungsbeträge werden im Jahr 2025 auf den Gemeinsamen Jahresbetrag angerechnet."},
                {"name": "Entlastungsbetrag (§ 45b SGB XI)", "value": "131 € pro Monat"},
                {"name": "Wohngruppenzuschlag (§ 38a SGB XI)", "value": "224 € pro Monat"},
                {"name": "Pflegehilfsmittel (nicht zum Verbrauch, z.B. Pflegebett)", "value": "Anspruch besteht"},
                {"name": "Pflegehilfsmittel (zum Verbrauch, z.B. Desinfektionsmittel)", "value": "42 € pro Monat"},
                {"name": "Zuschuss zu wohnumfeldverbessernden Maßnahmen (§ 40 SGB XI)", "value": "4.180 € pro Maßnahme"},
                {"name": "Beratungseinsatz (§ 37 Abs. 3 SGB XI)", "value": "Kostenlos", "details": "Bei Bezug von Pflegegeld 1x pro Halbjahr Pflicht. Bei Bezug von ausschließlich Pflegesachleistung 1x pro Halbjahr auf Wunsch."},
                {"name": "Beratung durch Pflegestützpunkte und anerkannte Pflegeberater (§§ 7a, 7b SGB XI)", "value": "Anspruch besteht"},
                {"name": "Vollstationäre Pflege (§ 43 SGB XI)", "value": "1.319 € pro Monat", "details": "plus Zuschuss zum Eigenanteil an den pflegebedingten Aufwendungen in Höhe von: 15 % vom 1. bis 12. Monat, 30 % vom 13. bis 24. Monat, 50 % vom 25. bis 36. Monat, 75 % ab dem 37. Monat des Heimaufenthalts"},
                {"name": "Zusätzliche Betreuung im Pflegeheim (§ 43b SGB XI)", "value": "Kostenlos", "details": "sofern vom Pflegeheim angeboten"},
            ]
        }
    },
    4: {  # Pflegegrad 4 - Data from document example
        "period_1": {
            "date_range": "01.01.2025 - 30.06.2025",
            "leistungen": [
                {"name": "Pflegesachleistungen (§ 36 SGB XI)", "value": "1.859 € pro Monat"},
                {"name": "Pflegegeld (§ 37 SGB XI)", "value": "800 € pro Monat"},
                {"name": "Teilstationäre Pflege (§ 41 SGB XI)", "value": "1.685 € pro Monat"},
                {"name": "Verhinderungspflege (§ 39 SGB XI)", "value": "1.685 € pro Kalenderjahr (bis zu 6 Wochen*)", "note": "*8 Wochen bei Pflegegrad 4 oder 5 bis vollendetes 25. Lebensjahr"},
                {"name": "Verhinderungspflege (Erhöhung aus Kurzzeitpflege)", "value": "843 € bzw. 1.854 € (U25) pro Kalenderjahr"},
                {"name": "Kurzzeitpflege (§ 42 SGB XI)", "value": "1.854 € pro Kalenderjahr (bis zu 8 Wochen)"},
                {"name": "Kurzzeitpflege (Erhöhung aus Verhinderungspflege)", "value": "1.685 € pro Kalenderjahr"},
                {"name": "Entlastungsbetrag (§ 45b SGB XI)", "value": "131 € pro Monat"},
                {"name": "Wohngruppenzuschlag (§ 38a SGB XI)", "value": "224 € pro Monat"},
                {"name": "Pflegehilfsmittel (nicht zum Verbrauch, z.B. Pflegebett)", "value": "Anspruch besteht"},
                {"name": "Pflegehilfsmittel (zum Verbrauch, z.B. Desinfektionsmittel)", "value": "42 € pro Monat"},
                {"name": "Zuschuss zu wohnumfeldverbessernden Maßnahmen (§ 40 SGB XI)", "value": "4.180 € pro Maßnahme"},
                {"name": "Beratungseinsatz (§ 37 Abs. 3 SGB XI)", "value": "Kostenlos", "details": "Bei Bezug von Pflegegeld 1x pro Vierteljahr Pflicht. Bei Bezug von ausschließlich Pflegesachleistung 1x pro Halbjahr auf Wunsch."},
                {"name": "Beratung durch Pflegestützpunkte und anerkannte Pflegeberater (§§ 7a, 7b SGB XI)", "value": "Anspruch besteht"},
                {"name": "Vollstationäre Pflege (§ 43 SGB XI)", "value": "1.855 € pro Monat", "details": "plus Zuschuss zum Eigenanteil an den pflegebedingten Aufwendungen in Höhe von: 15 % vom 1. bis 12. Monat, 30 % vom 13. bis 24. Monat, 50 % vom 25. bis 36. Monat, 75 % ab dem 37. Monat des Heimaufenthalts"},
                {"name": "Zusätzliche Betreuung im Pflegeheim (§ 43b SGB XI)", "value": "Kostenlos", "details": "sofern vom Pflegeheim angeboten"},
            ]
        },
        "period_2": {
            "date_range": "ab 01.07.2025",
            "leistungen": [
                {"name": "Pflegesachleistungen (§ 36 SGB XI)", "value": "1.859 € pro Monat"},
                {"name": "Pflegegeld (§ 37 SGB XI)", "value": "800 € pro Monat"},
                {"name": "Teilstationäre Pflege (§ 41 SGB XI)", "value": "1.685 € pro Monat"},
                {"name": "Gemeinsamer Jahresbetrag für Verhinderungs- und/oder Kurzzeitpflege", "value": "3.539 € pro Kalenderjahr (bis zu 8 Wochen)", "note": "Wichtig: Bereits im 1. Halbjahr 2025 genutzte Leistungsbeträge werden im Jahr 2025 auf den Gemeinsamen Jahresbetrag angerechnet."},
                {"name": "Entlastungsbetrag (§ 45b SGB XI)", "value": "131 € pro Monat"},
                {"name": "Wohngruppenzuschlag (§ 38a SGB XI)", "value": "224 € pro Monat"},
                {"name": "Pflegehilfsmittel (nicht zum Verbrauch, z.B. Pflegebett)", "value": "Anspruch besteht"},
                {"name": "Pflegehilfsmittel (zum Verbrauch, z.B. Desinfektionsmittel)", "value": "42 € pro Monat"},
                {"name": "Zuschuss zu wohnumfeldverbessernden Maßnahmen (§ 40 SGB XI)", "value": "4.180 € pro Maßnahme"},
                {"name": "Beratungseinsatz (§ 37 Abs. 3 SGB XI)", "value": "Kostenlos", "details": "Bei Bezug von Pflegegeld 1x pro Vierteljahr Pflicht. Bei Bezug von ausschließlich Pflegesachleistung 1x pro Halbjahr auf Wunsch."},
                {"name": "Beratung durch Pflegestützpunkte und anerkannte Pflegeberater (§§ 7a, 7b SGB XI)", "value": "Anspruch besteht"},
                {"name": "Vollstationäre Pflege (§ 43 SGB XI)", "value": "1.855 € pro Monat", "details": "plus Zuschuss zum Eigenanteil an den pflegebedingten Aufwendungen in Höhe von: 15 % vom 1. bis 12. Monat, 30 % vom 13. bis 24. Monat, 50 % vom 25. bis 36. Monat, 75 % ab dem 37. Monat des Heimaufenthalts"},
                {"name": "Zusätzliche Betreuung im Pflegeheim (§ 43b SGB XI)", "value": "Kostenlos", "details": "sofern vom Pflegeheim angeboten"},
            ]
        }
    },
    5: {  # Pflegegrad 5
        "period_1": {
            "date_range": "01.01.2025 - 30.06.2025",
            "leistungen": [
                {"name": "Pflegesachleistungen (§ 36 SGB XI)", "value": "2.299 € pro Monat"},
                {"name": "Pflegegeld (§ 37 SGB XI)", "value": "990 € pro Monat"},
                {"name": "Teilstationäre Pflege (§ 41 SGB XI)", "value": "2.085 € pro Monat"},
                {"name": "Verhinderungspflege (§ 39 SGB XI)", "value": "1.685 € pro Kalenderjahr (bis zu 6 Wochen*)", "note": "*8 Wochen bei Pflegegrad 4 oder 5 bis vollendetes 25. Lebensjahr"},
                {"name": "Verhinderungspflege (Erhöhung aus nicht genutzten Mitteln der Kurzzeitpflege)", "value": "843 € bzw. 1.854 € (U25) pro Kalenderjahr"},
                {"name": "Kurzzeitpflege (§ 42 SGB XI)", "value": "1.854 € pro Kalenderjahr (bis zu 8 Wochen)"},
                {"name": "Kurzzeitpflege (Erhöhung aus nicht genutzten Mitteln der Verhinderungspflege)", "value": "1.685 € pro Kalenderjahr"},
                {"name": "Entlastungsbetrag (§ 45b SGB XI)", "value": "131 € pro Monat"},
                {"name": "Wohngruppenzuschlag (§ 38a SGB XI)", "value": "224 € pro Monat"},
                {"name": "Pflegehilfsmittel (nicht zum Verbrauch, z.B. Pflegebett)", "value": "Anspruch besteht"},
                {"name": "Pflegehilfsmittel (zum Verbrauch, z.B. Desinfektionsmittel)", "value": "42 € pro Monat"},
                {"name": "Zuschuss zu wohnumfeldverbessernden Maßnahmen (§ 40 SGB XI)", "value": "4.180 € pro Maßnahme"},
                {"name": "Beratungseinsatz (§ 37 Abs. 3 SGB XI)", "value": "Kostenlos", "details": "Bei Bezug von Pflegegeld 1x pro Vierteljahr Pflicht. Bei Bezug von ausschließlich Pflegesachleistung 1x pro Halbjahr auf Wunsch."},
                {"name": "Beratung durch Pflegestützpunkte und anerkannte Pflegeberater (§§ 7a, 7b SGB XI)", "value": "Anspruch besteht"},
                {"name": "Vollstationäre Pflege (§ 43 SGB XI)", "value": "2.096 € pro Monat", "details": "plus Zuschuss zum Eigenanteil an den pflegebedingten Aufwendungen in Höhe von: 15 % vom 1. bis 12. Monat, 30 % vom 13. bis 24. Monat, 50 % vom 25. bis 36. Monat, 75 % ab dem 37. Monat des Heimaufenthalts"},
                {"name": "Zusätzliche Betreuung im Pflegeheim (§ 43b SGB XI)", "value": "Kostenlos", "details": "sofern vom Pflegeheim angeboten"},
            ]
        },
        "period_2": {
            "date_range": "ab 01.07.2025",
            "leistungen": [
                {"name": "Pflegesachleistungen (§ 36 SGB XI)", "value": "2.299 € pro Monat"},
                {"name": "Pflegegeld (§ 37 SGB XI)", "value": "990 € pro Monat"},
                {"name": "Teilstationäre Pflege (§ 41 SGB XI)", "value": "2.085 € pro Monat"},
                {"name": "Gemeinsamer Jahresbetrag für Verhinderungs- und/oder Kurzzeitpflege", "value": "3.539 € pro Kalenderjahr (bis zu 8 Wochen)", "note": "Wichtig: Bereits im 1. Halbjahr 2025 genutzte Leistungsbeträge werden im Jahr 2025 auf den Gemeinsamen Jahresbetrag angerechnet."},
                {"name": "Entlastungsbetrag (§ 45b SGB XI)", "value": "131 € pro Monat"},
                {"name": "Wohngruppenzuschlag (§ 38a SGB XI)", "value": "224 € pro Monat"},
                {"name": "Pflegehilfsmittel (nicht zum Verbrauch, z.B. Pflegebett)", "value": "Anspruch besteht"},
                {"name": "Pflegehilfsmittel (zum Verbrauch, z.B. Desinfektionsmittel)", "value": "42 € pro Monat"},
                {"name": "Zuschuss zu wohnumfeldverbessernden Maßnahmen (§ 40 SGB XI)", "value": "4.180 € pro Maßnahme"},
                {"name": "Beratungseinsatz (§ 37 Abs. 3 SGB XI)", "value": "Kostenlos", "details": "Bei Bezug von Pflegegeld 1x pro Vierteljahr Pflicht. Bei Bezug von ausschließlich Pflegesachleistung 1x pro Halbjahr auf Wunsch."},
                {"name": "Beratung durch Pflegestützpunkte und anerkannte Pflegeberater (§§ 7a, 7b SGB XI)", "value": "Anspruch besteht"},
                {"name": "Vollstationäre Pflege (§ 43 SGB XI)", "value": "2.096 € pro Monat", "details": "plus Zuschuss zum Eigenanteil an den pflegebedingten Aufwendungen in Höhe von: 15 % vom 1. bis 12. Monat, 30 % vom 13. bis 24. Monat, 50 % vom 25. bis 36. Monat, 75 % ab dem 37. Monat des Heimaufenthalts"},
                {"name": "Zusätzliche Betreuung im Pflegeheim (§ 43b SGB XI)", "value": "Kostenlos", "details": "sofern vom Pflegeheim angeboten"},
            ]
        }
    },
}

# You might add a helper function here later to get the correct period based on current date
