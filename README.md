
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
GET /api/v1/login?email=stephan.huber@a1.at&password=stephan
```
#### Antwort
```json
{
  "message": "Login successful.",
  "status": "success",
  "user_id": 4
}
```

### Login Passwort Reset
Ändert das Passwort eines Benutzers.
#### Request
```http
GET /api/v1/resetPassword?email=stephan.huber@a1.at&password=stephan&new_password=stephan123!
```
#### Antwort
```json
{
  "message": "Password changed successfully",
  "status": "success"
}
```

### Parkplatz ID bekommen
Retourniert die Parkplatz ID von einem User, falls er einen Parkplatz hat.
#### Request
```http
GET /api/v1/getSpotID?user_id=3
```
#### Antwort
```json
{
  "parkspot": "1",
  "status": "success"
}
```

### Anzahl an verfügbaren Parkplätzen bekommen
Retourniert die Anzahl an Parkplätzen welche man reservieren kann.
#### Request
```http
GET /api/v1/getAvailable
```
#### Antwort
```json
{
  "available": "2",
  "status": "success"
}
```

### Parkplatz verfügbar machen
Macht einen Parkplatz verfügbar welcher dann reserviert werden kann.
#### Request
```http
GET /api/v1/makeAvailable?parkspot_id=2
```
#### Antwort
```json
{
  "message": "Park spot 1 is now available for you the entire day today.",
  "status": "success"
}
```

### Parkplatz reservieren
Reserviert einen Parkplatz, welcher verfügbar ist.
#### Request
```http
GET /api/v1/reserve?user_id=1
```
#### Antwort
```json
{
  "message": "Park spot 1 reserved successfully.",
  "status": "success"
}
```
