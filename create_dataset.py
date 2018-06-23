#!/usr/bin/python

import os
import sys
import re

#add filter for <i> and ' - '
#filter srt ttle and other infos

SRC_ENCODING = 'iso-8859-1'
DST_ENCODING = 'utf8'

def cleanupChars(text):
	return text.replace("<i>","").replace("</i>","").replace("-","");

def parse_subtitle(sub):
	s = sub.replace("\n"," ")
	t = s.split("|")
	id = t[0].strip()
	times = t[1].split("-->")
	ts = times[0].strip()
	te = times[1].strip()
	text = cleanupChars(" ".join(map(str.strip,t[2:])))
	return id+"|"+ts+"|"+te+"|"+text

def extract_file_subtitle_list(file_path):
	print("Processing file: {}".format(file_path))
	subtitles = list()
	sub = ""
	with open(file_path,'r',encoding=SRC_ENCODING) as file:
		for line in  file:
			if (line != "\n"):
				sub += line
				sub += " | "
			else:
				try:
					subtitles.append(parse_subtitle(sub))
					sub = ""
				except:
					print("Error in file: ", file_path)
					print("!!!SKIPPED!!!")
	return subtitles

def extract_subtitles_text_dataset(srt_dir):
	with open("dataset.txt",'w',encoding=SRC_ENCODING) as f:
		header = "seq_id|start_time|end_time|sentence\n"
		f.write(header)
		for srt_file in [os.path.join(srt_dir,x) for x in filter(lambda s : s.endswith(".srt"), os.listdir(srt_dir))]:
			for entry in extract_file_subtitle_list(srt_file):
				f.write("{}\n".format(entry))




if (len(sys.argv) != 2):
        print('<<<Usage: create_dataset [srt path dir]>>>')
        exit(-1)

srt_dir = sys.argv[1]

#print([os.path.join(srt_dir,x) for x in filter(lambda s : s.endswith(".srt"), os.listdir(srt_dir))])


#subs = extract_file_subtitle_list(sys.argv[1])

#print(subs[0])

#print(subs[21])

extract_subtitles_text_dataset(srt_dir)
