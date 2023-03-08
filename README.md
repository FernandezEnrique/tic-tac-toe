# TIC-TAC-TOE GAME
We have developed a TIC TAC TOE game with Python3 using Pygame. 

You can only play locally against your friend but in the future you might be able to play against CPU or even online.

![Screenshot of menu](https://github.com/FernandezEnrique/tic-tac-toe/blob/main/img/readme/menu.png?raw=true)
![Screenshot of game](https://github.com/FernandezEnrique/tic-tac-toe/blob/main/img/readme/Game-img.png?raw=true)

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
