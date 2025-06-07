# Willkommen im Projekt

Dieses Projekt enthält einen einfachen Python-basierten AI-Agenten. Der Agent kann wahlweise die OpenAI-API nutzen oder lokal 
mit einem kleinen Transformers-Modell arbeiten. Er verwendet den Inhalt dieses README als Kontext.

## Voraussetzungen

- Python 3.8+
- Abhängigkeiten: `openai`, `transformers`
- Optional: Eine gültige `OPENAI_API_KEY` Umgebungsvariable

## Installation

Installiere die Abhängigkeiten mit pip:

```bash
pip install openai transformers
```

## Nutzung

Starte den Agenten über die Kommandozeile und übergebe eine Frage oder einen Prompt:

```bash
python ai_agent.py "Deine Frage hier"
```

Falls kein Prompt übergeben wird, fragt das Skript nach einer Eingabe. Der Agent sendet die Anfrage an OpenAI ChatGPT und gibt die Antwort aus.
Ohne gesetzte `OPENAI_API_KEY`-Variable nutzt der Agent automatisch ein lokales GPT-2-Modell 
aus der Transformers-Bibliothek.

## Docker

Du kannst den Agenten auch in einem Docker-Container ausführen. Baue zunächst das Image:

```bash
docker build -t ai-agent .
```

Starte danach den Container. Wenn du einen OpenAI-Schlüssel übergibst, wird die API verwendet,
ansonsten greift der Container auf das lokale Modell zurück. Beispiel mit Schlüssel:

```bash
docker run --rm -e OPENAI_API_KEY=<dein_schluessel> ai-agent "Deine Frage hier"
```

Ohne API-Schlüssel kannst du den Container einfach ohne Umgebungsvariable starten:

```bash
docker run --rm ai-agent "Deine Frage hier"
```
