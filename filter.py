import os
from file_services import copy_file
from file_services import get_time_from_metadata
from file_services import extract_date_from_filename
from file_services import is_image_or_video
from file_services import extract_file_names

def recursive_visit (files_path, built_name , dico ):
        root, dirnames, filenames = next(os.walk(files_path))
        count = len(filenames)
        for subdirname in dirnames:
                new_path = os.path.join(files_path, subdirname)
                new_built_name=''
                if not built_name: new_built_name = str(subdirname)
                else: new_built_name = built_name + '_' + str(subdirname)
                recursive_visit (new_path, new_built_name , dico )
        for filename in filenames:
                if is_image_or_video( filename ):
                        file_path = os.path.join(files_path, filename)
                        file_name, file_ext = extract_file_names( file_path )
                        time_shot = get_time_from_metadata(file_path)
                        if time_shot == None:
                                time_shot=extract_date_from_filename(file_name)
                        pre_final_name = str(built_name)  + '_' + file_name + file_ext
                        final_name = str(time_shot) + '_' + str(pre_final_name)
                        # Construction of the path
                        final_name=final_name.lower()
                        built_path = ''
                        built_path = built_name.replace('_','\\')
                        built_path = os.path.join(built_path, final_name)
                        print ("Adding %s as path" %built_path )
                        dico[file_path]=built_path


# Serialization
def serialize_dico (dico, output_path):
        bufsize = 0
        path = str(output_path) + '\\dico.pkl'
        try:
            output = open(path, 'w', bufsize)
            pickle.dump(dico, output)
            output.close()
        except Exception,e: 
                print ("Error in serialization process")
                print str(e)
                
def main():
        input_dir='C:\\Users\\Yassir\\Pictures\\Trips\\Asia'
        user_dir='All'
        output_dir = 'C:\\Users\\Yassir\\Downloads\\Asia\\'
        built_name = ''
        dico = {}
        print "#### Starting recursive visit ###"
        path_to_visit = os.path.join(input_dir,user_dir)
        recursive_visit (path_to_visit, built_name , dico )
        print "#### Starting serialization process ###"
        serialize_dico (dico, output_dir)
        print "#### Starting copy process ###"
        for k,v in dico.items():
                final_path=''
                final_path = os.path.join(output_dir,user_dir)
                final_path = os.path.join(final_path,v)
                copy_file (k , final_path)
        exit(0)
                

if __name__ == "__main__":
    main()


