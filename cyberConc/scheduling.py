#-*-coding:utf-8-*-
# 2018-2019 ProgramaÃ§Ã£o 1 (LTI)
# Grupo 39
# David Garcia - 53748
# JoÃ£o Nunes - 53745

import filesReading
import constants
import dateTime
import operator

def compareExpertsClients(expertsFile,clientsFile):
    """
    Takes one expert and compares the ability, location, rating and the payment with the need's of a client
    if the expert doesn't satisfy the client's, the expert changes to the next one and get's compared to the same client and so on
    until there are no experts that satisfy that client's needs, if so, the client gets labeled "decline"
    if the expert satisfies the client's needs, they get put on a list, with both names and the date and time that the appointment should start
    also orders the matchs from the soonest to the latest date of the appointment
    Requires: expertsFile is str, the name of a .txt file listing experts, following the format specified in the project.
              clientsFile is str, the name of a .txt file listing clients, following the format specified in the project.
    Ensures: list with the declined clients on top, and the sucessful matchs following it
    """

    schedule = []
    expertsList = filesReading.readExpertsFile(expertsFile)
    clientsList = filesReading.readClientsFile(clientsFile)
    tempList1 = []
    tempList2 = []
    
    final_list = []
    semi_list = []

    for c in range (len(clientsList)):
        for e in range (len(expertsList)):
            dateClient = clientsList[c][constants.clientRequestDate]
            hourClient = clientsList[c][constants.clientRequestHour]
            dateExpert = expertsList[e][constants.expertDateLastRequest]
            hourExpert = expertsList[e][constants.expertTimeLastRequest]
            if clientsList[c][constants.clientRequestAbility] in expertsList[e][constants.expertAbility]:
                if clientsList[c][constants.clientLocation] == expertsList[e][constants.expertLocation]:
                    if clientsList[c][constants.clientMinRating] <= expertsList[e][constants.expertRating]:
                        if float(clientsList[c][constants.clientMaxPayment]) >= float(expertsList[e][constants.expertPrice]):
                            if clientsList[c][constants.clientName] not in tempList1:
                                tempList1.append(clientsList[c][constants.clientName])
                                schedule.append([dateTime.compareDatesTimes(dateClient,hourClient,dateExpert,hourExpert)[0],dateTime.compareDatesTimes(dateClient,hourClient,dateExpert,hourExpert)[1],clientsList[c][constants.clientName],expertsList[e][constants.expertName]])

    schedule.sort(key = operator.itemgetter(constants.scheduleDate,constants.scheduleHour,constants.scheduleClient))
    
    for k in range(len(schedule)):
        tempList2.append(schedule[k][constants.scheduleClient])

    for j in range (len(clientsList)):
        if clientsList[j][constants.clientName] not in tempList2:
            final_list.append([dateTime.add30Mins(filesReading.readHeader(expertsFile)[constants.indexHeaderTime],filesReading.readHeader(expertsFile)[constants.indexHeaderDay])[1],dateTime.add30Mins(filesReading.readHeader(expertsFile)[constants.indexHeaderTime],filesReading.readHeader(expertsFile)[constants.indexHeaderDay])[0],clientsList[j][constants.clientName],"declined"])

    final_list.sort(key = operator.itemgetter(constants.scheduleClient))


    for i in schedule:
        final_list.append(i)

    return final_list

def updateExpert(expertsFile,clientsFile):
    """
    Using the same structure of the previous function, if the match is sucessful, updates the experts availability (date and time) for the next job
    and updates the accummulated amount that the expert has earned (multiplies the job duration with the price per hour of the expert)
    Requires: expertsFile is str, the name of a .txt file listing experts, following the format specified in the project.
              clientsFile is str, the name of a .txt file listing clients, following the format specified in the project.
    Ensures: experts list update with the available date and time for the next job, and the updated accummulated amount that the expert has earn, ordered from the earliest availability to the latest.
    """

    expertsList = filesReading.readExpertsFile(expertsFile)
    clientsList = filesReading.readClientsFile(clientsFile)
    tempList1 = []
    for c in range (len(clientsList)):
        for e in range (len(expertsList)):
            dateClient = clientsList[c][constants.clientRequestDate]
            hourClient = clientsList[c][constants.clientRequestHour]
            dateExpert = expertsList[e][constants.expertDateLastRequest]
            hourExpert = expertsList[e][constants.expertTimeLastRequest]
            newestDate = dateTime.compareDatesTimes(dateClient,hourClient,dateExpert,hourExpert)[0]
            newestHour = dateTime.compareDatesTimes(dateClient,hourClient,dateExpert,hourExpert)[1]
            if clientsList[c][constants.clientRequestAbility] in expertsList[e][constants.expertAbility]:
                if clientsList[c][constants.clientLocation] == expertsList[e][constants.expertLocation]:
                    if clientsList[c][constants.clientMinRating] <= expertsList[e][constants.expertRating]:
                        if float(clientsList[c][constants.clientMaxPayment]) >= float(expertsList[e][constants.expertPrice]):
                            if clientsList[c][constants.clientName] not in tempList1:
                                tempList1.append(clientsList[c][constants.clientName])
                                expertsList[e][constants.expertFullAmount] = float(expertsList[e][constants.expertFullAmount])+(dateTime.solveTime(clientsList[c][constants.clientSolveTime])*float(expertsList[e][constants.expertPrice]))
                                expertsList[e][constants.expertTimeLastRequest] = dateTime.updateExpertTime(clientsList[c][constants.clientSolveTime],dateExpert,hourExpert,hourClient,dateClient)[0]
                                expertsList[e][constants.expertDateLastRequest] = dateTime.updateExpertTime(clientsList[c][constants.clientSolveTime],dateExpert,hourExpert,hourClient,dateClient)[1]
                             

    expertsList.sort(key = operator.itemgetter(constants.expertDateLastRequest,constants.expertTimeLastRequest,constants.clientName))

    return expertsList


