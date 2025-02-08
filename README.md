📜 README.md – Discord Admin Bot

# 🚀 Discord Admin Bot

Ein leistungsstarker Discord-Bot mit Admin-Funktionen, einschließlich Benutzer-Info, Kick und Ban.  
Er wurde mit `discord.py` erstellt und hilft Server-Administratoren, ihre Community effizient zu verwalten.



📌 **Funktionen**
✅ `!userinfo [@User]` → Zeigt Benutzerinformationen mit Status, Rollen & Aktivität.  
🔨 `!kick @User [Grund]` → Kickt einen Benutzer vom Server (Admin-Rechte erforderlich).  
⛔ `!ban @User [Grund]` → Bannt einen Benutzer dauerhaft (Admin-Rechte erforderlich).  



🛠 **Installation**
1️⃣ Voraussetzungen
- **Python 3.8+** installieren → [Download](https://www.python.org/downloads/)
- Discord Bot erstellen → [Discord Developer Portal](https://discord.com/developers/applications)
- **Folgende Bibliothek installieren:
  pip install discord.py


2️⃣ **Bot-Token einfügen**
- Öffne die Datei `bot.py`
- Ersetze `YOUR_BOT_TOKEN` mit deinem **echten Token**:

3️⃣ **Bot starten**

🔧 **Befehle & Nutzung**
📜 `!userinfo [@User]`
Zeigt detaillierte Benutzerinformationen in einer Embed-Nachricht.
- **Beispiel:** `!userinfo @Max`
- **Antwort:**
  ```
  👤 Informationen über MaxMustermann

  🆔 Benutzer ID: 123456789012345678
  📅 Konto erstellt am: 01.01.2021 15:30:45
  📌 Server beigetreten am: 15.06.2023 18:45:10

  🔒 Administrator: ✅ Ja
  💬 Status: 🟢 Online
  🎮 Aktivität: Rocket League

  📜 Rollen:
  Admin ✅
  Moderator ❌
  Support ✅
  VIP ❌
  Member ✅
  ```

👢 `!kick @User [Grund]`
Kickt einen Benutzer vom Server.
- **Beispiel:** `!kick @Max Unhöfliches Verhalten`
- **Antwort:** `Max wurde von Admin gekickt. Grund: Unhöfliches Verhalten.`

⛔ `!ban @User [Grund]`
Bannt einen Benutzer dauerhaft.
- **Beispiel:** `!ban @Max Spam`
- **Antwort:** `Max wurde von Admin gebannt. Grund: Spam.`

❗ **Wichtige Hinweise**
- **Benutzer mit gleichem oder höherem Rang können nicht gekickt/gebannt werden.**
- **Der Bot benötigt die folgenden Berechtigungen:**
  - `Kick Members`
  - `Ban Members`
  - `Read Messages`
  - `Send Messages`
  - `Embed Links`

📝 **To-Do / Erweiterungen**

✅ `!userinfo` verbessert mit sortierten Rollen  
✅ `!kick` und `!ban` mit Berechtigungsprüfung  
🔜 `!mute` & `!warn` für erweiterte Moderation  
🔜 Logging-System für Admin-Aktionen  

👨‍💻 **Mitwirkende**
- **AlphaGames** – Entwicklung & Wartung  
- **Discord Community** – Feature-Vorschläge & Tests  

🌟 **Lizenz**
Dieses Projekt ist unter der MIT-Lizenz veröffentlicht.  
Frei nutzbar für alle, die ihren Discord-Server verbessern möchten! 🎉
