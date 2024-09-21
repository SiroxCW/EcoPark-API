
# EcoPark API Dokumentation

## Beschreibung
EcoPark ist eine Thunkable App welche für den Lehrlingshackathon 2024 vom A1 Team entwickelt wurde.<br><br>
Die App soll es ermöglichen, dass Mitarbeiter ihre Parkplätze in der Firmengarage z.B. bei Urlaub oder Krankenständen freigeben können. Andere Mitarbeiter können dann diese Parkplätze reservieren und nutzen. Die App soll auch eine Übersicht über die verfügbaren Parkplätze und die Reservierungen bieten um <b>lange Parkplatzsuchen zu vermeiden.</b>

## API Dokumentation
Dies ist die Dokumentation der API, welche die EcoPark App benutzt. Eine RESTful API war leider nicht möglich, da Thunkable Probleme mit dem HTTP Header hat.

### Login
Retourniert einen boolean Wert, ob die Anmeldedaten korrekt sind.
#### Request
```http
GET /api/v1/login?user=max.mustermann@a1.at&password=maxi123
```
#### Antwort
```json
{
    "status": "success",
    "message": "Login successful."
}
```

