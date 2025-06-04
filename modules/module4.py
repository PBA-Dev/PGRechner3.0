# modules/module4.py

module4 = {
    'id': 4,
    'name': 'Modul 4: Selbstversorgung',
    'weight': 40, # Weight in percent for final score calculation
    'questions': [
        {
            'id': '4.1',
            'text': 'Waschen des vorderen Oberkörpers',
            'explanation': 'Beinhaltet das Waschen von Händen, Gesicht, Hals, Armen, Achselhöhlen und vorderem Oberkörper.',
            'options': [
                {'text': 'Selbständig', 'score': 0},
                {'text': 'Überwiegend selbständig', 'score': 1},
                {'text': 'Überwiegend unselbständig', 'score': 2},
                {'text': 'Unselbständig', 'score': 3}
            ]
        },
        {
            'id': '4.2',
            'text': 'Körperpflege im Bereich des Kopfes',
            'explanation': 'Beinhaltet Kämmen, Zahnpflege/Prothesenreinigung, Rasieren.',
            'options': [
                {'text': 'Selbständig', 'score': 0},
                {'text': 'Überwiegend selbständig', 'score': 1},
                {'text': 'Überwiegend unselbständig', 'score': 2},
                {'text': 'Unselbständig', 'score': 3}
            ]
        },
        {
            'id': '4.3',
            'text': 'Waschen des Intimbereichs',
            'explanation': 'Beinhaltet das Waschen des Intimbereichs und das Abtrocknen.',
            'options': [
                {'text': 'Selbständig', 'score': 0},
                {'text': 'Überwiegend selbständig', 'score': 1},
                {'text': 'Überwiegend unselbständig', 'score': 2},
                {'text': 'Unselbständig', 'score': 3}
            ]
        },
        {
            'id': '4.4',
            'text': 'Duschen und Baden einschließlich Waschen der Haare',
            'explanation': 'Umfasst Ganzkörperwäsche in Dusche oder Badewanne, einschließlich Haare waschen und Abtrocknen.',
            'options': [
                {'text': 'Selbständig', 'score': 0},
                {'text': 'Überwiegend selbständig', 'score': 1},
                {'text': 'Überwiegend unselbständig', 'score': 2},
                {'text': 'Unselbständig', 'score': 3}
            ]
        },
        {
            'id': '4.5',
            'text': 'An- und Auskleiden des Oberkörpers',
            'explanation': 'Beinhaltet das An- und Ausziehen von Hemd, Bluse, Pullover, Unterhemd, BH etc.',
            'options': [
                {'text': 'Selbständig', 'score': 0},
                {'text': 'Überwiegend selbständig', 'score': 1},
                {'text': 'Überwiegend unselbständig', 'score': 2},
                {'text': 'Unselbständig', 'score': 3}
            ]
        },
        {
            'id': '4.6',
            'text': 'An- und Auskleiden des Unterkörpers',
            'explanation': 'Beinhaltet das An- und Ausziehen von Hose, Rock, Unterhose, Strümpfen, Schuhen.',
            'options': [
                {'text': 'Selbständig', 'score': 0},
                {'text': 'Überwiegend selbständig', 'score': 1},
                {'text': 'Überwiegend unselbständig', 'score': 2},
                {'text': 'Unselbständig', 'score': 3}
            ]
        },
        {
            'id': '4.7',
            'text': 'Mundgerechtes Zubereiten der Nahrung und Eingießen von Getränken',
            'explanation': 'Beinhaltet das Zerkleinern von Speisen, Öffnen von Verpackungen, Eingießen von Getränken.',
            'options': [
                {'text': 'Selbständig', 'score': 0},
                {'text': 'Überwiegend selbständig', 'score': 1},
                {'text': 'Überwiegend unselbständig', 'score': 2},
                {'text': 'Unselbständig', 'score': 3}
            ]
        },
        {
            'id': '4.8',
            'text': 'Essen',
            'explanation': 'Beinhaltet das Führen des Essens zum Mund, Abbeißen, Kauen, Schlucken.',
            'options': [
                {'text': 'Selbständig', 'score': 0},
                {'text': 'Überwiegend selbständig', 'score': 1},
                {'text': 'Überwiegend unselbständig', 'score': 2},
                {'text': 'Unselbständig', 'score': 3}
            ]
        },
        {
            'id': '4.9',
            'text': 'Trinken',
            'explanation': 'Beinhaltet das Ergreifen des Trinkgefäßes, Führen zum Mund, Trinken.',
            'options': [
                {'text': 'Selbständig', 'score': 0},
                {'text': 'Überwiegend selbständig', 'score': 1},
                {'text': 'Überwiegend unselbständig', 'score': 2},
                {'text': 'Unselbständig', 'score': 3}
            ]
        },
        {
            'id': '4.10',
            'text': 'Benutzen einer Toilette oder eines Toilettenstuhls',
            'explanation': 'Umfasst Hinsetzen, Aufstehen, Sitzen während der Blasen-/Darmentleerung, Intimhygiene, Richten der Kleidung.',
            'options': [
                {'text': 'Selbständig', 'score': 0},
                {'text': 'Überwiegend selbständig', 'score': 1},
                {'text': 'Überwiegend unselbständig', 'score': 2},
                {'text': 'Unselbständig', 'score': 3}
            ]
        },
        {
            'id': '4.11',
            'text': 'Bewältigen der Folgen einer Harninkontinenz und Umgang mit Dauerkatheter und Urostoma',
            'explanation': 'Beinhaltet das Wechseln von Inkontinenzmaterial, Umgang mit Katheter/Urostoma, Entsorgung.',
            'options': [
                {'text': 'Selbständig', 'score': 0},
                {'text': 'Überwiegend selbständig', 'score': 1},
                {'text': 'Überwiegend unselbständig', 'score': 2},
                {'text': 'Unselbständig', 'score': 3}
            ]
        },
        {
            'id': '4.12',
            'text': 'Bewältigen der Folgen einer Stuhlinkontinenz und Umgang mit Stoma',
            'explanation': 'Beinhaltet das Wechseln von Inkontinenzmaterial, Umgang mit Stoma, Entsorgung.',
            'options': [
                {'text': 'Selbständig', 'score': 0},
                {'text': 'Überwiegend selbständig', 'score': 1},
                {'text': 'Überwiegend unselbständig', 'score': 2},
                {'text': 'Unselbständig', 'score': 3}
            ]
        },
        # --- NEW QUESTION ---
        {
            'id': '4.13',
            'text': 'Ernährung parenteral oder über Sonde',
            'explanation': 'Bewertung der Notwendigkeit künstlicher Ernährung.',
            'options': [
                {'text': 'Keine, nicht täglich, nicht auf Dauer', 'score': 0}, # Assuming 0 points based on doc example 'x' placement
                {'text': 'Täglich, zusätzlich zu oraler Nahrung', 'score': 1}, # Assuming 1 point
                {'text': 'Ausschließlich oder nahezu ausschließlich', 'score': 3} # Assuming 3 points (needs verification)
                # NOTE: The exact scoring (0, 1, 3?) needs verification against official NBA guidelines.
                # The document example only shows 'x' under the first column (0 points).
            ]
        },
        # --- END NEW QUESTION ---
    ]
}