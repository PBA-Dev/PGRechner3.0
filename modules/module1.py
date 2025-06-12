# modules/module1.py

module1 = {
    'id': 1,
    'name': 'Modul 1: Mobilität',
    'weight': 10, # Weight in percent for final score calculation
    'questions': [
        {
            'id': '1.1',
            'text': 'Positionswechsel im Bett',
            'explanation': '''Die Einschätzung richtet sich ausschließlich danach, ob die Person in der Lage
ist, ohne personelle Unterstützung eine Körperhaltung einzunehmen/zu wechseln
und sich fortzubewegen. Zu beurteilen sind hier ausschließlich motorische
Aspekte wie Körperkraft, Balance, Bewegungskoordination et cetera und nicht
die zielgerichtete Fortbewegung. Hier werden nicht die Folgen kognitiver Beeinträchtigungen
auf Planung, Steuerung und Durchführung motorischer Handlungen
abgebildet.''',
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
            'explanation': '''Sich auf einem Bett, Stuhl oder Sessel aufrecht halten''',
            'options': [
                {
                    'text': 'Selbständig',
                    'score': 0,
                    'option_explanation': (
                        'Selbständig ist eine Person auch dann, wenn sie beim Sitzen gelegentlich ihre'
                        'Sitzposition korrigieren muss.'
                    )
                },
                {
                    'text': 'Überwiegend selbständig',
                    'score': 1,
                    'option_explanation': (
                        '''Die Person kann sich nur kurz, zum Beispiel für die Dauer einer Mahlzeit oder
eines Waschvorgangs selbständig in der Sitzposition halten, darüber hinaus
benötigt sie aber personelle Unterstützung zur Positionskorrektur.'''
                    )
                },
                {
                    'text': 'Überwiegend unselbständig',
                    'score': 2,
                    'option_explanation': (
                        '''Die Person kann sich wegen eingeschränkter Rumpfkontrolle auch mit Rückenund
Seitenstütze nicht in aufrechter Position halten und benötigt auch während
der Dauer einer Mahlzeit oder eines Waschvorgangs personelle Unterstützung
zur Positionskorrektur.'''
                    )
                },
                {
                    'text': 'Unselbständig',
                    'score': 3,  # Score 3 based on doc example
                    'option_explanation': (
                        '''Die Person kann sich nicht in Sitzposition halten. Bei fehlender Rumpf- und Kopfkontrolle
kann die Person nur im Bett oder Lagerungsstuhl liegend gelagert werden.'''
                    )
                }
            ]
        },
        {
            'id': '1.3',
            'text': 'Umsetzen',
            'explanation': '''Von einer üblich hohen Sitzgelegenheit aufstehen und sich auf eine andere
umsetzen (übliche Sitzhöhe etwa 45 cm)''',
            'options': [
                {
                    'text': 'Selbständig',
                    'score': 0,
                    'option_explanation': (
                        '''Selbständig ist jemand auch dann, wenn er keine Personenhilfe benötigt, aber
ein Hilfsmittel oder einen anderen Gegenstand zum Festhalten oder Hochziehen
(zum Beispiel Griffstangen) benutzt oder sich auf Tisch, Armlehnen oder sonstigen
Gegenständen abstützen muss, um aufzustehen. Als selbständig ist auch
zu bewerten, wer zwar nicht stehen kann, aber sich mit Armkraft ohne personelle
Hilfe umsetzen kann (zum Beispiel Rollstuhl – Toilette).'''
                    )
                },
                {
                    'text': 'Überwiegend selbständig',
                    'score': 1,
                    'option_explanation': (
                        '''Die Person kann aus eigener Kraft aufstehen oder sich umsetzen, wenn sie eine
Hand oder einen Arm gereicht bekommt.'''
                    )
                },
                {
                    'text': 'Überwiegend unselbständig',
                    'score': 2,
                    'option_explanation': (
                        '''Die Pflegeperson muss beim Aufstehen, Umsetzen (erheblichen) Kraftaufwand
aufbringen (hochziehen, halten, stützen, heben). Die beeinträchtigte Person hilft
jedoch in geringem Maße mit, kann zum Beispiel kurzzeitig stehen.'''
                    )
                },
                {
                    'text': 'Unselbständig',
                    'score': 3,  # Score 3 based on doc example
                    'option_explanation': (
                        '''Die Person muss gehoben oder getragen werden, Mithilfe ist nicht möglich.'''
                    )
                }
            ]
        },
        {
            'id': '1.4',
            'text': 'Fortbewegen innerhalb des Wohnbereichs',
            'explanation': '''Sich innerhalb einer Wohnung oder im Wohnbereich einer Einrichtung zwischen
den Zimmern sicher bewegen
Als Anhaltsgröße für übliche Gehstrecken innerhalb einer Wohnung werden mindestens
acht Meter festgelegt.
Die Fähigkeiten zur örtlichen Orientierung und zum Treppensteigen sind unter
Punkt F 4.2.2 beziehungsweise Punkt F 4.1.5 zu berücksichtigen.''',
             'options': [
                {
                    'text': 'Selbständig',
                    'score': 0,
                    'option_explanation': (
                        '''Die Person kann sich ohne Hilfe durch andere Personen fortbewegen. Dies kann
gegebenenfalls unter Nutzung von Hilfsmitteln, zum Beispiel Rollator, Rollstuhl
oder sonstigen Gegenständen, zum Beispiel Stock oder Möbelstück, geschehen.'''
                    )
                },
                {
                    'text': 'Überwiegend selbständig',
                    'score': 1,
                    'option_explanation': (
                        '''Die Person kann die Aktivität überwiegend selbständig durchführen. Personelle
Hilfe ist beispielsweise erforderlich im Sinne von Bereitstellen von Hilfsmitteln
(zum Beispiel Rollator oder Gehstock), punktuellem Stützen/Unterhaken oder
Beobachtung (Anwesenheit aus Sicherheitsgründen).'''
                    )
                },
                {
                    'text': 'Überwiegend unselbständig',
                    'score': 2,
                    'option_explanation': (
                        '''Die Person kann nur wenige Schritte gehen oder sich mit dem Rollstuhl nur
wenige Meter fortbewegen oder kann nur mit Stützung oder Festhalten einer
Pflegeperson gehen.
Auch wenn sich die Person darüber hinaus aus eigenem Willen in ihrer Wohnung
krabbelnd oder robbend fortbewegen kann, ändert dies nichts an der Bewertung
als „überwiegend unselbständig“.'''
                    )
                },
                {
                    'text': 'Unselbständig',
                    'score': 3,  # Score 3 based on doc example
                    'option_explanation': (
                        '''Die Person muss getragen oder vollständig im Rollstuhl geschoben werden.'''
                    )
                }
            ]
        },
        {
            'id': '1.5',
            'text': 'Treppensteigen',
            'explanation': '''Überwinden von Treppen zwischen zwei Etagen in aufrechter Position''',
            'options': [
                {
                    'text': 'Selbständig',
                    'score': 0,
                    'option_explanation': (
                        '''Die Person kann ohne Hilfe durch andere Personen in aufrechter Position eine
Treppe steigen.'''
                    )
                },
                {
                    'text': 'Überwiegend selbständig',
                    'score': 1,
                    'option_explanation': (
                        '''Die Person kann eine Treppe alleine steigen, benötigt aber Begleitung wegen
eines Sturzrisikos (Anwesenheit aus Sicherheitsgründen).'''
                    )
                },
                {
                    'text': 'Überwiegend unselbständig',
                    'score': 2,
                    'option_explanation': (
                        '''Treppensteigen ist nur mit Stützen oder Festhalten der Person möglich.'''
                    )
                },
                {
                    'text': 'Unselbständig',
                    'score': 3,  # Score 3 based on doc example
                    'option_explanation': (
                        '''Person muss getragen oder mit Hilfsmitteln transportiert werden, keine Eigenbeteiligung.'''
                    )
                }
            ]
        },

        {
            'id': '1.B',
            'text': 'Besondere Bedarfskonstellation',
            'explanation': '''Gemäß § 15 Absatz 4 SGB XI können Pflegebedürftige mit besonderen Bedarfskonstellationen,
die einen spezifischen, außergewöhnlich hohen Hilfebedarf mit
besonderen Anforderungen an die pflegerische Versorgung aufweisen, aus pflegefachlichen
Gründen dem Pflegegrad 5 zugeordnet werden, auch wenn ihre
Gesamtpunkte unter 90 liegen.''' + 
'''In Betracht kommen Pflegebedürftige, die rein nach Punkten den Pflegegrad 5
nicht erreichen würden, dieser aber aufgrund der Schwere der Beeinträchtigung
angemessen wäre. Als besondere Bedarfskonstellation ist nur die Gebrauchsunfähigkeit
beider Arme und beider Beine festgelegt. Hintergrund ist, dass die
jeweiligen gesundheitlichen Probleme sich einer pflegefachlichen Systematisie57
rung im neuen Begutachtungsinstrument entziehen. Trotz vollständiger Abhängigkeit
von personeller Hilfe ist es möglich, dass bei diesem Personenkreis im
Bereich der Module 2 und 3 keine und im Bereich des Moduls 6 Beeinträchtigungen
nur im geringen Maß vorliegen, so dass die Gesamtpunkte unter 90 liegen.
Gebrauchsunfähigkeit beider Arme und beider Beine mit vollständigem
Verlust der Greif-, Steh- und Gehfunktionen, die nicht durch Einsatz von
Hilfsmitteln kompensiert werden''' 
''' können, liegt vor, wenn die Person
Das Kriterium erfasst in der Regel Personen mit einer Bewegungsunfähigkeit
beider Arme und beider Beine unabhängig von der Ursache. Gebrauchsunfähigkeit
beider Arme und beider Beine mit vollständigem Verlust der Greif-, Steh- und
Gehfunktionen liegt zum Beispiel vor bei kompletten Lähmungen aller Extremitäten
oder bei Menschen im Wachkoma. Auch bei hochgradigen Kontrakturen,
Versteifungen, bei hochgradigem Tremor, Rigor oder Athetose kann die besondere
Bedarfskonstellation vorliegen. Eine Gebrauchsunfähigkeit beider Arme
und beider Beine liegt auch vor, wenn eine minimale Restbeweglichkeit der Arme
vorhanden ist oder nur noch unkontrollierbare Greifreflexe bestehen.'''
            
              
        }
    ]
}