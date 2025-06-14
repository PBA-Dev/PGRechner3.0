"""
Module 2: Kognitive und kommunikative Fähigkeiten
Weight: 15% (Note: Actual NBA weighting combines M2 & M3, then takes the higher score. We'll adjust calculation later if needed)
"""

module2 = {
    'id': 2,
    "name": "Modul 2: Kognitive und kommunikative Fähigkeiten",
    "weight": 0.15, # Placeholder weight, actual calculation might differ based on NBA rules
    "questions": [
        {
            "text": "2.1 Erkennen von Personen aus dem näheren Umfeld",
            "explanation": '''Fähigkeit, Personen aus dem näheren Umfeld wiederzuerkennen, das heißt Menschen,
zu denen im Alltag regelmäßig ein direkter Kontakt besteht
Dazu gehören zum Beispiel Familienmitglieder, Nachbarn, aber auch Pflegekräfte
eines ambulanten Dienstes oder einer stationären Pflegeeinrichtung.''',
            "options": [
                {"score": 0, "text": "Fähigkeit vorhanden", "option_explanation": '''Die Person erkennt andere Personen aus ihrem näheren Umfeld unmittelbar.'''},
                {"score": 1, "text": "Fähigkeit größtenteils vorhanden", "option_explanation": '''Die Person erkennt bekannte Personen beispielsweise erst nach einer längeren
Zeit des Kontaktes in einem Gespräch oder sie hat Schwierigkeiten, wenn auch
nicht täglich, aber doch in regelmäßigen Abständen, vertraute Personen zu
erkennen.'''},
                {"score": 2, "text": "Fähigkeit in geringem Maße vorhanden", "option_explanation": '''Die aus dem näheren Umfeld stammenden Personen werden nur selten erkannt
oder die Fähigkeit hängt gegebenenfalls von der Tagesform ab, das heißt die
Fähigkeit unterliegt im Zeitverlauf erheblichen Schwankungen.'''},
                {"score": 3, "text": "Fähigkeit nicht vorhanden", "option_explanation": '''Auch Familienmitglieder werden nicht oder nur ausnahmsweise erkannt.'''}
            ]
        },
        {
            "text": "2.2 Örtliche Orientierung",
            "explanation": '''Fähigkeit, sich in der räumlichen Umgebung zurechtzufinden, andere Orte
gezielt anzusteuern und zu wissen, wo man sich befindet''',
            "options": [
                {"score": 0, "text": "Fähigkeit vorhanden", "option_explanation": '''Die Person weiß, in welcher Stadt, auf welchem Stockwerk und gegebenenfalls
in welcher Einrichtung sie sich befindet. Sie kennt sich in den regelmäßig genutzten
Räumlichkeiten aus.'''},
                {"score": 1, "text": "Fähigkeit größtenteils vorhanden", "option_explanation": '''Es bestehen Schwierigkeiten, sich in der außerhäuslichen Umgebung zu orientieren,
beispielsweise nach Verlassen des Hauses wieder den Weg zurückzufinden.
In den eigenen Wohnräumen existieren solche Schwierigkeiten hingegen nicht.'''},
                {"score": 2, "text": "Fähigkeit in geringem Maße vorhanden", "option_explanation": '''Die Person hat auch in einer gewohnten Wohnumgebung Schwierigkeiten, sich
zurechtzufinden. Regelmäßig genutzte Räumlichkeiten und Wege in der Wohnumgebung
werden nicht immer erkannt.'''},
                {"score": 3, "text": "Fähigkeit nicht vorhanden", "option_explanation": '''Selbst in der eigenen Wohnumgebung ist die Person regelmäßig auf Unterstützung
angewiesen, um sich zurechtzufinden.'''}
            ]
        },
        {
            "text": "2.3 Zeitliche Orientierung",
            "explanation": '''Fähigkeit, zeitliche Strukturen zu erkennen
Dazu gehören Uhrzeit, Tagesabschnitte (Vormittag, Nachmittag, Abend et cetera),
Jahreszeiten und die zeitliche Abfolge des eigenen Lebens. Aufschluss über die
Fähigkeit zur zeitlichen Orientierung geben Antworten auf die Frage nach der
Jahreszeit, dem Jahr, dem Wochentag, dem Monat oder der Tageszeit.''',
            "options": [
                {"score": 0, "text": "Fähigkeit vorhanden", "option_explanation": '''Die zeitliche Orientierung ist ohne nennenswerte Beeinträchtigungen vorhanden.'''},
                {"score": 1, "text": "Fähigkeit größtenteils vorhanden", "option_explanation": '''Die Person ist die meiste Zeit über zeitlich orientiert, aber nicht durchgängig.
Sie hat zum Beispiel Schwierigkeiten, ohne äußere Orientierungshilfen (Uhr,
Dunkelheit et cetera) den Tagesabschnitt zu bestimmen.'''},
                {"score": 2, "text": "Fähigkeit in geringem Maße vorhanden", "option_explanation": '''Die zeitliche Orientierung ist die meiste Zeit nur in Ansätzen vorhanden. Die
Person ist auch unter Nutzung äußerer Orientierungshilfen zumeist nicht in der
Lage, Tageszeiten zu erkennen, zu denen regelmäßig bestimmte Ereignisse stattfinden
(zum Beispiel Mittagessen).'''},
                {"score": 3, "text": "Fähigkeit nicht vorhanden", "option_explanation": '''Das Verständnis für zeitliche Strukturen und Abläufe ist kaum oder nicht vorhanden.'''}
            ]
        },
        {
            "text": "2.4 Erinnerung an wesentliche Ereignisse oder Beobachtungen",
            "explanation": "Fähigkeit, sich an kurz und auch länger zurückliegende Ereignisse oder Beobachtungen zu erinnern. Dazu gehört, dass die Person zum Beispiel weiß, was sie zum Frühstück gegessen hat oder mit welchen Tätigkeiten sie den Vormittag verbracht hat. Im Hinblick auf das Langzeitgedächtnis geht es bei Erwachsenen zum Beispiel um die Kenntnis des Geburtsjahres, des Geburtsorts oder wichtiger Bestandteile des Lebensverlaufs wie Eheschließung und Berufstätigkeit.",
            "options": [
                {"score": 0, "text": "Fähigkeit vorhanden", "option_explanation": "Die Person kann über kurz zurückliegende Ereignisse Auskunft geben oder durch Handlungen und Gesten signalisieren, dass sie sich erinnert."},
                {"score": 1, "text": "Fähigkeit größtenteils vorhanden", "option_explanation": "Die Person hat Schwierigkeiten, sich an manche kurz zurückliegende Ereignisse zu erinnern, oder muss hierzu länger nachdenken, sie hat aber keine nennenswerten Probleme, sich an Ereignisse aus der eigenen Lebensgeschichte zu erinnern."},
                {"score": 2, "text": "Fähigkeit in geringem Maße vorhanden", "option_explanation": "Die Person vergisst kurz zurückliegende Ereignisse häufig. Nicht alle, aber wichtige Ereignisse aus der eigenen Lebensgeschichte sind (noch) präsent."},
                {"score": 3, "text": "Fähigkeit nicht vorhanden", "option_explanation": "Die Person ist nicht (oder nur selten) in der Lage, sich an Ereignisse, Dinge oder Personen aus der eigenen Lebensgeschichte zu erinnern."}
            ]
        },

    {
        "text": "2.5 Steuern von mehrschrittigen Alltagshandlungen",
        "explanation": "Fähigkeit, zielgerichtete Handlungen des Lebensalltags, die eine Abfolge von Teilschritten umfassen, zu steuern. Die Betonung liegt in diesem Fall auf dem Begriff Alltagshandlungen. Gemeint sind zielgerichtete Handlungen, die diese Person täglich oder nahezu täglich im Lebensalltag durchführt oder durchgeführt hat, wie zum Beispiel das komplette Ankleiden, Kaffeekochen oder Tischdecken. ",
        "options": [
            {"score": 0, "text": "Fähigkeit vorhanden", "option_explanation": "Die Person ist in der Lage, die erforderlichen Handlungsschritte selbständig in der richtigen Reihenfolge auszuführen oder zu steuern, so dass das angestrebte Ergebnis der Handlung erreicht wird. "},
            {"score": 1, "text": "Fähigkeit größtenteils vorhanden", "option_explanation": "Die Person verliert manchmal den Faden und vergisst, welcher Handlungsschritt der nächste ist. Erhält sie dabei eine Erinnerungshilfe, kann sie die Handlung aber selbständig fortsetzen. "},
            {"score": 2, "text": "Fähigkeit in geringem Maße vorhanden", "option_explanation": "Die Person hat erhebliche Schwierigkeiten. Sie verwechselt regelmäßig die Reihenfolge der einzelnen Handlungsschritte oder vergisst einzelne, notwendige Handlungsschritte. "},
            {"score": 3, "text": "Fähigkeit nicht vorhanden", "option_explanation": "Mehrschrittige Alltagshandlungen werden erst gar nicht begonnen oder nach den ersten Versuchen aufgegeben. "}
        ]
    },
    {
        "text": "2.6 Treffen von Entscheidungen im Alltag",
        "explanation": "Fähigkeit, folgerichtige und geeignete Entscheidungen im Alltag zu treffen. Dazu gehört zum Beispiel die dem Wetter angepasste Auswahl von Kleidung, die Entscheidung über die Durchführung von Aktivitäten wie Einkaufen, Familienangehörige oder Freunde anrufen, einer Freizeitbeschäftigung nachgehen. Zu klären ist hier die Frage, ob die Entscheidungen folgerichtig sind, das heißt geeignet sind, das angestrebte Ziel zu erreichen oder ein gewisses Maß an Sicherheit und Wohlbefinden oder Bedürfnisbefriedigung zu gewährleisten, zum Beispiel warme Kleidung. ",
        "options": [
            {"score": 0, "text": "Fähigkeit vorhanden", "option_explanation": "Die Person kann auch in unbekannten Situationen folgerichtige Entscheidungen treffen, beispielsweise beim Umgang mit unbekannten Personen, die an der Haustür klingeln. "},
            {"score": 1, "text": "Fähigkeit größtenteils vorhanden", "option_explanation": "Im Rahmen der Alltagsroutinen oder in zuvor besprochenen Situationen können Entscheidungen getroffen werden, die Person hat aber Schwierigkeiten in unbekannten Situationen. "},
            {"score": 2, "text": "Fähigkeit in geringem Maße vorhanden", "option_explanation": "Die Person trifft zwar Entscheidungen, diese Entscheidungen sind jedoch in der Regel nicht geeignet, ein bestimmtes Ziel zu erreichen. Dies ist beispielsweise der Fall, wenn die Person mit nur leichter Bekleidung bei winterlichen Temperaturen im Freien spazieren gehen will. Weiterhin liegt eine schwere Beeinträchtigung vor, wenn die Person nur mit Unterstützung in Form von Anleitung, Aufforderung, Aufzeigen von Handlungsalternativen in der Lage ist, Entscheidungen zu treffen. "},
            {"score": 3, "text": "Fähigkeit nicht vorhanden", "option_explanation": "Die Person kann Entscheidungen auch mit Unterstützung nicht mehr oder nur selten treffen. Sie zeigt keine deutbare Reaktion auf das Angebot mehrerer Entscheidungsalternativen. "}
        ]
    },
    {
        "text": "2.7 Verstehen von Sachverhalten und Informationen",
        "explanation": "Fähigkeit, Sachverhalte zu verstehen und Informationen inhaltlich einordnen zu können. Hier geht es um Ereignisse und Inhalte, die Bestandteil des Alltagslebens der meisten Menschen sind. Gemeint ist etwa die Fähigkeit, zu erkennen, dass man sich in einer bestimmten Situation befindet, zum Beispiel gemeinschaftliche Aktivitäten mit anderen Menschen, Versorgung durch eine Pflegekraft, sowie die Fähigkeit, Informationen zum Tagesgeschehen aus den Medien, zum Beispiel Fernsehgerät, Tageszeitung, aufzunehmen und inhaltlich zu verstehen. Gleiches gilt für mündlich von anderen Personen übermittelte Informationen. ",
        "options": [
            {"score": 0, "text": "Fähigkeit vorhanden", "option_explanation": "Die Person kann Sachverhalte und Informationen aus dem Alltagsleben ohne nennenswerte Probleme verstehen. "},
            {"score": 1, "text": "Fähigkeit größtenteils vorhanden", "option_explanation": "Die Person kann einfache Sachverhalte und Informationen nachvollziehen, hat bei komplizierteren jedoch Schwierigkeiten. "},
            {"score": 2, "text": "Fähigkeit in geringem Maße vorhanden", "option_explanation": "Die Person kann auch einfache Informationen häufig nur nachvollziehen, wenn sie wiederholt erklärt werden. Eine schwere Beeinträchtigung liegt auch dann vor, wenn das Verständnis sehr stark von der Tagesform abhängt. "},
            {"score": 3, "text": "Fähigkeit nicht vorhanden", "option_explanation": "Die Person gibt weder verbal noch nonverbal zu erkennen, dass sie Situationen und übermittelte Informationen verstehen kann. "}
        ]
    },
    {
        "text": "2.8 Erkennen von Risiken und Gefahren",
        "explanation": "Fähigkeit, Risiken und Gefahren zu erkennen. Dazu gehören Gefahren des Alltagslebens wie Strom- und Feuerquellen, Barrieren und Hindernisse auf dem Fußboden beziehungsweise auf Fußwegen, eine problematische Beschaffenheit des Bodens (zum Beispiel Glätte) oder Gefahrenzonen in der außerhäuslichen Umgebung (zum Beispiel verkehrsreiche Straßen, Baustellen). ",
        "options": [
            {"score": 0, "text": "Fähigkeit vorhanden", "option_explanation": "Die Person kann solche Risiken und Gefahrenquellen im Alltagsleben ohne weiteres erkennen, auch wenn sie ihnen aus anderen Gründen (zum Beispiel aufgrund von somatischen Beeinträchtigungen) nicht aus dem Weg gehen kann. "},
            {"score": 1, "text": "Fähigkeit größtenteils vorhanden", "option_explanation": "Die Person erkennt meist nur solche Risiken und Gefahren, die sich in der vertrauten innerhäuslichen Wohnumgebung wiederfinden. Es bestehen aber beispielsweise Schwierigkeiten, Risiken im Straßenverkehr angemessen einzuschätzen oder Gefährdungen in ungewohnter Umgebung zu erkennen. "},
            {"score": 2, "text": "Fähigkeit in geringem Maße vorhanden", "option_explanation": "Die Person kann auch Risiken und Gefahren, denen sie häufig auch in der Wohnumgebung begegnet, oft nicht als solche erkennen. "},
            {"score": 3, "text": "Fähigkeit nicht vorhanden", "option_explanation": "Die Person kann Risiken und Gefahren so gut wie gar nicht erkennen. "}
        ]
    },
    {
        "text": "2.9 Mitteilen von elementaren Bedürfnissen",
        "explanation": "Fähigkeit, elementare Bedürfnisse verbal oder nonverbal mitzuteilen. Das beinhaltet, sich bei stark belastenden Empfindungen in Bezug auf elementare Bedürfnisse wie Schmerzen, Frieren, Hunger oder Durst bemerkbar zu machen. Bei Sprachstörungen kann dies gegebenenfalls durch Laute, Mimik oder Gestik beziehungsweise unter Nutzung von Hilfsmitteln erfolgen. Liegt eine unzureichende Flüssigkeitsaufnahme aufgrund eines nicht ausreichenden Durstgefühls vor, so wird dies im Kriterium F 4.4.9 „Trinken“ bewertet. ",
        "options": [
            {"score": 0, "text": "Fähigkeit vorhanden", "option_explanation": "Die Person kann elementare Bedürfnisse benennen oder durch Laute, Gestik, Mimik oder Nutzung von Hilfsmitteln deutlich machen, um welches Bedürfnis es sich handelt. "},
            {"score": 1, "text": "Fähigkeit größtenteils vorhanden", "option_explanation": "Die Person äußert elementare Bedürfnisse nicht immer von sich aus oder nicht immer eindeutig, kann diese aber auf Nachfrage deutlich machen. "},
            {"score": 2, "text": "Fähigkeit in geringem Maße vorhanden", "option_explanation": "Es ist nur aus nicht eindeutigem Verhalten (zum Beispiel Mimik, Gestik, Lautgebung, sprachliche Äußerungen) ableitbar, dass elementare Bedürfnisse bestehen. Welches elementare Bedürfnis betroffen ist, kann nicht kommuniziert werden, sondern muss von der Pflegeperson aufwendig eruiert werden. Die Person hat häufig Schwierigkeiten, Zustimmung oder Ablehnung zu signalisieren. "},
            {"score": 3, "text": "Fähigkeit nicht vorhanden", "option_explanation": "Die Person äußert nicht oder nur sehr selten Bedürfnisse, auch nicht in nonverbaler Form. Sie kann weder Zustimmung noch Ablehnung deutlich machen. "}
        ]
    },
    {
        "text": "2.10 Verstehen von Aufforderungen",
        "explanation": "Fähigkeit, Aufforderungen in Hinblick auf alltägliche Grundbedürfnisse zu verstehen. Zu den alltäglichen Grundbedürfnissen gehören zum Beispiel Essen, Trinken, sich kleiden, sich beschäftigen. ",
        "options": [
            {"score": 0, "text": "Fähigkeit vorhanden", "option_explanation": "Aufforderungen und Bitten zu alltäglichen Grundbedürfnissen werden ohne weiteres verstanden. "},
            {"score": 1, "text": "Fähigkeit größtenteils vorhanden", "option_explanation": "Einfache Bitten und Aufforderungen, wie zum Beispiel „Setz dich bitte an den Tisch!“, „Zieh dir die Jacke über!“, „Komm zum Essen!“, werden verstanden; Aufforderungen zu komplexeren Handlungen müssen erklärt werden. Gegebenenfalls sind zum Beispiel bei Schwerhörigkeit besonders deutliche Ansprache, Wiederholungen, Zeichensprache, Gebärdensprache oder Schrift erforderlich, um Aufforderungen verständlich zu machen. "},
            {"score": 2, "text": "Fähigkeit in geringem Maße vorhanden", "option_explanation": "Die Person kann Aufforderungen und Bitten meist nicht verstehen, wenn diese nicht wiederholt geäußert und erläutert werden. Das Verständnis ist sehr von der Tagesform abhängig. Sie zeigt aber Zustimmung oder Ablehnung gegenüber nonverbalen Aufforderungen, zum Beispiel bei Berührungen oder Geleiten an den Esstisch. "},
            {"score": 3, "text": "Fähigkeit nicht vorhanden", "option_explanation": "Die Person kann Anleitungen und Aufforderungen kaum oder nicht verstehen. "}
        ]
    },
    {
        "text": "2.11 Beteiligen an einem Gespräch",
        "explanation": "Fähigkeit, in einem Gespräch Gesprächsinhalte aufzunehmen, sinngerecht zu antworten und zur Weiterführung des Gesprächs Inhalte einzubringen. ",
        "options": [
            {"score": 0, "text": "Fähigkeit vorhanden", "option_explanation": "Die Person kommt sowohl in Einzel- als auch in Gesprächen kleiner Gruppen gut zurecht. Sie zeigt im Gespräch Eigeninitiative, Interesse und beteiligt sich, wenn vielleicht auch nur auf direkte Ansprache hin. Ihre Äußerungen passen zu den Inhalten des Gesprächs. "},
            {"score": 1, "text": "Fähigkeit größtenteils vorhanden", "option_explanation": "Die Person kommt in Gesprächen mit einer Person gut zurecht, in Gruppen ist sie jedoch meist überfordert und verliert den Faden oder es treten Wortfindungsstörungen auf. Die Person ist darauf angewiesen, dass langsam und besonders deutlich gesprochen wird und immer wieder Worte und Sätze wiederholt werden, damit sie einem Gespräch folgen kann. Hier ist auch die Kommunikation mit Gebärdensprache zu berücksichtigen. "},
            {"score": 2, "text": "Fähigkeit in geringem Maße vorhanden", "option_explanation": "Die Person kann auch einem Gespräch nur mit einer Person kaum folgen oder sie kann sich nur wenig oder mit einzelnen Worten beteiligen. Die Person zeigt nur wenig Eigeninitiative, reagiert aber auf Ansprache oder Fragen mit wenigen Worten, zum Beispiel mit ja oder nein; die Person beteiligt sich am Gespräch, weicht aber in aller Regel vom Gesprächsinhalt ab (führt mehr ein Selbstgespräch) oder es besteht leichte Ablenkbarkeit durch Umgebungseinflüsse. "},
            {"score": 3, "text": "Fähigkeit nicht vorhanden", "option_explanation": "Ein Gespräch mit der Person, das über einfache Mitteilungen hinausgeht, ist auch unter Einsatz nonverbaler Kommunikation kaum oder nicht möglich. "}
        ]
    }

        # Add more questions as per your document if needed
    ]
}
