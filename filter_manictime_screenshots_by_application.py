#-----------------------------------------------------------------------------
# Name:        Filter Screenshots by Application
# Purpose:     Filters and copies Filenames based on Application Tags exported from Manictime
#
# Author:      Henning Krol
#
# Created:     18.01.2017
# Copyright:   (c) Henning Krol 2017
# Licence:     Do what you want, I'm not responsible
#-----------------------------------------------------------------------------
# encoding=utf8

import os
import csv
from os import listdir
from os.path import isfile, join
from datetime import datetime
from dateutil import parser
from shutil import copyfile


def only_fusion(row):
    return 'Fusion x64 7.01' in row.values()


def main():
    csvFile = r"d:\temp\manictime_screenshots\ManicTimeData_2017-03-28.csv"
    screenshotsFolder = r"d:\temp\manictime_screenshots\2017-03-28"
    filteredFolder = r"z:\projekte\187_MPM_neon\05_comp\makingof\bosch_canvas"

    onlyfiles = [f for f in listdir(screenshotsFolder) if isfile(join(screenshotsFolder, f))]
    files = filter(lambda k: "thumbnail" not in k, onlyfiles)
    selectedFiles = set()

    with open(csvFile) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in filter(only_fusion, reader):
            start = parser.parse(row["Start"])
            end = parser.parse(row["End"])

            for f in files:
                date = datetime.strptime(f.split('.')[0], "%Y-%m-%d_%H-%M-%S")

                if start < date < end:
                    selectedFiles.add(f)

        for f in selectedFiles:
            copyfile(join(screenshotsFolder, f), join(filteredFolder, f))

if __name__ == '__main__':
    main()
