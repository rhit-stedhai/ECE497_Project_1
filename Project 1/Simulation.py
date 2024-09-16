import Agent
import matplotlib.pyplot as pyplot
import numpy as np

def run_individual_sim(numSteps, walkType = 'random'):
    agent = Agent.Agent()
    xposList = [0]*(numSteps+1)
    yposList = [0]*(numSteps+1)
    
    for i in range(numSteps):
        agent.walk(type = walkType)
        xposList[i+1] = agent.get_xpos()
        yposList[i+1] = agent.get_ypos()

    figure, axes = pyplot.subplots()
    plot_runs(xposList, yposList, axes)
    pyplot.show()

    figure, axes = pyplot.subplots()
    plot_distances(xposList, yposList, axes)
    pyplot.show()

def run_group_sim(populationSize, numSteps, walkType = 'random'):
    figure, axes = pyplot.subplots()
    figure1, axes1 = pyplot.subplots()
    for i in range(populationSize):
        agent = Agent.Agent()
        xposList = [0]*numSteps
        yposList = [0]*numSteps
        
        for i in range(numSteps):
            agent.walk(type = walkType)
            xposList[i] = agent.get_xpos()
            yposList[i] = agent.get_ypos()

        plot_runs(xposList, yposList, axes)
        plot_distances(xposList, yposList, axes1)
    pyplot.show()

def plot_runs(xposList, yposList, axes):
    circle = pyplot.Circle((0, 0), 100, color='k', fill=False)
    axes.add_artist(circle)
    axes.plot(xposList, yposList)
    axes.plot(0,0,'ro')
    axes.plot(xposList[-1],yposList[-1],'ko')
    for i in range(len(xposList)):
        if np.sqrt(xposList[i]**2 + yposList[i]**2) >= 100:
            print("Number of Steps needed to escape cirlce: ", i)
            axes.plot(xposList[i], yposList[i],'mo')
            break
    pyplot.xlabel("X Position")
    pyplot.ylabel("Y Position")

def get_distances(xposList, yposList):
    distanceList = [0]*len(xposList)
    stepsList = [0]*len(xposList)
    for i in range(len(xposList)):
        distanceList[i] = np.sqrt(xposList[i]**2 + yposList[i]**2)
        stepsList[i] = i
    return distanceList, stepsList

def plot_distances(xposList, yposList, axes):
    distanceList, stepsList = get_distances(xposList, yposList)
    axes.plot(stepsList, distanceList)
    pyplot.xlabel("Step Number")
    pyplot.ylabel("Distance from Origin")
    

#run_individual_sim(1000) 
#run_individual_sim(1000, walkType = 'Orthokenesis')
#run_individual_sim(1000, walkType = 'Klinokenesis')
#run_individual_sim(1000, walkType = 'Klinotaxis')
#run_individual_sim(1000, walkType = 'Tropotaxis')

#run_group_sim(50, 1000)
#run_group_sim(10, 1000, walkType = 'Orthokenesis')
#run_group_sim(10, 1000, walkType = 'Klinokenesis')
run_group_sim(10, 1000, walkType = 'Klinotaxis')
#run_group_sim(10, 1000, walkType = 'Tropotaxis')

