---
text: cookie-policy
language: et
version: 1.0.0
status: approved
effective_date: ""
approved_by: "general-counsel"
supersedes: ""
---

# Küpsiste poliitika — Journey of Life turg

**Jõustumise kuupäev:** [määratakse avaldamisel]

See Küpsiste poliitika selgitab, kuidas JOL kasutab küpsiseid ja
sarnaseid salvestamistehnoloogiaid Turul.

## 1. Mida me salvestame ja miks

| Kategooria | Eesmärk | Kas nõutakse nõusolekut? |
|------------|---------|------------------------|
| **Hädavajalikud** | Põhiline Turu funktsionaalsus (seanss, turvalisus, CSRF, korv) | Ei — rangelt vajalikud |
| **Funktsionaalsed** | Kasutaja eelistused (keel, valuuta) | Ei — rangelt vajalikud |
| **Analüütilised** | Kasutamismustrite mõistmine | Jah |
| **Turundus** | Sihitud teated (ainult selge nõusolekuga) | Jah |

## 2. Kategooriate tabel

### 2.1 Hädavajalikud küpsised (nõusolekut ei nõuta)

| Nimi | Pakkuja | Eesmärk | Kestus |
|------|---------|---------|--------|
| `sessionid` | JOL | Serveri seansi identifikaator | Seanss |
| `csrftoken` | JOL | Päringuvõltsimise kaitse | 1 aasta |
| `cart` | JOL | Ostukorvi olek | Seanss |
| `consent` | JOL | Kasutaja küpsiste nõusoleku valikud | 24 kuud |

### 2.2 Funktsionaalsed küpsised (nõusolekut ei nõuta)

| Nimi | Pakkuja | Eesmärk | Kestus |
|------|---------|---------|--------|
| `language` | JOL | Eelistatud kuvamiskeel (lt/lv/et/en) | 12 kuud |
| `currency` | JOL | Eelistatud valuuta | 12 kuud |

### 2.3 Analüütilised küpsised (nõusolek vajalik)

| Nimi | Pakkuja | Eesmärk | Kestus |
|------|---------|---------|--------|
| `_ga` | Google Analytics (GA4) | Unikaalne külastaja identifitseerimine | 24 kuud |
| `_gid` | Google Analytics (GA4) | Seansside jälgimine | 24 tundi |

## 3. Teie valikud

### 3.1 Nõusoleku bänner

Esimesel visiidil kuvatakse nõusoleku bänner, mis võimaldab:

- **Nõustuda kõigiga** mittehädavajalike küpsistega;
- **Lükata tagasi kõik** mittehädavajalikud küpsised (võrdne esiletõstmine);
- **Kohandada** valikuid kategooriate kaupa.

### 3.2 Eelistuste muutmine

Nõusolekut saate igal ajal muuta või tagasi võtta „Küpsiste seaded"
lingi kaudu lehe allosas.

## 4. Nõusoleku leping (bänneri spetsifikatsioon)

### 4.1 Enne nõusolekut

- **Mittehädavajalikke küpsiseid** ei tohi seada enne, kui kasutaja on
  andnud selge nõusoleku.
- Vahevara eemaldab mittehädavajalikud `Set-Cookie` päised vastustest
  kasutajatele ilma kehtiva nõusoleku salvestiseta.

### 4.2 Võrdne esiletõstmine

- „Lükka tagasi" valik peab olema kuvatud sama visuaalse esiletõstmisega
  kui „Nõustu".
- Tumedad mustrid (eeltäidetud märkeruudud, värvi asümmeetria) on
  keelatud.

## 5. Kolmandate osapoolte SDK-d

| Teenus | Pakkuja | Küpsised | Eesmärk |
|--------|---------|----------|---------|
| Stripe Elements | Stripe Payments Europe Ltd. | `__stripe_mid`, `__stripe_sid` | Maksepettuste tuvastamine |
| Google Analytics | Google LLC | `_ga`, `_gid` | Kasutuse analüütika (ainult nõusolekuga) |

## 6. Muudatused

Uue küpsise või kategooria lisamisel kuvatakse nõusoleku bänner uuesti
kõigile kasutajatele, kes varem nõustusid.
