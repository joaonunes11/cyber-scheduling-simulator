#-*-coding:utf-8-*-
# 2018-2019 ProgramaÃ§Ã£o 1 (LTI)
# Grupo 39
# David Garcia - 53748
# JoÃ£o Nunes - 53745

import sys
import filesWriting
import filesReading
import constants

def assign(fileNameExperts, fileNameClients):
    """
    Obtain the assigment of clients given to experts.
    Assign given experts given to given clients.
    Requires: fileNameExperts, fileNameClients are str, with the names
    of the files representing the list of experts and clients, respectively,
    following the format indicated in the project.
    Ensures: Two output files, respectively, with the listing of schedules
    tasks and the updated listing of experts, following the format
    and naming convention indicated in the project.
    """
    for f in [fileNameExperts,fileNameClients]:
        headerDay = filesReading.readHeader(f)[constants.indexHeaderDay]
        headerTime = filesReading.readHeader(f)[constants.indexHeaderTime]
        headerType = filesReading.readHeader(f)[constants.indexHeaderType][1:-1]
        fileNameDay = f[:10]
        fileNameTime = f[-9:-4]
        fileNameType = f[11:-9]
        
        if headerType != fileNameType:
            raise IOError("Error in input file: inconsistent name and header in file ",f)

        if headerTime[0:2] != fileNameTime[0:2] or headerTime[-2:] != fileNameTime[-2:]:
            raise IOError("Error in input file: inconsistent name and header in file ",f)

        if headerDay[:4] != fileNameDay[:4] or headerDay[5:7] != fileNameDay[5:7] or headerDay[8:10] != fileNameDay[8:10]:            
            raise IOError("Error in input file: inconsistent name and header in file ",f)

    if filesReading.readHeader(fileNameExperts)[:-1] != filesReading.readHeader(fileNameClients)[:-1]:
        raise IOError("Error in input files: inconsistent files" + fileNameExperts + " and "+fileNameClients)
    
    filesWriting.writeExpertsFile(fileNameExperts,fileNameClients)
    filesWriting.writeScheduleFile(fileNameExperts,fileNameClients)

inputFileName1, inputFileName2 = sys.argv[1:]

assign(inputFileName1, inputFileName2)
