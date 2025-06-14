#-*-coding:utf-8-*-
# 2018-2019 ProgramaÃ§Ã£o 1 (LTI)
# Grupo 39
# David Garcia - 53748
# JoÃ£o Nunes - 53745



def minsInt(time):
    """
    Returns the minutes of a given time in the format "hh:mm".
    Requires: time as str, respecting the format.
    Ensures: returns minutes as int.
    """

    time = str(time)
    mins = time.split(":")
    return int(mins[1])

def hoursInt(time):
    """
    Returns the hour of a given time in the format "hh:mm".
    Requires: time as str, respecting the format.
    Ensures: returns hours as int.
    """
    
    time = str(time)
    hour = time.split(":")
    return int(hour[0])

def solveHours(time):
    """
    Returns the hours of the time the expert takes to complete the task in the format specified in the project (ex: 4h00).
    Requires: time as str, respecting the format.
    Ensures: returns hours as int
    """
    hours = time.split("h")
    return int(hours[0])

def solveMins(time):
    """
    Returns the mins of the time the expert takes to complete the task in the format specified in the project (ex: 4h00).
    Requires: time as str, respecting the format
    Ensures: returns mins as int
    """

    mins = time.split("h")
    return int(mins[1])

def solveTime(time):
    """
    Returns the hours plus the mins converted to decimal format (ex:10h30 == 10.5).
    Requires: time as str, respecting the format
    Ensures: returns hours as float
    """

    hours = solveHours(time) + (solveMins(time)/60)
    return hours

def doubleDigitTime(hour, mins):
    """
    If hours or mins > 10, adds a '0' behind them so they can be shown in the hh:mm format.
    Rquires: hour and mins as str.
    Ensures: returns hours and minutes as str in the hh:mm format
    """
    hStr = str(hour)
    mStr = str(mins)    

    if hour < 10:
        hStr = "0" + hStr

    if mins < 10:
        mStr = "0" + mStr

    return hStr+":"+mStr

def dayInt(date):
    """
    Returns the day of a given date in the format "yyyy-mm-dd".
    Requires: date as str, respecting the format.
    Ensures: returns day as int.
    """

    day = date.split("-")
    return int(day[2])

def monthInt(date):
    """
    Returns the month of a given date in the format "yyyy-mm-dd".
    Requires: date as str, respecting the format.
    Ensures: returns month as int.
    """

    month = date.split("-")
    return int(month[1])

def yearInt(date):
    """
    Returns the year of a given date in the format "yyyy-mm-dd".
    Requires: date as str, respecting the format.
    Ensures: returns year as int.
    """

    year = date.split("-")
    return int(year[0])

def doubleDigitDate(year, month, day):
    """
    If day or month > 10, adds a '0' behind them so they can be shown in the mm-dd format.
    Requires: year, month and day as str.
    Ensures: returns year, month and day as str in the format yyyy-mm-dd format.
    """

    dayStr = str(day)
    monthStr = str(month)
    yearStr = str(year)

    if day < 10:
        dayStr = "0" + dayStr

    if month < 10:
        monthStr = "0" + monthStr

    return yearStr+ "-" + monthStr + "-" + dayStr

def add30Mins(time,date):
    """
    Returns time and date with 30 minutes added
    Requires: time and date str in the format hh:mm and yyyy-mm-dd
    Ensures: Returns time and date plus 30 minutes in the respecting formats
    """
    
    hour = hoursInt(time)
    mins = minsInt(time)
    day = dayInt(date)
    month = monthInt(date)
    year = yearInt(date)
    if mins == 00:
        mins = 30
    elif mins == 30:
        mins = 00
        hour = hour + 1
        if hour >= 24:
            hour = 00
            day = day + 1
            if day >= 31:
                month = month + 1
                day = day - 30
                if month >= 13:
                    year = year + 1
                    month = 1
                    
    return doubleDigitTime(hour,mins), doubleDigitDate(year, month, day)


def compareDatesTimes(dateClient,timeClient,dateExpert,timeExpert):
    """
    Compares two dates to see which one is the newest and if the expert's hour has less than a hour difference between
    the clients hour, adds a hour to the expert's time which is the time that the experts takes to travel
    Requires: dateClient and dateExpert as str in the format yyyy-mm-dd, and timeClient and timeExpert as str in the format hh:mm
    Ensures: Returns the latest date of the two in the respecting formats, as str
    """
    minsClient = minsInt(timeClient)
    hoursClient = hoursInt(timeClient)
    dayClient = dayInt(dateClient)
    monthClient = monthInt(dateClient)
    yearClient = yearInt(dateClient)

    minsExpert = minsInt(timeExpert)
    hoursExpert = hoursInt(timeExpert)
    dayExpert = dayInt(dateExpert)
    monthExpert = monthInt(dateExpert)
    yearExpert = yearInt(dateExpert)

    if -1 <= hoursInt(timeExpert) - hoursInt(timeClient) <= 1 or dayInt(dateExpert)-dayInt(dateClient) >= 1 or monthInt(dateExpert)-monthInt(dateClient) >= 1 or yearInt(dateExpert)-yearInt(dateClient) >= 1:
        hoursExpert= hoursExpert + 1
        if minsExpert >= 60:
            minsExpert = minsExpert - 60
            hoursExpert = hoursExpert + 1
        
        if hoursExpert >= 20:
            hoursExpert = hoursExpert - 12
            dayExpert = dayExpert + 1
            if dayExpert >= 31:
                monthExpert = monthExpert + 1
                dayExpert = dayExpert - 30
                if monthExpert >= 13:
                    yearExpert = yearExpert + 1
                    monthExpert = 1
                    
        return doubleDigitDate(yearExpert, monthExpert, dayExpert), doubleDigitTime(hoursExpert,minsExpert)
    
    if yearClient == yearExpert:
        if monthClient == monthExpert:
            if dayClient == dayExpert:
                if hoursClient == hoursExpert:
                    if minsClient == minsExpert:          
                        return dateClient,timeClient               
                    elif minsClient > minsExpert:         
                        return dateClient,timeClient
                    else:
                        return dateExpert,timeExpert
                elif hoursClient > hoursExpert:
                    return dateClient,timeClient
                else:
                    return dateExpert,timeExpert
            elif dayClient > dayExpert:
                return dateClient,timeClient
            else:
                return dateExpert,timeExpert
        elif monthClient > monthExpert:
            return dateClient,timeClient
        else:
            return dateExpert,timeExpert
    elif yearClient > yearExpert:
        return dateClient,timeClient
    else:
        return dateExpert,timeExpert


def updateExpertTime(timeSolve,expertDate,expertTime,clientTime,clientDate):
    """
    Updates the time the expert is available, depending on the time the client is going
    to be attended, the time of the trip and the time it takes to complete the task.
    Requires: timeSolve as str in the format 4h00, expertDate and clientDate as str
    Ensures: returns the date and the time that we need, with the conditions that we gave.
    """

    hourSolve = solveHours(timeSolve)
    minsSolve = solveMins(timeSolve)
    hourExpert = hoursInt(expertTime)
    minsExpert = minsInt(expertTime)
    dayExpert = dayInt(expertDate)
    monthExpert = monthInt(expertDate)
    yearExpert = yearInt(expertDate)
    minsSum = minsExpert + minsSolve
    hourSum = hourExpert + hourSolve

    if -1 >= hoursInt(expertTime) - hoursInt(clientTime) >= 1 or dayInt(expertDate)-dayInt(clientDate) >= 1 or monthInt(expertDate)-monthInt(clientDate) >= 1 or yearInt(expertDate)-yearInt(clientDate) >= 1:
        hourSum = hourSum + 1
           
    if minsSum >= 60:
        minsSum = minsSum - 60
        hourSum = hourSum + 1
        
    if hourSum >= 20:
        hourSum = hourSum - 12
        dayExpert = dayExpert + 1
        if dayExpert >= 31:
            monthExpert = monthExpert + 1
            dayExpert = dayExpert - 30
            if monthExpert >= 13:
                yearExpert = yearExpert + 1
                monthExpert = 1
                    
    return doubleDigitTime(hourSum,minsSum), doubleDigitDate(yearExpert, monthExpert, dayExpert)


def nameFile(time,date):
    """
    Returns a given date to the format needed to name the .txt file (ex:2019y03m20schedule13h00)
    Requires: time and date str in the formats hh:mm and yyyy-mm-dd
    Ensures: returns date and time in order for the respecting format
    """

    time1 = (add30Mins(time,date)[0]).split(':')
    date1 = (add30Mins(time,date)[1]).split('-')
    hour = time1[0]
    mins = time1[1]
    year = date1[0]
    month = date1[1]
    day = date1[2]

    return hour, mins, year, month, day


