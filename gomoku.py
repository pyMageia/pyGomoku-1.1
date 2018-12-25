# empty :
# black : 1
# white : 2
### GOMOKU 2P (CUI) BY BYEONGHYUN PARK
### Version 1.1

sourcecode = 'https://github.com/pyMageia/pyGomoku-1.1'
print('Anytime type in #S for source code and #R for rule. ')


class Gomoku:
    def __init__(self):
        self.progress = 0
        self.winner = None
        self.isEndGame = None
        self.x_data = list()
        pass

    def reset(self):
        self.x_data = ['null']
        for times in range(0, 225):
            self.x_data.append(0)  # 225 0's in x_data list
        self.display()

    def display(self):
        """2x for loops"""
        total_xRef = str()
        total_x_data = str()
        yRef = 0
        for xRef in range(1, 16, 1):
            if xRef <= 10:
                total_xRef = total_xRef + ' '*3 + str(xRef)  # Generate Strings
            else:
                total_xRef = total_xRef + ' '*2 + str(xRef)  # because over 10, 2 spaces are needed
        print('\n\n')  # 2 blank rows
        print(total_xRef)  # print 1st row
        count = 0
        for value in range(1, 226):
            if count != 15 and yRef <= 14:
                total_x_data += str(self.x_data[value]) + ' ' * 3
                count += 1
            if count == 15 and yRef <= 14:
                yRef += 1
                if yRef <= 9:
                    print(str(yRef) + ' '*2 + total_x_data)
                elif yRef >= 10:
                    print(str(yRef) + ' ' + total_x_data)
                total_x_data = str()
                count = 0

    def play(self):
        self.isEndGame = 0
        self.errorcode = ''
        while self.isEndGame == 0:
            self.progress += 1
            if self.progress % 2 == 1:  ## Black start
                isInputOK = False
                while isInputOK == False:
                    blackRawInput = str(input('Please type in your selection as Black. Input example: 6, 9\n'))
                    # rule or sourcecode?
                    if blackRawInput == '#S':
                        print(sourcecode)
                        blackRawInput = str(input('Please type in your selection as Black. Input example: 6, 9\n'))
                    elif blackRawInput == '#R':
                        print("""
                        ##### Rule ##### \n\n
                        <BASICS>\n
                        - Input Should be 2 numbers between 1 and 15, separated by comma (,).\n
                        - Location should be in (1, 1) and (15, 15) range. \n
                        - You can't place stone on already selected positions. \n
                        <Renju RULES>\n
                        - Black starts first. (Therefore, it will get penalties)
                        - This program runs under Renju Rule, a national rule of Gomoku.\n
                        - Black Can't make multiple sangoku(3-stone row) at one time. \n
                        - Black Can't make a longer row than gomoku. Ex) Rokugoku, Nanagoku, Hachigoku, Kyugoku (6~9-stone row) \n
                        - Black may make multiple Sangokus if they're made continuously, one by one. \n
                        - White has no limitations.
                        * It is known that Renju rule has 58% winrate for Black. However, without Renju Rule, black has 80% of winrate. \n
                        Have Fun!
                        """)
                        blackRawInput = str(input('Please type in your selection as Black. Input example: 6, 9\n'))
                    else:
                        pass
                    try:
                        blackInput = blackRawInput.replace(' ', '').split(',')
                        check = int(blackInput[0]) * int(blackInput[1])
                        if len(blackInput) != 2:
                            self.errorcode = 'A- Not 2 numbers separated by one comma'
                            raise ValueError()
                        if not (1 <= int(blackInput[0]) <= 15) or not (1 <= int(blackInput[1]) <= 15):
                            self.errorcode = 'B- The location is not in the range between 1 and 15'
                            raise ValueError()
                        # Location ensuring - tasks are done here already
                        location = (int(blackInput[1]) - 1) * 15 + int(blackInput[0])
                        #33, 44, 6moku restriction
                        #6moku restriction



                        """6moku restrictin start"""
                        # X 6 Checking Algorithm
                        self.x_data[location] = 1  # temporary
                        for y in range(1, 16, 1):
                            for x in range(1, 11, 1):
                                loc_pointer = (y - 1) * 15 + x
                                if self.x_data[loc_pointer] != 0:  # doesnt count 0's.
                                    if self.x_data[loc_pointer] == self.x_data[loc_pointer + 1] == self.x_data[
                                        loc_pointer + 2] == \
                                            self.x_data[loc_pointer + 3] == self.x_data[loc_pointer + 4] == self.x_data[loc_pointer + 5]:
                                        self.errorcode = 'violating Rokumoku rule as black'
                                        self.x_data[location] = 0  # restoring
                                        raise ValueError()
                        # Y 6 Checking Algorithm
                        for y in range(1, 11, 1):
                            for x in range(1, 16, 1):
                                loc_pointer = (y - 1) * 15 + x
                                if self.x_data[loc_pointer] != 0:  # doesnt count 0's.
                                    if self.x_data[loc_pointer] == self.x_data[loc_pointer + 15] == self.x_data[
                                        loc_pointer + 30] == \
                                            self.x_data[loc_pointer + 45] == self.x_data[loc_pointer + 60] == self.x_data[loc_pointer + 75]:
                                        self.errorcode = 'violating Rokumoku rule as black'
                                        self.x_data[location] = 0  # restoring
                                        raise ValueError()
                        # Diagonal (\) 6 Checking Algorithm
                        for y in range(1, 11, 1):
                            for x in range(1, 11, 1):
                                loc_pointer = (y - 1) * 15 + x
                                if self.x_data[loc_pointer] != 0:  # doesnt count 0's.
                                    if self.x_data[loc_pointer] == self.x_data[loc_pointer + 16] == self.x_data[
                                        loc_pointer + 32] == \
                                            self.x_data[loc_pointer + 48] == self.x_data[loc_pointer + 64] == self.x_data[loc_pointer + 80]:
                                        self.errorcode = 'violating Rokumoku rule as black'
                                        self.x_data[location] = 0  # restoring
                                        raise ValueError()
                        # Diagonal (/) 6 Checking Algorithm
                        for y in range(1, 11, 1):
                            for x in range(6, 16, 1):
                                loc_pointer = (y - 1) * 15 + x
                                if self.x_data[loc_pointer] != 0:  # doesnt count 0's.
                                    if self.x_data[loc_pointer] == self.x_data[loc_pointer + 14] == self.x_data[
                                        loc_pointer + 28] == \
                                            self.x_data[loc_pointer + 42] == self.x_data[loc_pointer + 56] == self.x_data[loc_pointer + 70]:
                                        self.errorcode = 'violating Rokumoku rule as black'
                                        self.x_data[location] = 0  # restoring
                                        raise ValueError()
                        self.x_data[location] = 0  # restoring
                        """6moku restriction end"""

                        """3x3 restriction start"""
                        trigger = False
                        self.x_data[location] = 1

                        y = int(blackInput[1])
                        x = int(blackInput[0])
                        loc_pointer = (y - 1) * 15 + x
                        determiner = 0
                        '''plus'''
                        # right side
                        if self.x_data[loc_pointer] == self.x_data[loc_pointer + 1] == self.x_data[loc_pointer + 2]:
                            determiner += 1
                        # down right side
                        if self.x_data[loc_pointer] == self.x_data[loc_pointer + 16] == self.x_data[loc_pointer + 32]:
                            determiner += 10
                        # down side
                        if self.x_data[loc_pointer] == self.x_data[loc_pointer + 15] == self.x_data[loc_pointer + 30]:
                            determiner += 100
                        # down left side
                        if self.x_data[loc_pointer] == self.x_data[loc_pointer + 14] == self.x_data[loc_pointer + 28]:
                            determiner += 1000

                        '''minus'''
                        # left side
                        if self.x_data[loc_pointer] == self.x_data[loc_pointer - 1] == self.x_data[loc_pointer - 2]:
                            determiner -= 1
                        # up left side
                        if self.x_data[loc_pointer] == self.x_data[loc_pointer - 16] == self.x_data[loc_pointer - 32]:
                            determiner -= 10
                        # up side
                        if self.x_data[loc_pointer] == self.x_data[loc_pointer - 15] == self.x_data[loc_pointer - 30]:
                            determiner -= 100
                        # up right side
                        if self.x_data[loc_pointer] == self.x_data[loc_pointer - 14] == self.x_data[loc_pointer - 28]:
                            determiner -= 1000

                        # print(determiner, loc_pointer) ##### Debugging
                        whitelist = [0, 1, 10, 100, 1000, -1, -10, -100, -1000]  # whitelist of possible legal 3's
                        if determiner in whitelist:
                            trigger = False
                        else:
                            trigger = True


                        # final raising
                        if trigger == False:
                            pass
                        if trigger == True:
                            # 4-3 allowing
                            trigger43 = 0
                            if self.x_data[loc_pointer - 1] == 1:
                                trigger43 += 100
                                if self.x_data[loc_pointer - 2] == 1:
                                    trigger43 += 10
                                    if self.x_data[loc_pointer - 3] == 1:
                                        trigger43 += 1
                            if self.x_data[loc_pointer + 1] == 1:
                                trigger43 += 100
                                if self.x_data[loc_pointer + 2] == 1:
                                    trigger43 += 10
                                    if self.x_data[loc_pointer + 3] == 1:
                                        trigger43 += 1
                            if self.x_data[loc_pointer + 15] == 1:
                                trigger43 += 100
                                if self.x_data[loc_pointer - 30] ==1:
                                    trigger43 += 10
                                    if self.x_data[loc_pointer - 45] == 1:
                                        trigger43 += 1
                            if self.x_data[loc_pointer - 15] == 1:
                                trigger43 += 100
                                if self.x_data[loc_pointer - 30] == 1:
                                    trigger43 += 10
                                    if self.x_data[loc_pointer - 45] == 1:
                                        trigger43 += 1
                            if self.x_data[loc_pointer - 16] == 1:
                                trigger43 += 100
                                if self.x_data[loc_pointer - 32] == 1:
                                    trigger43 += 10
                                    if self.x_data[loc_pointer - 48] == 1:
                                        trigger43 += 1
                            if self.x_data[loc_pointer + 16] == 1:
                                trigger43 += 100
                                if self.x_data[loc_pointer + 32] == 1:
                                    trigger43 += 10
                                    if self.x_data[loc_pointer + 48] == 1:
                                        trigger43 += 1
                            if self.x_data[loc_pointer - 15] == 1:
                                trigger43 += 100
                                if self.x_data[loc_pointer - 30] == 1:
                                    trigger43 += 10
                                    if self.x_data[loc_pointer - 45] == 1:
                                        trigger43 += 1
                            if self.x_data[loc_pointer + 15] == 1:
                                trigger43 += 100
                                if self.x_data[loc_pointer + 30] == 1:
                                    trigger43 += 10
                                    if self.x_data[loc_pointer + 45] == 1:
                                        trigger43 += 1
                            blacklist = [220, 330, 440, 222, 333, 444]

                            if trigger43 in blacklist:
                                self.errorcode = 'Violating 3-3 or 4-4 rule as black.'
                                self.x_data[location] = 0  # restoring
                                raise ValueError()
                            if trigger43 not in blacklist:
                                pass
                        self.x_data[location] = 0  # restoring
                        """3x3 restriction end"""

                        if self.x_data[location] == 0:
                            self.x_data[location] = 1  # setting the location as '1' value, which is black
                        elif self.x_data[location] != 0:
                            self.errorcode = 'C- The location is already used'
                            raise ValueError()
                    except:
                        print('Not a good input! Errorcode: {0}'.format(self.errorcode))
                    else:  # Good Input
                        print("Black's Input: {0}, {1}".format(blackInput[0], blackInput[1]))
                        isInputOK = True
                        gomo.display()

            elif self.progress % 2 == 0:  # WHITE
                isInputOK = False
                while isInputOK == False:
                    whiteRawInput = str(input('Please type in your selection as White. Input example: 7, 12'))
                    # rule or sourcecode?
                    if whiteRawInput == '#S':
                        print(sourcecode)
                        whiteRawInput = str(input('Please type in your selection as Black. Input example: 6, 9\n'))
                    elif whiteRawInput == '#R':
                        print("""
                        ##### Rule ##### \n\n
                        <BASICS>\n
                        - Input Should be 2 numbers between 1 and 15, separated by comma (,).\n
                        - Location should be in (1, 1) and (15, 15) range. \n
                        - You can't place stone on already selected positions. \n
                        <Renju RULES>\n
                        - Black starts first. (Therefore, it will get penalties)
                        - This program runs under Renju Rule, a national rule of Gomoku.\n
                        - Black Can't make multiple sangoku(3-stone row) at one time. \n
                        - Black Can't make a longer row than gomoku. Ex) Rokugoku, Nanagoku, Hachigoku, Kyugoku (6~9-stone row) \n
                        - Black may make multiple Sangokus if they're made continuously, one by one. \n
                        - White has no limitations.
                        * It is known that Renju rule has 58% winrate for Black. However, without Renju Rule, black has 80% of winrate. \n
                        Have Fun!
                        """)
                        whiteRawInput = str(input('Please type in your selection as Black. Input example: 6, 9\n'))
                    try:
                        whiteInput = whiteRawInput.replace(' ', '').split(',')
                        check = int(whiteInput[0]) * int(whiteInput[1])
                        if len(whiteInput) != 2:
                            self.errorcode = 'A- Not 2 numbers separated by one comma'
                            raise ValueError()
                        if not (1 <= int(whiteInput[0]) <= 15) or not (1 <= int(whiteInput[1]) <= 15):
                            self.errorcode = 'B- The location is not in the range between 1 and 15'
                            raise ValueError()
                        # Location ensuring - tasks are done here already
                        location = (int(whiteInput[1]) - 1) * 15 + int(whiteInput[0])
                        if self.x_data[location] == 0:
                            self.x_data[location] = 2  # setting the location as '2' value, which is white
                        elif self.x_data[location] != 0:
                            self.errorcode = 'C- The location is already used'
                            raise ValueError()
                    except:
                        print('Not a good input!')
                    else:
                        print("White's Input: {0}, {1}".format(whiteInput[0], whiteInput[1]))
                        isInputOK = True
                        gomo.display()
            self.isEndGame = gomo.winCheck()
        else:
            gomo.endGame()

    def winCheck(self):
        # X Win Checking Algorithm
        for y in range(1, 16, 1):
            for x in range(1, 12, 1):
                loc_pointer = (y - 1) * 15 + x
                if self.x_data[loc_pointer] != 0:  # doesnt count 0's.
                    if self.x_data[loc_pointer] == self.x_data[loc_pointer+1] == self.x_data[loc_pointer+2] ==\
                      self.x_data[loc_pointer+3] == self.x_data[loc_pointer+4]:
                        return self.x_data[loc_pointer]
        # Y Win Checking Algorithm
        for y in range(1, 12, 1):
            for x in range(1, 16, 1):
                loc_pointer = (y - 1) * 15 + x
                if self.x_data[loc_pointer] != 0:  # doesnt count 0's.
                    if self.x_data[loc_pointer] == self.x_data[loc_pointer+15] == self.x_data[loc_pointer+30] ==\
                      self.x_data[loc_pointer+45] == self.x_data[loc_pointer+60]:
                        return self.x_data[loc_pointer]
        # Diagonal (\) Win Checking Algorithm
        for y in range(1, 12, 1):
            for x in range(1, 12, 1):
                loc_pointer = (y - 1) * 15 + x
                if self.x_data[loc_pointer] != 0:  # doesnt count 0's.
                    if self.x_data[loc_pointer] == self.x_data[loc_pointer+16] == self.x_data[loc_pointer+32] ==\
                      self.x_data[loc_pointer+48] == self.x_data[loc_pointer+64]:
                        return self.x_data[loc_pointer]
        # Diagonal (/) Win Checking Algorithm
        for y in range(1, 12, 1):
            for x in range(5, 16, 1):
                loc_pointer = (y - 1) * 15 + x
                if self.x_data[loc_pointer] != 0:  # doesnt count 0's.
                    if self.x_data[loc_pointer] == self.x_data[loc_pointer+14] == self.x_data[loc_pointer+28] ==\
                      self.x_data[loc_pointer+42] == self.x_data[loc_pointer+56]:
                        return self.x_data[loc_pointer]
        else:
            return 0  # 0 means blank here!

    def endGame(self):
        if self.isEndGame == 1:
            print('Black Wins!')
            input('Press enter to Exit')
        elif self.isEndGame == 2:
            print('White Wins!')
            input('Press enter to Exit')


gomo = Gomoku()
gomo.reset()
gomo.play()
