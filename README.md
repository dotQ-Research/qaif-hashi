**Quantum AI Foundation Quantum Games HACKATHON 2023**

# :space_invader: Quantum Hashi- Team DotQ

- [Team Introduction](#team-introduction)
- [Game Summary](#game-summary)
  - [Mission](#mission)
  - [Story](#story)
  - [How To Play](#how-to-play)
- [How to Install](#how-to-install)
- [Challenges Faced](#challenges-faced)
- [Software & Tools Used](#software--tools-used)
- [Future Plans](#future-plans)
- [License](#license)
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

**Enrique**

Discord ID: Enrique

GitHub ID: Enrique


 
------------


**Bakhao**


Discord ID: Bakhao


GitHub ID: Bakhao



------------

**Rahul Dev Sharma**


Discord ID: Rahul


GitHub ID: Rahul


------------





# Game Summary
The idea is to use Classical Hashi to understand the concept to understand the
concept of correcting errors on entangled states using parity measurements.
This will be done through a two part game (for each level).

# Description:
- [ ] Each island corespond to a Qubit
- [ ] The number on each qubit (island) corresponds to the number of qubits that are
- [ ] entangled with the island.
- [ ] The bridges correspond in the first part to the entanglement between qubits
and the parity measurement in the second part. I will discuss this more in details.

## Game rules
Rules Level 1: 
This is the only rule that has to change compared to Classical Hashi. There must
be at most a single bridge between two qubits. If anybody can give an
explanation of what having two entanglement links between same qubits could
mean, that rule could stay also.
The bridges cannot cross each other. This could mean we cannot copy quantum
unknown quantum states du to the No Cloning Theorem.
Qubits can only be linked perpendicularly : this could be a constraint on the
hardware in which we want to encode our qubits.
The goal is to connect all the qubits in the islands in a single group of entangled
qubits, while respecting the above rules. This could be a useful ressource for
fault-tolerance.

Rules Level 2:
We start with a full map where some parity measurements have been flipped to
1, indicating the presence of a bit flip error in some of our qubits or the parity
measurement itself.
The goal is to find the faulty qubits or parity measurement and correct them (by
using some interactive clics) to ensure all the parity measurements are back to 0.
And that's what will be considered a win.


## Game play 

In the Quantum world, h!


## How To Play

1. **Move the ball through the blocks. Each block represents a quantum gate.**
2. **Use the keypad to move through the hashi.**
3. **You must avoid the noise objects, otherwise, you’ll lose the game.**
4. [Watch the Gameplay/Walthrough](https://drive.google.com)


# How to Install
- Python & python libraries (as told is requirements.txt)
  - python version >= 3.11.4
  - pygame==2.5.2: ``` pip install pygame ```
  - pyyaml==6.0.1: ``` pip install pyyaml ```

If there is some MESA-LOADER error, please do what it says (here)[https://stackoverflow.com/questions/71010343/cannot-load-swrast-and-iris-drivers-in-fedora-35/72200748#72200748]: 

# Challenges Faced

Characterizing the player and conceptualizing the quantum world in a way that is easily interpretable.

- We es.
- Since there are no quantum games which were developed in hashi. We ran into a


# Software & Tools Used  


- Q
- Python


# Future Plans

1. The game can be adapted to a different Bell pair but that will require a
reinterpretation of the results of the parity measurements. This add some
unecessary complexity.
2. We could also consider the case of Phase Flip errors, it will not change the
principes of the game



# License

<a href="https://choosealicense.com/licenses/mit/"><img src="https://raw.githubusercontent.com/johnturner4004/readme-generator/master/src/components/assets/images/mit.svg" height=40 />MIT License</a>

# References

[_https://builtin.com/hardware/quantum-computer-games_](https://builtin.com/hardware/quantum-computer-games)

[_https://www.wilsoncenter.org/blog-post/games-round-quantum-computing_](https://www.wilsoncenter.org/blog-post/games-round-quantum-computing)

[_https://www.researchgate.net/publication/361022971_Defining_Quantum_Games_](https://www.researchgate.net/publication/361022971_Defining_Quantum_Games)

[_https://decodoku.medium.com/why-we-need-to-make-quantum-games-6f8c7bc4ace7_](https://decodoku.medium.com/why-we-need-to-make-quantum-games-6f8c7bc4ace7)

[_https://uwaterloo.ca/news/news/new-quantum-cats-game-launches-better-understanding-quantum_](https://uwaterloo.ca/news/news/new-quantum-cats-game-launches-better-understanding-quantum)

[_https://decodoku.medium.com/quantum-battleships-the-first-multiplayer-game-for-a-quantum-computer-e4d600ccb3f3_](https://decodoku.medium.com/quantum-battleships-the-first-multiplayer-game-for-a-quantum-computer-e4d600ccb3f3)


