## ProgrammZIEL: BackUppen: Kopiert Ordner+Inhalt verschiedener QuellOrte an gemeinsamen ZielOrt:
    ## --> den BackUp-DatumsOrdner[BU-Directory] (legt diesen zuvor an (checkt davor ob er bereits existiert))
    ## LAUFENDE_PROGRAMME vor dem Ausführen des BackUp-Programms schließen (wg.PermissionErrors)
    ## "CHECKSUM"[Anzahl&Größe]-Abgleich (jeweils von Quelle/Source & Ziel/Destination) per CountnSize_Function.py  (Aufrufen der externen ProgrammFunktion)


from datetime import datetime
import os
import shutil
import sys
import time
## Module Search Path List -> ADDING PATH of/for CountnSize-Function	(falls CountnSize_Function.py sich außerhalb des ProgrammOrdners befindet)
#sys.path.append(r'X:\another\path\somewhere\else')
from CountnSize_Function import *


###  PATHS  ############################################################

##  Quell
des = r"C:\Users\user\Desktop"
dow = r"C:\Users\user\Downloads"
hea = r"C:\Users\user\xyz_xyz"
roa = r"C:\Users\user\AppData\Roaming"	
scr = r"C:\Users\user\Pictures\Screenshots"

##  Ziel										# LaufwerksBuchstabe zuweisen
ddhr = r"Z:\BU_DDHR"

##  LIST of SourcePaths
src_pathList = [des, dow, hea, roa, scr]

##  CREATE NAME[path] of BU-Directory							# BU-Directory itself will be CREATEd while copying 
dat = datetime.today().strftime('%Y%m')
bu_dir = ddhr + '\\' + dat + '_DL5480'

print("\nBefore copying : Show BU_DDHR-Folder Contents : \n")
for i in os.listdir(ddhr):
	print(i)


input('\n\nReady to start copying? Firefox & Thunderbird closed? \nPress ENTER...')


###  CHECK if BU-Directory ALREADY EXISTS  ############################# Decide what to do if yes
###  IF_NOT : CREATE BU-Directory  #####################################

if os.path.exists(bu_dir):
	print('\n\nBU(-Directory) already exists! Whatcha wanna do?')
	## DELETE
	inp = input('Delete? (j/ )\n')
	if inp == 'j':
		try:
			shutil.rmtree(bu_dir)
			print('\n' + bu_dir + " \nBU(-Directory) already existed ...and was now deleted")
		except PermissionError:
			print('\n\nCAN NOT DELETE: "PermissionError : Zugriff verweigert"\n')
			print('   Going on makes no sense because there will be FileAlreadyExistsErrors later on while copying...')
			print('   You will have to Delete manually for now...')
			sys.exit(input('   Press ENTER to exit the program...'))
		except:
			print('\n\nCAN NOT DELETE: Something else went other than "PermissionError"\n')
			print('   Going on makes no sense because there will be FileAlreadyExistsErrors later on while copying...')
			print('   You will have to Delete manually for now...')
			sys.exit(input('   Press ENTER to exit the program...'))
	else:
		## TIMER/CountDown
		print('\nProgram exits in 5sec...')
		for i in range(5,0,-1):
			print(i)
			time.sleep(1)
		sys.exit('0')


###  COPY Directories  #################################################
									  
print('\n\nCreating BU-Directory "...\\' + dat + '_DL5480" & BU-SubDirectories... \n\n ...Copying... ')
print('\n----------------------------------------------------------------------------')
for j in src_pathList:
	tail = os.path.split(j)[1]								# QuellOrdnerPfad splitten um QuellOrdnerName zu erhalten
	print('\n' + tail)
	bu_dir_sub = bu_dir + '\\' + tail							# ZielVerzeichnisPfadName anlegen mithilfe QuellOrdnerName
	try:
		shutil.copytree(j, bu_dir_sub)							# KopierVorgang => dirs_exist_ok=True NICHT_NÖTIG solang ZielVerzeichnis (->BU-UnterOrdner) vorher noch nicht existiert -> übergeordneter_BU-Folder DARF_BEREITS_EXISTIEREN! -> copytree() gibt FM falls BU-SubFolder bereits existieren
		print('BU-Directory Contents :', os.listdir(bu_dir), '\n')
		print(' ...No Errors occurred...')
	except shutil.Error:
		print('\n\n!!! ERROR !!! \n\nSomething went wrong while Copying, probably "[Errno 13] Permission denied", probably because a file was already open or non-existent, because Firefox or Thunderbird or some other Program is still running and working with those files...\n\n')
	except:
		print('\n\n!!! ERROR !!! \n\nSomething went wrong while Copying, maybe another type of Error (other than shutil.Error), maybe something else. \nRun Program in IDE to find  out..\n\n')
	CountnSize(j,bu_dir_sub)								# Anzahl&Größe mit externer Funktion
	print('\n----------------------------------------------------------------------------')


###  SHOW BU-Directory Contents  #######################################

print("\n\nCopy-Job done! \n\n\nAfter copying : Show BU-Directory Contents : \n")
for i in os.listdir(bu_dir):
	print(i)


###  Programm beenden  #################################################

input("\n\nZum Beenden ENTER drücken...")
