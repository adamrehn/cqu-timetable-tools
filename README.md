CQUniversity Timetable Tools
============================

This repository contains tools designed to enhance the functionality of the [CQUniversity Timetable](https://handbook.cqu.edu.au/facet/timetables/index). The following tools are included:

- [**export-ics.py**](#exporting-calendar-events) - exports timetable events as an [iCalendar](https://en.wikipedia.org/wiki/ICalendar) (RFC 5545) file, suitable for importing into most common calendar software.
- [**export-json.py**](#exporting-json-data) - exports timetable events as raw JSON data, suitable for consumption and further processing by other tools.


## Requirements and installation

The scripts in this repository all require [Python](https://www.python.org/) 3.5 or newer, as well as the dependency packages listed in the file [requirements.txt](./requirements.txt).

To install the dependencies, simply run:

```
pip3 install -r requirements.txt
```


## Exporting calendar events

Timetable events can be exported to iCalendar format using the script [export-ics.py](./export-ics.py). The usage syntax is as follows (note that you may need to use `python` instead of `python3` under Windows):

```
python3 export-ics.py OUTFILE.ICS CAMPUS TERM SUBJECT1 SUBJECT2 ... SUBJECTN
```

For example, to export the timetable events for the subject [COIT11222](https://handbook.cqu.edu.au/he/units/view/COIT11222) for Term 1 on the Cairns campus and store the results in a file called `timetable.ics`, you would run:

```
python3 export-ics.py timetable.ics CNS 1 COIT11222
```

Wildcards are also supported. For example, to export the timetable events for all IT subjects, you would run:

```
python3 export-ics.py timetable.ics CNS 1 COIT*
```

See the file [common/Campus.py](./common/Campus.py) for a list of supported campus codes.


## Exporting JSON data

The usage syntax of [export-json.py](./export-json.py) is identical to that of [export-ics.py](./export-ics.py). See the section [Exporting calendar events](#exporting-calendar-events) for usage examples.


## Legal

Copyright &copy; 2019, Adam Rehn. Licensed under the MIT License, see the file [LICENSE](./LICENSE) for details.
