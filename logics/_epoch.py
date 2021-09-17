# resources: https://www.programiz.com/python-programming/datetime

from datetime import timezone


def EpochToISO8601(theEpoch):

    from datetime import datetime

    return datetime.fromtimestamp(theEpoch, timezone.utc).isoformat()


def ISO8601ToEpoch(theString):

    from datetime import datetime
    import calendar

    return calendar.timegm(datetime.strptime(theString, "%Y-%m-%dT%H:%M:%S.%fZ").timetuple()) # Not tested yet
