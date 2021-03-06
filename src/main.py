from os import listdir, mkdir, rename
from os.path import splitext, exists, isdir

extensions = ['.png','.jpg','.jpeg','.tif','.tiff']

def createMarkDown(path,filename):
    path += filename
    if not exists(path):
        with open(path,'w'):
            print("Successfully Created the file %s" % path)
            return True
    else:
        print("The file %s exists" % path)
        return True
    return False

def appendToMarkDown(filepath,text):
    if exists(filepath):
        my_file = open(filepath,'a+')
        text+="\n"
        my_file.write(text)
        my_file.close()
        return True
    else:
        return False

def createDir(path,dir):
    try:
        if not (isdir(path+dir)):
            mkdir(path+dir)
        else: 
            print ("The directory %s exists " % (path+dir))
            return True
    except OSError:
        print ("Creation of the directory %s failed" % path+dir)
        return False;
    print ("Successfully created the directory %s " % path+dir)
    return True;

def moveFile(src_path,dst_path):
    if exists(src_path):
        rename(src_path,dst_path)
        return True
    else:
        return False

def main():

    path="../test_folder/"

    ## keep a master list of all the documents at path
    if(isdir(path)):
        content_list_in_path = listdir(path)

    ## holds image names
    image_list_in_path = []

    ## get all the files in the path
    for f in content_list_in_path:
        if f.endswith(tuple(extensions)):
            image_list_in_path.append(f)
        print(f)

    # check and create README.md at path
    readme_path = path+"README.md"
    res_path = path+"res/"
    if not createMarkDown(readme_path,""):
        print("Incomplete")
        return
    if not createDir(res_path,""):
        print("Incomplete")
        return

    res_path = path+"res/"

    # move create edit 
    for file in image_list_in_path:
        src_file_name = path+file
        dst_file_name = res_path+file

        file_without_ext,ext = splitext(file)
        markdown_file_to_link = file_without_ext+".md"
        createMarkDown(path,markdown_file_to_link)

        res_link_relative_path = "res/"+file
        text_to_append = "![image]("+res_link_relative_path+") \n"
        appendToMarkDown(path+markdown_file_to_link,text_to_append)

        text_to_append_readme = "   - ["+file_without_ext+"]"+"("+markdown_file_to_link+")"
        appendToMarkDown(readme_path,text_to_append_readme)
        moveFile(src_file_name,dst_file_name)

        print(file)


if __name__ == "__main__":
    main()