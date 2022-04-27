import random
import pygame
from pygame import mixer
from tkinter import *
from tkinter import ttk
from time import strftime
import os
pygame.init()
pygame.mixer.init()



def computerChoice(self):
    my_list = ["0", "1", "2"]
    global compChoice
    global userChoice
    userChoice = 0

    compChoice = int(random.choice(my_list))
    # print(compChoice)


def destroy(self):

    self.rockButton.destroy()
    self.paperButton.destroy()
    self.scissorButton.destroy()
    self.backgroundLabel.destroy()


def create(self):

    self.rock_image = PhotoImage(file='gameIcon/rock.png')
    self.paper_image = PhotoImage(file='gameIcon/paper.png')
    self.scissor_image = PhotoImage(file='gameIcon/scissor.png')
    self.win_image = PhotoImage(file='gameIcon/win.png')
    self.lost_image = PhotoImage(file='gameIcon/lost.png')
    self.tied_image = PhotoImage(file='gameIcon/tied.png')
    self.background_image = PhotoImage(file='gameIcon/back.png')
    self.youWin_image = PhotoImage(file='gameIcon/youWin.png')
    self.compWin_image = PhotoImage(file='gameIcon/compWin.png')
    

    self.backgroundLabel = Label(self.bottom, image=self.background_image)
    self.backgroundLabel.place(x=0, y=0)

    self.rockButton = Button(
        self.bottom, image=self.rock_image, bg='#fcb52f', command=self.rock)
    self.rockButton.place(x=75, y=75)

    self.paperButton = Button(
        self.bottom, image=self.paper_image, bg='#fcb52f', command=self.paper)
    self.paperButton.place(x=275, y=75)

    self.scissorButton = Button(
        self.bottom, image=self.scissor_image, bg='#fcb52f', command=self.scissor)
    self.scissorButton.place(x=475, y=75)


def finalResult(self):

    if result == "w":
        destroy(self)

        self.result_image_label = Label(self.bottom, image=self.win_image)
        self.result_image_label.place(x=0, y=0)
        replace = image(self)
        self.message = Label(self.bottom, text="Congratulations you 'WON'",
                             font='arial 16 bold', background="black", foreground="cyan")
        self.message.place(x=225, y=250)
        self.userScore.destroy()
        self.userFinal += 1
        self.userScore = Label(self.bottom1, text=self.userFinal,
                               font='arial 12 bold', fg='#000000', bg='#ffffff')
        self.userScore.place(x=75, y=75)
        winSound = mixer.Sound('gameIcon/win.wav')
        winSound.play()

        if self.userFinal == 10:
            self.user_image_label.destroy()
            self.comp_image_label.destroy()
            self.message.destroy()
            self.result_image_label.destroy()

            self.result_image_label = Label(
                self.bottom, image=self.youWin_image)
            self.result_image_label.place(x=0, y=0)
            userWinSound = mixer.Sound('gameIcon/userWin.wav')
            userWinSound.play()

        else:
            self.userScore.after(2000, self.playAgain)

    elif result == "l":

        destroy(self)
        self.result_image_label = Label(self.bottom, image=self.lost_image)
        self.result_image_label.place(x=0, y=0)
        replace = image(self)
        self.message = Label(self.bottom, text="You 'LOST'",
                             font='arial 16 bold', background="black", foreground="cyan")
        self.message.place(x=290, y=250)
        self.compScore.destroy()
        self.compFinal += 1
        self.compScore = Label(self.bottom1, text=self.compFinal,
                               font='arial 12 bold', fg='#000000', bg='#ffffff')
        self.compScore.place(x=175, y=75)
        lostSound = mixer.Sound('gameIcon/lost.wav')
        lostSound.play()

        if self.compFinal == 10:
            self.user_image_label.destroy()
            self.comp_image_label.destroy()
            self.message.destroy()
            self.result_image_label.destroy()

            self.result_image_label = Label(
                self.bottom, image=self.compWin_image)
            self.result_image_label.place(x=0, y=0)
            compWinSound = mixer.Sound('gameIcon/compWin.wav')
            compWinSound.play()

        else:
            self.compScore.after(2000, self.playAgain)

    elif result == "d":
        destroy(self)
        self.result_image_label = Label(self.bottom, image=self.tied_image)
        self.result_image_label.place(x=0, y=0)
        replace = image(self)
        self.message = Label(self.bottom, text="Match tied",
                             font='arial 16 bold', background="black", foreground="cyan")
        self.message.place(x=275, y=250)
        tiedSound = mixer.Sound('gameIcon/tied.wav')
        tiedSound.play()
        self.message.after(2000, self.playAgain)


def image(self):
    self.user_image = self.imageSet.get(userChoice)
    self.comp_image = self.imageSet.get(compChoice)

    self.user_image = self.imageSet.get(userChoice)
    self.comp_image = self.imageSet.get(compChoice)
    # print(self.user_image)

    self.user_image_label = Label(self.bottom, image=self.user_image)
    self.user_image_label.place(x=100, y=75)

    self.comp_image_label = Label(self.bottom, image=self.comp_image)
    self.comp_image_label.place(x=500, y=75)


class Application(object):

    def __init__(self, master):

        self.userFinal = 0
        self.compFinal = 0

        # frames
        self.top = Frame(height=150, bg='#ffffff')
        self.top.pack(fill=X)

        self.bottom = Frame(height=300, bg='#00ffff')
        self.bottom.pack(fill=X)

        create(self)

        self.bottom1 = Frame(height=150, bg='#ffffff')
        self.bottom1.pack(fill=X)

        self.refreshButton = Button(
            self.bottom1, text="Refresh", bg='#fcb52f', command=self.refresh)
        self.refreshButton.place(x=475, y=75)
        self.playAgainButton = Button(
            self.bottom1, text="Play Again", bg='#fcb52f', command=self.playAgain)
        self.playAgainButton.place(x=475, y=25)

        self.infoLabel = Label(self.bottom1, text="First to win 10 matches wins the game",
                               font='arial 12 italic', fg='#000000', bg='#ffffff')
        self.infoLabel.place(x=15, y=5)

        self.userScoreLabel = Label(
            self.bottom1, text="Your Score", font='arial 12 bold', fg='#000000', bg='#ffffff')
        self.userScoreLabel.place(x=75, y=30)

        self.compScoreLabel = Label(
            self.bottom1, text="Computer Score", font='arial 12 bold', fg='#000000', bg='#ffffff')
        self.compScoreLabel.place(x=175, y=30)

        self.userScore = Label(self.bottom1, text=self.userFinal,
                               font='arial 12 bold', fg='#000000', bg='#ffffff')
        self.userScore.place(x=80, y=80)

        self.compScore = Label(self.bottom1, text=self.compFinal,
                               font='arial 12 bold', fg='#000000', bg='#ffffff')
        self.compScore.place(x=180, y=80)

        self.top_image = PhotoImage(file='gameIcon/logoRPS.png')
        self.top_image_label = Label(
            self.top, image=self.top_image, bg='#99ff33')
        self.top_image_label.place(x=0, y=0)

        computerChoice(self)

        self.imageSet = {
            0: self.rock_image,
            1: self.paper_image,
            2: self.scissor_image,
        }



    def rock(self):

        userChoice = 0
        r = ["d", "l", "w"]
        global result
        result = r[compChoice]
        final = finalResult(self)

    def paper(self):
        global userChoice

        userChoice = 1
        r = ["w", "d", "l"]
        global result
        result = r[compChoice]
        final = finalResult(self)

    def scissor(self):
        global userChoice

        userChoice = 2
        r = ["l", "w", "d"]
        global result
        result = r[compChoice]
        final = finalResult(self)

    def refresh(self):
        self.userFinal = 0
        self.compFinal = 0
        self.userScore.destroy()
        self.userScore = Label(self.bottom1, text=self.userFinal,
                               font='arial 12 bold', fg='#000000', bg='#ffffff')
        self.userScore.place(x=75, y=75)
        self.compScore.destroy()
        self.compScore = Label(self.bottom1, text=self.compFinal,
                               font='arial 12 bold', fg='#000000', bg='#ffffff')
        self.compScore.place(x=175, y=75)

    def playAgain(self):
        if self.userFinal == 10 or self.compFinal == 10:
            self.result_image_label.destroy()
            create(self)
            computerChoice(self)
            Application.refresh(self)
        else:
            self.user_image_label.destroy()
            self.comp_image_label.destroy()
            self.message.destroy()
            self.result_image_label.destroy()
            create(self)
            computerChoice(self)


def main():
    root = Tk()
    app = Application(root)

    root.title("Rock Paper Scissor")
    root.geometry('700x600')
    root.resizable(False, False)
    mixer.music.load('gameIcon/bg.wav')
    mixer.music.play(-1)

    root.mainloop()


if __name__ == '__main__':
    main()
