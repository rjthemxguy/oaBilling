#!/usr/bin/env python
# coding: utf-8


import pandas as pd
import sqlite3 as lite
import numpy as np
import sys
import csv
import mysql.connector
import DBModule as db

lines = "--------------------------------------------------------------------"

database = db.database_class("rjrobinson.net", "rjrob_admin", "hapkido", "rjrob_vernonDB")

summaryPath = "summary"
outputPath = "output"
inputPath = "input/"

dataFile = "claims1.csv"

# desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')


pd.options.display.max_rows = None
pd.options.display.max_columns = None

print(lines)
print("                 CLAIMS PROCESSING APPLICATION")
print("")
print("                    Vernon Oates, CPA, Inc")
print("")
print("           AUTHORIZED USERS ONLY  - ALL RIGHTS RESERVED")
print(lines)

print("")
print("Please rename your input file to 'input.csv' and place it in the 'input' folder")
print("")
print("Your processed file will be placed in the 'output' folder")
print("Your summary file will be in the 'summary' folder")
print("")

input("Please press any key to process your claims")
print("")


def numIn(s):
    return any(i.isdigit() for i in s)


class dataRowClass:

    def __init__(self):

        try:
            # Open raw csv file
            with open(inputPath + dataFile, 'r') as file:
                filedata = file.read()
                print("--- Data file loaded ---")
        except:
            print("-----------------------------------------------")
            print("ERROR OPENING INPUT FILE")
            print("-----------------------------------------------")
            print("Please make sure input file is in the 'Input' directory and is named 'input.csv'")
            print("and then run the program again")

            exit(1)

        # Remove quotation marks
        filedata = filedata.replace('"', '')

        # Save file as csv    
        with open('scratch/cleaned.csv', 'w') as file:
            file.write(filedata)

        with open('scratch/cleaned.csv', 'r') as csvfile:
            # creating a csv reader object
            csvreader = csv.reader(csvfile)

            with open('scratch/cleanedSuite.csv', "w", newline='') as result:
                writer = csv.writer(result)

                for row in csvreader:

                    if numIn(row[4]) == True:
                        row[3] = row[3] + row[4]
                        del row[4]

                    if numIn(row[27]) == True:
                        row[26] = row[26] + row[27]
                        del row[27]

                    if numIn(row[33]) == True:
                        row[32] = row[32] + row[33]
                        del row[33]

                    if "SUITE" in row[345]:
                        row[344] = row[344] + row[345]
                        row[345] = ""

                        del row[345]

                    print(row[14])

                    writer.writerow(row)

        # Open dataset csv
        self.dataset = pd.read_csv("scratch/goodclaims.csv", header=None)

        # Set row index to 0
        self.index = 0
        self.totalRows = (self.dataset.shape[0])

    def getDataSet(self):
        return self.dataset

    def getPatientSig(self):
        return (self.PatientFirst[0] + self.PatientLast[0])

    def getDataRowCount(self):
        return self.totalRows

    def dataRowExists(self):
        if self.index < (self.getDataRowCount() - 1):
            return True
        else:
            return False

    def incrementIndex(self):
        self.index += 1

    def resetIndex(self):
        self.index = 0

    def loadRow(self):
        self.InsurancePlanName = self.dataset.iloc[self.index, 1]
        self.InsurancePayerID = self.dataset.iloc[self.index, 2]
        self.InsuranceStreetAddr = self.dataset.iloc[self.index, 3]
        self.InsuranceCity = isNan(self.dataset.iloc[self.index, 4])
        self.InsuranceState = isNan(self.dataset.iloc[self.index, 5])
        self.InsuranceZip = isNan(str(self.dataset.iloc[self.index, 6]))
        self.InsuranceCityStateZip = self.InsuranceCity + " " + self.InsuranceState + " " + self.InsuranceZip
        self.PlanGroupHealthPlan = self.dataset.iloc[self.index, 14]
        self.PatientID = int(self.dataset.iloc[self.index, 17])
        self.PatientLast = self.dataset.iloc[self.index, 18]
        self.PatientFirst = self.dataset.iloc[self.index, 19]
        self.InsuredFirst = self.PatientFirst
        self.InsuredLast = self.PatientLast
        self.PatientMidInit = self.dataset.iloc[self.index, 20]
        self.InsuredMidInit = self.PatientMidInit
        self.PatientDOB = self.dataset.iloc[self.index, 21]
        self.Gender = self.dataset.iloc[self.index, 22]
        self.PatientStreetAddress = isNan(self.dataset.iloc[self.index, 26])
        self.PatientCity = isNan(self.dataset.iloc[self.index, 27])
        self.PatientState = isNan(self.dataset.iloc[self.index, 28])
        self.PatientZip = (self.dataset.iloc[self.index, 29])
        self.PatientPhone = isNan(self.dataset.iloc[self.index, 30])
        self.PatientSignatureDate = self.dataset.iloc[self.index, 61]
        self.ReferringPhysician = self.dataset.iloc[self.index, 75] + " " + self.dataset.iloc[self.index, 76]
        self.ReferPhysQualifier = self.dataset.iloc[self.index, 77]
        self.Refer_Phys_NPI = self.dataset.iloc[self.index, 78]
        self.DiagCode1 = self.dataset.iloc[self.index, 86]
        self.DiagCode2 = self.dataset.iloc[self.index, 87]
        self.DiagCode3 = self.dataset.iloc[self.index, 88]
        self.DiagCode4 = self.dataset.iloc[self.index, 89]
        self.DiagCode5 = self.dataset.iloc[self.index, 90]
        self.DiagCode6 = self.dataset.iloc[self.index, 91]
        self.DiagCode7 = self.dataset.iloc[self.index, 92]
        self.DiagCode8 = self.dataset.iloc[self.index, 93]
        self.DiagCode9 = self.dataset.iloc[self.index, 94]
        self.DiagCode10 = self.dataset.iloc[self.index, 95]
        self.DiagCode11 = self.dataset.iloc[self.index, 96]
        self.DiagCode12 = self.dataset.iloc[self.index, 97]
        self.FromDateOfService = self.dataset.iloc[self.index, 102]
        self.ToDateOfService = self.dataset.iloc[self.index, 103]
        self.CPT1 = self.dataset.iloc[self.index, 106]
        self.EMG = self.dataset.iloc[self.index, 105]
        self.DiagCode = self.dataset.iloc[self.index, 107]
        self.ReferringPhysicianID = self.dataset.iloc[self.index, 116]
        self.Session = self.dataset.iloc[self.index, 362]

    def setGender(self):
        if self.Gender == "F":
            oaTemplate.at[templateIndex, "PatientFemale"] = 1
            oaTemplate.at[templateIndex, "PatientMale"] = ""

        else:
            oaTemplate.at[templateIndex, "PatientFemale"] = ""
            oaTemplate.at[templateIndex, "PatientMale"] = 1

    def getPatientID(self):
        return self.PatientID


def isNan(numToTest):
    if isinstance(numToTest, str) == 1:
        return numToTest

    if np.isnan(numToTest) == 1:
        return ""


class claimClass:

    def __init__(self, rowData):

        # Open OA Template File
        self.oaTemplate = pd.read_csv("template/OATemplate.csv", header=0)

        # Set index to 0
        self.index = 0
        self.rowData = rowData
        self.cptIndex = 1
        self.totalCharges = 0
        self.claimTotal = 0
        self.claimCount = 0
        self.totalOfClaimsForClientAmount = 0
        self.noEMGList = []
        self.claimMarkCount = 0

    def parseSummary(self):

        with open("summary/summary.txt", 'r') as file:
            summarydata = file.read()

            summarydata = summarydata.replace('nan', '')

        with open('summary/summaryFinal.txt', 'w') as file:
            file.write(summarydata)

    def openSummaryFileAppend(self):

        # Open summary file to append
        self.summaryFile = open(summaryPath + '/summary.txt', 'a')

    def closeSummaryFile(self):
        self.summaryFile.close()

    def writeSummaryHeader(self):

        # Open summary file to write
        self.summaryFile = open(summaryPath + '/summary.txt', 'w')
        self.summaryFile.write("-- CLAIM SUMMARY --\n\n")

        self.summaryFile.write("Accession #".ljust(19, " "))
        self.summaryFile.write("PaitID".ljust(8, " "))
        self.summaryFile.write("PaitLast".ljust(15, " "))
        self.summaryFile.write("PaitFirst".ljust(15, " "))
        self.summaryFile.write("DOB".ljust(15, " "))
        self.summaryFile.write("M/F".ljust(8, " "))
        self.summaryFile.write("Refer Phy".ljust(30, " "))
        self.summaryFile.write("Refer Phy NPI".ljust(20, " "))
        self.summaryFile.write("Insurance".ljust(30, " "))

        self.summaryFile.write(
            "\n________________________________________________________________________________________________________________________________________")

        self.summaryFile.close()

    def writeSummaryClaimHeader(self, claim):

        self.claimCount += 1

        self.summaryFile = open(summaryPath + '/summary.txt', 'a')

        session = claim["Session"]
        self.summaryFile.write("\n\n" + "[" + str(self.claimCount) + "]" + " " + str(session).ljust(15, " "))

        patientID = claim["PatientID"]
        self.summaryFile.write(str(patientID).ljust(8, " "))

        patientLast = claim["PatientLast"]
        self.summaryFile.write(str(patientLast).ljust(15, " "))

        patientFirst = claim["PatientFirst"]
        self.summaryFile.write(str(patientFirst).ljust(15, " "))

        self.summaryFile.write(str(claim["PatientDOB"].ljust(15, " ")))

        self.summaryFile.write(str(claim["Gender"].ljust(8, " ")))

        ReferringPhysician = claim["ReferringPhysician"] + " " + claim["ReferPhysQualifier"]
        self.summaryFile.write(str(ReferringPhysician).ljust(30, " "))

        NPI = claim["Refer_Phys_NPI"]
        self.summaryFile.write(str(NPI).ljust(20, " "))

        insurance = claim["InsurancePlanName"]
        self.summaryFile.write(insurance.ljust(30, " "))
        self.summaryFile.write("\n")
        self.summaryFile.write(" ".ljust(28, " ") + str(claim["PatientStreetAddress"].ljust(25, " ")))
        self.summaryFile.write(" ".ljust(79, " ") + str(claim["InsuranceStreetAddr"]))
        self.summaryFile.write("\n")
        self.summaryFile.write(" ".ljust(28, " ") + str(claim["PatientCity"].ljust(16, " ")))
        self.summaryFile.write(" " + str(claim["PatientState"].ljust(8, " ")))
        self.summaryFile.write(" " + str(claim["PatientZip"])[0:5].ljust(12, " "))
        self.summaryFile.write(" ".ljust(66, " ") + str(claim["InsuranceCity"]))
        self.summaryFile.write(" " + str(claim["InsuranceState"]))
        self.summaryFile.write(" " + str(claim["InsuranceZip"])[0:5])

        self.summaryFile.write("\n\n")

        self.summaryFile.write("\t" + "Group ID: " + str(claim["PlanGroupHealthPlan"]))
        self.summaryFile.write("\n")
        self.summaryFile.write("\t")
        self.summaryFile.write("Diag Codes: ")
        self.summaryFile.write(isNan(str(claim["DiagCode1"])).ljust(8, " "))
        self.summaryFile.write(str(claim["DiagCode2"]).ljust(8, " "))
        self.summaryFile.write(str(claim["DiagCode3"]).ljust(8, " "))
        self.summaryFile.write(str(claim["DiagCode4"]).ljust(8, " "))
        self.summaryFile.write(str(claim["DiagCode5"]).ljust(8, " "))
        self.summaryFile.write(str(claim["DiagCode6"]).ljust(8, " "))
        self.summaryFile.write(str(claim["DiagCode7"]).ljust(8, " "))
        self.summaryFile.write(str(claim["DiagCode8"]).ljust(8, " "))
        self.summaryFile.write(str(claim["DiagCode9"]).ljust(8, " "))
        self.summaryFile.write(str(claim["DiagCode10"]).ljust(8, " "))
        self.summaryFile.write(str(claim["DiagCode11"]).ljust(8, " "))
        self.summaryFile.write(str(claim["DiagCode12"]).ljust(8, " "))

        self.summaryFile.write("\n\n")

        self.summaryFile.write("\t\t")
        # self.summaryFile.write(" ".ljust(6, " "))
        self.summaryFile.write("CPT".ljust(10, " "))
        self.summaryFile.write("Price".ljust(10, " "))
        self.summaryFile.write("EMG".ljust(12, " "))
        self.summaryFile.write("Frm Date Srv".ljust(15, " "))
        self.summaryFile.write("To Date Srv".ljust(15, " "))
        self.summaryFile.write("\n")
        self.summaryFile.write("\t\t")
        self.summaryFile.write("----------------------------------------------------------------------")
        self.summaryFile.write("\n")

        self.summaryFile.close()

    def claimTotal(self):
        return self.claimTotal

    def writeClaimTotal(self):
        self.oaTemplate.at[self.index, "TotalCharges"] = self.claimTotal
        self.oaTemplate.at[self.index, "BalanceDue"] = self.claimTotal
        # self.summaryFile.write("\n\t\tTotal for this claim: " + str(round(self.claimTotal,2)))
        # self.summaryFile.write("\n\n")

    def writeTestBlock(self, claim, blockIndex, lineCount):

        totalOfClaim = 0
        blockIndex = str(blockIndex)

        self.oaTemplate.at[self.index, "CPT" + blockIndex] = claim["CPT"]
        self.oaTemplate.at[self.index, "EMG" + blockIndex] = claim["EMG"]
        self.oaTemplate.at[self.index, "ModifierA" + blockIndex] = ""
        self.oaTemplate.at[self.index, "ModifierB" + blockIndex] = ""
        self.oaTemplate.at[self.index, "ModifierC" + blockIndex] = ""
        self.oaTemplate.at[self.index, "ModifierD" + blockIndex] = ""
        self.oaTemplate.at[self.index, "DiagCodePointer" + blockIndex] = ""
        self.oaTemplate.at[self.index, "Charges" + blockIndex] = claim["Price"]
        self.oaTemplate.at[self.index, "Units" + blockIndex] = "1"
        self.oaTemplate.at[self.index, "ToDateOfService" + blockIndex] = claim["ToDateOfService"]
        self.oaTemplate.at[self.index, "FromDateOfService" + blockIndex] = claim["FromDateOfService"]
        self.oaTemplate.at[self.index, "PlaceOfService" + blockIndex] = "11"
        self.oaTemplate.at[self.index, "RenderingPhysQualifier" + blockIndex] = "MD"
        self.oaTemplate.at[self.index, "RenderingPhysID" + blockIndex] = claim["ReferringPhysicianID"]
        self.oaTemplate.at[self.index, "RenderingPhysNPI" + blockIndex] = claim["Refer_Phys_NPI"]
        self.oaTemplate.at[self.index, "DiagCode" + blockIndex] = claim["DiagCode1"]
        self.oaTemplate.at[self.index, "DiagCodePointer" + blockIndex] = ""

        floatPrice = str(round(float(claim["Price"]), 2))

        self.claimTotal = self.claimTotal + claim["Price"]

        self.summaryFile = open(summaryPath + '/summary.txt', 'a')
        self.summaryFile.write("\t\t")
        self.summaryFile.write(str(claim["CPT"]).ljust(10, " "))
        self.summaryFile.write(floatPrice.ljust(10, " "))
        self.summaryFile.write(str(claim["EMG"]).ljust(12, " "))
        self.summaryFile.write(str(claim["FromDateOfService"]).ljust(15, " "))
        self.summaryFile.write(str(claim["ToDateOfService"]).ljust(15, " "))
        self.summaryFile.write("\n")
        self.summaryFile.close()

    def incrementCPTIndex(self):
        self.cptIndex += 1

    def resetCPTIndex(self):
        self.cptIndex = 1

    def setGender(self):
        if self.claimRow["Gender"] == "F":
            self.oaTemplate.at[self.index, "PatientFemale"] = 1
            self.oaTemplate.at[self.index, "PatientMale"] = ""

        else:
            self.oaTemplate.at[self.index, "PatientFemale"] = ""
            self.oaTemplate.at[self.index, "PatientMale"] = 1

    def getPatientSig(self):
        return (self.rowData.PatientFirst[0] + self.rowData.PatientLast[0])

    def showClaims(self):
        return self.oaTemplate

    def getDataSet(self):
        return self.rowData.getDataSet()

    def showHeader(self):
        print(self.oaTemplate.head())

    # Increment index    
    def incrementIndex(self):
        self.index += 1
        self.cptIndex = 1
        self.claimTotal = 0

    def writeClaimsToFile(self):
        self.oaTemplate.to_csv("scratch/oaClaims.csv", header=False, index=False)

        with open('scratch/oaClaims.csv', 'r') as csvfile:
            # creating a csv reader object
            csvreader = csv.reader(csvfile)

            with open('scratch/noBlanks.csv', "w", newline='') as result:
                writer = csv.writer(result)

                for row in csvreader:

                    if row[2] != "":
                        writer.writerow(row)

        with open('scratch/noBlanks.csv', 'r') as tabFile:
            tabFiledata = tabFile.read()

            tabFiledata = tabFiledata.replace(',', '\t')

        with open(outputPath + '/tabClaims.txt', 'w') as tabFile:
            tabFile.write(tabFiledata)

    def totalOfClaimsForClient(self, claims):
        claimTotal = 0

        for claim in claims:
            claimTotal = claimTotal + claim["Price"]

        return claimTotal

    def doClientClaimList(self):

        sameClient = True
        clientID = 0
        claimList = []
        endOfClaims = False

        clientID = self.rowData.PatientID

        while sameClient:

            self.claimRow = {
                "printYN": "Y",
                "InsurancePlanName": self.rowData.InsurancePlanName,
                "InsurancePayerID": self.rowData.InsurancePayerID,
                "InsuranceStreetAddr": self.rowData.InsuranceStreetAddr,
                "InsuranceCity": self.rowData.InsuranceCity,
                "InsuranceState": self.rowData.InsuranceState,
                "InsuranceZip": self.rowData.InsuranceZip,
                "InsuranceCityStateZip": self.rowData.InsuranceCityStateZip,
                "PlanGroupHealthPlan": self.rowData.PlanGroupHealthPlan,
                "PatientID": self.rowData.PatientID,
                "PatientLast": self.rowData.PatientLast,
                "PatientFirst": self.rowData.PatientFirst,
                "InsuredFirst": self.rowData.InsuredFirst,
                "InsuredLast": self.rowData.InsuredLast,
                "PatientMidInit": self.rowData.PatientMidInit,
                "InsuredMidInit": self.rowData.InsuredMidInit,
                "PatientDOB": self.rowData.PatientDOB,
                "Gender": self.rowData.Gender,
                "PatientStreetAddress": self.rowData.PatientStreetAddress,
                "PatientCity": self.rowData.PatientCity,
                "PatientState": self.rowData.PatientState,
                "PatientZip": self.rowData.PatientZip,
                "PatientPhone": self.rowData.PatientPhone,
                "PatientSignatureDate": self.rowData.PatientSignatureDate,
                "ReferringPhysician": self.rowData.ReferringPhysician,
                "ReferPhysQualifier": self.rowData.ReferPhysQualifier,
                "Refer_Phys_NPI": self.rowData.Refer_Phys_NPI,
                "DiagCode1": self.rowData.DiagCode1,
                "DiagCode2": self.rowData.DiagCode2,
                "DiagCode3": self.rowData.DiagCode3,
                "DiagCode4": self.rowData.DiagCode4,
                "DiagCode5": self.rowData.DiagCode5,
                "DiagCode6": self.rowData.DiagCode6,
                "DiagCode7": self.rowData.DiagCode7,
                "DiagCode8": self.rowData.DiagCode8,
                "DiagCode9": self.rowData.DiagCode9,
                "DiagCode10": self.rowData.DiagCode10,
                "DiagCode11": self.rowData.DiagCode11,
                "DiagCode12": self.rowData.DiagCode12,
                "FromDateOfService": self.rowData.FromDateOfService,
                "ToDateOfService": self.rowData.ToDateOfService,
                "CPT": self.rowData.CPT1,
                "EMG": self.rowData.EMG,
                "DiagCode": self.rowData.DiagCode,
                "DiagPointer": "",
                "Price": "",
                "ReferringPhysicianID": self.rowData.ReferringPhysicianID,
                "Session": self.rowData.Session
            }

            # append claim dict to claim list
            claimList.append(self.claimRow)

            # increment data index and get new row 
            if (self.rowData.index < (self.rowData.getDataRowCount() - 1)):
                dataRow.incrementIndex()
                self.rowData.loadRow()

            else:
                endOfClaims = True
                self.incrementIndex()

            # if client still the same?
            # if end of claims for current client, parse claims
            if clientID != self.rowData.PatientID or endOfClaims == True:
                parsedClaims = self.parseClaims(claimList)

                self.totalOfClaimsForClientAmount = self.totalOfClaimsForClient(parsedClaims)

                self.writeSummaryClaimHeader(parsedClaims[0])
                self.writeTestBlocks(parsedClaims)

                break

    def writeTestBlocks(self, claims):

        # set count indexes
        lineCount = 1
        blockIndex = 1
        blocksWritten = 0

        # loop through claims
        for claim in claims:

            if blockIndex == 1:
                self.writeClaimHeader(claim)

            self.writeTestBlock(claim, blockIndex, lineCount)
            blocksWritten += 1

            # increment counters

            blockIndex += 1
            lineCount += 1

            # check if 6 have been written or if at end of claims
            if blockIndex == 7 and lineCount != (len(claims) + 1):
                self.writeClaimTotal()

                # write new header for new line
                self.incrementIndex()
                # self.writeClaimHeader(claim)

                # if written 6, reset index for next claim
                blockIndex = 1
                diagPointerIndex = 0

        self.writeClaimTotal()
        self.incrementIndex()

        self.summaryFile = open(summaryPath + '/summary.txt', 'a')
        self.summaryFile.write("\n\t\t\t" + "Total for this claim: ")
        self.summaryFile.write(str(round(self.totalOfClaimsForClientAmount, 2)))
        self.summaryFile.write("\n")
        self.summaryFile.write("______________________________________________________________________________________")
        self.summaryFile.close()

    def getDiagCode(self, EMGcode):

        # open database
        con = None
        con = lite.connect('db/vernon.db')
        cur = con.cursor()

        cur.execute("SELECT diag FROM codes WHERE code=?", (EMGcode,))
        row = cur.fetchone()

        if row != None:
            return row[0]

        else:
            print("NO ENTRY FOR CODE: " + EMGcode)

    def queryCode(self, EMGcode):

        CPTPrice = {
            "CPT": "",
            "Price": 0
        }

        row = database.getCPT(EMGcode)

        if row is not None:
            CPTPrice["CPT"] = row[0]
        else:
            CPTPrice["CPT"] = "00000"
            self.noEMGList.append(EMGcode)

        # get price from CPT lookup and put in dict
        if CPTPrice["CPT"] != "00000":
            row = database.getPrice(CPTPrice["CPT"])

            CPTPrice["Price"] = float(row[0])

        return CPTPrice



    def getTableData(self, claimList):

        # iterate throuh claims    
        for claim in claimList:
            CPTPrice = self.queryCode(claim["EMG"])

            claim["CPT"] = CPTPrice["CPT"]
            claim["Price"] = CPTPrice["Price"]

    def doDiagCodes(self, claimList):

        pointerIndex = 0
        diagPointers = ["A", "B", "C", "D", "E", "F"]
        diagCodeList = []

        for diag_claim in claimList:

            if self.getDiagCode(diag_claim["EMG"]) in diagCodeList:
                print("")

            else:
                diagCodeList.append(self.getDiagCode(diag_claim["EMG"]))
                diag_claim["DiagPointer"] = diagPointers[pointerIndex]

    def checkForLP2lab(self, claimList):

        labcount = 0

        for lp2_claim in claimList:

            if "LP" in lp2_claim.values():
                labcount += 1
                LPClaim = lp2_claim

            if "LDLD" in lp2_claim.values():
                labcount += 1
                LDLDClaim = lp2_claim

            if labcount == 2:
                dict_LPprice = self.queryCode("LP")
                dict_LDLDprice = self.queryCode("LDLD")

                LPprice = dict_LPprice["Price"]
                LDLDprice = dict_LDLDprice["Price"]

                claimList.remove(LPClaim)
                LDLDClaim["EMG"] = "LP2"
                LDLDClaim["Price"] = LPprice + LDLDprice
                break

    def checkForLPLab(self, claimList):

        labCount = 0

        for claim in claimList:

            # check for 3 tests that make up panel
            if claim["EMG"] == "HDL":
                removeHDL = claim
                labCount += 1

            if claim["EMG"] == "CHOL":
                removeCHOL = claim
                labCount += 1

            if claim["EMG"] == "TRIG2":
                labCount += 1
                TRIGclaim = claim

            if labCount == 3:
                claimList.remove(removeCHOL)
                claimList.remove(removeHDL)

                TRIGclaim["EMG"] = "LP"
                TRIGclaim["CPT"] = "80061"

                CPTPrice = self.queryCode("LP")

                TRIGclaim["Price"] = CPTPrice["Price"]

                break

    def parseClaims(self, claimList):

        self.getTableData(claimList)

        self.checkForLPLab(claimList)

        self.checkForLP2lab(claimList)

        self.doDiagCodes(claimList)

        return claimList

    def writeClaimHeader(self, claim):

        print("*", end=" ")
        self.claimMarkCount += 1

        if self.claimMarkCount == 20:
            print("\n")
            self.claimMarkCount = 0

        self.oaTemplate.at[self.index, "ICD Indicator"] = ""
        self.oaTemplate.at[self.index, "InsurancePlanName"] = claim["InsurancePlanName"]
        self.oaTemplate.at[self.index, "InsurancePayerID"] = claim["InsurancePayerID"]
        self.oaTemplate.at[self.index, "InsuranceStreetAddr"] = claim["InsuranceStreetAddr"]
        self.oaTemplate.at[self.index, "InsuranceCity"] = claim["InsuranceCity"]
        self.oaTemplate.at[self.index, "InsuranceState"] = claim["InsuranceState"]
        self.oaTemplate.at[self.index, "InsuranceZip"] = claim["InsuranceZip"]
        self.oaTemplate.at[self.index, "InsuranceCityStateZip"] = claim["InsuranceCityStateZip"]
        self.oaTemplate.at[self.index, "InsurancePhone"] = ""
        self.oaTemplate.at[self.index, "PlanGroupHealthPlan"] = claim["PlanGroupHealthPlan"]
        self.oaTemplate.at[self.index, "PatientID"] = claim["PatientID"]
        self.oaTemplate.at[self.index, "PatientLast"] = claim["PatientLast"]
        self.oaTemplate.at[self.index, "PatientFirst"] = claim["PatientFirst"]
        self.oaTemplate.at[self.index, "PatientMidInit"] = isNan(claim["PatientMidInit"])
        self.oaTemplate.at[self.index, "PatientDOB"] = claim["PatientDOB"]
        self.oaTemplate.at[self.index, "InsuredLast"] = claim["InsuredLast"]
        self.oaTemplate.at[self.index, "InsuredFirst"] = claim["InsuredFirst"]
        self.oaTemplate.at[self.index, "InsuredMidInit"] = claim["InsuredMidInit"]
        self.oaTemplate.at[self.index, "PatientStreetAddress"] = claim["PatientStreetAddress"]
        self.oaTemplate.at[self.index, "PatientCity"] = claim["PatientCity"]
        self.oaTemplate.at[self.index, "PatientState"] = claim["PatientState"]
        self.oaTemplate.at[self.index, "PatientZip"] = claim["PatientZip"]
        self.oaTemplate.at[self.index, "PatientPhone"] = claim["PatientPhone"]
        self.oaTemplate.at[self.index, "PatientRelationSELF"] = 1
        self.oaTemplate.at[self.index, "PatientRelationSPOUSE"] = ""
        self.oaTemplate.at[self.index, "PatientRelationCHILD"] = ""
        self.oaTemplate.at[self.index, "PatientRelationOTHER"] = ""
        self.oaTemplate.at[self.index, "InsuredStreetAddress"] = ""
        self.oaTemplate.at[self.index, "InsuredCity"] = ""
        self.oaTemplate.at[self.index, "InsuredState"] = ""
        self.oaTemplate.at[self.index, "InsuredZip"] = ""
        self.oaTemplate.at[self.index, "InsuredPhone"] = ""
        self.oaTemplate.at[self.index, "PatientMaritalSingle"] = ""
        self.oaTemplate.at[self.index, "PatientMaritalMarried"] = ""
        self.oaTemplate.at[self.index, "PatientMaritalOther"] = ""
        self.oaTemplate.at[self.index, "PatientEmploymentEmployed"] = ""
        self.oaTemplate.at[self.index, "PatientEmploymentFullTimeStudent"] = ""
        self.oaTemplate.at[self.index, "PatientEmploymentPartTimeStudent"] = ""
        self.oaTemplate.at[self.index, "OtherInsuredLast"] = ""
        self.oaTemplate.at[self.index, "OtherInsuredFirst"] = ""
        self.oaTemplate.at[self.index, "OtherInsuredMidInit"] = ""
        self.oaTemplate.at[self.index, "OtherInsuredPolicyOrGroupNumber"] = ""
        self.oaTemplate.at[self.index, "OtherInsuredDOB"] = ""
        self.oaTemplate.at[self.index, "OtherInsuredSexMale"] = ""
        self.oaTemplate.at[self.index, "OtherInsuredSexFemale"] = ""
        self.oaTemplate.at[self.index, "OtherInsuredEmlpoyerNameOrSchoolName"] = ""
        self.oaTemplate.at[self.index, "OtherInsuredInsurancePlanorProgramName"] = ""
        self.oaTemplate.at[self.index, "CondtionRelatedToEmlpoymentYes"] = ""
        self.oaTemplate.at[self.index, "CondtionRelatedToEmlpoymentNo"] = ""
        self.oaTemplate.at[self.index, "CondtionRelatedToAutoAccidentYes"] = ""
        self.oaTemplate.at[self.index, "CondtionRelatedToAutoAccidentNo"] = ""
        self.oaTemplate.at[self.index, "AutoAccidentState"] = ""
        self.oaTemplate.at[self.index, "CondtionRelatedToOtherAccidentYes"] = ""
        self.oaTemplate.at[self.index, "CondtionRelatedToOtherAccidentNo"] = ""
        self.oaTemplate.at[self.index, "ReservedForLocalUse"] = ""
        self.oaTemplate.at[self.index, "InsuredPolicyGroupOrFecaNumber"] = ""
        self.oaTemplate.at[self.index, "InsuredDOB"] = ""
        self.oaTemplate.at[self.index, "InsuredGenderMale"] = ""
        self.oaTemplate.at[self.index, "InsuredGenderFemale"] = ""
        self.oaTemplate.at[self.index, "InsuredEmployerNameOrSchoolName"] = ""
        self.oaTemplate.at[self.index, "InsuredInsurancePlanNameOrProgramName"] = ""
        self.oaTemplate.at[self.index, "IsThereAnotherHealhPlanBenefitYes"] = ""
        self.oaTemplate.at[self.index, "IsThereAnotherHealhPlanBenefitNo"] = ""
        self.oaTemplate.at[self.index, "PatientSignature"] = "Signature on file"
        self.oaTemplate.at[self.index, "PatientSignatureDate"] = claim["PatientSignatureDate"]
        self.oaTemplate.at[self.index, "InsuredSignature"] = "Signature on File "
        self.oaTemplate.at[self.index, "DateOfCurrent"] = ""
        self.oaTemplate.at[self.index, "DateOfSimilarIllness"] = ""
        self.oaTemplate.at[self.index, "UnableToWorkFromDate"] = ""
        self.oaTemplate.at[self.index, "UnableToWorkToDate"] = ""
        self.oaTemplate.at[self.index, "ReferringPhysician"] = claim["ReferringPhysician"]
        self.oaTemplate.at[self.index, "ReferPhysQualifier"] = claim["ReferPhysQualifier"]
        self.oaTemplate.at[self.index, "ReferringPhysicianID"] = ""
        self.oaTemplate.at[self.index, "Refer_Phys_NPI"] = int(claim["Refer_Phys_NPI"])
        self.oaTemplate.at[self.index, "Super_Phys_NPI"] = ""
        self.oaTemplate.at[self.index, "HospitalizationFromDate"] = ""
        self.oaTemplate.at[self.index, "HospitalizationToDate"] = ""
        self.oaTemplate.at[self.index, "Box19Notes"] = ""
        self.oaTemplate.at[self.index, "OutsideLabChargesYes"] = ""
        self.oaTemplate.at[self.index, "OutsideLabChargesNo"] = ""
        self.oaTemplate.at[self.index, "OutsideLabFees"] = ""
        self.oaTemplate.at[self.index, "DiagCode1"] = claim["DiagCode1"]
        self.oaTemplate.at[self.index, "DiagCode2"] = claim["DiagCode2"]
        self.oaTemplate.at[self.index, "DiagCode3"] = claim["DiagCode2"]
        self.oaTemplate.at[self.index, "DiagCode4"] = claim["DiagCode4"]
        self.oaTemplate.at[self.index, "DiagCode5"] = claim["DiagCode5"]
        self.oaTemplate.at[self.index, "DiagCode6"] = claim["DiagCode6"]
        self.oaTemplate.at[self.index, "DiagCode7"] = claim["DiagCode7"]
        self.oaTemplate.at[self.index, "DiagCode8"] = claim["DiagCode8"]
        self.oaTemplate.at[self.index, "DiagCode9"] = claim["DiagCode9"]
        self.oaTemplate.at[self.index, "DiagCode10"] = claim["DiagCode10"]
        self.oaTemplate.at[self.index, "DiagCode11"] = claim["DiagCode11"]
        self.oaTemplate.at[self.index, "DiagCode12"] = claim["DiagCode12"]
        self.oaTemplate.at[self.index, "MedicaidResubCode"] = ""
        self.oaTemplate.at[self.index, "MedicaidRefNumber"] = ""
        self.oaTemplate.at[self.index, "PriorAuthNo"] = ""
        self.oaTemplate.at[self.index, "HCFACLIANumber"] = ""
        self.oaTemplate.at[self.index, "EMG1"] = ""
        self.oaTemplate.at[self.index, "PhysicianSignature"] = "Signature on File"
        self.oaTemplate.at[self.index, "PhysicianSignatureDate"] = claim["ToDateOfService"]
        self.oaTemplate.at[self.index, "PhysicianLast"] = "Prime Clinical"
        self.oaTemplate.at[self.index, "PhysicianFirst"] = "Lab"
        self.oaTemplate.at[self.index, "FacilityName"] = "Prime Clinical Lab"
        self.oaTemplate.at[self.index, "FacilityStreetAddr"] = "27825 Fremont Ct"
        self.oaTemplate.at[self.index, "FacilityCity"] = "Velencia"
        self.oaTemplate.at[self.index, "FacilityState"] = "CA"
        self.oaTemplate.at[self.index, "FacilityZip"] = "91355"
        self.oaTemplate.at[self.index, "FacilityCityStateZip"] = "Valencia CA 91355"
        self.oaTemplate.at[self.index, "FacilityNPI"] = "1871038778"
        self.oaTemplate.at[self.index, "SupplierName"] = "Prime Clinical Lab"
        self.oaTemplate.at[self.index, "SupplierStreetAddr"] = "27825 Fremont Ct"
        self.oaTemplate.at[self.index, "SupplierCity"] = "Velencia"
        self.oaTemplate.at[self.index, "SupplierState"] = "CA"
        self.oaTemplate.at[self.index, "SupplierZip"] = "91355"
        self.oaTemplate.at[self.index, "SupplierCityStateZip"] = "Valencia CA 91355"
        self.oaTemplate.at[self.index, "SupplierNPI"] = "1871038778"
        self.oaTemplate.at[self.index, "SupplierPhone"] = "(661) 253-1173"
        self.oaTemplate.at[self.index, "AcceptAssignYes"] = "1"
        self.oaTemplate.at[self.index, "PatientAcctNumber"] = claim["PatientID"]
        self.oaTemplate.at[self.index, "TaxID"] = "81-3301345"
        self.oaTemplate.at[self.index, "Session"] = claim["Session"]

        self.setGender()


dataRow = dataRowClass()
claim = claimClass(dataRow)

claim.writeSummaryHeader()

while (dataRow.dataRowExists()) == True:
    dataRow.loadRow()
    claim.doClientClaimList()

claim.writeClaimsToFile()
claim.parseSummary()

print("\n\n")
print(lines)
print("THE FOLLOWING EMG CODES ARE NOT IN THE DATABASE\n")

for code in claim.noEMGList:
    print(code)

print(lines)

print("")
print(lines)
print("         PROCESSING OF CLAIMS WAS SUCCESSFUL!")
print("")
print("           You can now retrieve your files")
print(lines)

# claim.showClaims()
