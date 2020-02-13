#!/usr/bin/python3
#coding=utf-8


def gethistoryScoreFromDb():
    return 10000


class Game(object):
    history_top_score = gethistoryScoreFromDb()

    def __init__(self, player_name):
        self.player_name = player_name
        self.cur_score = 0

    @staticmethod
    def show_help():
        print("游戏帮助信息:游戏训练营")

    @classmethod
    def showHistoryTopScore(cls):
        print("history top score is %d " % cls.history_top_score)

    def startGame(self):
        self.cur_score = 0
        print("%s 即将进入游戏...." % self.player_name)


Game.show_help()
Game.showHistoryTopScore()

#xiaoming = Game("小明")
#xiaoming.startGame()
Game("小明000").startGame()

