try:
    stream = open("C:\\Users\\affogdav000\\Dev\\POC_Sem2_Assignments\\10_Functional Programming\\03_File_Handling_2\\newfile.txt"
,'w')
    stream.write('This is the first message!')
    stream.write('This is the second message!')
    stream.write('This is the third message!')
    stream.close()
except Exception as e:
    print('An error occurred:', e)
