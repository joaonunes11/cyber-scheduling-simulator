#-*-coding:utf-8-*-
# 2018-2019 ProgramaÃ§Ã£o 1 (LTI)
# Grupo 39
# David Garcia - 53748
# JoÃ£o Nunes - 53745

import constants

def deleteHeader(fileName):
    '''
    Reads the first 7 (lenght of header) lines of the given .txt so they can be skipped
    Requires: fileName is str, the name of a .txt file with a header
              following the format specified in the project.
    Ensures: fileName without the header
    '''
    for line in range(constants.numberOfLineHeader):
        fileName.readline()
    return fileName

def readExpertsFile(fileName):
    """
    Converts a given file listing experts into a collection.
    Requires: fileName is str, the name of a .txt file listing experts,
    following the format specified in the project.
    Ensures: list whose first element is the first is the first expert on the list, second element is the second expert on the list and so on.
    """
    
    expertsList = []
    fileIn = deleteHeader(open(fileName, 'r'))
    for line in fileIn:
        expertsList.append(line.strip().replace("\n","").replace("(","").replace(")","").replace(";","").split(", "))
    fileIn.close()
    
    return expertsList


def readClientsFile(fileName):

    """
    Converts a given file listing experts into a collection.
    Requires: filename is str, the name of a .txt file listing exprets,
    following the format specified in the project.
    Ensures: list whose first element is the first is the first client on the list, second element is the second client on the list and so on.
    """
    
    clientsList = []
    fileIn = deleteHeader(open(fileName, 'r'))
    for line in fileIn:
        clientsList.append(line.strip().replace("\n","").split(", "))
    fileIn.close()

    return clientsList

def readHeader(fileName):

    """
    Converts the header (Day, Time, Company and the first expert/cliente of a given file.
    Requires: fileName is str, the name of a .txt file listing either experts or clients.
    Ensures: tuple of the day, time, company and the first expert/client.
    """
    
    fileIn = open(fileName,"r")
    fileIn.readline()
    day = fileIn.readline().strip().replace("\n", "")
    fileIn.readline()
    time = fileIn.readline().strip().replace("\n", "")
    fileIn.readline()
    company = fileIn.readline().strip().replace("\n", "")
    scope = fileIn.readline().strip().replace("\n", "")
    fileIn.close()
    
    return (day, time, company, scope)
