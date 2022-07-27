#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
import urandom
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile, Font
from array import *
import sys


while True:
 
 ev3 = EV3Brick()
 radius = 17     #радиус х и у
 poziciya = 1    #в каком клетке нахожусь
 x = 146         #начальная позиция а далее при перемешении меняется занчение переменной
 y = 105         #начальная позиция а далее при перемешении меняется занчение переменной
 russian_font = Font(size = 100, bold = True, lang = 'ru')
 x_font = Font(size = 30, bold = True)
 draw = 0 #ничья


 igrok_x = True  #ход делает игрок х

 x_one = False     #в клетке 1 произошел выбор (те записан х ) или нет
 x_two = False     #в клетке 2 произошел выбор (те записан х ) или нет
 x_three = False   #в клетке 3 произошел выбор (те записан х ) или нет ...
 x_four = False
 x_five = False
 x_six = False
 x_seven = False
 x_eight = False
 x_nine = False

 x_one_choice = False #если игрок записал х в первой клетке
 x_two_choice = False
 x_three_choice = False
 x_four_choice = False
 x_five_choice = False
 x_six_choice = False
 x_seven_choice = False
 x_eight_choice = False
 x_nine_choice = False


 igrok_y = False   #игрок У делает ход

 y_one = False     #в клетке 1 произошел выбор (те записан х ) или нет
 y_two = False     #в клетке 2 произошел выбор (те записан х ) или нет
 y_three = False   #в клетке 3 произошел выбор (те записан х ) или нет ...
 y_four = False
 y_five = False
 y_six = False
 y_seven = False
 y_eight = False
 y_nine = False

 y_one_choice = False #если игрок записал х в первой клетке
 y_two_choice = False
 y_three_choice = False
 y_four_choice = False
 y_five_choice = False
 y_six_choice = False
 y_seven_choice = False
 y_eight_choice = False
 y_nine_choice = False


 #реклама
 ev3.screen.clear()
 NauRobot_font = Font(size = 32, bold = True)
 ev3.screen.set_font(NauRobot_font)
 ev3.screen.draw_text(52, 25, ' Nau')
 ev3.screen.draw_text(42, 65, 'Robot')
 ev3.screen.draw_circle(90, 60, 80)
 ev3.screen.draw_circle(91, 60, 80)
 ev3.screen.draw_circle(92, 60, 80)
 ev3.screen.draw_circle(93, 60, 80) 
 ev3.speaker.play_file(SoundFile.MAGIC_WAND)
 while not Button.CENTER in (ev3.buttons.pressed()):
     pass
 ev3.speaker.play_file(SoundFile.CLICK)
 ev3.screen.clear()
 wait(300)


 while True:

     #начертить поле
     ev3.screen.draw_line(1, 1, 1, 126, width=5) 
     ev3.screen.draw_line(176, 1, 176, 126, width=5) 
     ev3.screen.draw_line(176, 1, 1, 1, width=5) 
     ev3.screen.draw_line(1, 126, 176, 126, width=5) 
     ev3.screen.draw_line(59, 1, 59, 126, width=5)
     ev3.screen.draw_line(116, 1, 116, 126, width=5) 
     ev3.screen.draw_line(1, 42, 176, 42, width=5) 
     ev3.screen.draw_line(1, 84, 176, 84, width=5)


     #листать по полю
     if Button.LEFT in(ev3.buttons.pressed()):
         poziciya += 1
         ev3.speaker.play_file(SoundFile.CLICK)
         ev3.screen.clear()
     if Button.RIGHT in(ev3.buttons.pressed()):
         poziciya -= 1  
         ev3.speaker.play_file(SoundFile.CLICK)
         ev3.screen.clear()
     if Button.UP in(ev3.buttons.pressed()):
         poziciya += 3  
         ev3.speaker.play_file(SoundFile.CLICK)
         ev3.screen.clear()  
     if Button.DOWN in(ev3.buttons.pressed()):
         poziciya -= 3  
         ev3.speaker.play_file(SoundFile.CLICK)
         ev3.screen.clear()  
 
     if poziciya == 1:
         #if x_one == False and y_one == False: #активировать если хочется чтобы после хода позиция перешла на свободную клетку
             x = 146
             y = 105
         #else:
           #  poziciya += 1
                  
     if poziciya == 2:
         #if x_two == False and y_two == False: 
             x = 88
             y = 105
         #else:
             #poziciya += 1

     if poziciya == 3:
         #if x_three == False and y_three == False: 
             x = 30
             y = 105
         #else:    
             #poziciya += 1
     
     if poziciya == 4:
         #if x_four == False and y_four == False: 
             x = 146
             y = 63
         #else:    
             #poziciya += 1

     if poziciya == 5:
         #if x_five == False and y_five == False: 
             x = 88
             y = 63
         #else:    
             #poziciya += 1

     if poziciya == 6:
         #if x_six == False and y_six == False: 
             x = 30
             y = 63
         #else:    
             #poziciya += 1

     if poziciya == 7:
         #if x_seven == False and y_seven == False: 
             x = 146
             y = 21
         #else:    
             #poziciya += 1

     if poziciya == 8:
         #if x_eight == False and y_eight == False: 
             x = 88
             y = 21
         #else:    
             #poziciya += 1

     if poziciya == 9:
         #if x_nine == False and y_nine == False: 
             x = 30
             y = 21
         #else:    
             #poziciya += 1

     if poziciya == 10:
         #if x_one == False and y_one == False: 
             x = 146
             y = 105 
             poziciya = 1
         #else:
             #poziciya += 1    

     if poziciya == 12:
         #if x_three == False and y_three == False: 
             x = 30
             y = 105         
             poziciya = 3
         #else:
             #poziciya += 1    

     if poziciya == 11:
         #if x_two == False and y_two == False: 
             x = 88
             y = 105
             poziciya = 2
         #else:
             #poziciya += 1    

     if poziciya == 0:
         #if x_nine == False and y_nine == False: 
             x = 30
             y = 21         
             poziciya = 9
         #else:
             #poziciya += 1    

     if poziciya == -2:
         #if x_seven == False and y_seven == False: 
             x = 146
             y = 21
             poziciya = 7
         #else:
             #poziciya += 1    

     if poziciya == -1:
         #if x_eight == False and y_eight == False: 
             x = 88
             y = 21         
             poziciya = 8
         #else:
             #poziciya += 1    


     ev3.screen.draw_circle(x, y, radius) #вывести на экран перемешение игроков


     #если (ход сделан) произошел выбор(те начертили х или у) в определенной клетке
     if Button.CENTER in(ev3.buttons.pressed()):
     
         ev3.speaker.beep()
         
         #если ход делал игрок Х:
         if igrok_x == True:        
             if poziciya == 1 and y_one == False and x_one == False:   #если игрок Х сделал ход в 1 клетке, и игрок У не сделал в этом клетке ход, и защита чтобы draw не увеличивался.
                 x_one = True         #истина - в первой клетке сделан ход
                 x_one_choice = True  #эта переменная использована вместо переменной poziciya чтобы сделанный ход после очистки экрана не исчезал
                 igrok_x = False       #игрок х уже сделал ход(те следующий ход делает игрок У)
                 igrok_y = True        #ход делает игрок У(типа активировали игрока У)
                 draw += 1 #ничья есил эта переменная станет 9
                 wait(400)
             if poziciya == 2 and y_two == False and x_two == False:
                 x_two = True
                 x_two_choice = True
                 igrok_x = False
                 igrok_y = True
                 draw += 1 #ничья есил эта переменная станет 9
                 wait(400)
             if poziciya == 3 and y_three == False and x_three == False:
                 x_three = True
                 x_three_choice = True
                 igrok_x = False
                 igrok_y = True
                 draw += 1 #ничья есил эта переменная станет 9
                 wait(400)
             if poziciya == 4 and y_four == False and x_four == False:
                 x_four = True
                 x_four_choice = True
                 igrok_x = False
                 igrok_y = True
                 draw += 1 #ничья есил эта переменная станет 9
                 wait(400)
             if poziciya == 5 and y_five == False and x_five == False:
                 x_five = True
                 x_five_choice = True
                 igrok_x = False
                 igrok_y = True
                 draw += 1 #ничья есил эта переменная станет 9
                 wait(400)
             if poziciya == 6 and y_six == False and x_six == False:
                 x_six = True
                 x_six_choice = True
                 igrok_x = False
                 igrok_y = True
                 draw += 1 #ничья есил эта переменная станет 9
                 wait(400)
             if poziciya == 7 and y_seven == False and x_seven == False:
                 x_seven = True
                 x_seven_choice = True
                 igrok_x = False
                 igrok_y = True
                 draw += 1 #ничья есил эта переменная станет 9
                 wait(400)
             if poziciya == 8 and y_eight == False and x_eight == False:
                 x_eight = True
                 x_eight_choice = True
                 igrok_x = False
                 igrok_y = True
                 draw += 1 #ничья есил эта переменная станет 9
                 wait(400)
             if poziciya == 9 and y_nine == False and x_nine == False:
                 x_nine = True
                 x_nine_choice = True
                 igrok_x = False
                 igrok_y = True
                 draw += 1 #ничья есил эта переменная станет 9
                 wait(400)
     
         #иначе ход сделал игрок У:
         else: 
             if poziciya == 1 and x_one == False and y_one == False:      #если игрок У сделал ход в 1 клетке, и игрок Х не сделал в этом клетке ход
                 y_one = True         #истина - в первой клетке сделан ход
                 y_one_choice = True  #эта переменная использована вместо переменной poziciya чтобы сделанный ход после очистки экрана не исчезал
                 igrok_y = False       #игрок y уже сделал ход(те следующий ход делает игрок x)
                 igrok_x = True      #ход делает игрок X(типа активировали игрока X)
                 draw += 1 #ничья есил эта переменная станет 9
                 wait(400)
             if poziciya == 2 and x_two == False and y_two == False:
                 y_two = True
                 y_two_choice = True
                 igrok_y = False
                 igrok_x = True
                 draw += 1 #ничья есил эта переменная станет 9
                 wait(400)
             if poziciya == 3 and x_three == False and y_three == False:
                 y_three = True
                 y_three_choice = True
                 igrok_y = False
                 igrok_x = True
                 draw += 1 #ничья есил эта переменная станет 9
                 wait(400)
             if poziciya == 4 and x_four == False and y_four == False:
                 y_four = True
                 y_four_choice = True
                 igrok_y = False
                 igrok_x = True
                 draw += 1 #ничья есил эта переменная станет 9
                 wait(400)
             if poziciya == 5 and x_five == False and y_five == False:
                 y_five = True
                 y_five_choice = True
                 igrok_y = False
                 igrok_x = True
                 draw += 1 #ничья есил эта переменная станет 9
                 wait(400)
             if poziciya == 6 and x_six == False and y_six == False:
                 y_six = True
                 y_six_choice = True
                 igrok_y = False
                 igrok_x = True
                 draw += 1 #ничья есил эта переменная станет 9
                 wait(400)
             if poziciya == 7 and x_seven == False and y_seven == False:
                 y_seven = True
                 y_seven_choice = True
                 igrok_y = False
                 igrok_x = True
                 draw += 1 #ничья есил эта переменная станет 9
                 wait(400)
             if poziciya == 8 and x_eight == False and y_eight == False:
                 y_eight = True
                 y_eight_choice = True
                 igrok_y = False
                 igrok_x = True
                 draw += 1 #ничья есил эта переменная станет 9
                 wait(400)
             if poziciya == 9 and x_nine == False and y_nine == False:
                 y_nine = True
                 y_nine_choice = True
                 igrok_y = False
                 igrok_x = True
                 draw += 1 #ничья есил эта переменная станет 9
                 wait(400)

         #ev3.screen.clear()    #активировать если хочется чтобы после хода позиция перешла на свободную клетку

     #ход сделал игрок Х
     if x_one_choice == True and x_one == True:     
         ev3.screen.set_font(x_font)
         ev3.screen.draw_text(136, 90, "X")
     if x_two_choice == True and x_two == True:     
         ev3.screen.set_font(x_font)
         ev3.screen.draw_text(78, 90, "X")
     if x_three_choice == True and x_three == True:     
         ev3.screen.set_font(x_font)
         ev3.screen.draw_text(20, 90, "X")
     if x_four_choice == True and x_four == True:     
         ev3.screen.set_font(x_font)
         ev3.screen.draw_text(136, 48, "X")
     if x_five_choice == True and x_five == True:     
         ev3.screen.set_font(x_font)
         ev3.screen.draw_text(78, 48, "X")
     if x_six_choice == True and x_six == True:     
         ev3.screen.set_font(x_font)
         ev3.screen.draw_text(20, 48, "X")
     if x_seven_choice == True and x_seven == True:     
         ev3.screen.set_font(x_font)
         ev3.screen.draw_text(136, 6, "X")
     if x_eight_choice == True and x_eight == True:     
         ev3.screen.set_font(x_font)
         ev3.screen.draw_text(78, 6, "X")
     if x_nine_choice == True and x_nine == True:     
         ev3.screen.set_font(x_font)
         ev3.screen.draw_text(20, 6, "X")
               

     #ход сделал игрок Y
     if y_one_choice == True and y_one == True:     
         ev3.screen.set_font(x_font)
         ev3.screen.draw_text(134, 90, "O")
     if y_two_choice == True and y_two == True:     
         ev3.screen.set_font(x_font)
         ev3.screen.draw_text(76, 90, "O")
     if y_three_choice == True and y_three == True:     
         ev3.screen.set_font(x_font)
         ev3.screen.draw_text(18, 90, "O")
     if y_four_choice == True and y_four == True:     
         ev3.screen.set_font(x_font)
         ev3.screen.draw_text(134, 48, "O")
     if y_five_choice == True and y_five == True:     
         ev3.screen.set_font(x_font)
         ev3.screen.draw_text(76, 48, "O")
     if y_six_choice == True and y_six == True:     
         ev3.screen.set_font(x_font)
         ev3.screen.draw_text(18, 48, "O")
     if y_seven_choice == True and y_seven == True:     
         ev3.screen.set_font(x_font)
         ev3.screen.draw_text(134, 6, "O")
     if y_eight_choice == True and y_eight == True:     
         ev3.screen.set_font(x_font)
         ev3.screen.draw_text(76, 6, "O")
     if y_nine_choice == True and y_nine == True:     
         ev3.screen.set_font(x_font)
         ev3.screen.draw_text(18, 6, "O")



     #вывод на экран победителя X
     if x_one == True and x_two == True and x_three == True:
         ev3.screen.draw_line(1, 104, 175, 105, width=10) 
         ev3.speaker.play_file(SoundFile.CHEERING)
         ev3.screen.clear()
         ev3.screen.set_font(russian_font)
         ev3.screen.draw_text(25, 30, ' Игрок - Х ',text_color = Color.WHITE,background_color = Color.BLACK)
         ev3.screen.draw_text(25, 70, '  ПОБЕДИЛ! ',text_color = Color.WHITE,background_color = Color.BLACK)
         while not Button.CENTER in(ev3.buttons.pressed()): #ждать пока не нажата центральная кнопка на мозге
             pass
         ev3.speaker.play_file(SoundFile.CLICK)
         break #выйти из цикла

     if x_one == True and x_five == True and x_nine == True:
         ev3.screen.draw_line(1, 1, 175, 125, width=10) 
         ev3.speaker.play_file(SoundFile.CHEERING)
         ev3.screen.clear()
         ev3.screen.set_font(russian_font)
         ev3.screen.draw_text(25, 30, ' Игрок - Х ',text_color = Color.WHITE,background_color = Color.BLACK)
         ev3.screen.draw_text(25, 70, '  ПОБЕДИЛ! ',text_color = Color.WHITE,background_color = Color.BLACK)
         while not Button.CENTER in(ev3.buttons.pressed()): #ждать пока не нажата центральная кнопка на мозге
             pass
         ev3.speaker.play_file(SoundFile.CLICK)
         break #выйти из цикла

     if x_four == True and x_five == True and x_six == True:
         ev3.screen.draw_line(1, 63, 175, 63, width=10) 
         ev3.speaker.play_file(SoundFile.CHEERING)
         ev3.screen.clear()
         ev3.screen.set_font(russian_font)
         ev3.screen.draw_text(25, 30, ' Игрок - Х ',text_color = Color.WHITE,background_color = Color.BLACK)
         ev3.screen.draw_text(25, 70, '  ПОБЕДИЛ! ',text_color = Color.WHITE,background_color = Color.BLACK)
         while not Button.CENTER in(ev3.buttons.pressed()): #ждать пока не нажата центральная кнопка на мозге
             pass
         ev3.speaker.play_file(SoundFile.CLICK)
         break #выйти из цикла

     if x_seven == True and x_eight == True and x_nine == True:
         ev3.screen.draw_line(1, 21, 175, 21, width=10) 
         ev3.speaker.play_file(SoundFile.CHEERING)
         ev3.screen.clear()
         ev3.screen.set_font(russian_font)
         ev3.screen.draw_text(25, 30, ' Игрок - Х ',text_color = Color.WHITE,background_color = Color.BLACK)
         ev3.screen.draw_text(25, 70, '  ПОБЕДИЛ! ',text_color = Color.WHITE,background_color = Color.BLACK)
         while not Button.CENTER in(ev3.buttons.pressed()): #ждать пока не нажата центральная кнопка на мозге
             pass
         ev3.speaker.play_file(SoundFile.CLICK)
         break #выйти из цикла

     if x_one == True and x_four == True and x_seven == True:
         ev3.screen.draw_line(145, 1, 145, 125, width=10) 
         ev3.speaker.play_file(SoundFile.CHEERING)
         ev3.screen.clear()
         ev3.screen.set_font(russian_font)
         ev3.screen.draw_text(25, 30, ' Игрок - Х ',text_color = Color.WHITE,background_color = Color.BLACK)
         ev3.screen.draw_text(25, 70, '  ПОБЕДИЛ! ',text_color = Color.WHITE,background_color = Color.BLACK)
         while not Button.CENTER in(ev3.buttons.pressed()): #ждать пока не нажата центральная кнопка на мозге
             pass
         ev3.speaker.play_file(SoundFile.CLICK)
         break #выйти из цикла
         
     if x_two == True and x_five == True and x_eight == True:
         ev3.screen.draw_line(87, 1, 87, 125, width=10) 
         ev3.speaker.play_file(SoundFile.CHEERING)
         ev3.screen.clear()
         ev3.screen.set_font(russian_font)
         ev3.screen.draw_text(25, 30, ' Игрок - Х ',text_color = Color.WHITE,background_color = Color.BLACK)
         ev3.screen.draw_text(25, 70, '  ПОБЕДИЛ! ',text_color = Color.WHITE,background_color = Color.BLACK)
         while not Button.CENTER in(ev3.buttons.pressed()): #ждать пока не нажата центральная кнопка на мозге
             pass
         ev3.speaker.play_file(SoundFile.CLICK)
         break #выйти из цикла

     if x_three == True and x_six == True and x_nine == True:
         ev3.screen.draw_line(30, 1, 30, 125, width=10) 
         ev3.speaker.play_file(SoundFile.CHEERING)
         ev3.screen.clear()
         ev3.screen.set_font(russian_font)
         ev3.screen.draw_text(25, 30, ' Игрок - Х ',text_color = Color.WHITE,background_color = Color.BLACK)
         ev3.screen.draw_text(25, 70, '  ПОБЕДИЛ! ',text_color = Color.WHITE,background_color = Color.BLACK)
         while not Button.CENTER in(ev3.buttons.pressed()): #ждать пока не нажата центральная кнопка на мозге
             pass
         ev3.speaker.play_file(SoundFile.CLICK)
         break #выйти из цикла

     if x_three == True and x_five == True and x_seven == True:
         ev3.screen.draw_line(1, 125, 175, 1, width=10) 
         ev3.speaker.play_file(SoundFile.CHEERING)
         ev3.screen.clear()
         ev3.screen.set_font(russian_font)
         ev3.screen.draw_text(25, 30, ' Игрок - Х ',text_color = Color.WHITE,background_color = Color.BLACK)
         ev3.screen.draw_text(25, 70, '  ПОБЕДИЛ! ',text_color = Color.WHITE,background_color = Color.BLACK)
         while not Button.CENTER in(ev3.buttons.pressed()): #ждать пока не нажата центральная кнопка на мозге
             pass
         ev3.speaker.play_file(SoundFile.CLICK)
         break #выйти из цикла
 
     #вывод на экран победителя Y
     if y_one == True and y_two == True and y_three == True:
         ev3.screen.draw_line(1, 104, 175, 105, width=10) 
         ev3.speaker.play_file(SoundFile.CHEERING)
         ev3.screen.clear()
         ev3.screen.set_font(russian_font)
         ev3.screen.draw_text(25, 30, ' Игрок - O ',text_color = Color.WHITE,background_color = Color.BLACK)
         ev3.screen.draw_text(25, 70, '  ПОБЕДИЛ! ',text_color = Color.WHITE,background_color = Color.BLACK)
         while not Button.CENTER in(ev3.buttons.pressed()): #ждать пока не нажата центральная кнопка на мозге
             pass
         ev3.speaker.play_file(SoundFile.CLICK)
         break #выйти из цикла

     if y_one == True and y_five == True and y_nine == True:
         ev3.screen.draw_line(1, 1, 175, 125, width=10) 
         ev3.speaker.play_file(SoundFile.CHEERING)
         ev3.screen.clear()
         ev3.screen.set_font(russian_font)
         ev3.screen.draw_text(25, 30, ' Игрок - O ',text_color = Color.WHITE,background_color = Color.BLACK)
         ev3.screen.draw_text(25, 70, '  ПОБЕДИЛ! ',text_color = Color.WHITE,background_color = Color.BLACK)
         while not Button.CENTER in(ev3.buttons.pressed()): #ждать пока не нажата центральная кнопка на мозге
             pass
         ev3.speaker.play_file(SoundFile.CLICK)
         break #выйти из цикла

     if y_four == True and y_five == True and y_six == True:
         ev3.screen.draw_line(1, 63, 175, 63, width=10) 
         ev3.speaker.play_file(SoundFile.CHEERING)
         ev3.screen.clear()
         ev3.screen.set_font(russian_font)
         ev3.screen.draw_text(25, 30, ' Игрок - O ',text_color = Color.WHITE,background_color = Color.BLACK)
         ev3.screen.draw_text(25, 70, '  ПОБЕДИЛ! ',text_color = Color.WHITE,background_color = Color.BLACK)
         while not Button.CENTER in(ev3.buttons.pressed()): #ждать пока не нажата центральная кнопка на мозге
             pass
         ev3.speaker.play_file(SoundFile.CLICK)
         break #выйти из цикла

     if y_seven == True and y_eight == True and y_nine == True:
         ev3.screen.draw_line(1, 21, 175, 21, width=10) 
         ev3.speaker.play_file(SoundFile.CHEERING)
         ev3.screen.clear()
         ev3.screen.set_font(russian_font)
         ev3.screen.draw_text(25, 30, ' Игрок - O ',text_color = Color.WHITE,background_color = Color.BLACK)
         ev3.screen.draw_text(25, 70, '  ПОБЕДИЛ! ',text_color = Color.WHITE,background_color = Color.BLACK)
         while not Button.CENTER in(ev3.buttons.pressed()): #ждать пока не нажата центральная кнопка на мозге
             pass
         ev3.speaker.play_file(SoundFile.CLICK)
         break #выйти из цикла

     if y_one == True and y_four == True and y_seven == True:
         ev3.screen.draw_line(145, 1, 145, 125, width=10) 
         ev3.speaker.play_file(SoundFile.CHEERING)
         ev3.screen.clear()
         ev3.screen.set_font(russian_font)
         ev3.screen.draw_text(25, 30, ' Игрок - O ',text_color = Color.WHITE,background_color = Color.BLACK)
         ev3.screen.draw_text(25, 70, '  ПОБЕДИЛ! ',text_color = Color.WHITE,background_color = Color.BLACK)
         while not Button.CENTER in(ev3.buttons.pressed()): #ждать пока не нажата центральная кнопка на мозге
             pass
         ev3.speaker.play_file(SoundFile.CLICK)
         break #выйти из цикла
         
     if y_two == True and y_five == True and y_eight == True:
         ev3.screen.draw_line(87, 1, 87, 125, width=10) 
         ev3.speaker.play_file(SoundFile.CHEERING)
         ev3.screen.clear()
         ev3.screen.set_font(russian_font)
         ev3.screen.draw_text(25, 30, ' Игрок - O ',text_color = Color.WHITE,background_color = Color.BLACK)
         ev3.screen.draw_text(25, 70, '  ПОБЕДИЛ! ',text_color = Color.WHITE,background_color = Color.BLACK)
         while not Button.CENTER in(ev3.buttons.pressed()): #ждать пока не нажата центральная кнопка на мозге
             pass
         ev3.speaker.play_file(SoundFile.CLICK)
         break #выйти из цикла

     if y_three == True and y_six == True and y_nine == True:
         ev3.screen.draw_line(30, 1, 30, 125, width=10) 
         ev3.speaker.play_file(SoundFile.CHEERING)
         ev3.screen.clear()
         ev3.screen.set_font(russian_font)
         ev3.screen.draw_text(25, 30, ' Игрок - O ',text_color = Color.WHITE,background_color = Color.BLACK)
         ev3.screen.draw_text(25, 70, '  ПОБЕДИЛ! ',text_color = Color.WHITE,background_color = Color.BLACK)
         while not Button.CENTER in(ev3.buttons.pressed()): #ждать пока не нажата центральная кнопка на мозге
             pass
         ev3.speaker.play_file(SoundFile.CLICK)
         break #выйти из цикла

     if y_three == True and y_five == True and y_seven == True:
         ev3.screen.draw_line(1, 125, 175, 1, width=10) 
         ev3.speaker.play_file(SoundFile.CHEERING)
         ev3.screen.clear()
         ev3.screen.set_font(russian_font)
         ev3.screen.draw_text(25, 30, ' Игрок - O ',text_color = Color.WHITE,background_color = Color.BLACK)
         ev3.screen.draw_text(25, 70, '  ПОБЕДИЛ! ',text_color = Color.WHITE,background_color = Color.BLACK)
         while not Button.CENTER in(ev3.buttons.pressed()): #ждать пока не нажата центральная кнопка на мозге
             pass
         ev3.speaker.play_file(SoundFile.CLICK)
         break #выйти из цикла
 
     if draw == 9: #если ничья
         ev3.speaker.play_file(SoundFile.BOING)
         ev3.screen.clear()
         ev3.screen.set_font(russian_font)
         ev3.screen.draw_text(50, 50, ' Ничья ',text_color = Color.WHITE,background_color = Color.BLACK)
         while not Button.CENTER in(ev3.buttons.pressed()): #ждать пока не нажата центральная кнопка на мозге
             pass
         ev3.speaker.play_file(SoundFile.CLICK)
         break #выйти из цикла
 
 
 wait(500)
 ev3.screen.clear()
 ev3.screen.set_font(russian_font)
 ev3.screen.draw_text(40, 50, ' Еще раз ')

 while not Button.CENTER in(ev3.buttons.pressed()): 
     pass                                           #ничего не делать пока не нажата центральная кнопка на мозге
     if Button.LEFT in(ev3.buttons.pressed()):
         sys.exit() #вырубить всю программу
 
 ev3.speaker.play_file(SoundFile.CLICK)

    
    