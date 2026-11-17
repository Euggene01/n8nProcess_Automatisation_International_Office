# Get all items from the input
items = _items
output = []

for item in items:
    data = item["json"]

    vorname = data.get("Vorname", "")
    name = data.get("Name", "")
    strasse = data.get("Straße", "")
    plz_ort = data.get("PLZ Ort", "")
    zi_nr = data.get("Zi.Nr.", "")
    pers_nr = data.get("Pers.-Nr.", "")
    programm = data.get("Programm", "")

    kaution = str(data.get("Kaution", ""))
    monatsmiete = str(data.get("Monatsmiete", ""))

    # --- ENGLISH VERSION (HTML) ---
    if programm == "Overseas":
        payment_en = "You do not need to transfer any money, as your program is Overseas. All costs are covered by our partners."
    else:
        payment_en = f"""Please transfer the amount of <b>{kaution} € deposit</b> + <b>{monatsmiete} € monthly rent</b> to the following account:
        <br><br>
        <b>Account Holder:</b> International Office, University of Marburg<br>
        <b>Bank Name:</b> Sparkasse Marburg-Biedenkopf<br>
        <b>IBAN:</b> DE12 3456 7890 1234 5678 90<br>
        <b>BIC:</b> HELADEF1MAR<br><br>
        <b>Reference:</b> {pers_nr}"""

    body_en = f"""<p>Hello {vorname} {name},</p>
<p>We would like to inform you that your reservation is confirmed. Your address is: <b>{strasse}, {plz_ort}</b>, room number <b>{zi_nr}</b>.</p>
<p>{payment_en}</p>
<p>Best regards,<br>International Office</p>"""

    # --- GERMAN VERSION (HTML) ---
    if programm == "Overseas":
        payment_de = "Sie müssen nichts überweisen, da Sie am Overseas-Programm teilnehmen. Alle Kosten werden von unseren Partnern übernommen."
    else:
        payment_de = f"""Bitte überweisen Sie den Betrag von <b>{kaution} € Kaution</b> + <b>{monatsmiete} € Monatsmiete</b> auf folgendes Konto:
        <br><br>
        <b>Kontoinhaber:</b> International Office, Universität Marburg<br>
        <b>Bank:</b> Sparkasse Marburg-Biedenkopf<br>
        <b>IBAN:</b> DE12 3456 7890 1234 5678 90<br>
        <b>BIC:</b> HELADEF1MAR<br><br>
        <b>Verwendungszweck:</b> {pers_nr}"""

    body_de = f"""<p>Hallo {vorname} {name},</p>
<p>wir freuen uns, Ihnen mitteilen zu können, dass Ihre Reservierung bestätigt ist. Ihre Adresse ist: <b>{strasse}, {plz_ort}</b>, Zimmernummer <b>{zi_nr}</b>.</p>
<p>{payment_de}</p>
<p>Mit freundlichen Grüßen,<br>International Office</p>"""

    # --- COMBINED EMAIL ---
    subject = "Room Reservation Confirmation / Zimmerreservierungsbestätigung"

    # Separator using HTML (horizontal line)
    body = f"""
    {body_en}
    <hr style="border: 1px solid #ccc; margin: 20px 0;">
    {body_de}
    """

    # Create a NEW dictionary
    new_data = dict(data)
    new_data["emailSubject"] = subject
    new_data["emailBody"] = body

    output.append({"json": new_data})

return output