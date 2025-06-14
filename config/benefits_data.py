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
    1: { # Pflegegrad 1 - Add specific benefits
        "period_1": {"date_range": "01.01.2025 - 30.06.2025", "leistungen": [
            {"name": "Entlastungsbetrag (§ 45b SGB XI)", "value": "131 € pro Monat"},
            {"name": "Pflegehilfsmittel (zum Verbrauch, § 40 SGB XI)", "value": "42 € pro Monat"},
            {"name": "Zuschuss Wohnumfeldverbesserung (§ 40 SGB XI)", "value": "4.180 € pro Maßnahme"},
            # Add other PG1 specific benefits (Beratung, Wohngruppenzuschlag etc.)
        ]},
        "period_2": {"date_range": "ab 01.07.2025", "leistungen": [
             {"name": "Entlastungsbetrag (§ 45b SGB XI)", "value": "131 € pro Monat"},
             {"name": "Pflegehilfsmittel (zum Verbrauch, § 40 SGB XI)", "value": "42 € pro Monat"},
             {"name": "Zuschuss Wohnumfeldverbesserung (§ 40 SGB XI)", "value": "4.180 € pro Maßnahme"},
            # Add other PG1 specific benefits (Beratung, Wohngruppenzuschlag etc.)
        ]},
    },
    2: { # Pflegegrad 2 - Add specific benefits
        "period_1": {"date_range": "01.01.2025 - 30.06.2025", "leistungen": []}, # Populate PG2 benefits
        "period_2": {"date_range": "ab 01.07.2025", "leistungen": []}, # Populate PG2 benefits
    },
    3: { # Pflegegrad 3 - Add specific benefits
        "period_1": {"date_range": "01.01.2025 - 30.06.2025", "leistungen": []}, # Populate PG3 benefits
        "period_2": {"date_range": "ab 01.07.2025", "leistungen": []}, # Populate PG3 benefits
    },
    4: { # Pflegegrad 4 - Data from document example
        "period_1": {
            "date_range": "01.01.2025 - 30.06.2025",
            "leistungen": [
                {"name": "Pflegesachleistungen (§ 36 SGB XI)", "value": "1.859 € pro Monat"},
                {"name": "Pflegegeld (§ 37 SGB XI)", "value": "800 € pro Monat"},
                {"name": "Teilstationäre Pflege (§ 41 SGB XI)", "value": "1.685 € pro Monat"},
                {"name": "Verhinderungspflege (§ 39 SGB XI)", "value": "1.685 € pro Kalenderjahr (bis 6 Wochen*)"},
                {"name": "Verhinderungspflege (Erhöhung Kurzzeitpflege)", "value": "843 € / 1.854 € (U25) pro Kalenderjahr"},
                {"name": "Kurzzeitpflege (§ 42 SGB XI)", "value": "1.854 € pro Kalenderjahr (bis 8 Wochen)"},
                {"name": "Kurzzeitpflege (Erhöhung Verhinderungspflege)", "value": "1.685 € pro Kalenderjahr"},
                {"name": "Entlastungsbetrag (§ 45b SGB XI)", "value": "131 € pro Monat"},
                {"name": "Wohngruppenzuschlag (§ 38a SGB XI)", "value": "224 € pro Monat"},
                {"name": "Pflegehilfsmittel (nicht zum Verbrauch)", "value": "Anspruch besteht"},
                {"name": "Pflegehilfsmittel (zum Verbrauch)", "value": "42 € pro Monat"},
                {"name": "Zuschuss Wohnumfeldverbesserung (§ 40 SGB XI)", "value": "4.180 € pro Maßnahme"},
                {"name": "Beratungseinsatz (§ 37 Abs. 3 SGB XI)", "value": "1x pro Vierteljahr (Pflegegeld) / 1x pro Halbjahr (Sachleistung)"},
                {"name": "Beratung (§§ 7a, 7b SGB XI)", "value": "Anspruch besteht"},
                {"name": "Vollstationäre Pflege (§ 43 SGB XI)", "value": "1.855 € pro Monat + Zuschuss"},
                {"name": "Zusätzliche Betreuung im Pflegeheim (§ 43b SGB XI)", "value": "Anspruch besteht"},
            ]
        },
        "period_2": {
            "date_range": "ab 01.07.2025",
            "leistungen": [
                {"name": "Pflegesachleistungen (§ 36 SGB XI)", "value": "1.859 € pro Monat"},
                {"name": "Pflegegeld (§ 37 SGB XI)", "value": "800 € pro Monat"},
                {"name": "Teilstationäre Pflege (§ 41 SGB XI)", "value": "1.685 € pro Monat"},
                {"name": "Gemeinsamer Jahresbetrag (VHP/Kzp)", "value": "3.539 € pro Kalenderjahr (bis 8 Wochen)"},
                # Note: VHP/Kzp are combined from July 1st
                {"name": "Entlastungsbetrag (§ 45b SGB XI)", "value": "131 € pro Monat"},
                {"name": "Wohngruppenzuschlag (§ 38a SGB XI)", "value": "224 € pro Monat"},
                {"name": "Pflegehilfsmittel (nicht zum Verbrauch)", "value": "Anspruch besteht"},
                {"name": "Pflegehilfsmittel (zum Verbrauch)", "value": "42 € pro Monat"},
                {"name": "Zuschuss Wohnumfeldverbesserung (§ 40 SGB XI)", "value": "4.180 € pro Maßnahme"},
                {"name": "Beratungseinsatz (§ 37 Abs. 3 SGB XI)", "value": "1x pro Vierteljahr (Pflegegeld) / 1x pro Halbjahr (Sachleistung)"},
                {"name": "Beratung (§§ 7a, 7b SGB XI)", "value": "Anspruch besteht"},
                {"name": "Vollstationäre Pflege (§ 43 SGB XI)", "value": "1.855 € pro Monat + Zuschuss"},
                {"name": "Zusätzliche Betreuung im Pflegeheim (§ 43b SGB XI)", "value": "Anspruch besteht"},
            ]
        }
    },
    5: { # Pflegegrad 5 - Add specific benefits
        "period_1": {"date_range": "01.01.2025 - 30.06.2025", "leistungen": []}, # Populate PG5 benefits
        "period_2": {"date_range": "ab 01.07.2025", "leistungen": []}, # Populate PG5 benefits
    },
}

# You might add a helper function here later to get the correct period based on current date
