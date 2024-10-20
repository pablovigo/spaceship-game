# SpaceShip game

## Descripció

"SpaceShip Game" és un joc senzill desenvolupat amb Pygame, en què el jugador controla una nau que ha d'esquivar naus enemigues que cauen del cel. 
L'objectiu del joc és sobreviure el màxim temps possible mentre s'eviten col·lions i s'acumula puntuació.

## Característiques

- **Controls:** 
  - Mou la nau del jugador a l'esquerra i a la dreta utilitzant les tecles de fletxa esquerra i dreta.
  - El jugador ha d'evitar les naus que cauen.

- **Naus Enemigues:**
  - Les naus cauen des de la part superior de la pantalla a una velocitat aleatòria.
  - Si una nau arriba a la part inferior de la pantalla, s'elimina i el jugador guanya un punt.

- **Col·lisions:**
  - Si la nau del jugador col·lisiona amb una altra nau, el joc acaba.

- **Puntuació:**
  - La puntuació s'incrementa cada vegada que una nau cau sense colisionar amb el jugador.

## Requisits

- Python 3.x
- Pygame (pots instal·lar-lo utilitzant `pip install pygame`)

## Instal·lació

1. Clona aquest repositori:
  ```
  git clone https://github.com/pablovigo/spaceship-game.git
  cd spacehip-game
  ```

2. Assegura't de tenir Pygame instal·lat:
  ```
  pip install pygame
  ```

3. Executa el joc:
  ```
  python3 spaceship-game.py
  ```

## Contribucions

Les contribucions són benvingudes. Si desitges millorar el joc o afegir noves característiques, si us plau, obre un "issue" o envia un "pull request".

## Llicència

Aquest projecte està llicenciat sota la Llicència MIT.

