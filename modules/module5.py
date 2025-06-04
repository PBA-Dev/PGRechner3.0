# modules/module5.py

# NOTE: This structure needs the specific scoring logic based on frequency rules.
# The 'score' in options might be replaced or supplemented by frequency inputs later.

module5 = {
    'id': 5,
    'name': 'Modul 5: Bewältigung von und selbständiger Umgang mit krankheits- oder therapiebedingten Anforderungen und Belastungen',
    'weight': 20, # Weight in percent for final score calculation
    'parts': [ # Organize by parts as in the document
        {
            'part_id': '5.1',
            'name': 'Teil 1: Medikation, Injektionen, Versorgung intravenöser Zugänge, Absaugen und Sauerstoffgabe, Einreibungen, Messungen, Hilfsmittel',
            'questions': [
                {
                    'id': '5.1.1',
                    'text': 'Medikation',
                    'explanation': 'Regelmäßige Medikamenteneinnahme.',
                    'type': 'frequency', # Indicate this needs frequency input
                    'options': [{'text': 'Entfällt'}, {'text': 'Selbständig'}], # Base options
                    'frequency_units': ['pro Tag', 'pro Woche', 'pro Monat'] # Units for input
                    # Scoring logic based on frequency needed here
                },
                {
                    'id': '5.1.2',
                    'text': 'Injektionen (subcutan und intramuskulär)',
                    'explanation': 'Verabreichung von Injektionen.',
                    'type': 'frequency',
                    'options': [{'text': 'Entfällt'}, {'text': 'Selbständig'}],
                    'frequency_units': ['pro Tag', 'pro Woche', 'pro Monat']
                },
                {
                    'id': '5.1.3',
                    'text': 'Versorgung intravenöser Zugänge (Port)',
                    'explanation': 'Pflege und Nutzung von IV-Zugängen.',
                     'type': 'frequency',
                    'options': [{'text': 'Entfällt'}, {'text': 'Selbständig'}],
                    'frequency_units': ['pro Tag', 'pro Woche', 'pro Monat']
                },
                {
                    'id': '5.1.4',
                    'text': 'Absaugen und Sauerstoffgabe',
                    'explanation': 'Notwendigkeit von Absaugung oder Sauerstoff.',
                     'type': 'frequency',
                    'options': [{'text': 'Entfällt'}, {'text': 'Selbständig'}],
                    'frequency_units': ['pro Tag', 'pro Woche', 'pro Monat']
                },
                {
                    'id': '5.1.5',
                    'text': 'Einreibungen oder Kälte- und Wärmeanwendungen',
                    'explanation': 'Anwendung von Salben, Cremes, Kälte-/Wärmepackungen.',
                     'type': 'frequency',
                    'options': [{'text': 'Entfällt'}, {'text': 'Selbständig'}],
                    'frequency_units': ['pro Tag', 'pro Woche', 'pro Monat']
                },
                {
                    'id': '5.1.6',
                    'text': 'Messung und Deutung von Körperzuständen',
                    'explanation': 'Blutzucker-, Blutdruckmessung etc.',
                     'type': 'frequency',
                    'options': [{'text': 'Entfällt'}, {'text': 'Selbständig'}],
                    'frequency_units': ['pro Tag', 'pro Woche', 'pro Monat']
                },
                 {
                    'id': '5.1.7',
                    'text': 'Körpernahe Hilfsmittel',
                    'explanation': 'Umgang mit Prothesen, Orthesen, Kompressionsstrümpfen etc.',
                     'type': 'frequency',
                    'options': [{'text': 'Entfällt'}, {'text': 'Selbständig'}],
                    'frequency_units': ['pro Tag', 'pro Woche', 'pro Monat']
                },
            ]
        },
        {
            'part_id': '5.2',
            'name': 'Teil 2: Verbandswechsel, Stomaversorgung, Katheterisierung, Therapiemaßnahmen',
             'questions': [
                 {
                    'id': '5.2.1',
                    'text': 'Verbandswechsel und Wundversorgung',
                    'explanation': 'Versorgung von Wunden, Anlegen von Verbänden.',
                    'type': 'frequency',
                    'options': [{'text': 'Entfällt'}, {'text': 'Selbständig'}],
                    'frequency_units': ['pro Tag', 'pro Woche', 'pro Monat']
                 },
                 {
                    'id': '5.2.2',
                    'text': 'Versorgung mit Stoma',
                    'explanation': 'Pflege und Wechsel von Stomabeuteln.',
                    'type': 'frequency',
                    'options': [{'text': 'Entfällt'}, {'text': 'Selbständig'}],
                    'frequency_units': ['pro Tag', 'pro Woche', 'pro Monat']
                 },
                 {
                    'id': '5.2.3',
                    'text': 'Regelmäßige Einmalkatheterisierung und Nutzung von Abführmethoden',
                    'explanation': 'Durchführung von Katheterisierung oder Abführmaßnahmen.',
                    'type': 'frequency',
                    'options': [{'text': 'Entfällt'}, {'text': 'Selbständig'}],
                    'frequency_units': ['pro Tag', 'pro Woche', 'pro Monat']
                 },
                 {
                    'id': '5.2.4',
                    'text': 'Therapiemaßnahmen in der häuslichen Umgebung',
                    'explanation': 'Durchführung von z.B. Physiotherapie, Ergotherapie zu Hause.',
                    'type': 'frequency',
                    'options': [{'text': 'Entfällt'}, {'text': 'Selbständig'}],
                    'frequency_units': ['pro Tag', 'pro Woche', 'pro Monat']
                 },
             ]
        },
        {
            'part_id': '5.3',
            'name': 'Teil 3: Zeit- und technikintensive Maßnahmen',
             'questions': [
                 {
                    'id': '5.3.1',
                    'text': 'Zeit- und technikintensive Maßnahmen in häuslicher Umgebung',
                    'explanation': 'z.B. Beatmung, Dialyse.',
                    'type': 'frequency',
                    'options': [{'text': 'Entfällt'}, {'text': 'Selbständig'}],
                    'frequency_units': ['pro Tag', 'pro Woche', 'pro Monat'] # Check units needed
                 },
             ]
        },
        {
            'part_id': '5.4',
            'name': 'Teil 4: Arztbesuche und andere Termine',
             'questions': [
                 {
                    'id': '5.4.1',
                    'text': 'Arztbesuche',
                    'explanation': 'Häufigkeit von Arztbesuchen.',
                    'type': 'frequency',
                    'options': [{'text': 'Entfällt'}, {'text': 'Selbständig'}],
                    'frequency_units': ['pro Woche', 'pro Monat'] # Units from doc
                 },
                 {
                    'id': '5.4.2',
                    'text': 'Besuch anderer medizinischer oder therapeutischer Einrichtungen (bis zu drei Stunden)',
                    'explanation': 'Termine bei Therapeuten, Sanitätshaus etc.',
                    'type': 'frequency',
                    'options': [{'text': 'Entfällt'}, {'text': 'Selbständig'}],
                    'frequency_units': ['pro Woche', 'pro Monat']
                 },
                 {
                    'id': '5.4.3',
                    'text': 'Zeitlich ausgedehnte Besuche anderer medizinischer und therapeutischer Einrichtungen (länger als drei Stunden)',
                    'explanation': 'Längere Termine, z.B. Tagesklinik.',
                    'type': 'frequency',
                    'options': [{'text': 'Entfällt'}, {'text': 'Selbständig'}],
                    'frequency_units': ['pro Woche', 'pro Monat']
                 },
             ]
        },
        {
            'part_id': '5.5',
            'name': 'Teil 5: Diät und Verhaltensvorschriften',
             'questions': [
                 {
                    'id': '5.5.1',
                    'text': 'Einhaltung einer Diät und anderer krankheits- oder therapiebedingter Verhaltensvorschriften',
                    'explanation': 'Fähigkeit, Diätpläne oder spezielle Verhaltensregeln einzuhalten.',
                    'type': 'standard', # This seems to be a standard choice question
                    'options': [
                        {'text': 'Entfällt/Selbständig', 'score': 0}, # Combine based on doc? Needs clarification
                        # {'text': 'Selbständig', 'score': 0}, # Or separate?
                        {'text': 'Überwiegend selbständig', 'score': 1}, # Scores need verification
                        {'text': 'Überwiegend unselbständig', 'score': 2},
                        {'text': 'Unselbständig', 'score': 3}
                    ]
                 },
             ]
        },
    ]
    # Add function here later to calculate total raw score based on frequencies
}