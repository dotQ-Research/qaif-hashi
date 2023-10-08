**Quantum AI Foundation Quantum Games HACKATHON 2023**

# :space_invader: Quantum Hashi- Team DotQ

- [Team Introduction](#team-introduction)
- [Game Summary](#game-summary)
  - [Description](#description)
- [Part 1](#part-1)
  - [Game Rules](#game-rules)
  - [How To Play](#how-to-play)
- [Part 2](#part-2)
  - [Game Rules](#game-rules)
  - [How To Play](#how-to-play)
- [How to Install](#how-to-install)
- [Significance of the game](#Significance-of-the-game)
- [Software & Tools Used](#software--tools-used)
- [Future Plans](#future-plans)
- [License](#license)
- [Acknowledgement](#Acknowledgement)
- [References](#references)

# Team Introduction
**Team Name:** DotQ

**Game Name:** Quantum Hashi



****Member Names:****

------------

**Abdullah Kazi**

Discord ID: **LudWig Maxwell Planck**

GitHub ID: **AbdullahKazi500**


------------

**Enrique Anguiano Vara**

Discord ID: **EnriqueAnguianoVara**

GitHub ID: **EnriqueAnguianoVara**


 
------------


**Bakhao Dioum**


Discord ID: Bakhao


GitHub ID: papidioum



------------

**Rahul Dev Sharma**


Discord ID: Rahul Dev Sharma


GitHub ID: Rahul Dev Sharma


------------





# Game Summary
The game is called Quantum Hashi, and it is a two-part game that teaches and tests your knowledge of quantum error correction on entangled qubits. 
The game is partially inspired by the classical Hashi game, where you have to connect islands with bridges following some rules. 
In Quantum Hashi, the islands are qubits and the bridges are entanglement links.  In this game, we teach :
- How to encode quantum information using entangled qubits,
- How to detect and correct errors using syndrome measurements.

## Description:
- [ ] Each island corresponds to a Qubit.
- [ ] The number on each qubit (island) that tells you how many other qubits it's entangled with.
- [ ] The bridges correspond in the first part to the entanglement link between pairs of qubits
and in the second part to the syndrome measurement. It will discussed more in detail.
- [ ] For a much more simplified rule, see [simplified rules](https://github.com/dotQ-Research/qaif-hashi/blob/main/Simplified%20rules.md)
- [ ] For a quick introduction to what error correction is see [Error Correction](https://github.com/dotQ-Research/qaif-hashi/blob/main/error%20correctio.md)
- [ ] For game concept please check [Game Concept](https://github.com/dotQ-Research/qaif-hashi/blob/main/Game-Concept-for-Quantum-Hashi.pdf)
# Part 1

## Game Rules

In this part, you have to create a quantum error-correcting code using entangled qubits. 
A quantum error-correcting code is a way to encode qubits in such a way that errors can
be detected and corrected without destroying the quantum information.

In this first part, you are given numbered qubits (represented by islands) that you have 
to connect with entanglement links (represented by bridges) following these rules:

- [ ] Each qubit has a number that tells you how many other qubits it's entangled with. 
- [ ] There can be at most one entangled link between two qubits.
- [ ] The entangled links cannot cross each other. This rule represents the no-cloning theorem,
which states that quantum information cannot be copied exactly.
- [ ] Qubits can only be linked perpendicularly. These are constraints that are imposed by the hardware.
- [ ] The goal is to connect all the qubits in a fully entangled system following these rules,
 which means that they share the maximum amount of quantum information and correlation.
This rule is very important since it ensures that measuring directly some qubits will collapse the whole state of the system.

![image](https://github.com/dotQ-Research/qaif-hashi/assets/108539802/a05f61d0-1f9d-4e0a-a738-a9899a08f324)

## How To Play
![hashiqs](https://github.com/dotQ-Research/qaif-hashi/assets/75779966/bb050a7e-2eea-4cb3-9d0f-e3a4331976ae)

![hashii](https://github.com/dotQ-Research/qaif-hashi/assets/75779966/4130476a-3485-4633-a9db-7eff8b8d4e9d)

1. **Click with your mouse on two qubits to link them. Click on the same qubits to unlink them.**
2. **Once a qubit has as many entangled links as the number on it, it will switch to a different colour.**
3. **Finding the most optimal entanglement map wins you the game**
4. **Once all qubits are fully connected in a single group, you win.**
5. [Watch the Gameplay/Walthrough](PUT LINK HERE)


# Part 2

## Game Rules
In this part, you have to use syndrome measurement to detect and correct the errors on the qubits. 
A syndrome measurement is a way to detect errors in your qubits without measuring them, to avoid the collapse.
An example of syndrome measurement could be to check the parity (equality) of two qubits to return a true or false answer. 
This can be used to determine whether a correction needs to occur. 
If the syndrome measurement is different from what you expect for the encoded state, it means that there is an error on one of the qubits.

We start with a fully entangled map where some syndrome measurements are shown to be faulty
The goal is to use the clues on the syndrome measurement to detect which of the qubits have errors in them.
Then the player, using some interactive clicks, ensures to correct the concerned qubits
until all the syndrome measurements are back to their normal states.

![image](https://github.com/dotQ-Research/qaif-hashi/assets/108539802/c970fc7a-83e6-46ab-82c0-8bf636fba7e4)

Beware, a faulty syndrome measurement alone will not tell us which of the two qubits of the pair is the faulty one. 
We need to take into account the other bridges (the neighbouring syndrome measurements).

![image](https://github.com/dotQ-Research/qaif-hashi/assets/108539802/c132d87a-2f17-4c89-8892-d9308e7d480b)


## How To Play

1. **Figure out which of the qubits are faulty.**
2. **Click on them to correct them.**
3. **You win when all the syndrome measurements (bridges) are back to their normal states .**
4. [Watch the Gameplay/Walthrough](PUT LINK HERE)


# How to Install
- Python & python libraries (as told is requirements.txt)
  - python version >= 3.11.4
  - pygame==2.5.2: ``` pip install pygame ```
  - pyyaml==6.0.1: ``` pip install pyyaml ```

If there is some MESA-LOADER error, please do what it says [here](https://stackoverflow.com/questions/71010343/cannot-load-swrast-and-iris-drivers-in-fedora-35/72200748#72200748): 


## Significance of the Game 
Quantum error correction is a crucial aspect of quantum computing. By gamifying it, you can make this complex topic more accessible and engaging to a broader audience, including students and enthusiasts. It can help demystify quantum error correction codes like the surface code and the principles behind them.

Games are an effective way to facilitate hands-on learning. A Quantum Error Correction Hashi Game provides a practical way for players to understand how qubits can be protected from errors using error correction codes. It allows players to actively participate in the error correction process within the game context.

Hashi puzzles involve connecting islands with bridges under specific rules. By incorporating quantum error correction into this puzzle, players can intuitively grasp the idea that qubits (represented as islands) need to be connected or "entangled" in a specific way to correct errors, just like bridges connecting islands in Hashi.

Hashi puzzles are known for enhancing players' problem-solving skills. By adding a quantum error correction element, you challenge players to not only solve traditional Hashi puzzles but also strategically correct errors in their quantum configurations. This adds complexity and depth to the game.

Games can serve as a fun introduction to quantum concepts. A Quantum Error Correction Hashi Game can promote awareness and interest in quantum computing and quantum error correction among individuals who may not have prior exposure to these fields.

Combining educational elements with gameplay makes learning more enjoyable and engaging. Players are more likely to invest time and effort in understanding quantum error correction if it's presented in a game format.

# Software & Tools Used  

- Python
- Pygame
  
## Acknowledgement
**We would like to extend our heartfelt gratitude to the Quantum AI Foundation, particularly Pawel Gora, for their exceptional efforts in organizing and hosting the Quantum Games Hackathon 2023**. 
We would also like to express our sincere appreciation to mentors Adam Glos and Artur , whose expertise and guidance were invaluable throughout the hackathon. We would also like to Thank **Abdullah Khalid** for providing insights and reviewing the game.
We would also like to thank Piotr Biskupski from IBM for an insightful talk on Error mitigation with Qiskit Runtime 
**This hackathon has been an incredible learning experience, and it wouldn't have been possible without the support and encouragement of the Quantum AI Foundation**


# Future Plans

- [ ] The game can be adapted to a different Bell pair but that will require a
reinterpretation of the results of the parity measurements. This add some
unecessary complexity.
- [ ] We could also consider the case of Phase Flip errors, it will not change the
principes of the game
- [ ] we can increase difficulty in the future game levels by implementing More qubits + larger grids.
- [ ] we can increase difficulty by implementing Harder to deduce types of error and larger number of errors in the map.



# License

<a href="https://choosealicense.com/licenses/mit/"><img src="https://raw.githubusercontent.com/johnturner4004/readme-generator/master/src/components/assets/images/mit.svg" height=40 />MIT License</a>

# References

[_https://builtin.com/hardware/quantum-computer-games_](https://builtin.com/hardware/quantum-computer-games)

[_https://www.wilsoncenter.org/blog-post/games-round-quantum-computing_](https://www.wilsoncenter.org/blog-post/games-round-quantum-computing)

[_https://www.researchgate.net/publication/361022971_Defining_Quantum_Games_](https://www.researchgate.net/publication/361022971_Defining_Quantum_Games)

[_https://decodoku.medium.com/why-we-need-to-make-quantum-games-6f8c7bc4ace7_](https://decodoku.medium.com/why-we-need-to-make-quantum-games-6f8c7bc4ace7)

[_https://uwaterloo.ca/news/news/new-quantum-cats-game-launches-better-understanding-quantum_](https://uwaterloo.ca/news/news/new-quantum-cats-game-launches-better-understanding-quantum)

[_https://decodoku.medium.com/quantum-battleships-the-first-multiplayer-game-for-a-quantum-computer-e4d600ccb3f3_](https://decodoku.medium.com/quantum-battleships-the-first-multiplayer-game-for-a-quantum-computer-e4d600ccb3f3)


