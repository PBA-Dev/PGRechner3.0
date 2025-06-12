# modules/module1.py

module1 = {
    'id': 1,
    'name': 'Modul 1: Mobilität',
    'weight': 10, # Weight in percent for final score calculation
    'questions': [
        {
            'id': '1.1',
            'text': 'Positionswechsel im Bett',
            'explanation': 'Fähigkeit, sich im Bett selbständig zu drehen und aufzurichten.',
            'options': [
                {
                    'text': 'Selbständig',
                    'score': 0,
                    'option_explanation': (
                        'Selbständig ist auch eine Person, die ihre Position unter '
                        'Nutzung von Hilfsmitteln (Aufrichthilfe, Bettseitenteil, '
                        'Strickleiter, elektrisch verstellbares Bett) allein verändern kann.'
                    )
                },
                {
                    'text': 'Überwiegend selbständig',
                    'score': 1,
                    'option_explanation': (
                        'Die Person kann beispielsweise nach Anreichen eines Hilfsmittels '
                        'oder Reichen der Hand ihre Lage im Bett verändern.'
                    )
                },
                {
                    'text': 'Überwiegend unselbständig',
                    'score': 2,
                    'option_explanation': (
                        'Die Person kann beim Positionswechsel nur wenig mithelfen, zum '
                        'Beispiel auf den Rücken rollen, am Bettgestell festhalten, oder '
                        'zum Lagern die Arme vor der Brust verschränken und den Kopf auf '
                        'die Brust legen.'
                    )
                },
                {
                    'text': 'Unselbständig',
                    'score': 3,  # Score 3 based on doc example
                    'option_explanation': (
                        'Die Person kann sich beim Positionswechsel nicht oder nur minimal '
                        'beteiligen.'
                    )
                }
            ]
        },
        {
            'id': '1.2',
            'text': 'Halten einer stabilen Sitzposition',
            'explanation': 'Fähigkeit, ohne oder mit nur geringer Unterstützung aufrecht zu sitzen.',
            'options': [
                {'text': 'Selbständig', 'score': 0},
                {'text': 'Überwiegend selbständig', 'score': 1},
                {'text': 'Überwiegend unselbständig', 'score': 2},
                {'text': 'Unselbständig', 'score': 3} # Score 3 based on doc example
            ]
        },
        {
            'id': '1.3',
            'text': 'Umsetzen',
            'explanation': 'Fähigkeit, z.B. vom Bett in den Rollstuhl oder auf einen Stuhl zu wechseln.',
            'options': [
                {'text': 'Selbständig', 'score': 0},
                {'text': 'Überwiegend selbständig', 'score': 1},
                {'text': 'Überwiegend unselbständig', 'score': 2},
                {'text': 'Unselbständig', 'score': 3} # Score 3 based on doc example
            ]
        },
        {
            'id': '1.4',
            'text': 'Fortbewegen innerhalb des Wohnbereichs',
            'explanation': 'Fähigkeit, sich in der Wohnung (auch mit Hilfsmitteln wie Rollator) fortzubewegen.',
            'options': [
                {'text': 'Selbständig', 'score': 0},
                {'text': 'Überwiegend selbständig', 'score': 1},
                {'text': 'Überwiegend unselbständig', 'score': 2},
                {'text': 'Unselbständig', 'score': 3} # Score 3 based on doc example
            ]
        },
        {
            'id': '1.5',
            'text': 'Treppensteigen',
            'explanation': 'Fähigkeit, eine Treppe (mind. eine Etage) auf- und abzusteigen.',
            'options': [
                {'text': 'Selbständig', 'score': 0},
                {'text': 'Überwiegend selbständig', 'score': 1},
                {'text': 'Überwiegend unselbständig', 'score': 2},
                {'text': 'Unselbständig', 'score': 3} # Score 3 based on doc example
            ]
        }
    ]
}