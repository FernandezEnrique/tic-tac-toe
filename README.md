# TIC-TAC-TOE GAME
We have developed a TIC TAC TOE game with Python3 using Pygame. 

There are 2 modes, you can play locally against your friends or agains the computer.

<img src="https://github.com/FernandezEnrique/.github/blob/main/tic-tac-toe/menu.png" width="300"/>
<img src="https://github.com/FernandezEnrique/.github/blob/main/tic-tac-toe/Game-img.png" width="300"/>

# How to install it
First of all, clone it
```
git clone https://github.com/FernandezEnrique/tic-tac-toe.git
```
We need python3, it is using PyGame and Tkinter libraries so you need to install it, on Windows we will install it inside a virtual env.
```
virtualenv env
```
Once it is created, we activate it (Windows)
```
env/Scripts/activate
```
On linux (you may need to install PyGame locally)
```
source env/bin/activate
```
We have prepared a requirements.txt file that includes every single dependence.
```
pip3 install -r requirements.txt
```
And we simply run it
```
python3 main.py
```
