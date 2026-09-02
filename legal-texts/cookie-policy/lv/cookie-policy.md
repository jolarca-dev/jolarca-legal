---
text: cookie-policy
language: lv
version: 1.0.0
status: approved
effective_date: ""
approved_by: "general-counsel"
supersedes: ""
---

# Sīkdatņu politika — Journey of Life tirgus vieta

**Spēkā stāšanās datums:** [jānosaka pēc publicēšanas]

Šī Sīkdatņu politika izskaidro, kā JOL izmanto sīkdatnes un līdzīgas
glabāšanas tehnoloģijas Tirgus vietā.

## 1. Ko mēs glabājam un kāpēc

| Kategorija | Nolūks | Nepieciešama piekrišana? |
|------------|--------|-------------------------|
| **Būtiskās** | Pamata Tirgus vietas funkcionalitāte (sesija, drošība, CSRF, grozs) | Nē — stingri nepieciešamas |
| **Funkcionālās** | Lietotāja preferences (valoda, valūta) | Nē — stingri nepieciešamas |
| **Analītiskās** | Lietojuma modeļu izpratne | Jā |
| **Mārketinga** | Mērķtiecīga saziņa (tikai ar skaidru piekrišanu) | Jā |

## 2. Kategoriju tabula

### 2.1 Būtiskās sīkdatnes (piekrišana nav nepieciešama)

| Nosaukums | Sniedzējs | Nolūks | Ilgums |
|-----------|-----------|--------|--------|
| `sessionid` | JOL | Servera sesijas identifikators | Sesija |
| `csrftoken` | JOL | Pieprasījumu viltošanas aizsardzība | 1 gads |
| `cart` | JOL | Iepirkumu groza stāvoklis | Sesija |
| `consent` | JOL | Lietotāja sīkdatņu piekrišanas izvēles | 24 mēneši |

### 2.2 Funkcionālās sīkdatnes (piekrišana nav nepieciešama)

| Nosaukums | Sniedzējs | Nolūks | Ilgums |
|-----------|-----------|--------|--------|
| `language` | JOL | Vēlamā attēlošanas valoda (lt/lv/et/en) | 12 mēneši |
| `currency` | JOL | Vēlamā valūta | 12 mēneši |

### 2.3 Analītiskās sīkdatnes (nepieciešama piekrišana)

| Nosaukums | Sniedzējs | Nolūks | Ilgums |
|-----------|-----------|--------|--------|
| `_ga` | Google Analytics (GA4) | Unikāla apmeklētāja identifikācija | 24 mēneši |
| `_gid` | Google Analytics (GA4) | Sesiju izsekošana | 24 stundas |

## 3. Jūsu izvēles

### 3.1 Piekrišanas baneris

Pirmās vizītes laikā tiek parādīts piekrišanas baneris, kas ļauj:

- **Piekrist visām** nebūtiskajām sīkdatnēm;
- **Noraidīt visas** nebūtiskās sīkdatnes (vienāds izcēlums);
- **Pielāgot** izvēles pa kategorijām.

### 3.2 Iestatījumu maiņa

Piekrišanu varat mainīt vai atsaukt jebkurā laikā caur „Sīkdatņu
iestatījumi" saiti lapas apakšā.

## 4. Piekrišanas līgums (banera specifikācija)

### 4.1 Pirms piekrišanas

- **Nebūtiskas sīkdatnes** nedrīkst tikt iestatītas pirms lietotājs ir
  devis skaidru piekrišanu.
- Starpprogramma noņem nebūtiskās `Set-Cookie` galvenes no atbildēm
  lietotājiem bez derīga piekrišanas ieraksta.

### 4.2 Vienlīdzīgs izcēlums

- „Noraidīt" opcijai jābūt parādītai ar tādu pašu vizuālo izcēlumu kā
  „Piekrist".
- Tumšie raksti (iepriekš atzīmētas izvēles rūtiņas, krāsu asimetrija)
  ir aizliegti.

## 5. Trešo pušu SDK

| Pakalpojums | Sniedzējs | Sīkdatnes | Nolūks |
|-------------|-----------|-----------|--------|
| Stripe Elements | Stripe Payments Europe Ltd. | `__stripe_mid`, `__stripe_sid` | Maksājumu krāpšanas noteikšana |
| Google Analytics | Google LLC | `_ga`, `_gid` | Lietojuma analītika (tikai ar piekrišanu) |

## 6. Izmaiņas

Pievienojot jaunu sīkdatni vai kategoriju, piekrišanas baneris tiks
atkal parādīts visiem lietotājiem, kas iepriekš piekrita.
