# -*- coding: utf-8 -*-
"""
Spyder Editor
The default col for background substraction is 3rd. 
Change the code to process the entire folder.

"""


import pandas as pd
 

#This is the help file to combine the documents.
#Right now only use create_job. combine_data2 is not used.
#
def combine_data2(r_orig_data,g_orig_data,b_orig_data,red_bkg=0,green_bkg=0,blue_bkg=0):
    DAPI=b_orig_data
    green=g_orig_data
    red=r_orig_data

    bkg_r=red_bkg 
    bkg_g=green_bkg
    bkg_b=blue_bkg

    combine=pd.DataFrame(DAPI, columns=['Area', 'Mean','X','Y'])

    combine['green_nbkg']=green['Mean'].values-bkg_g
    combine['red_nbkg']=red['Mean'].values-bkg_r

    combine['blue_nbkg']=combine['Mean']-bkg_b
    combine.pop('Mean')
    return combine

def create_job(user_input_dir, file_names,user_input_bkg,col=3,new_name='fileName'):
    print(user_input_dir,file_names[0],user_input_bkg[0])
    file_names_temp=user_input_dir+file_names[0]
    try:
        files=pd.read_csv(file_names_temp, sep=",",header=0, index_col=False)
    except:  
        print("cannot read the first file, check file name, directory")
        return
    files.iloc[:,col]=files.iloc[:,col]-float(user_input_bkg[0])
    files[new_name]=file_names[0]

    for i in range(1,len(file_names)):
       file_names_temp=user_input_dir+file_names[i]
       try:
           temp=pd.read_csv(file_names_temp, sep=",",header=0, index_col=False)
       except:  
           print("cannot read file:{}, check file name, directory".format(file_names_temp))
           return
           
       temp.iloc[:,col]=temp.iloc[:,col]-float(user_input_bkg[i])
       temp[new_name]=file_names[i]   
       print("read..",temp.tail())
       files=files.append(temp, ignore_index=True)
    save_path=user_input_dir+"togther.csv"
    files.to_csv(save_path)
    print("save your result to: "+save_path)
  
        
        
if __name__ == "__main__" :
    try:
        user_input_dir = input('Enter directory:' ).split(',')
        user_input_file = input('Enter documents to be combined split by comma:' ).split(',')
        user_input_bkg = input('Enter backgroud you want to substract by comma:' ).split(',')    
    except:  
      print ('need your input')
    create_job(user_input_dir[0], user_input_file,user_input_bkg,new_name="animal")