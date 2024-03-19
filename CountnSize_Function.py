###  VERGLEICH / "CHECKSUM" zweier Pfade/Ordner(&UnterOrdner)
	###  Anzahl Dateien&Ordner und Summen-Größe aller Files eines Pfads werden mit denen des anderen vergleichen 
		 ###  Zusätzl.: Checks ob Pfade identisch sind oder nicht existieren 
	###  erweiterbar auf CheckSum/Vergleich (aller Files) über Hashs (CHECKSUM : hashlib : md5 , blake2b)



import os 
import glob
import pathlib
import sys



def CountnSize(path1,path2):

	#####  ÜBERPRÜFUNG der PFADE  ##########################################
		
	###  CHECK : Beide Pfade identisch?									# Sind beide Pfade identisch UND non-existent wird das hier nicht geprüft
	
	while path1 == path2: 													
		print("\nBeide Pfade sind identisch. Bitte gebe 2 unterschiedliche Pfade ein: \n(Zum sofortigen Beenden 2mal ENTER drücken)\n")
		path1 = input("Gebe den 1sten Pfad zum Überprüfen ein: \n")	
		path2 = input("Gebe den 2ten Pfad zum Vergleichen ein: \n")
		if (path1 or path2) == "":
			sys.exit("\nProgramm wird beendet...")
			
	###  CHECK : Existieren die Pfade? Schreibfehler?
	
	if not os.path.exists(path1) or not os.path.exists(path2):
		print("\nEiner oder beide der eingegebenen Pfade existieren nicht. \nStarte das Programm anschließend erneut und versuche es noch einmal.")
		input("\n\nZum Beenden ENTER drücken...")
		sys.exit("\nProgramm wird beendet...")
	
		
	#####  IDENTIFIKATION & SORTIERUNG : Dateien & Ordner  #################
	
	print("\nVergleich der VerzeichnisInhalte läuft...\n")
	
	###  Alle Folder&SubFolder durchblättern und in eine Liste packen, später Pfade zählen & deren Größe ermitteln
	
	pathList1_all = glob.glob(path1 + '/**/*', recursive=True)				# Matches all objects in the current directory and in all following subdirectories
	pathList2_all = glob.glob(path2 + '/**/*', recursive=True)
	
	###  Alle Ordner in eigene Liste
	
	pathList1_dir = []
	for p1_1 in pathList1_all:
		if os.path.isdir(p1_1): 
			pathList1_dir.append(p1_1)
	
	pathList2_dir = []
	for p2_1 in pathList2_all:
		if os.path.isdir(p2_1): 
			pathList2_dir.append(p2_1)
	
	###  Alle Dateien in eigene Liste
	
	pathList1_fil = []
	for p1_2 in pathList1_all:
		if os.path.isfile(p1_2):
			pathList1_fil.append(p1_2)
	
	pathList2_fil = []
	for p2_2 in pathList2_all:
		if os.path.isfile(p2_2):
			pathList2_fil.append(p2_2)


	#####  STARTE VERGLEICH  ###############################################
	
	### ZÄHLEN / COUNT 
	
	# path1 : Alle
	cnt1_all = 0
	for i in pathList1_all:
		cnt1_all = cnt1_all + 1

	# path1 : Ordner
	cnt1_dir = 0
	for i in pathList1_dir:
		cnt1_dir = cnt1_dir + 1
	
	# path1 : Files
	cnt1_fil = 0
	for i in pathList1_fil:
		cnt1_fil = cnt1_fil + 1	
	
	# path2 : Alle
	cnt2_all = 0
	for i in pathList2_all:
		cnt2_all = cnt2_all + 1
	
	# path2 : Ordner
	cnt2_dir = 0
	for i in pathList2_dir:
		cnt2_dir = cnt2_dir + 1
	
	# path2 : Files
	cnt2_fil = 0
	for i in pathList2_fil:
		cnt2_fil = cnt2_fil + 1


	print("Anzahl_Objekte[path1/src] : " + str(cnt1_all)     + " : Ordner: " + str(cnt1_dir)     + " , Dateien: " + str(cnt1_fil)     + " , Andere: " + str(cnt1_all-cnt1_dir-cnt1_fil))				# "Andere" ist Kontrolle -> Und: Gibt es UFOs [UnidentifiedFileObjects] ? -> Bisher nicht...:)
	print("Anzahl_Objekte[path2/dst] : " + str(cnt2_all)     + " : Ordner: " + str(cnt2_dir)     + " , Dateien: " + str(cnt2_fil)     + " , Andere: " + str(cnt2_all-cnt2_dir-cnt2_fil))
	
	
	### GRÖßE / SIZE
	
	sizeSum1 = 0 
	for j in pathList1_fil: 
		size1 = os.stat(j).st_size
		sizeSum1 = sizeSum1 + size1
	print("Größe_Summe[path1/src]:", sizeSum1/(1000*1000),"MB")
	
	sizeSum2 = 0 
	for j in pathList2_fil: 
		size2 = os.stat(j).st_size
		sizeSum2 = sizeSum2 + size2
	print("Größe_Summe[path2/dst]:", sizeSum2/(1000*1000),"MB")																		

	
	print("\nVergleich der VerzeichnisInhalte abgeschossen.\n")
	
	
	#####  FAZIT_VERGLEICH  ################################################
	
	if (cnt1_all != cnt2_all) or (cnt1_dir != cnt2_dir) or (cnt1_fil != cnt2_fil):
		print("ALERT! ALERT! ALERT!    Anzahl an Dateien&Ordnern beider Verzeichnisse stimmt nicht überein!")
	else:
		print("NICE! NICE! NICE!    Anzahl an Dateien&Ordnern beider Verzeichnisse stimmt überein!")
	
	if sizeSum1 != sizeSum2 :
		print("ALERT! ALERT! ALERT!    Größe der Dateien         beider Verzeichnisse stimmt nicht überein!")
	else:
		print("NICE! NICE! NICE!    Größe der Dateien         beider Verzeichnisse stimmt überein!")
