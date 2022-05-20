# A covid inspired 70's style 2D 8-bit arcade game written using Pygame.

### Sample from the game:

### Main game rules / logics to control game progression, difficulty and end game conditions:


- User selects what difficulty they wish to start at 1-10.
- Bats spawn increasingly at each level.
- Lives spawn when player health < 50.
- Vaccine Ammo spawns when player ammo < 50.
- Bats spawn some viruses (limited by time on screen).
- Player shoots vaccines (limited by ammo and ability
to pick up the ammo drop).
- Player increases ammo inventory by 50 on collecting ammo drop.
- Collisions of virus or bat with granny or player, results in decreasing health 10 %.
- Player has 5 lives, when player health is depleted lives is decremented and health is replenished.
- Player health is increased by 25% if the player picks up powerup.
- Granny health is replenished if it by luck picks up a powerup.
- If granny health is 0 or, player health and lives are 0 the game reaches the end, a score is output
- Score is the number of bats killed.
- If all bats are killed and the end conditions haven’t been met, next level is progressed to, and repeat.

### Control of game object abilities:

The game objects are, Granny, Boris, Bat, Virus, vaccine and powerup [health, ammo]. Boris is the player who is controlled by the mouse and shoots with the space bar. The granny is automated to have no user controllable feature, she is a target which makes the game harder, she walks from one end of the screen to the other. The bats aim and shoot towards the granny; there is also an element of randomness as to weather or not they will shoot knowing they can reach the target; the player controls the aim of their shot with the mouse and a vaccine is shot, I explained in the other sections what happens on various collisions.
If the player has no ammo; they cannot shoot they need an ammo drop and collect it, if they have no lives if their health reaches 0 the game is over. If granny looses all her health the game is over.

### Usage:

In your terminal, access this directory, and run: `python main.py`