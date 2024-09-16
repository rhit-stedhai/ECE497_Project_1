import numpy as np

class Agent:
    def __init__(self):
        self.velocity = 1
        self.angle = 0
        self.xpos = 0
        self.ypos = 0
        self.lastX = 0
        self.lastY = 0

    def walk(self, type = 'random'):
        match type:
            case 'random':
                self.angle = np.random.random() * np.pi * 2
                self.xpos += self.velocity * np.cos(self.angle)
                self.ypos += self.velocity * np.sin(self.angle)
            case 'Orthokenesis':
                # angle will move at random within a 45 degree window of its current orientation
                # velocity will be proportional to the distance away from the origin. set up so that at 1000 units 
                #    away from origin the velocity will be doubled
                if np.random.random() > 0.5:
                    self.angle += np.random.random() * np.pi * 0.25
                else:
                    self.angle -= np.random.random() * np.pi * 0.25

                self.velocity = (np.sqrt(self.xpos**2 + self.ypos**2) / 1000) + 1
                self.xpos += self.velocity * np.cos(self.angle)
                self.ypos += self.velocity * np.sin(self.angle)
            case 'Klinokenesis':
                # this implementation uses Klinokenesis 2
                # if the agent is further away from the point of origin that the previous step they change their angle change
                #    within a 27 degree window. if they are closer than it is a 63 degree window
                distanceDifference = np.sqrt(self.xpos**2 + self.ypos**2) - np.sqrt(self.lastX**2 + self.lastY**2) 
                if distanceDifference > 0:
                    if np.random.random() > 0.5:
                        self.angle += np.random.random() * np.pi * 0.15
                    else:
                        self.angle -= np.random.random() * np.pi * 0.15
                else:
                    if np.random.random() > 0.5:
                        self.angle += np.random.random() * np.pi * 0.35
                    else:
                        self.angle -= np.random.random() * np.pi * 0.35

                self.lastX = self.xpos
                self.lastY = self.ypos
                self.xpos += self.velocity * np.cos(self.angle)
                self.ypos += self.velocity * np.sin(self.angle)
                pass
            case 'Klinotaxis':
                # The agent will find its desired angle to maximize distance from origin and move to face that direction
                if np.random.random() > 0.5:
                    noise = np.random.random()
                else:
                    noise = -1 * np.random.random()
                
                # Added 0.00001 so i dont do 0/0 at the start
                desiredAngle = np.arctan((self.ypos+0.00001)/(self.xpos+0.00001))
                self.angle = np.random.random() * desiredAngle + noise

                self.xpos += self.velocity * np.cos(self.angle)
                self.ypos += self.velocity * np.sin(self.angle)                                           
            case 'Tropotaxis':
                # The agent has 2 sensors and will change orientation to move towards
                # whichever sensor's trajectory will maximize distance from the origin
                if np.random.random() > 0.5:
                    noise = np.random.random()
                else:
                    noise = -1 * np.random.random()
                sensorOneX = self.xpos + np.cos(self.angle + np.pi/2)
                sensorOneY = self.ypos + np.sin(self.angle + np.pi/2)
                sensorTwoX = self.xpos + np.cos(self.angle - np.pi/2)
                sensorTwoY = self.ypos + np.sin(self.angle - np.pi/2)
                sensorOneDistance = np.sqrt(sensorOneX**2 + sensorOneY**2)
                sensorTwoDistance = np.sqrt(sensorTwoX**2 + sensorTwoY**2)

                if sensorOneDistance > sensorTwoDistance:
                    self.angle += np.cos(self.angle + np.pi/4) + noise
                else:
                    self.angle += np.sin(self.angle - np.pi/4) + noise
                
                self.xpos += self.velocity * np.cos(self.angle)
                self.ypos += self.velocity * np.sin(self.angle)

    def get_xpos(self):
        return self.xpos
    
    def get_ypos(self):
        return self.ypos
    
    def get_distance(xpos, ypos):
        return np.sqrt(xpos**2 + ypos**2)