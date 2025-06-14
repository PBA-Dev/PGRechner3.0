# modules/module4.py

module4 = {
    'id': 4,
    'name': 'Modul 4: Selbstversorgung',
    'weight': 40, # Weight in percent for final score calculation
    'questions': [
        {
            "id": "4.1",
            "text": "Waschen des vorderen Oberkörpers",
            "explanation": "Sich die Hände, das Gesicht, die Arme, die Achselhöhlen sowie den vorderen Hals- und Brustbereich waschen und abtrocknen.",
            "options": [
                {"text": "Selbständig", "score": 0, "option_explanation": "Die Person kann die beschriebene Aktivität ohne personelle Hilfe durchführen."},
                {"text": "Überwiegend selbständig", "score": 1, "option_explanation": "Die Person kann die Aktivität selbständig durchführen, wenn benötigte Gegenstände, zum Beispiel Seife, Waschlappen, bereitgelegt werden oder sie Aufforderung beziehungsweise punktuelle Teilhilfen, zum Beispiel Waschen unter den Achseln oder der Brust, erhält."},
                {"text": "Überwiegend unselbständig", "score": 2, "option_explanation": "Die Person kann geringe Anteile der Aktivität selbständig durchführen, sich zum Beispiel nur Hände oder Gesicht waschen, oder benötigt umfassende Anleitung."},
                {"text": "Unselbständig", "score": 3, "option_explanation": "Die Person kann sich an der Aktivität nicht oder nur minimal beteiligen."}
            ]
        },
        {
            "id": "4.2",
            "text": "Körperpflege im Bereich des Kopfes",
            "explanation": "Kämmen, Zahnpflege, Prothesenreinigung, Rasieren.",
            "options": [
                {"text": "Selbständig", "score": 0, "option_explanation": "Die Person kann die beschriebenen Aktivitäten ohne personell Hilfe durchführen."},
                {"text": "Überwiegend selbständig", "score": 1, "option_explanation": "Die Person kann die Aktivitäten selbständig durchführen, wenn benötigte Gegenstände bereitgelegt oder gerichtet werden, zum Beispiel Aufdrehen der Zahnpastatube, Auftragen der Zahnpasta auf die Bürste, Aufbringen von Haftcreme auf die Prothese, Anreichen oder Säubern des Rasierapparates. Alternativ sind Aufforderungen oder punktuelle Teilhilfen erforderlich wie Korrekturen nach dem Kämmen oder nur das Kämmen des Hinterkopfes, das Reinigen der hinteren Backenzähne bei der Zahn-, Mundpflege beziehungsweise die Nachrasur bei sonst selbständigem Rasieren."},
                {"text": "Überwiegend unselbständig", "score": 2, "option_explanation": "Die Person kann geringe Anteile der Aktivität selbständig leisten, so beginnt sie zum Beispiel mit dem Zähneputzen oder der Rasur, ohne die Aktivität zu Ende zu führen."},
                {"text": "Unselbständig", "score": 3, "option_explanation": "Die Person kann sich an den Aktivitäten nicht oder nur minimal beteiligen."}
            ]
        },
        {
            "id": "4.3",
            "text": "Waschen des Intimbereichs",
            "explanation": "Den Intimbereich waschen und abtrocknen.",
            "options": [
                {"text": "Selbständig", "score": 0, "option_explanation": "Die Person kann die beschriebene Aktivität ohne personelle Hilfe durchführen."},
                {"text": "Überwiegend selbständig", "score": 1, "option_explanation": "Die Person kann die Aktivität selbständig durchführen, wenn benötigte Utensilien, zum Beispiel Seife, Waschlappen bereitgelegt werden oder sie Aufforderung beziehungsweise punktuelle Teilhilfen erhält."},
                {"text": "Überwiegend unselbständig", "score": 2, "option_explanation": "Die Person kann geringe Anteile der Aktivität selbständig durchführen, sich zum Beispiel nur den vorderen Intimbereich waschen."},
                {"text": "Unselbständig", "score": 3, "option_explanation": "Die Person kann sich an der Aktivität nicht oder nur minimal beteiligen."}
            ]
        },
        {
            "id": "4.4",
            "text": "Duschen und Baden einschließlich Waschen der Haare",
            "explanation": "Durchführung des Dusch- und Wannenbades einschließlich des Waschens der Haare. Dabei sind neben der Fähigkeit, den Körper waschen zu können, auch Sicherheitsaspekte zu berücksichtigen. (Teil-)Hilfen beim Waschen in der Dusche und Wanne sind hier ebenso zu berücksichtigen wie die Hilfe beim Ein- und Aussteigen oder eine notwendige Überwachung während des Duschens und Badens. Dazu gehört auch das Abtrocknen, Haare waschen und föhnen.",
            "options": [
                {"text": "Selbständig", "score": 0, "option_explanation": "Die Person kann die beschriebene Aktivität ohne personelle Hilfe durchführen."},
                {"text": "Überwiegend selbständig", "score": 1, "option_explanation": "Die Person kann die Aktivität selbständig durchführen, wenn Utensilien vorbereitet beziehungsweise bereitgestellt werden, einzelne Handreichungen geleistet werden, zum Beispiel Stützen beim Ein-, Aussteigen, Bedienung eines Badewannenlifters, Hilfe beim Haarewaschen oder Föhnen, beim Abtrocknen, oder wenn während des Duschens und Badens aus nachvollziehbaren Sicherheitsgründen Anwesenheit erforderlich ist."},
                {"text": "Überwiegend unselbständig", "score": 2, "option_explanation": "Die Person kann geringe Anteile der Aktivität selbständig durchführen, zum Beispiel das Waschen des vorderen Oberkörpers."},
                {"text": "Unselbständig", "score": 3, "option_explanation": "Die Person kann sich an der Aktivität nicht oder nur minimal beteiligen."}
            ]
        },
        {
            "id": "4.5",
            "text": "An- und Auskleiden des Oberkörpers",
            "explanation": "Bereitliegende Kleidungsstücke, zum Beispiel Unterhemd, T-Shirt, Hemd, Bluse, Pullover, Jacke, BH, Schlafanzugoberteil oder Nachthemd, an- und ausziehen. Die Beurteilung ist unabhängig davon vorzunehmen, ob solche Kleidungsstücke derzeit getragen werden. Die situationsgerechte Auswahl der Kleidung ist nicht hier, sondern unter Punkt F 4.2.6 zu berücksichtigen. Das An- und Ablegen von körpernahen Hilfsmitteln ist unter Punkt F 4.5.7 zu berücksichtigen.",
            "options": [
                {"text": "Selbständig", "score": 0, "option_explanation": "Die Person kann die beschriebene Aktivität ohne personelle Hilfe durchführen."},
                {"text": "Überwiegend selbständig", "score": 1, "option_explanation": "Die Person kann die Aktivität beispielsweise selbständig durchführen, wenn Kleidungsstücke passend angereicht oder gehalten werden beim Anziehen eines Hemdes et cetera. Auch wenn Hilfe nur bei Verschlüssen erforderlich ist, trifft die Bewertung „überwiegend selbständig“ zu, ebenso wenn nur Kontrolle des Sitzes der Kleidung und Aufforderungen zur Vervollständigung der Handlung erforderlich sind."},
                {"text": "Überwiegend unselbständig", "score": 2, "option_explanation": "Die Person kann beispielsweise nur die Hände in die Ärmel eines bereitgehaltenen T-Shirts schieben."},
                {"text": "Unselbständig", "score": 3, "option_explanation": "Die Person kann sich an der Aktivität nicht oder nur minimal beteiligen."}
            ]
        },
        {
            "id": "4.6",
            "text": "An- und Auskleiden des Unterkörpers",
            "explanation": "Bereitliegende Kleidungsstücke, zum Beispiel Unterwäsche, Hose, Rock, Strümpfe und Schuhe, an- und ausziehen. Die Beurteilung ist unabhängig davon vorzunehmen, ob solche Kleidungsstücke derzeit getragen werden. Die situationsgerechte Auswahl der Kleidung ist unter Punkt F 4.2.6 zu berücksichtigen. Das An- und Ablegen von körpernahen Hilfsmitteln ist unter Punkt F 4.5.7 zu berücksichtigen, zum Beispiel Kompressionsstrümpfe.",
            "options": [
                {"text": "Selbständig", "score": 0, "option_explanation": "Die Person kann die beschriebene Aktivität ohne personelle Hilfe durchführen."},
                {"text": "Überwiegend selbständig", "score": 1, "option_explanation": "Die Person kann die Aktivität selbständig durchführen, wenn ihr Schuhe beziehungsweise Kleidungsstücke angereicht oder gehalten werden (Einstiegshilfe). Auch wenn Hilfe nur bei Verschlüssen, zum Beispiel Schnürsenkel binden, Knöpfe schließen oder Kontrolle des Sitzes der Kleidung, und Aufforderungen, die Handlung zu beginnen oder zur Vervollständigung der Handlung erforderlich sind, trifft die Bewertung „überwiegend selbständig“ zu."},
                {"text": "Überwiegend unselbständig", "score": 2, "option_explanation": "Die Person kann die Aktivität zu einem geringen Anteil selbständig durchführen. Beispielsweise gelingt nur das Hochziehen von Hose oder Rock vom Oberschenkel zur Taille selbständig."},
                {"text": "Unselbständig", "score": 3, "option_explanation": "Die Person kann sich an der Aktivität nicht oder nur minimal beteiligen."}
            ]
        },
        {
            "id": "4.7",
            "text": "Mundgerechtes Zubereiten der Nahrung und Eingießen von Getränken",
            "explanation": "Zerteilen von Nahrung in mundgerechte Stücke und Eingießen von Getränken. Dazu gehört das Zerteilen von belegten Brotscheiben, Obst oder anderen Speisen in mundgerechte Stücke, zum Beispiel das Kleinschneiden von Fleisch, das Zerdrücken von Kartoffeln, Verschlüsse von Getränkeflaschen öffnen, Getränke aus einer Flasche oder Kanne in ein Glas beziehungsweise eine Tasse eingießen, gegebenenfalls unter Nutzung von Hilfsmitteln wie Antirutschbrett oder sonstigen Gegenständen wie Spezialbesteck.",
            "options": [
                {"text": "Selbständig", "score": 0, "option_explanation": "Die Person kann die beschriebene Aktivität ohne personelle Hilfe durchführen."},
                {"text": "Überwiegend selbständig", "score": 1, "option_explanation": "Es ist punktuelle Hilfe erforderlich, zum Beispiel beim Öffnen einer Flasche oder beim Schneiden von harten Nahrungsmitteln."},
                {"text": "Überwiegend unselbständig", "score": 2, "option_explanation": "Die Person kann die Aktivität zu einem geringen Teil selbständig durchführen, beispielsweise schneidet sie zwar belegte Brotscheiben, schafft es aber nicht, mundgerechte Stücke herzustellen. Die Person kann Getränke nicht eingießen."},
                {"text": "Unselbständig", "score": 3, "option_explanation": "Die Person kann sich an der Aktivität nicht oder nur minimal beteiligen."}
            ]
        },
        {
            "id": "4.8",
            "text": "Essen",
            "explanation": "Bereitgestellte, mundgerecht zubereitete Speisen essen. Dies beinhaltet das Aufnehmen, Zum-Mund-Führen, gegebenenfalls Abbeißen, Kauen und Schlucken von mundgerecht zubereiteten Speisen, die üblicherweise mit den Fingern gegessen werden, zum Beispiel Brot, Kekse, Obst oder das Essen mit Gabel oder Löffel, gegebenenfalls mit speziellen Hilfsmitteln wie adaptiertem Besteck. Zu berücksichtigen ist auch, inwieweit die Notwendigkeit der ausreichenden Nahrungsaufnahme (auch ohne Hungergefühl oder Appetit) erkannt und die empfohlene, gewohnte Menge tatsächlich gegessen wird. Das Einhalten von Diäten ist nicht hier, sondern unter Punkt F 4.5.16 zu bewerten. Die Beurteilung ist auch dann vorzunehmen, wenn die Nahrungsaufnahme über eine Sonde beziehungsweise parenteral erfolgt.",
            "options": [
                {"text": "Selbständig", "score": 0, "option_explanation": "Die Person kann die beschriebene Aktivität ohne personelle Hilfe durchführen."},
                {"text": "Überwiegend selbständig", "score": 3, "option_explanation": "Die Person kann überwiegend selbständig essen, benötigt aber punktuelle Anleitung, muss beispielsweise aufgefordert werden, mit dem Essen zu beginnen oder weiterzuessen. Es sind punktuelle Hilfen erforderlich, zum Beispiel Zurücklegen aus der Hand gerutschter Speisen oder Besteck in die Hand geben."},
                {"text": "Überwiegend unselbständig", "score": 6, "option_explanation": "Es muss aufwendig zur Nahrungsaufnahme motiviert werden oder die Nahrung muss größtenteils gereicht werden oder es ist ständige und unmittelbare Eingreifbereitschaft der Pflegeperson erforderlich, aufgrund von Aspirationsgefahr."},
                {"text": "Unselbständig", "score": 9, "option_explanation": "Die Nahrung muss (nahezu) komplett gereicht werden. Als unselbständig zu bewerten sind auch Personen, die nicht schlucken können."}
            ]
        },
        {
            "id": "4.9",
            "text": "Trinken",
            "explanation": "Bereitstehende Getränke aufnehmen, gegebenenfalls mit Gegenständen wie Strohhalm, Spezialbecher mit Trinkaufsatz. Zu berücksichtigen ist auch, inwieweit die Notwendigkeit der Flüssigkeitsaufnahme (auch ohne ausreichendes Durstgefühl) erkannt und die empfohlene oder gewohnte Menge tatsächlich getrunken wird. Die Beurteilung der Selbständigkeit ist auch dann vorzunehmen, wenn die Flüssigkeitsaufnahme über eine Sonde beziehungsweise parenteral erfolgt.",
            "options": [
                {"text": "Selbständig", "score": 0, "option_explanation": "Die Person kann die beschriebene Aktivität ohne personelle Hilfe durchführen."},
                {"text": "Überwiegend selbständig", "score": 2, "option_explanation": "Die Person kann selbständig trinken, wenn über das Bereitstellen hinaus ein Glas, eine Tasse unmittelbar in den Aktionsradius der Person positioniert oder sie ans Trinken erinnert wird."},
                {"text": "Überwiegend unselbständig", "score": 4, "option_explanation": "Das Trinkgefäß muss beispielsweise in die Hand gegeben werden, das Trinken erfolgt jedoch selbständig, oder die Person muss zu fast jedem Schluck motiviert werden oder es ist ständige und unmittelbare Eingreifbereitschaft der Pflegeperson erforderlich, aufgrund von Aspirationsgefahr."},
                {"text": "Unselbständig", "score": 6, "option_explanation": "Getränke müssen (nahezu) komplett gereicht werden. Als unselbständig zu bewerten sind auch Personen, die nicht schlucken können."}
            ]
        },
        {
            "id": "4.10",
            "text": "Benutzen einer Toilette oder eines Toilettenstuhls",
            "explanation": "Gehen zur Toilette, Hinsetzen und Aufstehen, Sitzen während der Blasen- oder Darmentleerung, Intimhygiene und Richten der Kleidung. Die Beurteilung ist auch dann vorzunehmen, wenn anstelle der Toilettenbenutzung eine Versorgung mit Hilfsmitteln erfolgt, zum Beispiel Inkontinenzmaterial, Katheter, Urostoma, Ileo- oder Colostoma.",
            "options": [
                {"text": "Selbständig", "score": 0, "option_explanation": "Die Person kann die Aktivität ohne personelle Hilfe durchführen."},
                {"text": "Überwiegend selbständig", "score": 2, "option_explanation": "Die Person kann den größten Anteil der Aktivität selbständig durchführen. Personelle Hilfe kann sich beispielsweise beschränken auf einzelne Handlungsschritte wie: nur Bereitstellen und Leeren des Toilettenstuhls (alternativ Urinflasche oder anderer Behälter), nur Aufforderung oder Orientierungshinweise zum Auffinden der Toilette oder Begleitung auf dem Weg zur Toilette, nur Anreichen von Toilettenpapier oder Waschlappen, Intimhygiene nur nach Stuhlgang, nur Unterstützung beim Hinsetzen, Aufstehen von der Toilette, nur punktuelle Hilfe beim Richten der Bekleidung."},
                {"text": "Überwiegend unselbständig", "score": 4, "option_explanation": "Die Person kann nur einen geringen Anteil der Aktivität selbständig durchführen, zum Beispiel nur Richten der Bekleidung oder Intimhygiene nur nach Wasserlassen."},
                {"text": "Unselbständig", "score": 6, "option_explanation": "Die Person kann sich nicht oder nur minimal an der Aktivität beteiligen."}
            ]
        },
        {
            "id": "4.11",
            "text": "Bewältigen der Folgen einer Harninkontinenz und Umgang mit Dauerkatheter und Urostoma",
            "explanation": "Inkontinenz- und Stomasysteme sachgerecht verwenden, nach Bedarf wechseln und entsorgen. Dazu gehört, Inkontinenzsysteme, zum Beispiel Inkontinenzvorlagen, Inkontinenzhose mit Klebestreifen oder Pants, sachgerecht verwenden, nach Bedarf wechseln und entsorgen. Dazu gehört auch das Entleeren, Wechseln eines Urinbeutels bei Dauerkatheter, Urostoma oder die Anwendung eines Urinalkondoms. Die regelmäßige Einmalkatheterisierung ist nicht hier, sondern unter Punkt F 4.5.10 zu erfassen.",
            "options": [
                {"text": "Selbständig", "score": 0, "option_explanation": "Die Person kann Hilfsmittel selbständig benutzen."},
                {"text": "Überwiegend selbständig", "score": 1, "option_explanation": "Die Person kann die Aktivität überwiegend selbständig durchführen, wenn Inkontinenzsysteme angereicht oder entsorgt werden oder die Person an den Wechsel erinnert wird."},
                {"text": "Überwiegend unselbständig", "score": 2, "option_explanation": "Die Person kann sich am Wechsel der Inkontinenzsysteme beteiligen, zum Beispiel nur Vorlagen einlegen oder Inkontinenzhosen nur entfernen."},
                {"text": "Unselbständig", "score": 3, "option_explanation": "Beteiligung ist nicht oder nur minimal möglich."}
            ]
        },
        {
            "id": "4.12",
            "text": "Bewältigen der Folgen einer Stuhlinkontinenz und Umgang mit Stoma",
            "explanation": "Inkontinenz- und Stomasysteme sachgerecht verwenden, nach Bedarf wechseln und entsorgen. Dazu gehört, Inkontinenzsysteme, zum Beispiel große Vorlagen mit Netzhose, Inkontinenzhose mit Klebestreifen oder Pants, sachgerecht verwenden, nach Bedarf wechseln und entsorgen. Dazu gehört auch die Anwendung eines Analtampons oder das Entleeren oder Wechseln eines Stomabeutels bei Enterostoma. Die Pflege des Stomas und der Wechsel einer Basisplatte sind unter F 4.5.9 zu berücksichtigen.",
            "options": [
                {"text": "Selbständig", "score": 0, "option_explanation": "Die Person kann Hilfsmittel selbständig benutzen."},
                {"text": "Überwiegend selbständig", "score": 1, "option_explanation": "Die Person kann die Aktivität überwiegend selbständig durchführen, wenn Inkontinenzsysteme bereitgelegt und entsorgt werden oder die Person an den Wechsel erinnert wird."},
                {"text": "Überwiegend unselbständig", "score": 2, "option_explanation": "Die Person kann sich am Wechsel der Inkontinenzsysteme beteiligen, zum Beispiel Mithilfe beim Wechsel eines Stomabeutels. Bei Vorliegen einer Stuhlinkontinenz sind Ressourcen beim Wechsel des Inkontinenzmaterials eher selten."},
                {"text": "Unselbständig", "score": 3, "option_explanation": "Beteiligung ist nicht oder nur minimal möglich."}
            ]
        },
        {
            "id": "4.13",
            "text": "Ernährung parenteral oder über Sonde",
            "explanation": "Ernährung über einen parenteralen Zugang (zum Beispiel einen Port) oder über einen Zugang in Magen oder Dünndarm (PEG/PEJ).",
            "options": [
                {"text": "Selbständig", "score": 0, "option_explanation": "Die Person führt die Versorgung ohne Fremdhilfe durch."},
                {"text": "Nicht täglich, nicht auf Dauer", "score": 1, "option_explanation": "Die Person erhält zusätzlich zur oralen Nahrungsaufnahme Nahrung oder Flüssigkeit parenteral oder über Sonde, aber nur gelegentlich oder vorübergehend."},
                {"text": "Täglich, zusätzlich zu oraler Ernährung", "score": 2, "option_explanation": "Die Person erhält in der Regel täglich Nahrung oder Flüssigkeit parenteral oder über Sonde und täglich oral Nahrung. Sie wird zum Teil, aber nicht ausreichend über die orale Nahrungsaufnahme ernährt und benötigt zur Nahrungsergänzung beziehungsweise zur Vermeidung von Mangelernährung täglich Sondenkost oder Flüssigkeit."},
                {"text": "Ausschließlich oder nahezu ausschließlich", "score": 3, "option_explanation": "Die Person erhält ausschließlich oder nahezu ausschließlich Nahrung und Flüssigkeit parenteral oder über Sonde. Eine orale Gabe erfolgt nicht oder nur in geringem Maße zur Förderung der Sinneswahrnehmung."}
            ]
        }
    ]
}
