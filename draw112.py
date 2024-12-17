from cmu_graphics import *
import random
import pyautogui
import os
import pyttsx3

# variables defined 
def onAppStart(app):
    # CITATION: Microsoft Copilot was used for debugging purposes - I asked it about specific errors.
    # CITATION: Microsoft Copilot taught me how to use pyautogui to make popup boxes
    # as well as how to take a screenshot of the page and save it to a file location and also how to do the tect to voice conversion
    # CITATION: I refered to the app Microsoft Paint for functionality ideas, as well as a previous term project called '2D CAD' by Alisha Patel
    # CITATION: I refered to the following pdf link to find colorblind friendly colors:
    # https://www.nceas.ucsb.edu/sites/default/files/2022-06/Colorblind%20Safe%20Color%20Schemes.pdf

    # TITLE SCREEN
    app.titleScreen = True

    # TEMPS
    app.drawTemp = False
    # Temp Rectangles
    app.tempCoordinateX = 0
    app.tempCoordinateY = 0
    app.tempWidth = 0
    app.tempHeight = 0
    # Temp Circles
    app.tempRadius = 0
    # Temp Line
    app.drawTemp = False
    app.tempLine = []

    # SHAPES
    # Rectangle
    app.drawRect = False
    app.coordinatesTopCorner = []
    app.coordinatesBottomCorner = []
    app.pastRects = []
    app.rectHeight = 0
    app.rectWidth = 0
    # Circle
    app.drawCircle = False
    app.coordinatesCenter = []
    app.circleRadius = []
    app.radius = 0
    app.pastCircles = []
    # Regular Polygon
    app.drawRegularPolygon = False
    app.pastRegPoly = []
    app.polyRadius = []
    app.numberSides = 0
    # Straight Line
    app.drawLine = False
    app.coordinatesFirstPoint = []
    app.coordinatesSecondPoint = []
    app.pastLines = []
    # Curved Line
    app.drawCurvedLines = False
    app.lineCircleCenters = []
    app.pastCurvedLines = []
    app.lastMouseX = None
    app.lastMouseY = None
    app.thickness = 1

    # COLOR
    app.color = 'black'
    app.colorblindMode = False

    # BOLDNESS
    app.boldnessSlider = False
    app.boldness = 1
    app.sliderX = 0

    # INSTRUCTIONS (BEGINNING)
    app.instructions = False

    # GAME MODE
    app.word = ''
    app.drawingFreeze = False
    app.gameInstructions = None
    app.gameMode = False
    app.stepsPerSecond = 1
    app.counter = 0
    app.drawingList = ['cat', 'hat', 'house', 'dog', 'car', 'pizza', 'watermelon', 'strawberry', 'lemon', 'pants', 'shirt', 'potato', 'tree', 'apple', 'rice', 'igloo']
    app.easy = ['cat', 'hat', 'house', 'dog', 'car', 'pizza', 'watermelon', 'strawberry', 'lemon', 'pants', 'shirt', 'potato', 'tree', 'apple', 'rice', 'igloo']
    app.medium = ['condensation', 'microwave', 'robot', 'cemetary', 'hospital', 'limousine', 'brain', 'octopus', 'dinosaur', 'chicken', 'chopsticks']
    app.hard = ['entropy', 'pharmacist', 'psychologist', 'blacksmith', 'philosopher', 'neutron', 'microscope', 'cheerleader', 'archaeologist', 'cartographer']
    app.displayLetters = ''
    app.displayWarning = False
    app.displayWord = False
    app.displayOk = False
    app.displayStart = False
    app.index = 0
    app.singleWord = 0
    app.guessMode = False
    app.guess = ''
    app.winner = False
    app.restart = False
    app.exitGame = False
    app.tryAgain = False
    app.timer = 60
    app.gameOver = False
    app.guessCount = 0
    app.wordCount = 0

    # ERASER
    app.eraser = False

    # UNDO SHAPE
    app.undoShape = False

    # UNDO LAST
    app.undoLast = False

    # MASTER LIST
    app.masterList = []
    app.shape = []

    # READ ALOUD
    app.readAloud = False

# drawing begins 
def redrawAll(app):
    if app.titleScreen == True: # title screen
        drawRect(0,  0, app.width, app.height, fill = 'mediumblue')
        drawLabel("Draw 112!", app.width/2, app.height/2, fill = 'white', align = 'center', font = 'montserrat', size = app.height/5)
        drawRect(app.width/2, app.height/2 + 150, app.width/5, app.height/10, fill = 'white', align = 'center')
        drawLabel("Let's Draw!", app.width/2, (app.height/2)+150, align = 'center', font = 'montserrat', size = app.height/30, fill = 'orange', bold = True, italic = True)
    elif app.instructions == True: # instructions screen
        drawInstructions(app)
    else:
        pastDrawings(app)
        currentDrawings(app)
        buttonDrawings(app)
    gameModeDrawings(app)

# helper to draw instructions page 
def drawInstructions(app):
    popupPageColors = ['mediumBlue', 'red']
    if app.colorblindMode == True:
        popupPageColors = [rgb(46, 37, 133), rgb(126, 41, 84)]
    drawRect(0, 0, app.width, app.height, fill=popupPageColors[0])
    
    instructions = [
        "Welcome to Draw 112 - The Newest Artist Palette and Game!",
        "Keyboard Shortcuts are used to draw Shapes, as well as carry out other commands.",
        "Please press 'q' at any time to see all Keyboard Shortcuts.",
        "",
        "In order to draw a shape, one must first select the Thickness and Color",
        "and then select the key corresponding to the shape or line you want to draw.",
        "",
        "The 'RGB' Button allows users to choose colors that are not default options.",
        "Simply press the 'RGB' Button and follow the popup prompt on the screen.",
        "",
        "The 'Choose' Button allows users to choose line thicknesses that are not default options.",
        "Simply press the 'Choose' Button, use the slider to select a thickness and then hit the 'enter' key to lock it in.",
        "",
        "The 'Eraser' Button will erase when the user clicks the button and then drags the mouse across the screen.",
        "",
        "The 'Clear' Button will clear the entire screen.",
        "",
        "The 'Delete' Button will allow the user to select a shape type and then delete the most recently drawn version of that type.",
        "",
        "The 'Undo' Button will undo the last thing the user drew/erased.",
        "",
        "The 'Save Img' Button saves a png screenshot of the page to the user's Downloads.",
        "",
        "Pressing 'g' will activate Game Mode and instructions will be explained upon activation."
    ]

    yPosition = app.height / 12

    drawLabel(instructions[0], app.width/2, yPosition, fill='white', align='center', font='montserrat', size=app.height/20, bold=True)
    yPosition += app.height/10

    for instruction in instructions[1:]:
        drawLabel(instruction, app.width/2, yPosition, fill='white', align='center', font='montserrat', size=app.height/30)
        yPosition += app.height/30

    drawRect(0,  0, app.width/15, app.height/20, fill = popupPageColors[1], border = 'black')
    drawLabel("EXIT", app.width/30, app.height/40, fill = 'white', align = 'center', size = app.height/35)
    drawRect(app.width/15,  0, app.width/15*2, app.height/20, fill = 'white', border = 'black') 
    drawLabel("Click for Read Aloud!", app.width/30*4, app.height/40, fill = 'black', align = 'center', size = app.height/50)

# helper to draw past shapes
def pastDrawings(app):
    # RECTANGLE
    # draw past rectangles
    for rect in app.pastRects:
        drawRect(rect[1], rect[2], rect[3], rect[4], border=rect[5], fill = None, borderWidth = rect[6])

    # CIRCLE
    # draw past circles
    for circle in app.pastCircles:
        drawCircle(circle[1], circle[2], circle[3], border=circle[4], borderWidth=circle[5], fill = None)

    # REGULAR POLYGON
    # draw past regular polygons
    for regPoly in app.pastRegPoly:
        drawRegularPolygon(regPoly[1], regPoly[2], regPoly[3], regPoly[4], border = regPoly[5], borderWidth = regPoly[6], fill=None)

    # STRAIGHT LINE
    # draw past lines
    for line in app.pastLines:
        drawLine(line[1], line[2], line[3], line[4], fill = line[5], lineWidth = line[6]) 

    # CURVED LINES
    # draw past curved lines
    for lineSegments in app.pastCurvedLines:
        for i in range(1, len(lineSegments)): # draw circles and then connect the centers w a line 
            drawLine(lineSegments[i-1][0], lineSegments[i-1][1], lineSegments[i][0], lineSegments[i][1], fill = lineSegments[i][2], lineWidth = lineSegments[i][4])
            drawCircle(lineSegments[i][0], lineSegments[i][1], lineSegments[i][3], fill = lineSegments[i][2])

    # for order of drawings
    for sublists in app.masterList:
        if sublists[0] == 'Rectangle':
            drawRect(sublists[1], sublists[2], sublists[3], sublists[4], border=sublists[5], fill = None, borderWidth = sublists[6])
        elif sublists[0] == 'Circle':
            drawCircle(sublists[1], sublists[2], sublists[3], border=sublists[4], borderWidth=sublists[5], fill = None)
        elif sublists[0] == 'Regular Polygon':
            drawRegularPolygon(sublists[1], sublists[2], sublists[3], sublists[4], border = sublists[5], borderWidth = sublists[6], fill=None)
        elif sublists[0] == 'Line':
            drawLine(sublists[1], sublists[2], sublists[3], sublists[4], fill = sublists[5], lineWidth = sublists[6]) 
        else:
            for i in range(1, len(sublists)): # draw circles and then connect the centers w a line 
                drawLine(sublists[i-1][0], sublists[i-1][1], sublists[i][0], sublists[i][1], fill = sublists[i][2], lineWidth = sublists[i][4])
                drawCircle(sublists[i][0], sublists[i][1], sublists[i][3], fill = sublists[i][2])

# helper to draw current shape
def currentDrawings(app):
    # RECTANGLE
    # draw current rectangle
    if app.drawRect and len(app.coordinatesTopCorner) == 2 and len(app.coordinatesBottomCorner) == 0:
        drawCircle(app.coordinatesTopCorner[0], app.coordinatesTopCorner[1], 4, fill = app.color)
    if app.drawTemp and app.drawRect:
        drawRect(app.tempCoordinateX, app.tempCoordinateY, app.tempWidth, app.tempHeight, border=app.color, fill = None, borderWidth = app.thickness)
    if app.drawRect and len(app.coordinatesTopCorner) == 2 and len(app.coordinatesBottomCorner) == 2:
        drawRect(app.coordinatesTopCorner[0], app.coordinatesTopCorner[1], app.rectWidth, app.rectHeight, border = app.color, fill = None, borderWidth = app.thickness)

    # CIRCLE
    # draw current circle
    if app.drawCircle and len(app.coordinatesCenter) == 2 and len(app.circleRadius) == 0:
        drawCircle(app.coordinatesCenter[0], app.coordinatesCenter[1], 4, fill = app.color, borderWidth = app.thickness)
    if app.drawTemp and app.drawCircle and len(app.coordinatesCenter) == 2 and app.tempRadius > 0:
        drawCircle(app.coordinatesCenter[0], app.coordinatesCenter[1], app.tempRadius, border = app.color, fill = None, borderWidth = app.thickness)

    # REGULAR POLYGON
    # draw current reg polygon
    if app.drawRegularPolygon and len(app.coordinatesCenter) == 2 and len(app.polyRadius) == 0:
        drawCircle(app.coordinatesCenter[0], app.coordinatesCenter[1], 4, fill=app.color)
    if app.drawTemp and app.drawRegularPolygon and len(app.coordinatesCenter) == 2 and app.tempRadius > 0:
        drawRegularPolygon(app.coordinatesCenter[0], app.coordinatesCenter[1], app.tempRadius, app.numberSides, border = app.color, fill=None, borderWidth = app.thickness)

    # STRAIGHT LINE
    # draw current straight line
    if app.drawLine == True and len(app.coordinatesFirstPoint) == 2 and len(app.coordinatesSecondPoint) == 0:
        drawCircle(app.coordinatesFirstPoint[0], app.coordinatesFirstPoint[1], 4, fill = app.color)
    if app.drawLine == True and len(app.coordinatesFirstPoint) == 2 and len(app.coordinatesSecondPoint) == 2:
        drawLine(app.coordinatesFirstPoint[0], app.coordinatesFirstPoint[1], app.coordinatesSecondPoint[0], 
                 app.coordinatesSecondPoint[1], fill = app.color, lineWidth = app.thickness)
    if app.drawLine == True and app.drawTemp:
        drawLine(app.coordinatesFirstPoint[0], app.coordinatesFirstPoint[1], app.tempLine[0], app.tempLine[1], fill=app.color, lineWidth = app.thickness)

    # CURVED LINES
    # draw current curved line
    for i in range(1, len(app.lineCircleCenters)):
        drawLine(app.lineCircleCenters[i-1][0], app.lineCircleCenters[i-1][1], app.lineCircleCenters[i][0], 
                 app.lineCircleCenters[i][1], fill=app.lineCircleCenters[i][2], lineWidth = app.lineCircleCenters[i][4])
        drawCircle(app.lineCircleCenters[i][0], app.lineCircleCenters[i][1], app.lineCircleCenters[i][3], fill=app.lineCircleCenters[i][2])

# helper to get colors to draw the buttons depending on what color scheme mode
def getColorList(app):
    # CITATION: This is mentioned at the top but I used the following link to find the colorblind friendly colors: 
    # https://www.nceas.ucsb.edu/sites/default/files/2022-06/Colorblind%20Safe%20Color%20Schemes.pdf
    if app.colorblindMode == False:
        colorList = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet', 'black', 'dodgerblue', 'lightgreen', 'red', 'midnightblue', 'mediumblue', 
                     'royalblue', 'cornflowerblue', 'gold']
    else:
        colorList = [rgb(204, 121, 167), rgb(213, 94, 0), rgb(230, 159, 0), rgb(240, 228, 66), rgb(86, 180, 233), rgb(0, 114, 178), rgb(0, 158, 115), 
                     rgb(0,0,0), rgb(126, 41, 84), rgb(51, 117, 56), rgb(46, 37, 133), rgb(46, 37, 133), rgb(0, 114, 178), rgb(86, 180, 233), rgb(148, 203, 236), rgb(220, 205, 125)]
    return colorList

# drawing the buttons - colors, boldness and clears 
def buttonDrawings(app):
    # COLOR
    drawRect(app.width/15, 0, app.width/ 15*2, app.height/15, fill='white', border='black')
    colorList = getColorList(app)
    
    if app.colorblindMode == False:
        drawLabel('Click for Colorblind Friendly Mode!', app.width/15*2, app.height/15/2, align='center', size=app.width/120, fill='black')
    else:
        drawLabel('Click for Regular Mode!', app.width/15*2, app.height/15/2, align='center', size=app.width/90, fill='black')

    if app.readAloud == False and app.gameInstructions == True:
        drawRect(app.width/15*3, 0, app.width/15*2, app.height/15, fill= 'white', border='black')
        drawLabel('Click for Read Aloud!', app.width/15*4, app.height/15/2, align='center', size=app.width/90, fill='black')
    
    for i in range(8):
        drawRect(0, (app.height/15)*i, app.width/15, app.height/15, fill=colorList[i])

    colorRGB = gradient(colorList[8], colorList[9], colorList[10])

    drawRect(0, (app.height/15)*8, app.width/15, app.height/15, fill = colorRGB)
    rgbLetterFill = 'black'
    if app.colorblindMode == True:
        rgbLetterFill = 'white'
    drawLabel('RGB', app.width/30, (app.height/15)*8 + (app.height/30), align = 'center', size = app.width/42, fill = rgbLetterFill)

    # THICKNESS - BOLD, MED, THIN, CHOOSE labels
    boldnessLabels = [
        ('Bold', 9, colorList[11], app.width/42),
        ('Med', 10, colorList[12], app.width/40),
        ('Thin', 11, colorList[13], app.width/40),
        ('Choose', 12, colorList[14], app.width/55),
    ]

    for label in boldnessLabels:
        drawRect(0, (app.height/15) * label[1], app.width/15, app.height/15, fill=label[2])
        drawLabel(label[0], app.width/30, (app.height/15) * label[1] + (app.height/30), align='center', size=label[3], fill='white')

    # draw INSTRUCTIONS label
    drawRect(0, (app.height/15)*13, app.width/15, app.height/15, fill=colorList[15], border = 'black')
    drawLabel('Directions', app.width/30, (app.height/15)*13 + (app.height/30), align = 'center', size = app.width/80)

    # draw BOLDNESS SLIDER
    if app.boldnessSlider == True:
        drawRect(0, (app.height/15)*12, app.width/15*3, app.height/15, fill='white', border = 'black')
        drawRect(0, (app.height/15)*12+(app.height/15)/3, app.width/15*3, app.height/15/3, fill='black')
        drawCircle(app.sliderX, (app.height/15)*12 + (app.height/15)/2, app.width/90, fill=colorList[0])
        drawLabel(f'Thickness: {app.sliderX}', app.width/15*3 + 10, (app.height/15)*12 + (app.height/15)/2, align='left', size=app.width/80)

    # draw ERASER label
    colorList2 = []
    if app.colorblindMode == False:
        colorList2 = ['orangered', 'tomato', 'coral', 'lightsalmon', 'darkgreen']
    else:
        colorList2 = [rgb(116, 40, 129), rgb(152, 110, 172), rgb(195, 164, 207), rgb(229, 212, 232), rgb(27, 121, 57)]
        
    drawRect(app.width-app.width/15, 0, app.width/15, app.height/15, fill = colorList2[0])
    drawLabel("Eraser", app.width-app.width/30, (app.height/30), align = 'center', size = app.width/50, fill = 'white')

    clearButtons = [
        ("Eraser", 0, colorList2[0], app.width/50),
        ("Clear", 1, colorList2[1], app.width/50),
        ("Delete", 2, colorList2[2], app.width/50),
        ("Undo", 3, colorList2[3], app.width/50),
    ]

    for button in clearButtons:
        drawRect(app.width - app.width/15, (app.height/15) * button[1], app.width/15, app.height/15, fill=button[2])
        drawLabel(button[0], app.width - app.width/30, (app.height/30) * (button[1] + 1) + (app.height/30) * button[1], align='center', size=button[3], fill='white')

    # draw SAVE button
    drawRect(app.width-(app.width/15), (app.height/15)*4, app.width/15, app.height/15, fill = colorList2[4], border = 'black')
    drawLabel("Save Img", app.width-app.width/30, (app.height/30)*5 + (app.height/30)*4, align = 'center', size = app.width/70, fill = 'white')

    if app.gameMode == True and app.gameInstructions == True:
    # draw WORD DIFFICULTY buttons
        modeColor = 'red'
        if app.colorblindMode == True:
            modeColor = rgb(126, 41, 84)
        drawLabel("Choose", app.width-app.width/30, (app.height/30)*6 + (app.height/30)*5-15, align = 'center', size = 20, fill = modeColor)
        drawLabel("Your Mode!", app.width-app.width/30, (app.height/30)*6 + (app.height/30)*5+10, align = 'center', size = 20, fill = modeColor)
        
        difficultyColors = ['green', 'orange', 'red']
        if app.colorblindMode == True:
            difficultyColors = [rgb(000, 158, 115), rgb(230, 159, 0), rgb(204, 121, 167)]

        difficultyLevels = [
            ("EASY", 6, difficultyColors[0]),
            ("MED", 7, difficultyColors[1]),
            ("HARD", 8, difficultyColors[2])
        ]

        for difficulty in difficultyLevels:
            drawRect(app.width - (app.width/15), (app.height/15) * difficulty[1], app.width/15, app.height/15, fill=difficulty[2])
            drawLabel(difficulty[0], app.width - app.width/30, (app.height/30) * (difficulty[1] + 1) + (app.height/30) * difficulty[1], 
                      align='center', size=app.width/50, fill='white')

# helper to add extra stuff during game mode - instructions, timer, guess count, word count, game over, word notification, screen prompts
def gameModeDrawings(app):
    # GAME MODE
    if app.gameOver == True:
        drawLabel(f"The word was '{app.word}.'", app.width/2, 30, fill = 'red', size = 50)
    if app.gameMode == True and app.instructions == False:
        if app.gameOver == False and app.winner == False:
            clueColor = 'red'
            if app.colorblindMode == True:
                clueColor = rgb(126, 42, 84)
            drawLabel(f"CLUE: {app.displayLetters}", app.width/2, 30, fill = clueColor, size = 50)
        drawLabel(f"{app.timer}", app.width - 60, app.height - 60, fill = 'black', size = 40)
        drawLabel(f'Guess Count: {app.guessCount}', app.width - 250, 25, fill = 'black', size = 20)
        drawLabel(f'Word Count: {app.wordCount}', app.width - 250, 50, fill = 'black', size = 20)
        if app.gameInstructions == True:
            instructions = [
                "INSTRUCTIONS: There will be 2 players: an artist and a guesser.",
                "The artist will be given a word and will start drawing it while the guesser must try guessing what it is.",
                "You may choose the difficulty of the possible words by selecting a mode (see screen right).",
                "At any point during the 60 allotted seconds, if the guesser knows what the picture is they will press 'w' and enter their guess.",
                "You can keep guessing as long as there's time left, but the game will keep track of the number of guesses.",
                "To help the guesser, letters of the word will begin appearing at the top of the screen as time progresses.",
                "Press 'b' to begin."
            ]
            for i, instruction in enumerate(instructions):
                drawLabel(instruction, app.width / 2, app.height / 2 - 25 + 25 * i, fill='black', size=20)
        if app.displayWarning == True:
            drawLabel("Guesser, please look away from the screen until further notice.", app.width/2, app.height/2, fill = 'black', size = 20) 
        if app.displayWord == True:
            drawLabel(f"Your Word is '{app.drawingList[app.index]}.'", app.width/2, app.height/2, fill = 'black', size = 20)
        if app.displayOk == True:
            drawLabel("The guesser may now look at the screen.", app.width/2, app.height/2, fill = 'black', size = 20) 
        if app.displayStart == True:
            drawLabel("Ready...Set.. DRAW!!!", app.width/2, app.height/2, fill = 'black', size = 20) 
        if app.winner == True:
            if app.wordCount == 1:
                drawLabel(f'You found {app.wordCount} word!', app.width/2, app.height/2, fill = 'black', size = 40)
            else:
                drawLabel(f'You found {app.wordCount} words!', app.width/2, app.height/2, fill = 'black', size = 40)

        #drawRect(0, (app.height/15)*13, app.width/15, app.height/15, fill='midnightblue', border = 'black')
        #drawLabel('Game Info', app.width/30, (app.height/15)*13 + (app.height/30), align = 'center', size = app.width/80, fill = 'white')
        # EXIT GAME BUTTON
        exitButtonColor = 'crimson'
        if app.colorblindMode == True:
            exitButtonColor = rgb(126, 41, 84)
        drawRect(0, (app.height/15)*14, app.width/15, app.height/15, fill=exitButtonColor, border = 'black')
        drawLabel('Exit Game', app.width/30, (app.height/15)*14 + (app.height/30), align = 'center', size = app.width/80, fill = 'white')

    if app.gameOver == True:
        drawLabel("GAME OVER", app.width/2, app.height/2, fill = 'red', size = app.width/10)

# finalize current drawing before moving to the next one - i.e. save to past drawings list
def finalizeCurrentDrawing(app, key):
    if app.drawingFreeze == False and app.instructions == False and app.titleScreen == False:
        # finalize current drawing before toggling to new shape
        if key in ['r', 'c', 'p', 'l', 'e']:
            pastAppend(app)
            fullReset(app)
            if key == 'e':
                app.eraser = True

# appending past shapes to shapes list so that past shapes do not disspear
def pastAppend(app):
    if len(app.coordinatesTopCorner) == 2 and len(app.coordinatesBottomCorner) == 2:
        app.shape = 'Rectangle'
        appendList = [app.shape, app.coordinatesTopCorner[0], app.coordinatesTopCorner[1], app.rectWidth, app.rectHeight, app.color, app.thickness]
        app.pastRects.append(appendList)
        app.masterList.append(appendList)
    if len(app.coordinatesCenter) == 2 and len(app.circleRadius) == 1:
        app.shape = 'Circle'
        appendList = [app.shape, app.coordinatesCenter[0], app.coordinatesCenter[1], app.circleRadius[0], app.color, app.thickness]
        app.pastCircles.append(appendList)
        app.masterList(appendList)
    if len(app.coordinatesCenter) == 2 and len(app.polyRadius) == 1:
        app.shape = 'Regular Polygon'
        appendList = [app.shape, app.coordinatesCenter[0], app.coordinatesCenter[1], app.polyRadius[0], app.numberSides, app.color, app.thickness]
        app.pastRegPoly.append(appendList)
        app.masterList.append(appendList)
    if len(app.coordinatesFirstPoint) == 2 and len(app.coordinatesSecondPoint) == 2:
        if app.eraser == True:
            color = 'white'
        else:
            color = app.color
        app.shape = 'Line'
        appendingList = [app.shape, app.coordinatesFirstPoint[0], app.coordinatesFirstPoint[1], app.coordinatesSecondPoint[0], 
                            app.coordinatesSecondPoint[1], color, app.thickness]
        app.pastLines.append(appendingList)
        app.masterList.append(appendingList)

# other key presses - undo, clear, exit game mode, popup for keyboard shortcut reminders, screenshot
def onKeyPress(app, key):
    finalizeCurrentDrawing(app, key)
    if app.drawingFreeze == False and app.instructions == False and app.titleScreen == False:
        rectangleKey(app, key)
        circleKey(app, key)
        polygonKey(app, key)
        lineKey(app, key) 
        scribbleKey(app, key)
        releaseCurrentDrawingKey(app, key)
        if key == 'u':
            app.undoLast = True
            undoLastShape(app)

    if key == 'enter':
        app.boldnessSlider = False

    if key == 'o':
        clearScreen(app)

    if key == 'z' and app.gameMode == True: # exit game mode at any time 
        exitGame(app)

    if key == 'q':
        pyautogui.alert(
            "KEYBOARD SHORTCUTS:\n"
            "'r' ==> rectangle (click to place 2 points)\n"
            "'p' ==> polygon (click to place center and edge)\n"
            "'c' ==> circle (click to place center and edge)\n"
            "'l' ==> line (click to place two points)\n"
            "'s' ==> scribble (drag mouse to draw)\n"
            "'e' ==> eraser (drag mouse to erase)\n"
            "'u' ==> undo last drawn shape of choice\n"
            "'o' ==> clear screen\n"
            "'x' ==> exit current drawing operation\n"
            "'t' ==> save screenshot\n\n"
            "GAME SHORTCUTS\n"
            "'g' ==> game mode\n"
            "'b' ==> begin game once in game mode\n"
            "'w' ==> guessing mode\n"
            "'z' ==> exit game mode at any time"
        )

    if key == 't':
        makeScreenshot(app)

    gameModeKey(app, key)

# rectangle key shortcut
def rectangleKey(app, key):
    # RECTANGLE
    if key == 'r':
        app.eraser = False
        app.drawRegularPolygon = False
        app.drawCircle = False
        app.drawLine = False
        app.drawCurvedLines = False
        app.drawRect = True

# circle key shortcut
def circleKey(app, key):
    # CIRCLE
    if key == 'c':
        app.eraser = False
        app.drawRegularPolygon = False
        app.drawRect = False
        app.drawLine = False
        app.drawCurvedLines = False
        app.drawCircle = True

# regular polygon key shortcut
def polygonKey(app, key):
    # REGULAR POLYGON
    if key == 'p':
        app.eraser = False
        app.drawRect = False
        app.drawCircle = False
        app.drawLine = False
        app.drawCurvedLines = False
        app.numberSides = None
        while not app.numberSides or not app.numberSides.isdigit() or int(app.numberSides) < 3:
            # make sure its a valid number 
            app.numberSides = pyautogui.prompt("Enter Number of Sides (Enter a Number Greater Than or Equal To 3)")
        app.numberSides = int(app.numberSides)
        app.drawRegularPolygon = True

# line key shortcut
def lineKey(app, key):
    # STRAIGHT LINE
    if key == 'l':
        app.eraser = False
        app.drawRegularPolygon = False
        app.drawRect = False
        app.drawCircle = False
        app.drawCurvedLines = False
        app.drawLine = True
        app.coordinatesFirstPoint = []
        app.coordinatesSecondPoint = []
        app.drawTemp = False
        app.tempLine = []

# scribble key shortcut
def scribbleKey(app, key):
    # CURVED LINES
    if key == 's':
        app.eraser = False
        startNewCurvedLine(app)

# game mode key shortcuts 
def gameModeKey(app, key):
    # GAME MODE
    if key == 'g' and app.titleScreen == False:
        turnOnGameMode(app)
    if key == "w" and app.counter > 17: # freeze drawing when game mode activated
        app.guessMode = True
        app.drawingFreeze = True
    if key == 'b':
        app.gameInstructions = False

# stop current drawing operation
def releaseCurrentDrawingKey(app, key):
    # RELEASE
    if key == 'x':
        pastAppend(app)
        app.eraser = False
        fullReset(app)

# exit popup screens by pressing exit button 
def exitButtons(app, mouseX, mouseY):
    if (app.titleScreen == True and mouseX > app.width/2 - (app.width/5)/2 and mouseX < app.width/2 + (app.width/5)/2 
        and mouseY > (app.height/2 + 150) - (app.height/10)/2 and mouseY < (app.height/2 + 150) + (app.height/10)/2):
        app.titleScreen = False
    if (app.instructions == True and mouseX > 0 and mouseX<app.width/15 and mouseY > 0 and mouseY<app.height/20):
        app.instructions = False

def onMouseMove(app, mouseX, mouseY):
    rectangleVisualization(app, mouseX, mouseY)
    circleAndPolygonVisualization(app, mouseX, mouseY)
    lineVisualization(app, mouseX, mouseY)
    startNewCurvedLine(app)

def onMouseDrag(app, mouseX, mouseY):
    if app.boldnessSlider == False:
        scribbleAppend(app, mouseX, mouseY)
        eraserAppend(app, mouseX, mouseY)
    if app.boldnessSlider == True:
        if mouseX >= 0 and mouseX <= app.width/15*3:
            app.sliderX = mouseX
            app.thickness = mouseX

# append past rectangles 
def rectangleAppend(app, mouseX, mouseY):
    # RECTANGLE
    if len(app.coordinatesTopCorner) == 2 and len(app.coordinatesBottomCorner) == 2:
        app.shape = 'Rectangle'
        appendList = [app.shape, app.coordinatesTopCorner[0], app.coordinatesTopCorner[1], app.rectWidth, app.rectHeight, app.color, app.thickness]
        app.pastRects.append(appendList)
        app.masterList.append(appendList)
        app.coordinatesTopCorner = []
        app.coordinatesBottomCorner = []
        app.drawTemp = False
    if len(app.coordinatesTopCorner) == 0 and app.drawRect:
        app.coordinatesTopCorner.append(mouseX)
        app.coordinatesTopCorner.append(mouseY)
    elif len(app.coordinatesBottomCorner) == 0 and app.drawRect:
        app.coordinatesBottomCorner.append(mouseX)
        app.coordinatesBottomCorner.append(mouseY)
        # calculate width and height
        app.rectWidth = abs(mouseX - app.coordinatesTopCorner[0])
        app.rectHeight = abs(mouseY - app.coordinatesTopCorner[1])
        if app.rectWidth == 0:
            app.rectWidth = 0.1
        if app.rectHeight == 0:
            app.rectHeight = 0.1
        
        # if user moves the mouse in the other direction, adjust the corner 
        if mouseX < app.coordinatesTopCorner[0]:
            app.coordinatesTopCorner[0], app.coordinatesBottomCorner[0] = app.coordinatesBottomCorner[0], app.coordinatesTopCorner[0]
        if mouseY < app.coordinatesTopCorner[1]:
            app.coordinatesTopCorner[1], app.coordinatesBottomCorner[1] = app.coordinatesBottomCorner[1], app.coordinatesTopCorner[1]

# append past circles
def circleAppend(app, mouseX, mouseY):
    # CIRCLE
    if len(app.coordinatesCenter) == 0 and app.drawCircle == True:
        app.coordinatesCenter.append(mouseX)
        app.coordinatesCenter.append(mouseY)
    elif len(app.coordinatesCenter) == 2 and app.drawCircle:
        app.circleRadius.append(((mouseX - app.coordinatesCenter[0])**2 + (mouseY - app.coordinatesCenter[1])**2)**0.5)
        app.radius = app.circleRadius[0]
        if app.radius == 0:
            app.radius = 0.1
        app.shape = 'Circle'
        appendList = [app.shape, app.coordinatesCenter[0], app.coordinatesCenter[1], app.circleRadius[0], app.color, app.thickness]
        app.pastCircles.append(appendList)
        app.masterList.append(appendList)
        app.coordinatesCenter = []
        app.circleRadius = []
        app.tempRadius = 0

# append past polygons 
def polygonAppend(app, mouseX, mouseY):
    # REGULAR POLYGON
    if len(app.coordinatesCenter) == 0 and app.drawRegularPolygon == True:
        app.coordinatesCenter.append(mouseX)
        app.coordinatesCenter.append(mouseY)
    elif len(app.coordinatesCenter) == 2 and app.drawRegularPolygon:
        app.polyRadius.append(((mouseX - app.coordinatesCenter[0])**2 + (mouseY - app.coordinatesCenter[1])**2)**0.5)
        app.radius = app.polyRadius[0]
        if app.radius == 0:
            app.radius = 0.1
        app.shape = 'Regular Polygon'
        appendList = [app.shape, app.coordinatesCenter[0], app.coordinatesCenter[1], app.polyRadius[0], app.numberSides, app.color, app.thickness]
        app.pastRegPoly.append(appendList)
        app.masterList.append(appendList)
        app.coordinatesCenter = []
        app.polyRadius = []
        app.tempRadius = 0

# append past lines 
def lineAppend(app, mouseX, mouseY):
    # STRAIGHT LINE
    if app.drawLine == True and len(app.coordinatesFirstPoint) == 2 and len(app.coordinatesSecondPoint) == 2:
        app.shape = 'Line'
        appendList = [app.shape, app.coordinatesFirstPoint[0], app.coordinatesFirstPoint[1], app.coordinatesSecondPoint[0], 
                              app.coordinatesSecondPoint[1], app.color, app.thickness]
        app.pastLines.append(appendList)
        app.masterList.append(appendList)
        app.coordinatesFirstPoint = []
        app.coordinatesSecondPoint = []
        app.drawTemp = False
    if app.drawLine == True and len(app.coordinatesFirstPoint) == 0 and len(app.coordinatesSecondPoint) == 0:
        app.coordinatesFirstPoint.append(mouseX)
        app.coordinatesFirstPoint.append(mouseY)
    elif app.drawLine == True and len(app.coordinatesFirstPoint) == 2 and len(app.coordinatesSecondPoint) == 0:
        app.coordinatesSecondPoint.append(mouseX)
        app.coordinatesSecondPoint.append(mouseY)
        app.drawTemp = False

# append past scribbles
def scribbleAppend(app, mouseX, mouseY):
    # CURVED LINES
    if app.drawingFreeze == False:
        if app.drawCurvedLines == True:
            # append if mouse has moved more than 1 in distance - ensure smooth line
            if app.lastMouseX is None or app.lastMouseY is None:
                if app.eraser == False:
                    app.lineCircleCenters.append([mouseX, mouseY, app.color, app.thickness/2, app.thickness])
                else:
                    app.lineCircleCenters.append([mouseX, mouseY, 'white', app.thickness/2, app.thickness])
            elif abs(mouseX - app.lastMouseX) > 1 or abs(mouseY - app.lastMouseY) > 1:
                if app.eraser == False:
                    app.lineCircleCenters.append([mouseX, mouseY, app.color, app.thickness/2, app.thickness])
                else:
                    app.lineCircleCenters.append([mouseX, mouseY, 'white', app.thickness/2, app.thickness])
            app.lastMouseX = mouseX
            app.lastMouseY = mouseY

# append past eraser strokes
def eraserAppend(app, mouseX, mouseY):
    # ERASER
    if app.eraser == True:
        fullReset(app)
        if app.lastMouseX is None or app.lastMouseY is None:
            app.thickness = 20
            app.lineCircleCenters.append([mouseX, mouseY, 'white', app.thickness/2, app.thickness])
        elif abs(mouseX - app.lastMouseX) > 1 or abs(mouseY - app.lastMouseY) > 1:
            app.thickness = 20
            app.lineCircleCenters.append([mouseX, mouseY, 'white', app.thickness/2, app.thickness])
        app.lastMouseX = mouseX
        app.lastMouseY = mouseY
        app.eraser = True

# start new curved line when stop pressing on mouse - starts a new line
def startNewCurvedLine(app):
    if app.lineCircleCenters:
        app.pastCurvedLines.append(app.lineCircleCenters)
        app.masterList.append(app.lineCircleCenters)
        fullReset(app)
    app.lineCircleCenters = []
    app.drawCurvedLines = True

# save screenshot of drawing to downloads folder
def makeScreenshot(app):
    # CITATION: This is also mentioned at the top but Microsoft Copilot was used for this function - it helped me learn how to get file path on every computer instead of just mine
    screenshot = pyautogui.screenshot()

    downloadsPath = os.path.join(os.path.expanduser('~'), 'Downloads')
    filePath = os.path.join(downloadsPath, 'screenshot.png')

    screenshot.save(filePath)
    pyautogui.alert(
        f'Screenshot saved to {filePath}.\n'
        "Please change the file name from 'screenshot.png' to something else if you would like to save a new screenshot in the future."
    )

# read aloud option for accessibility
def readAloudTime(app):
    # CITATION: This is mentioned at the top but Microsoft Copilot helped me write this text to speech function
    text = ''

    if app.readAloud == True and app.gameInstructions == True:
        text = (
            "INSTRUCTIONS: There will be 2 players: an artist and a guesser. "
            "The artist will be given a word and will start drawing it while the guesser must try guessing what it is. "
            "You may choose the difficulty of the possible words by selecting a mode. "
            "At any point during the 60 allotted seconds, if the guesser knows what the picture is they will press 'w' and enter their guess. "
            "You can keep guessing as long as there's time left, but the game will keep track of the number of guesses. "
            "To help the guesser, letters of the word will begin appearing at the top of the screen as time progresses. "
            "Press 'b' to begin."
        )

    if app.readAloud == True and app.instructions == True:
        text = (
            "Welcome to Draw one twelve - The Newest Artist Palette and Game! "
            "Keyboard Shortcuts are used to draw Shapes, as well as carry out other commands. "
            "Please press 'q' at any time to see all Keyboard Shortcuts. "
            "In order to draw a shape, one must first select the Thickness and Color and then select the key corresponding to the shape or line you want to draw. "
            "The RGB Button allows users to choose colors that are not default options. "
            "Simply press the RGB Button and follow the popup prompt on the screen. "
            "The Choose Button allows users to choose line thicknesses that are not default options. "
            "Simply press the Choose Button, use the slider to select a thickness and then hit the 'enter' key to lock it in. "
            "The Eraser Button will erase when the user clicks the button and then drags the mouse across the screen. "
            "The Clear Button will clear the entire screen. "
            "The Delete Button will allow the user to select a shape type and then delete the most recently drawn version of that type. "
            "The Undo Button will undo the last thing the user drew/erased. "
            "The Save Image Button saves a png screenshot of the page to the user's Downloads. "
            "Pressing 'g' will activate Game Mode and instructions will be explained upon activation."
        )

    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    app.readAloud = False

# rgb color choice after pressing on rgb button 
def rgbChoice(app):
    red = 'r'
    green = 'g'
    blue = 'b'

    while not (red.isdigit()) or not (0 <= int(red) <= 255):
        red = pyautogui.prompt('Enter Red Value as a 3 Digit Integer less than 255.')
        if red is None:
            red = '0'
    while not (green.isdigit()) or not (0 <= int(green) <= 255):
        green = pyautogui.prompt('Enter Green Value as a 3 Digit Integer less than 255.')
        if green is None:
            green = '0'
    while not (blue.isdigit()) or not (0 <= int(blue) <= 255):
        blue = pyautogui.prompt('Enter Blue Value as a 3 Digit Integer less than 255.')
        if blue is None:
            blue = '0'

    red = int(red)
    green = int(green)
    blue = int(blue)

    color = rgb(red, green, blue)
    app.color = color
    

# color buttons + RGB chouce button and also colorblindness mode toggle
# thickness buttons and boldness slider toggle
def colorThicknessAndInstructionButtons(app, mouseX, mouseY):
    if mouseX>app.width/15 and mouseX<app.width/15*3 and mouseY < app.height/15:
        fullReset(app)
        if app.colorblindMode == False and app.instructions == False:
            app.colorblindMode = True
        else:
            app.colorblindMode = False
    
    if mouseX>app.width/15*3 and mouseX<app.width/15*6 and mouseY < app.height/15 and app.gameInstructions == True:
        fullReset(app)
        if app.readAloud == False:
            app.readAloud = True
            readAloudTime(app)
        if app.readAloud == True:
            app.readAloud = False

    # COLOR AND THICKNESS
    if mouseX < app.width/15 and mouseX > 0 and mouseY < app.height and mouseY > 0:
        fullReset(app)
        colorList = getColorList(app)
        
        for i in range(8):
            if mouseY > (app.height/15)*i and mouseY < (app.height/15) * (i+1):
                app.color = colorList[i]
                break
        else:
            if mouseY > (app.height/15) * 8 and mouseY < (app.height/15) * 9:
                rgbChoice(app)
            elif mouseY > (app.height/15) * 9 and mouseY < (app.height/15) * 10:
                app.thickness = 30
            elif mouseY > (app.height/15) * 10 and mouseY < (app.height/15) * 11:
                app.thickness = 15
            elif mouseY > (app.height/15) * 11 and mouseY < (app.height/15) * 12:
                app.thickness = 1
            elif mouseY > (app.height/15) * 12 and mouseY < (app.height/15) * 13:
                app.boldnessSlider = True
            elif mouseY > (app.height/15) * 13 and mouseY < (app.height/15) * 14:
                app.instructions = True
            elif mouseY > (app.height/15) * 14 and mouseY < (app.height/15) * 15 and not app.instructions:
                exitGame(app)
    if mouseX > app.width/15 and mouseX < app.width/15*3 and mouseY < app.height/15 and app.instructions == True:
        app.readAloud = True
        readAloudTime(app)

# eraser, clear, undo, delete buttons 
def clearAndEraseButtons(app, mouseX, mouseY):
    # CLEAR AND ERASER
    if mouseX < app.width and mouseX > (app.width/15)*14:
        if mouseY < (app.height/15) and mouseY > 0:
            app.eraser = True
            #app.color = 'white'
            app.drawCurvedLines = False
            fullReset(app)
        elif mouseY < (app.height/15)*2 and mouseX > (app.height/15):
            clearScreen(app)
        elif mouseY < (app.height/15)*3 and mouseX > (app.height/15)*2:
            #app.color = 'white'
            app.undoShape = True
            deleteShape(app)
            fullReset(app)
        elif mouseY < (app.height/15)*4 and mouseX > (app.height/15)*3:
            #app.color = 'white'
            app.undoLast = True
            undoLastShape(app)
            fullReset(app)
        elif mouseY < (app.height/15)*5 and mouseX > (app.height/15)*4:
            fullReset(app)
            makeScreenshot(app)

# game difficulty buttons
def difficultyButtons(app, mouseX, mouseY):
    if mouseX < app.width and mouseX > (app.width/15)*14:
        if mouseY < (app.height/15)*7 and mouseX > (app.height/15)*4:
            if app.gameMode == True and app.gameInstructions == True:
                app.drawingList = app.easy
        elif mouseY < (app.height/15)*8 and mouseX > (app.height/15)*5:
            if app.gameMode == True and app.gameInstructions == True:
                app.drawingList = app.medium
        elif mouseY < (app.height/15)*9 and mouseX > (app.height/15)*6:
            if app.gameMode == True and app.gameInstructions == True:
                app.drawingList = app.hard

def onMousePress(app, mouseX, mouseY):
    rectangleAppend(app, mouseX, mouseY)
    circleAppend(app, mouseX, mouseY)
    polygonAppend(app, mouseX, mouseY)
    lineAppend(app, mouseX, mouseY)

    exitButtons(app, mouseX, mouseY)
    colorThicknessAndInstructionButtons(app, mouseX, mouseY)
    clearAndEraseButtons(app, mouseX, mouseY)
    difficultyButtons(app, mouseX, mouseY)

# when you click to create a point and drag you can see what these shapes look like if you were to click in a certain place
def rectangleVisualization(app, mouseX, mouseY):
    # RECTANGLE
    if len(app.coordinatesTopCorner) == 2 and len(app.coordinatesBottomCorner) == 0:
        app.drawTemp = True
        app.tempWidth = abs(mouseX - app.coordinatesTopCorner[0])
        app.tempHeight = abs(mouseY - app.coordinatesTopCorner[1])
        if app.tempHeight == 0:
            app.tempHeight = 0.1
        if app.tempWidth == 0:
            app.tempWidth = 0.1
        app.tempCoordinateX = min(app.coordinatesTopCorner[0], mouseX)
        app.tempCoordinateY = min(app.coordinatesTopCorner[1], mouseY)

def circleAndPolygonVisualization(app, mouseX, mouseY):
    # CIRCLE & REGULAR POLYGON
    if len(app.coordinatesCenter) == 2 and (app.drawCircle == True or app.drawRegularPolygon == True):
        app.drawTemp = True
        app.tempRadius = ((mouseX - app.coordinatesCenter[0])**2 + (mouseY - app.coordinatesCenter[1])**2)**0.5
        if app.tempRadius == 0:
            app.tempRadius = 0.1

def lineVisualization(app, mouseX, mouseY):
    # STRAIGHT LINE
    if app.drawLine == True and len(app.coordinatesFirstPoint) == 2 and len(app.coordinatesSecondPoint) == 0:
        app.drawTemp = True
        app.tempLine = [mouseX, mouseY]

# delete function - deletes last draw version of entered shape type
def deleteShape(app):
    if app.undoShape == True:
        fullReset(app)
        desiredShape = pyautogui.prompt(
            "Please enter the type of shape/line that you would like to delete.\n"
            "This button deletes the last drawn version of your selected shape/line.\n\n"
            "Your options are 'Rectangle,' 'Circle,' 'Polygon,' 'Line,' and 'Scribble.'"
        )
        desiredShapeDict = {'Rectangle': app.pastRects, 'Circle': app.pastCircles, 'Polygon': app.pastRegPoly, 'Line': app.pastLines, 'Scribble': app.pastCurvedLines}
        if desiredShape in desiredShapeDict:
            pastList = desiredShapeDict[desiredShape]
            if len(pastList) != 0:
                if desiredShape == 'Scribble':
                    popVal = pastList.pop()
                    app.masterList.remove(popVal)
                else:
                    popVal = pastList.pop()
                    indexVal = app.masterList.index(popVal)
                    app.masterList.pop(indexVal)
        else:
            pyautogui.alert('Invalid Shape or Line Choice.\nMake sure you capitalize the first letter and spell correctly.')
        app.undoShape = False

# undo most recently drawn shape
def undoLastShape(app):
    # dont use dictionary, cannot have lists bc mutable
    # CITATION: I kept getting an error that something was unhashable and was confused - copilot told me I could do this with a 2D list instead 
    shapeList = [['Rectangle', app.pastRects], ['Circle', app.pastCircles], ['Polygon', app.pastRegPoly], ['Line', app.pastLines]]

    if app.undoLast:
        if len(app.masterList) >= 1:
            popVal = app.masterList.pop()
            shapeFound = False
            for shape, pastList in shapeList:
                if popVal[0] == shape:
                    pastList.pop()
                    shapeFound = True
                    break
            if shapeFound == False:
                app.pastCurvedLines.pop()
            app.undoLast = False
        else:
            clearScreen(app)
            app.undoLast = False

# deals with different scenarios
def onStep(app):
    # loser if game mode becomes false while the counter is beyond 17 (past the instruction pages)
    if app.gameMode == False and app.counter > 17:
        loser(app)

    outOfTime(app)

    # if game mode on, for the first 17 seconds (counter) do the instruction scenes at 5 second intervals except for the ready set draw screen which is only 3 seconds 
    if app.gameMode == True:
        gameStartSequence(app)
        # guessing, increment guess count when guess, increment word count when correct guess
        if app.guessMode == True:
            guessMode(app)
            
    if app.restart == True: # new game, continues with same word amd guess count 
        clearScreen(app)
        gameReset(app)
        app.gameMode = True
        app.restart = False # put variable back to False

    if app.exitGame == True: # leave game mode 
        clearScreen(app)
        app.gameMode = False
        gameReset(app)
        app.exitGame = False # put back to False

# turn on game mode 
def turnOnGameMode(app):
    clearScreen(app)
    app.gameMode = True
    app.gameInstructions = None
    app.drawingFreeze = True

# display instructions and the prompts (spaced out over intervals)
def gameStartSequence(app):
    if app.gameInstructions is None:
            app.gameInstructions = True
    if app.gameInstructions == False:
        app.counter += 1
        if app.counter <= 5:
            app.displayWarning = True
        elif app.counter <= 10:
            app.displayWarning = False
            app.displayWord = True
            if app.singleWord == 0:
                app.index = random.randrange(0, len(app.drawingList))
                app.singleWord += 1
        elif app.counter <= 15:
            app.displayWord = False
            app.displayOk = True
        elif app.counter <= 17:
            app.displayOk = False
            app.displayStart = True
        else:
            app.displayStart = False
            app.drawingFreeze = False # unfreeze drawing so the artist can now draw (after instructions)

# timer decrement and gradual clue reveal
def clueReveal(app):
    app.word = app.drawingList[app.index]
    if len(app.word) >= 6:
        if app.timer <= 60 and app.timer > 50:
            app.displayLetters = ''
        elif app.timer >= 50 and app.timer:
            app.displayLetters = app.word[0]
        elif app.timer <=40 and app.timer >30:
            app.displayLetters = app.word[0:2]
        elif app.timer <= 30 and app.timer >20:
            app.displayLetters = app.word[0:3]
        elif app.timer <= 20 and app.timer>10:
            app.displayLetters = app.word[0:4]
        elif app.timer <= 10 and app.timer>0:
            app.displayLetters = app.word[0:5]
        elif app.timer <= 0 or app.gameOver == True or app.winner == True:
            app.displayLetters = app.word
    else:
        if app.timer <= 60 and app.timer > 50:
            app.displayLetters = ''
        elif app.timer <= 55 and app.timer >= 50:
            app.displayLetters = app.word[0]
        elif app.timer <= 30:
            app.displayLetters = app.word[0:2]
        elif app.timer <= 0 or app.gameOver == True or app.winner == True:
            app.displayLetters = app.word

# what happens when time runs out
def outOfTime(app):
    # timer decrement, if time runs out (becomes less than 0) then the game is over
    if app.gameMode == True and app.counter > 17 and app.instructions == False:
        app.timer -= 1
        if app.timer < 0:
            app.gameOver = True
            app.gameMode = False
    clueReveal(app)

# guess mode when press w, gives second chance, sends back to game if wrong guesses or choose to leave guess mode
# increment guess and word count based on outcome
def guessMode(app):
    app.guess = pyautogui.prompt("What's your guess?")
    if app.guess == app.drawingList[app.index]:
        app.guessCount += 1
        app.wordCount += 1
        winner(app)
    elif app.guess != app.drawingList[app.index]:
        app.guessCount += 1
        app.tryAgain = pyautogui.prompt("Try again or exit guess mode by typing 'exit.'")
        if app.tryAgain == 'exit':
            app.guessMode = False
            app.drawingFreeze = False
        elif app.tryAgain == app.drawingList[app.index]:
            app.guessCount += 1
            app.wordCount += 1
            winner(app)
        else:
            pyautogui.alert("Please return to the game. The artist may continue drawing.")
            app.guessCount += 1
            app.guessMode = False
            app.drawingFreeze = False

# what happens if you guess the right word
def winner(app): # exit and continue option when win
    app.winner = True
    app.endGame = pyautogui.prompt("YOU WIN!! Type 'continue' to play another round and 'exit' to exit game.")
    if app.endGame == 'continue':
        clearScreen(app)
        gameReset(app)
        app.restart = True
    elif app.endGame == 'exit':
        exitGame(app)
    else:
        pyautogui.alert("Input was neither 'continue' nor 'exit. Game will now automically be exited.")
        exitGame(app)

# exit and reset option when lose 
def loser(app):
    app.gameOver, app.endGame = True, pyautogui.prompt("YOU LOSE!! Type 'reset' to reset and 'exit' to exit game.")
    if app.endGame == 'reset':
        clearScreen(app)
        app.restart = True
    elif app.endGame == 'exit':
        exitGame(app)
    else:
        pyautogui.alert("Input was neither 'reset' nor 'exit. Game will now automically be exited.")
        exitGame(app)

def fullReset(app): # resetting to empty list/false - removes all shapes/lines from screen by resetting everything
    app.coordinatesTopCorner = []
    app.coordinatesBottomCorner = []
    app.circleRadius = []
    app.polyRadius = []
    app.coordinatesCenter = []
    app.coordinatesFirstPoint = []
    app.coordinatesSecondPoint = []
    app.drawTemp = False
    app.drawRect = False
    app.drawCircle = False
    app.drawRegularPolygon = False
    app.drawLine = False
    app.drawCurvedLine = False

def clearScreen(app): # clear past shapes/lines and eraser - back to white screen
    app.masterList = []
    app.pastRects = []
    app.pastCircles = []
    app.pastCurvedLines = []
    app.lineCircleCenters = []
    app.pastRegPoly = []
    app.pastLines = []
    app.eraser = False
    fullReset(app)

def exitGame(app): # exit game
    app.counter = 0
    clearScreen(app)
    app.gameMode = False
    gameReset(app)
    app.drawingFreeze = False
    app.guessCount = 0
    app.wordCount = 0
    app.instructions = False
    app.gameInstructions = None
    app.eraser = False

def gameReset(app): # reset everything except guess count and word count, which will continue between rounds 
    app.drawingFreeze = True
    app.counter = 0
    app.displayWarning = False
    app.displayWord = False
    app.displayOk = False
    app.displayStart = False
    app.index = 0
    app.singleWord = 0
    app.guessMode = False
    app.guess = ''
    app.winner = False
    app.restart = False
    app.exitGame = False
    app.tryAgain = False
    app.timer = 60
    app.gameOver = False

def main():
    runApp()

main()