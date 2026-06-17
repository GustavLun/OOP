# 3. Banken:
## Krav:
Systemet ska tillåta användaren att sätta in pengar samt ta ut pengar. Systemet ska även kunna returnera användarens nuvarande saldo. Sytemet ska även kunna applicera och räkna ut räntan på kontot. sist ska systemet kunna berätta för användare om den har råd att betala en specifik faktura.

## AK 1
Användaren ska kunna sätta in pengar på ett konto.
- Input: Belopp att sätta in 500:-
- Resultat: 
  - Saldo ökar
  - Bekräftelse visas

## AK 2
Användaren ska kunna ta ut pengar samt bli nekad om saldot är stort nog för vad användaren vill ta ut.'
- Input: Ta ut 500:-
- Resultat:
  - Saldo minskar
  - Bekräftelse visas

## AK 3
Användaren ska titta på sitt nuvarande saldo.
- Input: Välj: se saldo
- Resultat: Nuvarande saldo visas

## AK 4
Användaren ska kunna se ränteberäkningar på kontot
- Input: Räkna ut ränta
- Resultat: Nuvarande ränteberäkning visas

## AK 5
Användaren ska kunna skriva in summan på en faktura och baserat på om saldot täcker fakturan eller inte returneras `False` eller `True`
- Input: Skriv in faktura summa
- Resultat:
  - Saldo täcker summan på fakturan ``True`` returneras.
  - Saldo täcker inte summan på fakturan ``False`` returneras