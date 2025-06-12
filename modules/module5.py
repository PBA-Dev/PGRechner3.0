# modules/module5.py

# NOTE: This structure needs the specific scoring logic based on frequency rules.
# The 'score' in options might be replaced or supplemented by frequency inputs later.

module5 = {
    'id': 5,
    'name': 'Modul 5: Bewältigung von und selbständiger Umgang mit krankheits- oder therapiebedingten Anforderungen und Belastungen',
    'weight': 20,
    'parts': [
        {
            'part_id': '5.1',
            'name': 'Teil 1: Medikation, Injektionen, Versorgung intravenöser Zugänge, Absaugen und Sauerstoffgabe, Einreibungen, Messungen, Hilfsmittel',
            'questions': [
                {
                    'id': '5.1.1',
                    'text': 'Medikation',
                    'explanation': '''Orale Medikation, Augen- oder Ohrentropfen, Dosieraerosole oder Pulverinhalatoren, Zäpfchen und Medikamentenpflaster.
Das Ausmaß der Hilfestellung kann von einmal wöchentlichem Stellen der Medikamente im Wochendispenser bis zu mehrfach täglicher Einzelgabe differieren. Werden Medikamente verabreicht, ist das Stellen nicht gesondert zu berücksichtigen.
Berücksichtigt wird der einzelne Applikationsort (Ohren- und Augen zählen als jeweils ein Ort) und die Applikationshäufigkeit. Unter oraler Medikation wird auch die Gabe über PEG berücksichtigt. Abführmethoden sind unter F 4.5.10 zu bewerten.''',
                    'type': 'frequency',
                    'options': [{'text': 'Entfällt'}, {'text': 'Selbständig'}],
                    'frequency_units': ['pro Tag', 'pro Woche', 'pro Monat']
                },
                {
                    'id': '5.1.2',
                    'text': 'Injektionen',
                    'explanation': '''Subkutane und intramuskuläre Injektionen und subkutane Infusionen, z.B. Insulingaben oder die Versorgung von Medikamentenpumpen über einen subkutanen Zugang.''',
                    'type': 'frequency',
                    'options': [{'text': 'Entfällt'}, {'text': 'Selbständig'}],
                    'frequency_units': ['pro Tag', 'pro Woche', 'pro Monat']
                },
                {
                    'id': '5.1.3',
                    'text': 'Versorgung intravenöser Zugänge',
                    'explanation': '''Versorgung und Verbände venöser Zugänge wie Shaldon oder Broviac sowie die Port-Versorgung. Auch das Einbringen von Medikamenten in einen vorhandenen Zugang wird berücksichtigt. Die Versorgung intrathekaler Zugänge ist ebenfalls hier einzuordnen.''',
                    'type': 'frequency',
                    'options': [{'text': 'Entfällt'}, {'text': 'Selbständig'}],
                    'frequency_units': ['pro Tag', 'pro Woche', 'pro Monat']
                },
                {
                    'id': '5.1.4',
                    'text': 'Absaugen und Sauerstoffgabe',
                    'explanation': '''Absaugen, zum Beispiel bei beatmeten oder tracheotomierten Personen, sowie das An- und Ablegen von Sauerstoffbrillen oder Atemmasken. Auch das Bereitstellen und Reinigen eines Inhalationsgerätes wird hier berücksichtigt.''',
                    'type': 'frequency',
                    'options': [{'text': 'Entfällt'}, {'text': 'Selbständig'}],
                    'frequency_units': ['pro Tag', 'pro Woche', 'pro Monat']
                },
                {
                    'id': '5.1.5',
                    'text': 'Einreibungen oder Kälte- und Wärmeanwendungen',
                    'explanation': '''Anwendungen von ärztlich angeordneten Salben, Cremes oder Emulsionen sowie Kälte- und Wärmeanwendungen, zum Beispiel bei rheumatischen Erkrankungen. Die allgemeine Hautpflege ist nicht zu berücksichtigen.''',
                    'type': 'frequency',
                    'options': [{'text': 'Entfällt'}, {'text': 'Selbständig'}],
                    'frequency_units': ['pro Tag', 'pro Woche', 'pro Monat']
                },
                {
                    'id': '5.1.6',
                    'text': 'Messung und Deutung von Körperzuständen',
                    'explanation': '''Ärztlich angeordnete Messungen wie Blutdruck, Puls, Blutzucker, Temperatur oder Gewicht. Es geht auch darum, aus den Messwerten notwendige Schlüsse zu ziehen, etwa zur Anpassung von Medikamenten oder zum Aufsuchen eines Arztes.''',
                    'type': 'frequency',
                    'options': [{'text': 'Entfällt'}, {'text': 'Selbständig'}],
                    'frequency_units': ['pro Tag', 'pro Woche', 'pro Monat']
                },
                {
                    'id': '5.1.7',
                    'text': 'Körpernahe Hilfsmittel',
                    'explanation': '''An- oder Ablegen von Prothesen, Orthesen, Epithesen, Sehhilfen, Hörgeräten, kieferorthopädischen Apparaturen sowie Kompressionsstrümpfen für Arme und Beine inklusive deren Reinigung. Das alleinige Reinigen ohne An- oder Ablegen wird nicht bewertet.''',
                    'type': 'frequency',
                    'options': [{'text': 'Entfällt'}, {'text': 'Selbständig'}],
                    'frequency_units': ['pro Tag', 'pro Woche', 'pro Monat']
                }
            ]
        },
        {
            'part_id': '5.2',
            'name': 'Teil 2: Verbandswechsel, Stomaversorgung, Katheterisierung, Therapiemaßnahmen',
            'questions': [
                {
                    'id': '5.2.1',
                    'text': 'Verbandswechsel und Wundversorgung',
                    'explanation': '''Versorgung chronischer Wunden wie Ulcus cruris oder Dekubitus. Auch intermittierendes Wundgeschehen, das regelmäßig und dauerhaft versorgt werden muss, zählt dazu.''',
                    'type': 'frequency',
                    'options': [{'text': 'Entfällt'}, {'text': 'Selbständig'}],
                    'frequency_units': ['pro Tag', 'pro Woche', 'pro Monat']
                },
                {
                    'id': '5.2.2',
                    'text': 'Versorgung mit Stoma',
                    'explanation': '''Pflege künstlicher Körperöffnungen wie Tracheostoma, PEG, suprapubischer Katheter, Urostoma oder Colo-/Ileostoma. Dazu gehören Reinigung, Desinfektion der Einstichstelle und gegebenenfalls Verbandswechsel.''',
                    'type': 'frequency',
                    'options': [{'text': 'Entfällt'}, {'text': 'Selbständig'}],
                    'frequency_units': ['pro Tag', 'pro Woche', 'pro Monat']
                },
                {
                    'id': '5.2.3',
                    'text': 'Regelmäßige Einmalkatheterisierung und Nutzung von Abführmethoden',
                    'explanation': '''Einmalkatheterisierungen, vor allem bei neurogenen Blasenentleerungsstörungen, sowie Abführmethoden wie Klistier, Einlauf oder digitale Ausräumung. Die alleinige Gabe von Laxantien wird unter F 4.5.1 erfasst.''',
                    'type': 'frequency',
                    'options': [{'text': 'Entfällt'}, {'text': 'Selbständig'}],
                    'frequency_units': ['pro Tag', 'pro Woche', 'pro Monat']
                },
                {
                    'id': '5.2.4',
                    'text': 'Therapiemaßnahmen in häuslicher Umgebung',
                    'explanation': '''Dauerhafte Eigenübungen aus Heilmitteltherapien wie Krankengymnastik, Atem- oder Sprachübungen sowie aufwendige therapeutische Maßnahmen zur Sekretelimination oder ambulante Peritonealdialyse.''',
                    'type': 'frequency',
                    'options': [{'text': 'Entfällt'}, {'text': 'Selbständig'}],
                    'frequency_units': ['pro Tag', 'pro Woche', 'pro Monat']
                }
            ]
        },
        {
            'part_id': '5.3',
            'name': 'Teil 3: Zeit- und technikintensive Maßnahmen',
            'questions': [
                {
                    'id': '5.3.1',
                    'text': 'Zeit- und technikintensive Maßnahmen in häuslicher Umgebung',
                    'explanation': '''Therapiemaßnahmen wie Hämodialyse oder Beatmung, die sowohl zeit- als auch technikintensiv sind und eine ständige Überwachung durch geschulte Pflegepersonen erfordern.''',
                    'type': 'frequency',
                    'options': [{'text': 'Entfällt'}, {'text': 'Selbständig'}],
                    'frequency_units': ['pro Tag', 'pro Woche', 'pro Monat']
                }
            ]
        },
        {
            'part_id': '5.4',
            'name': 'Teil 4: Arztbesuche und andere Termine',
            'questions': [
                {
                    'id': '5.4.1',
                    'text': 'Arztbesuche',
                    'explanation': '''Regelmäßige Besuche bei Haus- oder Fachärzten zu diagnostischen oder therapeutischen Zwecken. Unterstützung auf dem Weg oder während des Besuchs wird in durchschnittlicher Häufigkeit erfasst.''',
                    'type': 'frequency',
                    'options': [{'text': 'Entfällt'}, {'text': 'Selbständig'}],
                    'frequency_units': ['pro Woche', 'pro Monat']
                },
                {
                    'id': '5.4.2',
                    'text': 'Besuch anderer medizinischer oder therapeutischer Einrichtungen (bis zu drei Stunden)',
                    'explanation': '''Aufsuchen von Therapeuten oder anderen Einrichtungen des Gesundheitswesens zur Behandlung oder Diagnostik, sofern der Gesamtzeitaufwand einschließlich Fahrtzeiten bis zu drei Stunden beträgt.''',
                    'type': 'frequency',
                    'options': [{'text': 'Entfällt'}, {'text': 'Selbständig'}],
                    'frequency_units': ['pro Woche', 'pro Monat']
                },
                {
                    'id': '5.4.3',
                    'text': 'Zeitlich ausgedehnte Besuche anderer medizinischer oder therapeutischer Einrichtungen (länger als drei Stunden)',
                    'explanation': '''Besuche von spezialisierten Einrichtungen oder aufwendige diagnostische beziehungsweise therapeutische Maßnahmen, bei denen der Zeitaufwand für die Pflegeperson pro Termin mehr als drei Stunden beträgt.''',
                    'type': 'frequency',
                    'options': [{'text': 'Entfällt'}, {'text': 'Selbständig'}],
                    'frequency_units': ['pro Woche', 'pro Monat']
                }
            ]
        },
        {
            'part_id': '5.5',
            'name': 'Teil 5: Diät und Verhaltensvorschriften',
            'questions': [
                {
                    'id': '5.5.1',
                    'text': 'Einhaltung einer Diät und anderer krankheits- oder therapiebedingter Verhaltensvorschriften',
                    'explanation': '''Einhalten einer Diät und anderer krankheits- oder therapiebedingter
Verhaltensvorschriften Fähigkeit, die Notwendigkeit einer Diät oder einer ärztlich angeordneten Vorschrift,
die sich auf vitale Funktionen bezieht, einzusehen
In diesem Kriterium geht es um die Einsichtsfähigkeit der Person zur Einhaltung
von ärztlich angeordneten Diäten sowie Vorschriften, die sich auf vitale Funktionen
(insbesondere Atmung und Herzkreislauffunktion) beziehen.

Es geht nicht um die Vorbereitung oder Durchführung einer Verhaltensvorschrift
oder Diät. Ausschlaggebend für eine Wertung ist, ob die Person mental in der
Lage ist, die Notwendigkeit zu erkennen und die Verhaltensvorschrift einzuhalten.
Zu werten ist, wie häufig aufgrund des Nichtbeachtens ein direktes Eingreifen
erforderlich ist, sofern dies nicht in anderen Modulen berücksichtigt wurde.

Bei manchen Erkrankungen werden bestimmte Diäten oder Essvorschriften
oder andere Verhaltensvorschriften von der Ärztin oder vom Arzt angeordnet.
Dazu gehören auch die ärztlich angeordnete Nahrungs- und Flüssigkeitszufuhr,
in der sowohl die Art und Menge der Lebensmittel wie auch die Art und der
Zeitpunkt der Aufnahme aus therapeutischen Gründen geregelt sind, zum Beispiel
bei Stoffwechselstörungen, Nahrungsmittelallergien, bei Essstörungen wie

Anorexie oder Prader-Willi-Syndrom. Verhaltensvorschriften zur gesunden
Lebensführung im Sinne von zum Beispiel einer ausgewogenen Ernährung und
einer ausreichenden Flüssigkeitsmenge sowie die Vermeidung von Suchtmitteln
sind hier nicht zu berücksichtigen. Andere Verhaltensvorschriften können sich
zum Beispiel auf die Sicherstellung einer Langzeit-Sauerstoff-Therapie bei unruhigen
Personen beziehen.
Diese Vorschriften sind im Einzelnen zu benennen. Im Weiteren sind der Grad
der Selbständigkeit bei der Einhaltung dieser Vorschriften und der daraus resultierende
Bedarf an personeller Unterstützung zu beurteilen. Nicht gemeint ist
die selbstbestimmte Ablehnung von ärztlichen Vorschriften bei erhaltenen mentalen
Funktionen.
Liegen keine Vorschriften vor, ist das Feld „entfällt, nicht erforderlich“ anzukreuzen.''',
                    'type': 'standard',
                    'options': [
                        {
                            'text': 'Selbständig',
                            'score': 0,
                            'option_explanation': 'Die Person kann die Vorschriften selbständig einhalten. Das Bereitstellen einer Diät reicht aus.'
                        },
                        {
                            'text': 'Überwiegend selbständig',
                            'score': 1,
                            'option_explanation': '''Die Person benötigt Erinnerung, Anleitung. In der Regel reicht das Bereitstellen
der Diät nicht aus. Darüberhinausgehendes Eingreifen ist maximal einmal täglich
erforderlich.'''
                        },
                        {
                            'text': 'Überwiegend unselbständig',
                            'score': 2,
                            'option_explanation': '''Die Person benötigt meistens Anleitung, Beaufsichtigung. Das Bereitstellen der
Diät reicht nicht aus. Darüberhinausgehendes Eingreifen ist mehrmals täglich
erforderlich.'''
                        },
                        {
                            'text': 'Unselbständig',
                            'score': 3,
                            'option_explanation': '''Die Person benötigt immer Anleitung, Beaufsichtigung. Das Bereitstellen der
Diät reicht nicht aus. Darüberhinausgehendes Eingreifen ist (fast) durchgehend
erforderlich.'''
                        }
                    ]
                }
            ]
        }
    ]
}

