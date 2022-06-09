reactGameCount = 0;
reactShowWordPress = [];
reactTimePerQuestions = [];
x = False
with open("Participant 1 - React.log", "r") as file:
    for line in file:
        if "App.js:" in line:
            line = line.split(' ', 1)[1].strip('\n');
            if "Play Game Pressed: " in line:
                x = True;
            if "Time Spent in Q: " in line:
                reactTimePerQuestions.append(int(line.split(' ')[-1]));
            if "Show Word Presses: " in line:
                reactShowWordPress.append(int(line.split("Show Word Presses: ", 1)[1]));
            if "Finish Pressed: " in line:
                reactGameCount += 1
            #if x == True:
                #print(line)
print(reactTimePerQuestions)
print("Average Question Time: " + str(sum(reactTimePerQuestions)/len(reactTimePerQuestions)))
print("Game Length: " + str(sum(reactTimePerQuestions)))
print("React Game Count: " + str(reactGameCount))
print("React Show Word Presses: " + str(reactShowWordPress))
print("----------------------")
unityGameCount = 0;
unityShowWordPress = [];
unityTimePerQuestions = [];
x = False
with open("Participant 1 - Unity.log", "r") as file:
    for line in file:
        if "Build.framework.js:" in line:
            line = line.split(' ', 1)[1].strip('\n');
            if "Play Game Pressed: " in line:
                x = True;
            if "Time Spent in Q: " in line:
                unityTimePerQuestions.append(int(line.split(' ')[-1]));
            if "Show Word Presses: " in line:
                unityShowWordPress.append(int(line.split("Show Word Presses: ", 1)[1]));
            if "Finish Pressed: " in line:
                unityShowWordPress.append(0);
                unityGameCount += 1
            #if x == True:
                #print(line)
print(unityTimePerQuestions)
print("Average Question Time: " + str(sum(unityTimePerQuestions)/len(unityTimePerQuestions)))
print("Game Length: " + str(sum(unityTimePerQuestions)))
print("Unity Show Word Presses: " + str(unityShowWordPress))
print("Unity Game Count: " + str(unityGameCount))
# Average Show Word Presses Per Game - 10 questions, average
# Total show word presses per game - 10 questions, sum
# Average Time per Question - ALL question times, average
# Game Length - 10 Question times, with 10, sum, get game time.
# Number of Times Played per gametype
