# Functions to handle files
import os
import re
import shutil
import pickle
from collections import defaultdict
from pprint import pprint
from hachoir_core.error import HachoirError
from hachoir_core.cmd_line import unicodeFilename
from hachoir_parser import createParser
from hachoir_core.tools import makePrintable
from hachoir_metadata import extractMetadata
from hachoir_core.i18n import getTerminalCharset



# Extracts the time from the name
def extract_date_from_filename(filename):
    expr_1 = r"(2016([0-9]){4})[_](([0-9]){6})$"
    expr_2 = r"(2016([0-9]){4})[-](WA([0-9]){4})$"
    match=re.search(expr_1, filename)
    if match==None:
        match=re.search(expr_2, filename)
    if match!=None:
        res=str(match.group(0))
        res=res.replace('-', '_')
        return res 
    return None



# Extracts the time from the current image/video
def get_time_from_metadata(filename):
    filename, realname = unicodeFilename(filename), filename
    parser = createParser(filename, realname)
    if not parser:
        print ("Unable to parse file " + filename)
        return None
    try:
        metadata = extractMetadata(parser)
    except HachoirError, err:
        print "Metadata extraction error: %s" % unicode(err)
        metadata = None
    if not metadata:
        print "Unable to extract metadata"
        return None
    res = None
    # See what keys you can extract
    for k,v in metadata._Metadata__data.iteritems():
        if v.values:
            if v.key == 'creation_date':
                res = str(v.values[0].value)
    if res!=None :
        res = res.replace(':','')
        res = res.replace('-','')
        res = res.replace(' ','') 
    return res



# Extracts the name and the extension from the current file
def extract_file_names( file_path ):
        file_path_no_ext=""
        file_ext = ""
        path_to_file=""
        file_name = ""
        file_path_no_ext, file_ext = os.path.splitext(file_path)
        path_to_file, file_name = os.path.split(file_path_no_ext)     
        return file_name, file_ext
  

# Tells if the current file is a video or an image     
def is_image_or_video( file_path ):
        list_image_ext = ['.jpg', '.jpeg', '.JPG', '.JPEG', '.png', '.PNG']
        list_video_ext = ['.mp4', '.MP4' ,'.mov', '.MOV', '.avi', '.AVI']
        file_name=""
        file_ext =""
        file_name, file_ext = os.path.splitext(file_path) 
        if file_ext in list_image_ext : return True
        elif file_ext in list_video_ext : return True
        return False
                

# Copies object from location to another
def copy_file(orig,dest):
    try:
        shutil.copy(orig,dest)
    except Exception,e:
        print ("Error while copying %s to %s" % (orig, dest))
        print str(e)
        






        
