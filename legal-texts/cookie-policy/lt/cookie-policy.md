---
text: cookie-policy
language: lt
version: 1.0.0
status: approved
effective_date: ""
approved_by: "general-counsel"
supersedes: ""
---

# Slapukų politika — Journey of Life prekyvietė

**Įsigaliojimo data:** [bus nustatyta paskelbus]

Ši Slapukų politika paaiškina, kaip JOL naudoja slapukus ir panašias
saugojimo technologijas Prekyvietėje.

## 1. Ką saugome ir kodėl

| Kategorija | Tikslas | Reikalingas sutikimas? |
|------------|---------|----------------------|
| **Būtini** | Pagrindinė Prekyvietės funkcija (sesija, saugumas, CSRF, krepšelis) | Ne — griežtai būtini |
| **Funkciniai** | Naudotojo nustatymai (kalba, valiuta) | Ne — griežtai būtini |
| **Analitiniai** | Naudojimo modelių supratimas | Taip |
| **Rinkodaros** | Tiksliniai pranešimai (tik su aiškiu sutikimu) | Taip |

## 2. Kategorijų lentelė

### 2.1 Būtini slapukai (sutikimo nereikia)

| Pavadinimas | Teikėjas | Tikslas | Trukmė |
|-------------|----------|---------|--------|
| `sessionid` | JOL | Serverio sesijos identifikatorius | Sesija |
| `csrftoken` | JOL | Kryžminio užklausos klastojimo apsauga | 1 metai |
| `cart` | JOL | Pirkinių krepšelio būsena | Sesija |
| `consent` | JOL | Naudotojo slapukų sutikimo pasirinkimai | 24 mėnesiai |

### 2.2 Funkciniai slapukai (sutikimo nereikia)

| Pavadinimas | Teikėjas | Tikslas | Trukmė |
|-------------|----------|---------|--------|
| `language` | JOL | Pageidaujama rodymo kalba (lt/lv/et/en) | 12 mėnesių |
| `currency` | JOL | Pageidaujama valiuta | 12 mėnesių |

### 2.3 Analitiniai slapukai (reikalingas sutikimas)

| Pavadinimas | Teikėjas | Tikslas | Trukmė |
|-------------|----------|---------|--------|
| `_ga` | Google Analytics (GA4) | Unikalus lankytojo identifikavimas | 24 mėnesiai |
| `_gid` | Google Analytics (GA4) | Sesijos sekimas | 24 valandos |

## 3. Jūsų pasirinkimai

### 3.1 Sutikimo baneris

Pirmojo apsilankymo metu rodomas sutikimo baneris, leidžiantis:

- **Sutikti su visais** nebūtinais slapukais;
- **Atmesti visus** nebūtinais slapukais (lygiavertis „Sutikti");
- **Tinkinti** pasirinkimus pagal kategorijas.

### 3.2 Nuostatų keitimas

Sutikimą galite pakeisti arba atšaukti bet kuriuo metu per „Slapukų
nustatymų" nuorodą puslapio apačioje.

## 4. Sutikimo sutartis (banerio specifikacija)

### 4.1 Iki sutikimo

- **Jokie nebūtini slapukai** negali būti nustatyti prieš naudotojui
  suteikiant aiškų sutikimą.
- Vidurinė programa (middleware) pašalina nebūtinus `Set-Cookie`
  antraštes iš atsakymų naudotojams be galiojančio sutikimo įrašo.

### 4.2 Lygiavertiškumas

- „Atmesti" parinktis turi būti rodoma su tokia pat vizualine svarba
  kaip „Sutikti".
- Tamsūs raštai (iš anksto pažymėti langeliai, spalvų asimetrija)
  draudžiami.

### 4.3 Pakartotinio klausimo dažnumas

- Sutikimo baneris pakartotinai rodomas tik kai: naudotojas nepadarė
  pasirinkimo; kategorijos materialiai pasikeitė; sutikimo versija
  pasibaigė (po 24 mėnesių).

## 5. Trečiųjų šalių SDK

| Paslauga | Teikėjas | Slapukai | Tikslas |
|----------|----------|----------|---------|
| Stripe Elements | Stripe Payments Europe Ltd. | `__stripe_mid`, `__stripe_sid` | Mokėjimų sukčiavimo aptikimas |
| Google Analytics | Google LLC | `_ga`, `_gid` | Naudojimo analitika (tik su sutikimu) |

## 6. Pakeitimai

Pridėjus naują slapuką ar kategoriją, sutikimo baneris bus pakartotinai
rodomas visiems naudotojams, kurie anksčiau sutiko.
