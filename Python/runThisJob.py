import configparser
import sys

# Globals

#   Get Section name as a argument.  Note: It could be multiple sections / environments. Enhance to that later
#   Also put checking in regards to args coming in. Maybe none

print(sys.argv[1], "\n")
print(sys.argv[2], "\n")
# targetEnv = sys.argv[2]

confiG = configparser.ConfigParser()

confiG.read(sys.argv[1])
print(confiG.sections())
workingOnSection    =   confiG[sys.argv[2]]
userName            =   workingOnSection.get('userName')
serverName          =   workingOnSection.get('serverName')
smbTargets          =   workingOnSection.get('smbTargets')

print("Credentials --> USERNAME = ", userName, "\tSERVERNAME = ", serverName, "\tSMBTARGETS = ", smbTargets, "\n")






