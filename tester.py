import re
from hachoir_core.error import HachoirError
from hachoir_core.cmd_line import unicodeFilename
from hachoir_parser import createParser
from hachoir_core.tools import makePrintable
from hachoir_metadata import extractMetadata
from hachoir_core.i18n import getTerminalCharset




# Extracts the time from the current image/video
def get_time_from_metadata(filename):
    filename, realname = unicodeFilename(filename), filename
    parser = createParser(filename, realname)
    if not parser:
        print >>stderr, "Unable to parse file"
        exit(1)
    try:
        metadata = extractMetadata(parser)
    except HachoirError, err:
        print "Metadata extraction error: %s" % unicode(err)
        metadata = None
    if not metadata:
        print "Unable to extract metadata"
        exit(1)
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



filename_1='20160511_164846'
filename_2='IMG-20160512-WA0076'
filename_3='IMG_3435'
filename_4='toto'


res = extract_date_from_filename(filename_1)
print('For file ' + filename_1 + ' res = ' + str(res))
res = extract_date_from_filename(filename_2)
print('For file ' + filename_2 + ' res = ' + str(res))
res = extract_date_from_filename(filename_3)
print('For file ' + filename_3 + ' res = ' + str(res))
res = extract_date_from_filename(filename_4)
print('For file ' + filename_4 + ' res = ' + str(res))


print'################ BEGIN'
file_path='C:\\Users\\Yassir\\my_images_organizer\\tests\\IMG_3435.jpg'
time=get_time_from_metadata(file_path)
print time
print'################ END'


