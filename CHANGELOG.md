# Changelog

## 1.2.0 — 2026-10-31

### Přidáno
- **Klaviatura u každé písničky:** akordová tlačítka, zvýraznění kláves (C4–C6), kliknutí na klávesu zahraje tón, akord se přehraje arpeggiem.
- **Noty pro klávesy:** houslový klíč, noty s nožičkami, taktové čáry, pomocné linky, názvy tónů pod notami, zalamování do systémů.
- **Přehrání melodie** (Web Audio, 96 BPM) se současným zvýrazňováním kláves.
- Melodie zatím u 6 písní: Twinkle Twinkle, Row Your Boat, London Bridge, Jingle Bells, Old MacDonald, When the Saints.

### Opraveno
- Service worker je u navigace a `songs.js` **network-first** — po aktualizaci se už nezobrazuje stará verze z cache.
- `songs.js` má `no-cache` a v HTML je verzovací parametr (`?v=1.2.0`), takže update je vidět okamžitě.

## 1.1.0 — 2026-10-31

### Přidáno
- **Táborovky (10 písní):** Tři kříže, Hlídač krav, Bedna od whisky, Okoř, Červená řeka,
  Tisíc mil, Pověste ho vejš, Stánky, Severní vítr, Bláznova ukolébavka.
- **Zahraniční klasika (14 písní):** Oh! Susanna, Clementine, Kumbaya, Michael Row the Boat,
  Down by the Riverside, When the Saints, Coming Round the Mountain, Old MacDonald,
  Twinkle Twinkle, Row Your Boat, London Bridge, Jingle Bells, Auld Lang Syne, Swing Low.
- Nové kategorie v přepínači a počítadlo písniček v patičce.
- Akordy v mollových tóninách a s velkým H7 (Emi, Ami, Dmi, Gmi) — diagramy se generují i pro ně.

### Poznámka k licencím
Táborovky jsou klasické písně trampské a country scény, texty jsou uvedené ve zkrácené
podobě pro soukromé zpívání. Texty současných interpretů (Beatles, Nohavica, Ryvola apod.)
v aplikaci záměrně nejsou — jsou chráněné autorským právem. Vlastní písničku lze přidat
do `data/songs.js`.

## 1.0.0 — 2026-10-31

### Přidáno
- Zpěvník **24 českých říkanek** s akordy pro kytaru (zvířata, lidové, ukolébavky, hry).
- Zobrazení akordů přímo nad textem, automaticky generované **diagramy akordů** (kytara).
- **Transpozice ±11 půltónů** s nápovědou na kapodastr.
- Hledání bez diakritiky, filtr kategorií, oblíbené, náhodná písnička, zvětšení písma, tisk.
- **PWA** — offline režim a instalace na plochu.
- **Home Assistant add-on** (nginx, ingress, panel „Zpěvník“), žádný otevřený port.
