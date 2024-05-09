import pandas as pd
import os, json


# read students.json
f = open('students.json')
students = json.load(f)

paths = [
  {'name': 'Class 1', 'path': 'Week_01'},
  {'name': 'Class 2', 'path': 'Week_02'},
  {'name': 'Class 2.5', 'path': 'Week_02.5'},
]


def getMeetingInfo(path):
  # read and get meetingInfo
  meetingInfo = pd.read_csv(path, nrows=1)
  meetingInfo = meetingInfo.to_dict('records')[0]
  print(meetingInfo)
  return meetingInfo


def getParticipants(path):
  # read csv
  # skip lines 0, 1, 2
  # only use columns 0 (Name) & 2 (Duration)
  df = pd.read_csv(path, skiprows=[0,1,2], usecols=[0,2])

  # rename columns
  df.rename(columns={"Name (Original Name)":"name", "Total Duration (Minutes)":"duration"},inplace=True)

  # convert df to dict
  participants = df.to_dict('records')

  for p in participants:
    p['name'] = p['name'].replace("#", ",")
    a = p['name'].partition(" (")   # partition always returns array[3]
    if (a[2]):
      p['name'] = a[0]
      p['alias'] = a[2].strip(")")

  print(participants)
  return participants
  




for p in paths:
  folderName = os.path.join("ZoomReports", p['path'])
  fileNames = os.listdir(folderName)
  for fileName in fileNames:
    if not fileName.startswith("."):
      csv = os.path.join(folderName, fileName)
      print(csv)
      print("\n")
      meetingInfo = getMeetingInfo(csv)
      participants = getParticipants(csv)








#df = rawDF[1:2]
#df.columns = rawDF[:1].values[0]    # add header from row 0
#df.reset_index(drop=True, inplace=True)
#meetingDF = df.loc[:, df.columns.notna()]  # remove cols with NaN as name
#print(meetingDF)

#df = rawDF[3:]
#df.columns = rawDF[2:3].values[0]
#df = df.loc[:, df.columns.notna()]  # remove cols with NaN as name
#df.drop(columns=['User Email', 'Guest'], inplace=True)
#df.rename(columns={"Name (Original Name)":"Name", "Total Duration (Minutes)":"Duration"}, inplace=True)
#df.reset_index(drop=True, inplace=True)

#df.Name = df.Name.str.replace('#', ',')
#df.Name.str.split(" ")

#print(df)