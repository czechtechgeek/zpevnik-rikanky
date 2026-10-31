# Zpěvník říkanek 🎵

České lidové říkanky s akordy pro kytaru — jako malý atlas, který jde otevřít na tabletu
v kuchyni, v autě i v Home Assistantovi.

## Co umí
- **48 písniček** ve šesti kategoriích: říkanky (zvířata, lidové, ukolébavky, hry), **táborovky** a **zahraniční klasika**
- **Akordy přímo nad textem** — žádné přepisování, hraje se hned
- **Diagramy akordů** (kytara, 6 strun) — prstoklady se vykreslují automaticky
- **Klaviatura**: u každé písničky se zobrazí klávesy pro akord, dají se klikat a přehrát
- **Noty** (houslový klíč) s názvy tónů u šesti písní + přehrání melodie
- **Transpozice ±11 půltónů** včetně nápovědy na kapodastr
- **Hledání bez diakritiky** (`kone` najde „koně“)
- **Oblíbené** (hvězdička) — uložené v prohlížeči
- **Větší písmo** pro čtení z dálky a tisk
- **Náhodná písnička** — tlačítko 🎲
- Noty a klaviatura fungují offline, zvuk jde přes Web Audio (bez souborů)
- Funguje offline (PWA) a jako add-on v Home Assistantu

## Ovládání
| Prvek | Co dělá |
|---|---|
| 🔍 hledání | filtruje podle názvu i textu, ignoruje diakritiku |
| štítky | Zvířata / Lidové / Ukolébavky / Hry / Táborovky / Zahraniční |
| ★ | oblíbené písničky |
| − / + | transpozice po půltónech |
| A− / A+ | velikost textu |
| 🖨 | tisk (bez ovládacích prvků) |

## Instalace v Home Assistantu
1. **Nastavení → Doplňky → Obchod s doplňky → ⋮ → Repozitáře**
2. Přidat `https://github.com/czechtechgeek/zpevnik-rikanky`
3. Nainstalovat **Zpěvník říkanek** a otevřít v levém panelu

Add-on používá jen ingress (žádný otevřený port), takže je dostupný jen přihlášeným uživatelům HA.

## Přidání písničky
Písničky jsou v `data/songs.js`. Formát:

```js
{
  id: "moje-pisnicka",
  title: "Moje písnička",
  cat: "lidove",            // zvirata | lidove | ukolebavky | hry | taborove | zahranicni
  key: "C",
  lines: [
    "[C]První řádek [G]textu,",
    "[F]druhý [C]řádek."
  ]
}
```

Akord se píše do hranatých závorek před slabiku, na kterou se hraje.
Po úpravě spusť `./packaging/sync_addon.sh` a přebuildi add-on.

## Struktura
```
index.html              # celá aplikace (CSS + JS)
data/songs.js           # písničky a akordy
manifest.webmanifest    # PWA
sw.js                   # offline cache
addon/                  # Home Assistant add-on (nginx)
packaging/sync_addon.sh # kopie webu do addon/www
tools/make_icons.py     # ikony add-onu
```

## Akordy
Používá se české značení: `H` = H dur (B natural), `B` = B dur (Bb).
Diagramy se generují z barré tvarů, takže fungují i pro transponované akordy.

## Zdroje textů a akordů
Říkanky jsou ověřené proti:
- `zpevnik.beil.cz` — statický zpěvník s akordy
- `spisnickou.cz` — akordy a texty
- `akordy.kytary.cz` — akordy a texty

Táborovky vycházejí ze *Zpěvníku k táboráku* (ccv.upol.cz) a zahraniční písně jsou tradicionály.

## Licence
MIT — texty jsou lidové písně v public domain.
