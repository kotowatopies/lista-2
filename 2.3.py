from zipfile import ZipFile
import os 
import datetime as dt
def buckup_zip(input_path, output_path):
    '''makes backup zip file of choosen directory
    arguments:
        input_path (str): path of directory to copy
        output_path (str): path to the folder where zip file is gonna be made
    raises:
        TypeError: raises when at least one variable has wrong type
        FileNotFound: raises when path to directory doesnt exist
        FileExistError: raises when zip file whth the same name already exist
    returns:
        None
    '''
    if not isinstance(input_path, str) or not isinstance(output_path, str):
        raise TypeError("at least one variable has wrong type")
    if not os.path.exists(input_path):
        raise FileNotFoundError("path to the directory doesnt exist")
    current_time = dt.datetime.now()
    prefix = current_time.strftime("%d_%m_%Y_%H-%M-%S")
    zipfile_name = f"{prefix}_{os.path.basename(input_path)}.zip"
    zipfile_path = os.path.join(output_path, zipfile_name) #czy dodawanie stringów?
    if os.path.exists(zipfile_path):
        raise FileExistsError("zip file with same name as directory exists")
    with ZipFile(zipfile_path, 'w') as zip:
        for dir_path, dir_names, file_names in os.walk(input_path):
            for file in file_names:
                file_path = os.path.join(dir_path, file) 
                zip.write(file_path, os.path.relpath(file_path))
    if os.path.exists(zipfile_path):
        print("ZIP file was created")
    else:
        print("something went wrong")

buckup_zip(r"E:\277477\programowanie\sem 2\lista 2\test_folder", r"E:\277477\programowanie\sem 2\lista 2")  
