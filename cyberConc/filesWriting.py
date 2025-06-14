#-*-coding:utf-8-*-
# 2018-2019 ProgramaÃ§Ã£o 1 (LTI)
# Grupo 39
# David Garcia - 53748
# JoÃ£o Nunes - 53745

import filesReading
import constants
import dateTime
import scheduling

def writeExpertsFile(expertsFile,clientsFile):
    """
    Writes the header updated with plus 30 minutes.
    Writes every expert that were inicially given and the ones that were matched in the schedule,
    have their date, time and acumulated amount updated.
    Writes the .txt file name with the date, scope and time, also updated with 30 plus minutes
    Requires: expertsFile is str, the name of a .txt file listing experts, following the format specified in the project.
              clientsFile is str, the name of a .txt file listing clients, following the format specified in the project.
    Ensures: Returns a file with all experts their updated information
    """
    
    time = filesReading.readHeader(expertsFile)[constants.indexHeaderTime]
    date = filesReading.readHeader(expertsFile)[constants.indexHeaderDay]
    fileOut = open(dateTime.nameFile(time,date)[2]+'y'+dateTime.nameFile(time,date)[3]+'m'+dateTime.nameFile(time,date)[4]+'experts'+dateTime.nameFile(time,date)[0]+'h'+dateTime.nameFile(time,date)[1]+'.txt','w')
    fileOut.write('Day:\n')
    fileOut.write(dateTime.add30Mins(time,date)[1]+'\n')
    fileOut.write('Time:\n')
    fileOut.write(dateTime.add30Mins(time,date)[0]+'\n')
    fileOut.write('Company:\n')
    fileOut.write(filesReading.readHeader(expertsFile)[constants.indexHeaderCompany]+'\n')
    fileOut.write('Experts:\n')
    for e in range (len(filesReading.readExpertsFile(expertsFile))):
        fileOut.write(str(scheduling.updateExpert(expertsFile,clientsFile)[e][constants.expertName])+', ')
        fileOut.write(str(scheduling.updateExpert(expertsFile,clientsFile)[e][constants.expertLocation])+', ')
        fileOut.write('('+str(scheduling.updateExpert(expertsFile,clientsFile)[e][constants.expertAbility].strip(' ').replace(' ','; ')+'), '))
        fileOut.write(str(scheduling.updateExpert(expertsFile,clientsFile)[e][constants.expertRating])+', ')
        fileOut.write(str(scheduling.updateExpert(expertsFile,clientsFile)[e][constants.expertPrice])+', ')
        fileOut.write(str(scheduling.updateExpert(expertsFile,clientsFile)[e][constants.expertDateLastRequest])+', ')
        fileOut.write(str(scheduling.updateExpert(expertsFile,clientsFile)[e][constants.expertTimeLastRequest])+', ')
        fileOut.write(str(scheduling.updateExpert(expertsFile,clientsFile)[e][constants.expertFullAmount])+'\n')
    fileOut.close()
    return fileOut

def writeScheduleFile(expertsFile,clientsFile):
    """
    Writes the header updated with plus 30 minutes.
    Writes every match client/expert and their respect date and time that the appointment should start
    Writes the .txt file name with the date, scope and time, also updated with 30 plus minutes
    Requires: expertsFile is str, the name of a .txt file listing experts, following the format specified in the project.
              clientsFile is str, the name of a .txt file listing clients, following the format specified in the project.
    Ensures: Returns a file with all the scheduled appointments
    """

    time = filesReading.readHeader(expertsFile)[constants.indexHeaderTime]
    date = filesReading.readHeader(expertsFile)[constants.indexHeaderDay]
    fileOut = open(dateTime.nameFile(time,date)[2]+'y'+dateTime.nameFile(time,date)[3]+'m'+dateTime.nameFile(time,date)[4]+'schedule'+dateTime.nameFile(time,date)[0]+'h'+dateTime.nameFile(time,date)[1]+'.txt','w')
    fileOut.write('Day:\n')
    fileOut.write(dateTime.add30Mins(filesReading.readHeader(expertsFile)[constants.indexHeaderTime],filesReading.readHeader(expertsFile)[constants.indexHeaderDay])[1]+'\n')
    fileOut.write('Time:\n')
    fileOut.write(dateTime.add30Mins(filesReading.readHeader(expertsFile)[constants.indexHeaderTime],filesReading.readHeader(expertsFile)[constants.indexHeaderDay])[0]+'\n')
    fileOut.write('Company:\n')
    fileOut.write(filesReading.readHeader(expertsFile)[constants.indexHeaderCompany]+'\n')
    fileOut.write('Experts:\n')
    for s in range (len(scheduling.compareExpertsClients(expertsFile,clientsFile))):
        fileOut.write(str(scheduling.compareExpertsClients(expertsFile,clientsFile)[s][constants.scheduleDate])+', ')
        fileOut.write(str(scheduling.compareExpertsClients(expertsFile,clientsFile)[s][constants.scheduleHour])+', ')
        fileOut.write(str(scheduling.compareExpertsClients(expertsFile,clientsFile)[s][constants.scheduleClient])+', ')
        fileOut.write(str(scheduling.compareExpertsClients(expertsFile,clientsFile)[s][constants.scheduleExpert])+'\n')
    fileOut.close()
