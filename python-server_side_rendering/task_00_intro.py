def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Erreur : le template doit être une chaîne de caractères.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Erreur : attendees doit être une liste de dictionnaires.")
        return

    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):
        content = template
        for key in ['name', 'event_title', 'event_date', 'event_location']:
            value = attendee.get(key)
            if not value:
                value = "N/A"
            content = content.replace(f"{{{key}}}", str(value))

        with open(f"output_{index}.txt", "w") as f:
            f.write(content)
