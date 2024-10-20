# SpaceShip game

## Descripció

"SpaceShip Game" és un joc senzill desenvolupat amb Pygame, en què el jugador controla una caixa que ha d'esquivar blocs que cauen del cel. 
L'objectiu del joc és sobreviure el màxim temps possible mentre s'eviten els blocs i s'acumula puntuació.

## Característiques

- **Controls:** 
  - Mou la caixa del jugador a l'esquerra i a la dreta utilitzant les tecles de fletxa esquerra i dreta.
  - El jugador ha d'evitar els blocs que cauen.

- **Blocs Enemics:**
  - Els blocs cauen des de la part superior de la pantalla a una velocitat aleatòria.
  - Si un bloc arriba a la part inferior de la pantalla, s'elimina i el jugador guanya un punt.

- **Col·lisions:**
  - Si la caixa del jugador col·lisiona amb un bloc, el joc acaba.

- **Puntuació:**
  - La puntuació s'incrementa cada vegada que un bloc cau sense colisionar amb el jugador.

## Requisits

- Python 3.x
- Pygame (pots instal·lar-lo utilitzant `pip install pygame`)

## Instal·lació

1. Clona aquest repositori:
  ```
  git clone https://github.com/tu_usuari/esquiva-els-blocs-que-cauen.git
  cd spacehip-game
  ```

2. Assegura't de tenir Pygame instal·lat:
  ```
  pip install pygame
  ```

3. Executa el joc:
  ```
  python main.py  # O el nom del fitxer on està el codi
  ```

## Ús

Al iniciar el joc, controla la caixa negra (jugador) movent-la d'esquerra a dreta.
Esquiva els blocs vermells que cauen.
Intenta obtenir la màxima puntuació possible evitant colisions.

## Contribucions

Les contribucions són benvingudes. Si desitges millorar el joc o afegir noves característiques, si us plau, obre un "issue" o envia un "pull request".

## Llicència

Aquest projecte està llicenciat sota la Llicència MIT.

