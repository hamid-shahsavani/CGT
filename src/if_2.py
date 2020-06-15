# Copyright SYS113 2019. gpl v3.0 license , see readme file.

try:
    from os import startfile    
except:
    pass
from tarfile import open as TarFileOpen
from re import search
from error import error
from pathlib import Path
from zipfile import ZipFile
from time import sleep
from shutil import move , make_archive , rmtree
from os import chdir , listdir , rename , remove , stat , system 
from os.path import isfile , isdir , splitext , basename , exists , realpath
from platform import system as os_type
from platform import release as os_release

def xinput(s, *args, **kwargs):
    print(s, end='')
    return input('')

home = (str(Path.home()))

if os_type().upper() == 'WINDOWS':
    if isfile(home+'\\.CGT\\files\\LANGUAGE'):
        language = open(home + '\\.CGT\\files\\LANGUAGE', 'r').read()
elif os_type().upper() == 'LINUX':
    if isfile(home+'/.CGT/files/LANGUAGE'):
        language = open(home + '/.CGT/files/LANGUAGE', 'r').read()
else:
    pass
    
if os_release() == '7':
	class c:
	  MAGENTA = ''
	  YELLOW = ''
	  CYAN = ''
	  BLUE = ''
	  DARKCYAN = ''
	  GREEN = ''
	  RED = ''
	  GRAY = ''
	  BOLD = ''
	  WHITE = ''
	  END = ''
else:
	class c:
	  MAGENTA = '\033[35m'
	  YELLOW = '\033[33m'
	  CYAN = '\033[36m'
	  BLUE = '\033[94m'
	  DARKCYAN = '\033[96m'
	  GREEN = '\033[92m'
	  RED = '\033[91m'
	  GRAY = '\033[90m'
	  BOLD = '\033[1m'
	  WHITE = '\033[37m'
	  END = '\033[0m'

def windows():
    def compress_repack_directory():
        sleep(1)
        if language == 'FA':
            print(c.BLUE+'feshorde kardan'+c.RED+' dependencies'+c.BLUE+' va tabdil an beh '+c.RED+'repack_dependencies.zip '+c.BLUE+'.'+c.GREEN+'.'+c.RED+'.')
        else:
            print(c.BLUE+'packed'+c.RED+' dependencies'+c.BLUE+' to '+c.RED+'repack_dependencies.zip '+c.BLUE+'.'+c.GREEN+'.'+c.RED+'.')
        chdir(home + "\\Desktop\\CGT-Files\\2\\repack_dependencies\\")
        def kernel_file():
            FILE_DIRECTORY_PATH = home + '\\Desktop\\CGT-Files\\2\\repack_dependencies\\'
            FILE_PATTERN = ".+-zImage"
            for file_name in listdir(home + '\\Desktop\\CGT-Files\\2\\repack_dependencies\\'):
                if search(FILE_PATTERN, file_name):
                    return file_name
        def cmdline_file():
            FILE_DIRECTORY_PATH = home + '\\Desktop\\CGT-Files\\2\\repack_dependencies\\'
            FILE_PATTERN = ".+-cmdline"
            for file_name in listdir(home + '\\Desktop\\CGT-Files\\2\\repack_dependencies\\'):
                if search(FILE_PATTERN, file_name):
                    return file_name
        def base_file():
            FILE_DIRECTORY_PATH = home + '\\Desktop\\CGT-Files\\2\\repack_dependencies\\'
            FILE_PATTERN = ".+-base"
            for file_name in listdir(home + '\\Desktop\\CGT-Files\\2\\repack_dependencies\\'):
                if search(FILE_PATTERN, file_name):
                    return file_name
        def pagesize_file():
            FILE_DIRECTORY_PATH = home + '\\Desktop\\CGT-Files\\2\\repack_dependencies\\'
            FILE_PATTERN = ".+-pagesize"
            for file_name in listdir(home + '\\Desktop\\CGT-Files\\2\\repack_dependencies\\'):
                if search(FILE_PATTERN, file_name):
                    return file_name
        def dt_file():
            FILE_DIRECTORY_PATH = home + '\\Desktop\\CGT-Files\\2\\repack_dependencies\\'
            FILE_PATTERN = ".+-dtb"
            for file_name in listdir(home + '\\Desktop\\CGT-Files\\2\\repack_dependencies\\'):
                if search(FILE_PATTERN, file_name):
                    return file_name
        def kerneloffset_file():
            FILE_DIRECTORY_PATH = home + '\\Desktop\\CGT-Files\\2\\repack_dependencies\\'
            FILE_PATTERN = ".+-kerneloff"
            for file_name in listdir(home + '\\Desktop\\CGT-Files\\2\\repack_dependencies\\'):
                if search(FILE_PATTERN, file_name):
                    return file_name
        def ramdiskoffset_file():
            FILE_DIRECTORY_PATH = home + '\\Desktop\\CGT-Files\\2\\repack_dependencies\\'
            FILE_PATTERN = ".+-ramdiskoff"
            for file_name in listdir(home + '\\Desktop\\CGT-Files\\2\\repack_dependencies\\'):
                if search(FILE_PATTERN, file_name):
                    return file_name
        def secondoffset_file():
            FILE_DIRECTORY_PATH = home + '\\Desktop\\CGT-Files\\2\\repack_dependencies\\'
            FILE_PATTERN = ".+-secondoff"
            for file_name in listdir(home + '\\Desktop\\CGT-Files\\2\\repack_dependencies\\'):
                if search(FILE_PATTERN, file_name):
                    return file_name
        def tagsoffset_file():
            FILE_DIRECTORY_PATH = home + '\\Desktop\\CGT-Files\\2\\repack_dependencies\\'
            FILE_PATTERN = ".+-tagsoff"
            for file_name in listdir(home + '\\Desktop\\CGT-Files\\2\\repack_dependencies\\'):
                if search(FILE_PATTERN, file_name):
                    return file_name
        def hash_file():
            FILE_DIRECTORY_PATH = home + '\\Desktop\\CGT-Files\\2\\repack_dependencies\\'
            FILE_PATTERN = ".+-hash"
            for file_name in listdir(home + '\\Desktop\\CGT-Files\\2\\repack_dependencies\\'):
                if search(FILE_PATTERN, file_name):
                    return file_name
        old_kernel = home+'\\Desktop\\CGT-Files\\2\\repack_dependencies\\'+kernel_file()
        old_cmdline = home+'\\Desktop\\CGT-Files\\2\\repack_dependencies\\'+cmdline_file()
        old_base = home+'\\Desktop\\CGT-Files\\2\\repack_dependencies\\'+base_file()
        old_pagesize = home+'\\Desktop\\CGT-Files\\2\\repack_dependencies\\'+pagesize_file()
        if dt_file() != None:
            old_dt = home+'\\Desktop\\CGT-Files\\2\\repack_dependencies\\'+dt_file()
        old_kerneloffset = home+'\\Desktop\\CGT-Files\\2\\repack_dependencies\\'+kerneloffset_file()
        old_ramdiskoffset = home+'\\Desktop\\CGT-Files\\2\\repack_dependencies\\'+ramdiskoffset_file()
        old_secondoffset = home+'\\Desktop\\CGT-Files\\2\\repack_dependencies\\'+secondoffset_file()
        old_tagsoffset = home+'\\Desktop\\CGT-Files\\2\\repack_dependencies\\'+tagsoffset_file()
        old_hash = home+'\\Desktop\\CGT-Files\\2\\repack_dependencies\\'+hash_file()
        new_kernel = home+'\\Desktop\\CGT-Files\\2\\repack_dependencies\\CGT_50484c19f1afdaf3841a0d821ed393d2_CGT'
        new_cmdline = home+'\\Desktop\\CGT-Files\\2\\repack_dependencies\\CGT_95f44086bc13f782435dd6356310e7bd_CGT'
        new_base = home+'\\Desktop\\CGT-Files\\2\\repack_dependencies\\CGT_593616de15330c0fb2d55e55410bf994_CGT'
        new_pagesize = home+'\\Desktop\\CGT-Files\\2\\repack_dependencies\\CGT_7525d528a3457f0227997c25239c4507_CGT'
        if dt_file() != None:
            new_dt = home+'\\Desktop\\CGT-Files\\2\\repack_dependencies\\CGT_3017d911efceb27d1de6a92b70979795_CGT'
        new_kerneloffset = home+'\\Desktop\\CGT-Files\\2\\repack_dependencies\\CGT_706cf6b230a6d77ee280a40b54246762_CGT'
        new_ramdiskoffset = home+'\\Desktop\\CGT-Files\\2\\repack_dependencies\\CGT_0e16d6f83afe32911816ef683ad5d639_CGT'
        new_secondoffset = home+'\\Desktop\\CGT-Files\\2\\repack_dependencies\\CGT_d753658059439ac8a93d411e68e5d66a_CGT'
        new_tagsoffset = home+'\\Desktop\\CGT-Files\\2\\repack_dependencies\\CGT_a4d756b70ed4593b8d0f2abd01694f39_CGT'
        new_hash = home+'\\Desktop\\CGT-Files\\2\\repack_dependencies\\CGT_0800fc577294c34e0b28ad2839435945_CGT'
        rename(old_kernel , new_kernel)
        rename(old_cmdline , new_cmdline)
        rename(old_base , new_base)
        rename(old_pagesize , new_pagesize)
        if dt_file() != None:   
            rename(old_dt , new_dt)
        rename(old_kerneloffset , new_kerneloffset)
        rename(old_ramdiskoffset , new_ramdiskoffset)
        rename(old_secondoffset , new_secondoffset)
        rename(old_tagsoffset , new_tagsoffset)
        rename(old_hash , new_hash)
        system('mkdir '+home + "\\Desktop\\CGT-Files\\2\\repack\\")
        rpk = home + "\\Desktop\\CGT-Files\\2\\repack\\"
        move(new_kernel,rpk)
        move(new_cmdline,rpk)
        move(new_base,rpk)
        move(new_pagesize,rpk)
        if isfile(home+'\\Desktop\\CGT-Files\\2\\repack_dependencies\\CGT_3017d911efceb27d1de6a92b70979795_CGT'):
            move(new_dt,rpk)
        move(new_kerneloffset,rpk)
        move(new_ramdiskoffset,rpk)
        move(new_secondoffset,rpk)
        move(new_tagsoffset,rpk)
        move(new_hash,rpk)
        chdir(home + "\\Desktop\\CGT-Files\\2\\")
        make_archive('repack_dependencies', 'zip', 'repack')
    if language == 'FA':
        print(c.END+c.GREEN+'drag'+c.RED+' & '+c.GREEN +'drop'+c.BLUE+' konid '+c.YELLOW+'boot'+c.RED+' / ' + c.YELLOW+'recovery'+c.RED +' ['+c.GREEN+'.img' + c.RED + '|' + c.GREEN + '.img.lz4'+c.RED+'|'+c.GREEN+'.tar'+c.RED+'|'+c.GREEN+'tar.md5'+c.RED+']'+c.BLUE+' ra va '+c.RED+'klid enter' + c.BLUE+' ra '+c.RED+'befesharid' + c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
        file = xinput(c.MAGENTA+'> '+c.YELLOW)
        file = file.replace("\"", "")
        file = file.replace("\'", "")
        file_name, file_extension = splitext(file)
        if ' ' in file:
            print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'2' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
            error(2)
        else:
            if exists(file) == True:
                if file_extension == '.lz4':
                    if (basename(file) == 'boot.img.lz4') or (basename(file) == 'recovery.img.lz4'):
                        file = file.replace(".lz4", "")
                        if isdir(home + "\\Desktop\\CGT-Files\\2\\"):
                            try:
                                sleep(1)
                                print(c.END+c.RED+'poshe'+c.YELLOW+' 2 '+c.BLUE + 'vojod darad'+c.GREEN+' ; '+c.RED + 'hazf '+c.GREEN+'&'+c.RED+' sakht dobare ' + c.BLUE + '.' + c.GREEN + '.' + c.RED + '.')
                                rmtree(home + "\\Desktop\\CGT-Files\\2\\")
                            except:
                                sleep(1)
                                print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'5' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                error(5)
                                return
                        else:
                            print(c.RED+'sakht'+c.BLUE+' poshe '+c.YELLOW+'2'+c.RED+' .'+c.GREEN+'.'+c.BLUE+'.')
                        system('mkdir '+home + '\\Desktop\\CGT-Files\\2\\')
                        chdir(home + '\\Desktop\\CGT-Files\\2\\')
                        sleep(1)
                        print(c.END+c.BLUE + 'tabdil '+c.RED + basename(file+'.lz4') + c.BLUE + ' beh ' +c.RED + basename(file) + c.BLUE + ' .' + c.GREEN + '.' + c.RED + '.')
                        system(home + '\\.CGT\\programs\\lz4.exe -d ' + file+'.lz4')
                        img_lz4_size = stat(file)
                        if img_lz4_size.st_size == 0:
                          sleep(1)
                          print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'4' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                          error(4)
                          sleep(1)
                          print(c.BLUE+'hazf'+c.RED+' log ha '+c.BLUE+'va'+c.RED+' khoroj '+c.BLUE+'.'+c.GREEN+'.'+c.RED+'.')
                          chdir(home)
                          remove(file)
                          try:
                            rmtree(home + "\\Desktop\\CGT-Files\\2\\")
                          except:
                            print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'5' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                            error(5)
                            return
                          return
                        sleep(1)
                        print(c.END+c.BLUE + 'estekhraj '+c.RED+basename(file)+ c.BLUE + ' .' + c.GREEN + '.' + c.RED + '.')
                        system('mkdir '+home + '\\Desktop\\CGT-Files\\2\\repack_dependencies\\')
                        system(home+'\\.CGT\\programs\\unpackbootimg.exe' + ' -i ' + file + ' -o ' + home + '\\Desktop\\CGT-Files\\2\\repack_dependencies\\ > NUL')
                        sleep(1)
                        print(c.END+c.BLUE + 'estekhraj'+c.RED+' ramdisk ' + c.BLUE + '.' + c.GREEN + '.' + c.RED + '.')
                        try:
                            ramdisk_size = stat(home+'\\Desktop\\CGT-Files\\2\\repack_dependencies\\'+basename(file)+'-ramdisk.gz')
                        except:
                            sleep(1)
                            print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'8' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                            error(8)
                            sleep(1)
                            print(c.BLUE+'hazf'+c.RED+' log ha '+c.BLUE+'va'+c.RED+' khoroj '+c.BLUE+'.'+c.GREEN+'.'+c.RED+'.')
                            chdir(home)
                            remove(file)
                            try:
                              rmtree(home + "\\Desktop\\CGT-Files\\2\\")
                            except:
                              print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'5' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                              error(5)
                            return
                        if ramdisk_size.st_size != 0:
                            system('mkdir unpack')
                            chdir('unpack')
                            system(home+'\\.CGT\\programs\\gzip.exe -dcq '+home+'\\Desktop\\CGT-Files\\2\\repack_dependencies\\' + basename(file)+'-ramdisk.gz | '+home+'\\.CGT\\programs\\cpio -i > NUL 2>&1')
                            compress_repack_directory()
                            _file_name = basename(file)
                            file_name_ = open('CGT_435ed7e9f07f740abf511a62c00eef6e_CGT','w')
                            file_name_.write(_file_name)
                            file_name_.close()
                            depen = ZipFile('repack_dependencies.zip','a')
                            depen.write(home+'\\Desktop\\CGT-Files\\2\\CGT_435ed7e9f07f740abf511a62c00eef6e_CGT', 'CGT_435ed7e9f07f740abf511a62c00eef6e_CGT')
                            depen.close()
                            sleep(1)
                            print(c.END+c.BLUE+'hazf'+c.RED+' log ha '+c.BLUE+'.'+c.GREEN+'.'+c.RED+'.')
                            readme_unpack_write = '--- estekhraj shod '+basename(file+'.lz4') + ' tavasote CGT ---'+'\n\n'+ '- lotfan [ file repack_dependencies.zip / poshe unpack ] ra hazf nakonid ya taghir name nadahid ...'
                            readme_unpack = open(home + '\\Desktop\\CGT-Files\\2\\CGT.txt', 'w')
                            readme_unpack.write(readme_unpack_write)
                            readme_unpack.close()
                            remove(file)
                            rmtree(home + "\\Desktop\\CGT-Files\\2\\repack_dependencies\\")
                            rmtree(home + "\\Desktop\\CGT-Files\\2\\repack\\")
                            remove(home + '\\Desktop\\CGT-Files\\2\\CGT_435ed7e9f07f740abf511a62c00eef6e_CGT')
                            sleep(1)
                            print(c.END+c.RED + basename(file+'.lz4') + c.BLUE+' estekhraj shod dar' + c.RED + ' : ' + c.YELLOW + 'CGT-Files\\2\\'+c.RED+'unpack')
                            chdir(home+'\\Desktop\\')
                            startfile(realpath(home+'\\Desktop\\CGT-Files\\2\\unpack\\'))
                            startfile(home+'\\Desktop\\CGT-Files\\2\\CGT.txt')
                        elif ramdisk_size.st_size == 0:
                            sleep(1)
                            print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'6' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                            error(6)
                            print(c.BLUE+'hazf'+c.RED+' log ha '+c.BLUE+'va'+c.RED+' khoroj '+c.BLUE+'.'+c.GREEN+'.'+c.RED+'.')
                            chdir(home)
                            remove(file)
                            try:
                              rmtree(home + "\\Desktop\\CGT-Files\\2\\")
                            except:
                              print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'5' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                              error(5)
                              return
                    else:
                        print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'11' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                        error(11)
                elif file_extension == '.img':
                    if (basename(file) == 'boot.img') or (basename(file) == 'recovery.img'):
                        if isdir(home + "\\Desktop\\CGT-Files\\2\\"):
                            try:
                                sleep(1)
                                print(c.END+c.RED+'poshe'+c.YELLOW+' 2 '+c.BLUE + 'vojod darad'+c.GREEN+' ; '+c.RED + 'hazf '+c.GREEN+'&'+c.RED+' sakht dobare ' + c.BLUE + '.' + c.GREEN + '.' + c.RED + '.')
                                rmtree(home + "\\Desktop\\CGT-Files\\2\\")
                            except:
                                sleep(1)
                                print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'5' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                error(5)
                                return
                        else:
                            print(c.RED+'sakht'+c.BLUE+' poshe '+c.YELLOW+'2'+c.RED+' .'+c.GREEN+'.'+c.BLUE+'.')
                        sleep(1)
                        print(c.END+c.BLUE + 'estekhraj '+c.RED+basename(file)+ c.BLUE + ' .' + c.GREEN + '.' + c.RED + '.')
                        system('mkdir '+home + '\\Desktop\\CGT-Files\\2\\')
                        chdir(home + '\\Desktop\\CGT-Files\\2\\')
                        system('mkdir '+home +'\\Desktop\\CGT-Files\\2\\repack_dependencies\\')
                        system(home+'\\.CGT\\programs\\unpackbootimg.exe' + ' -i ' +file + ' -o ' + home + '\\Desktop\\CGT-Files\\2\\repack_dependencies\\ > NUL')
                        sleep(1)
                        print(c.END+c.BLUE + 'estekhraj'+c.RED+' ramdisk ' +c.BLUE + '.' + c.GREEN + '.' + c.RED + '.')
                        try:
                            ramdisk_size = stat(home+'\\Desktop\\CGT-Files\\2\\repack_dependencies\\'+basename(file)+'-ramdisk.gz')
                        except:
                            sleep(1)
                            print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'8' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                            error(8)
                            sleep(1)
                            print(c.BLUE+'hazf'+c.RED+' log ha '+c.BLUE+'va'+c.RED+' khoroj '+c.BLUE+'.'+c.GREEN+'.'+c.RED+'.')
                            chdir(home)
                            try:
                              rmtree(home + "\\Desktop\\CGT-Files\\2\\")
                            except:
                              print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'5' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                              error(5)
                              return
                            return
                        if ramdisk_size.st_size != 0:
                            system("mkdir unpack")
                            chdir('unpack')
                            system(home+'\\.CGT\\programs\\gzip.exe -dcq '+home+'\\Desktop\\CGT-Files\\2\\repack_dependencies\\' + basename(file)+'-ramdisk.gz | '+home+'\\.CGT\\programs\\cpio -i > NUL 2>&1')
                            compress_repack_directory()
                            _file_name = basename(file)
                            file_name_ = open('CGT_435ed7e9f07f740abf511a62c00eef6e_CGT','w')
                            file_name_.write(_file_name)
                            file_name_.close()
                            depen = ZipFile('repack_dependencies.zip','a')
                            depen.write(home+'\\Desktop\\CGT-Files\\2\\CGT_435ed7e9f07f740abf511a62c00eef6e_CGT', 'CGT_435ed7e9f07f740abf511a62c00eef6e_CGT')
                            depen.close()
                            sleep(1)
                            print(c.END+c.BLUE+'hazf'+c.RED+' log ha '+c.BLUE+'.'+c.GREEN+'.'+c.RED+'.')
                            readme_unpack_write = '--- estekhraj shod '+basename(file) + ' tavasote CGT ---'+'\n\n'+ '- lotfan [ file repack_dependencies.zip / poshe unpack ] ra hazf nakonid ya taghir name nadahid ...'
                            readme_unpack = open(home + '\\Desktop\\CGT-Files\\2\\CGT.txt', 'w')
                            readme_unpack.write(readme_unpack_write)
                            readme_unpack.close()
                            rmtree(home + "\\Desktop\\CGT-Files\\2\\repack_dependencies\\")
                            rmtree(home + "\\Desktop\\CGT-Files\\2\\repack\\")
                            remove(home + '\\Desktop\\CGT-Files\\2\\CGT_435ed7e9f07f740abf511a62c00eef6e_CGT')
                            sleep(1)
                            print(c.END+c.RED + basename(file) + c.BLUE+' estekhraj shod dar' + c.RED + ' : ' + c.YELLOW + 'CGT-Files\\2\\'+c.RED+'unpack')
                            chdir(home)
                            startfile(realpath(home+'\\Desktop\\CGT-Files\\2\\unpack\\'))
                            startfile(home+'\\Desktop\\CGT-Files\\2\\CGT.txt')
                        elif ramdisk_size.st_size == 0:
                            sleep(1)
                            print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'6' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                            error(6)
                            print(c.BLUE+'hazf'+c.RED+' log ha '+c.BLUE+'va'+c.RED+' khoroj '+c.BLUE+'.'+c.GREEN+'.'+c.RED+'.')
                            chdir(home)
                            try:
                              rmtree(home + "\\Desktop\\CGT-Files\\2\\")
                            except:
                              print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'5' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                              error(5)
                              return
                            return
                    else:
                        print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'10' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                        error(10)
                elif (file_extension == '.md5') or (file_extension == '.tar'):
                    tar_file = TarFileOpen(file)
                    if ('recovery.img' not in tar_file.getnames()) and ('recovery.img.lz4' not in tar_file.getnames()) and ('boot.img' not in tar_file.getnames()) and ('boot.img.lz4' not in tar_file.getnames()):
                        print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'9' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                        error(9)
                    else:
                        sleep(1)
                        print(c.END+c.YELLOW+'a'+c.GREEN+'.'+c.BLUE+'unpack '+c.RED+'recovery')
                        print(c.END+c.YELLOW+'b'+c.GREEN+'.'+c.BLUE+'unpack '+c.RED+'boot')
                        un = xinput(c.GREEN+'> '+c.YELLOW)
                        if un == 'a':
                            if 'recovery.img' in tar_file.getnames():
                                if isdir(home + "\\Desktop\\CGT-Files\\2\\"):
                                    try:
                                        sleep(1)
                                        print(c.END+c.RED+'poshe'+c.YELLOW+' 2 '+c.BLUE + 'vojod darad'+c.GREEN+' ; '+c.RED + 'hazf '+c.GREEN+'&'+c.RED+' sakht dobare ' + c.BLUE + '.' + c.GREEN + '.' + c.RED + '.')
                                        rmtree(home + "\\Desktop\\CGT-Files\\2\\")
                                    except:
                                        sleep(1)
                                        print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'5' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                        error(5)
                                        return
                                else:
                                    print(c.RED+'sakht'+c.BLUE+' poshe '+c.YELLOW+'2'+c.RED+' .'+c.GREEN+'.'+c.BLUE+'.')
                                system('mkdir '+home + '\\Desktop\\CGT-Files\\2\\')
                                chdir(home + '\\Desktop\\CGT-Files\\2\\')
                                sleep(1)
                                print(c.END+c.BLUE+'yaft shod '+c.RED+'recovery.img'+c.BLUE+' dar '+c.RED+basename(file)+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                sleep(1)
                                print(c.END+c.BLUE+'estekhraj'+c.RED+' recovery.img '+c.BLUE+'az '+c.RED+basename(file)+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                tar_file.extract('recovery.img')
                                sleep(1)
                                print(c.END+c.BLUE + 'estekhraj ' + c.RED + 'recovery.img' + c.BLUE + ' .' + c.GREEN + '.' + c.RED + '.')
                                system('mkdir '+home + '\\Desktop\\CGT-Files\\2\\repack_dependencies\\')
                                system(home+'\\.CGT\\programs\\unpackbootimg.exe' + ' -i ' +
                                home+'\\Desktop\\CGT-Files\\2\\recovery.img' + ' -o ' + home + '\\Desktop\\CGT-Files\\2\\repack_dependencies\\ > NUL')
                                sleep(1)
                                print(c.END+c.BLUE + 'estekhraj'+c.RED+' ramdisk ' + c.BLUE + '.' + c.GREEN + '.' + c.RED + '.')
                                ramdisk_size = stat(home+'\\Desktop\\CGT-Files\\2\\repack_dependencies\\recovery.img-ramdisk.gz')
                                if ramdisk_size.st_size != 0:
                                    system("mkdir unpack")
                                    chdir('unpack')
                                    system(home+'\\.CGT\\programs\\gzip.exe -dcq '+home+'\\Desktop\\CGT-Files\\2\\repack_dependencies\\recovery.img-ramdisk.gz | '+home+'\\.CGT\\programs\\cpio -i > NUL 2>&1')
                                    compress_repack_directory()
                                    _file_name = 'recovery.img'
                                    file_name_ = open('CGT_435ed7e9f07f740abf511a62c00eef6e_CGT','w')
                                    file_name_.write(_file_name)
                                    file_name_.close()
                                    depen = ZipFile('repack_dependencies.zip','a')
                                    depen.write(home+'\\Desktop\\CGT-Files\\2\\CGT_435ed7e9f07f740abf511a62c00eef6e_CGT', 'CGT_435ed7e9f07f740abf511a62c00eef6e_CGT')
                                    depen.close()
                                    sleep(1)
                                    print(c.END+c.BLUE+'hazf ' + c.RED+'log ha' + c.BLUE + ' .' + c.GREEN + '.' + c.RED + '.')
                                    remove(home+'\\Desktop\\CGT-Files\\2\\recovery.img')
                                    readme_unpack_write = '--- estekhraj shod recovery.img az '+basename(file) + ' tavasote CGT ---'+'\n\n'+ '- lotfan [ file repack_dependencies.zip / poshe unpack ] ra hazf nakonid ya taghir name nadahid ...'
                                    readme_unpack = open(home + '\\Desktop\\CGT-Files\\2\\CGT.txt', 'w')
                                    readme_unpack.write(readme_unpack_write)
                                    readme_unpack.close()
                                    rmtree(home + "\\Desktop\\CGT-Files\\2\\repack_dependencies\\")
                                    rmtree(home + "\\Desktop\\CGT-Files\\2\\repack\\")
                                    remove(home + '\\Desktop\\CGT-Files\\2\\CGT_435ed7e9f07f740abf511a62c00eef6e_CGT')
                                    sleep(1)
                                    print(c.END+c.BLUE+'estekhraj shod '+c.RED+'recovery.img'+c.BLUE+' az '+c.RED+basename(file)+c.BLUE+' dar' + c.RED + ' : ' + c.YELLOW + 'CGT-Files\\2\\'+c.RED+'unpack')
                                    chdir(home)
                                    startfile(realpath(home+'\\Desktop\\CGT-Files\\2\\unpack\\'))
                                    startfile(home+'\\Desktop\\CGT-Files\\2\\CGT.txt')
                                elif ramdisk_size.st_size == 0:
                                    sleep(1)
                                    print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'6' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                    error(6)
                                    sleep(1)
                                    print(c.BLUE+'hazf'+c.RED+' log ha '+c.BLUE+'va'+c.RED+' khoroj '+c.BLUE+'.'+c.GREEN+'.'+c.RED+'.')
                                    chdir(home)
                                    try:
                                        rmtree(home + "\\Desktop\\CGT-Files\\2\\")
                                    except:
                                        sleep(1)
                                        print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'5' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                        error(5)
                                        sleep(1)
                                        print(c.BLUE+'hazf'+c.RED+' log ha '+c.BLUE+'va'+c.RED+' khoroj '+c.BLUE+'.'+c.GREEN+'.'+c.RED+'.')
                                        chdir(home)
                                        return
                            elif 'recovery.img.lz4' in tar_file.getnames():
                                if isdir(home + "\\Desktop\\CGT-Files\\2\\"):
                                    try:
                                        sleep(1)
                                        print(c.END+c.RED+'poshe'+c.YELLOW+' 2 '+c.BLUE + 'vojod darad'+c.GREEN+' ; '+c.RED + 'hazf '+c.GREEN+'&'+c.RED+' sakht dobare ' + c.BLUE + '.' + c.GREEN + '.' + c.RED + '.')
                                        rmtree(home + "\\Desktop\\CGT-Files\\2\\")
                                    except:
                                        sleep(1)
                                        print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'5' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                        error(5)
                                        return
                                else:
                                    print(c.RED+'sakht'+c.BLUE+' poshe '+c.YELLOW+'2'+c.RED+' .'+c.GREEN+'.'+c.BLUE+'.')
                                system('mkdir '+home + '\\Desktop\\CGT-Files\\2\\')
                                chdir(home + '\\Desktop\\CGT-Files\\2\\')
                                sleep(1)
                                print(c.END+c.BLUE+'yaft shod '+c.RED+'recovery.img.lz4'+c.BLUE+' dar '+c.RED+basename(file)+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                sleep(1)
                                print(c.END+c.BLUE+'estekhraj'+c.RED+' recovery.img.lz4 '+c.BLUE+'az '+c.RED+basename(file)+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                tar_file.extract('recovery.img.lz4')
                                sleep(1)
                                print(c.END+c.BLUE + 'tabdil '+c.RED + 'recovery.img.lz4' + c.BLUE + ' beh ' +c.RED + 'recovery.img' + c.BLUE + ' .' + c.GREEN + '.' + c.RED + '.')
                                system(home +'\\.CGT\\programs\\lz4.exe -d recovery.img.lz4')
                                img_lz4_size = stat(home+'\\Desktop\\CGT-Files\\2\\recovery.img')
                                if img_lz4_size.st_size == 0:
                                  sleep(1)
                                  print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'4' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                  error(4)
                                  sleep(1)
                                  print(c.BLUE+'hazf'+c.RED+' log ha '+c.BLUE+'va'+c.RED+' khoroj '+c.BLUE+'.'+c.GREEN+'.'+c.RED+'.')
                                  chdir(home)
                                  try:
                                    rmtree(home + "\\Desktop\\CGT-Files\\2\\")
                                  except:
                                    print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'5' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                    error(5)
                                    return
                                  return
                                sleep(1)
                                print(c.END+c.BLUE + 'estekhraj ' + c.RED + 'recovery.img' + c.BLUE + ' .' + c.GREEN + '.' + c.RED + '.')
                                system('mkdir '+home + '\\Desktop\\CGT-Files\\2\\repack_dependencies\\')
                                system(home+'\\.CGT\\programs\\unpackbootimg.exe' + ' -i ' + home+'\\Desktop\\CGT-Files\\2\\recovery.img' + ' -o ' + home + '\\Desktop\\CGT-Files\\2\\repack_dependencies\\ > NUL')
                                sleep(1)
                                print(c.END+c.BLUE + 'estekhraj'+c.RED+' ramdisk ' + c.BLUE + '.' + c.GREEN + '.' + c.RED + '.')
                                ramdisk_size = stat(home+'\\Desktop\\CGT-Files\\2\\repack_dependencies\\recovery.img-ramdisk.gz')
                                if ramdisk_size.st_size != 0:
                                    system("mkdir unpack")
                                    chdir('unpack')
                                    system(home+'\\.CGT\\programs\\gzip.exe -dcq '+home+'\\Desktop\\CGT-Files\\2\\repack_dependencies\\recovery.img-ramdisk.gz | '+home+'\\.CGT\\programs\\cpio -i > NUL 2>&1')
                                    compress_repack_directory()
                                    _file_name = 'recovery.img'
                                    file_name_ = open('CGT_435ed7e9f07f740abf511a62c00eef6e_CGT','w')
                                    file_name_.write(_file_name)
                                    file_name_.close()
                                    depen = ZipFile('repack_dependencies.zip','a')
                                    depen.write(home+'\\Desktop\\CGT-Files\\2\\CGT_435ed7e9f07f740abf511a62c00eef6e_CGT', 'CGT_435ed7e9f07f740abf511a62c00eef6e_CGT')
                                    depen.close()
                                    sleep(1)
                                    print(c.END+c.BLUE+'hazf ' + c.RED+'log ha' + c.BLUE + ' .' + c.GREEN + '.' + c.RED + '.')
                                    remove(home+'\\Desktop\\CGT-Files\\2\\recovery.img')
                                    remove(home+'\\Desktop\\CGT-Files\\2\\recovery.img.lz4')
                                    readme_unpack_write = '--- estekhraj shod recovery.img.lz4 az '+basename(file) + ' tavasote CGT ---'+'\n\n'+ '- lotfan [ file repack_dependencies.zip / poshe unpack ] ra hazf nakonid ya taghir name nadahid ...'
                                    readme_unpack = open(home + '\\Desktop\\CGT-Files\\2\\CGT.txt', 'w')
                                    readme_unpack.write(readme_unpack_write)
                                    readme_unpack.close()
                                    rmtree(home + "\\Desktop\\CGT-Files\\2\\repack_dependencies\\")
                                    rmtree(home + "\\Desktop\\CGT-Files\\2\\repack\\")
                                    remove(home + '\\Desktop\\CGT-Files\\2\\CGT_435ed7e9f07f740abf511a62c00eef6e_CGT')
                                    sleep(1)
                                    print(c.END+c.BLUE+'estekhraj shod '+c.RED+'recovery.img.lz4'+c.BLUE+' az '+c.RED+basename(file)+c.BLUE+' dar' + c.RED + ' : ' + c.YELLOW + 'CGT-Files\\2\\'+c.RED+'unpack')
                                    chdir(home)
                                    startfile(realpath(home+'\\Desktop\\CGT-Files\\2\\unpack\\'))
                                    startfile(home+'\\Desktop\\CGT-Files\\2\\CGT.txt')
                                elif ramdisk_size.st_size == 0:
                                    sleep(1)
                                    print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'6' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                    error(6)
                                    sleep(1)
                                    print(c.BLUE+'hazf'+c.RED+' log ha '+c.BLUE+'va'+c.RED+' khoroj '+c.BLUE+'.'+c.GREEN+'.'+c.RED+'.')
                                    chdir(home)
                                    try:
                                        rmtree(home + "\\Desktop\\CGT-Files\\2\\")
                                    except:
                                        sleep(1)
                                        print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'5' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                        error(5)
                                        sleep(1)
                                        print(c.BLUE+'hazf'+c.RED+' log ha '+c.BLUE+'va'+c.RED+' khoroj '+c.BLUE+'.'+c.GREEN+'.'+c.RED+'.')
                                        chdir(home)
                                        return
                            else:
                                print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'13' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                error(13)
                        elif un == 'b':
                            if 'boot.img' in tar_file.getnames():
                                if isdir(home + "\\Desktop\\CGT-Files\\2\\"):
                                    try:
                                        sleep(1)
                                        print(c.END+c.RED+'poshe'+c.YELLOW+' 2 '+c.BLUE + 'vojod darad'+c.GREEN+' ; '+c.RED + 'hazf '+c.GREEN+'&'+c.RED+' sakht dobare ' + c.BLUE + '.' + c.GREEN + '.' + c.RED + '.')
                                        rmtree(home + "\\Desktop\\CGT-Files\\2\\")
                                    except:
                                        sleep(1)
                                        print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'5' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                        error(5)
                                        return
                                else:
                                    print(c.RED+'sakht'+c.BLUE+' poshe '+c.YELLOW+'2'+c.RED+' .'+c.GREEN+'.'+c.BLUE+'.')
                                system('mkdir '+home + '\\Desktop\\CGT-Files\\2\\')
                                chdir(home + '\\Desktop\\CGT-Files\\2\\')
                                sleep(1)
                                print(c.END+c.BLUE+'yaft shod '+c.RED+'boot.img'+c.BLUE+' dar '+c.RED+basename(file)+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                sleep(1)
                                print(c.END+c.BLUE+'estekhraj'+c.RED+' boot.img '+c.BLUE+'az '+c.RED+basename(file)+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                tar_file.extract('boot.img')
                                sleep(1)
                                print(c.END+c.BLUE + 'estekhraj ' + c.RED + 'boot.img' +c.BLUE + ' .' + c.GREEN + '.' + c.RED + '.')
                                system('mkdir '+home + '\\Desktop\\CGT-Files\\2\\repack_dependencies\\')
                                system(home+'\\.CGT\\programs\\unpackbootimg.exe' + ' -i ' +home+'\\Desktop\\CGT-Files\\2\\boot.img' + ' -o ' + home + '\\Desktop\\CGT-Files\\2\\repack_dependencies\\ > NUL')
                                sleep(1)
                                print(c.END+c.BLUE + 'estekhraj'+c.RED+' ramdisk ' + c.BLUE + '.' + c.GREEN + '.' + c.RED + '.')
                                ramdisk_size = stat(home+'\\Desktop\\CGT-Files\\2\\repack_dependencies\\boot.img-ramdisk.gz')
                                if ramdisk_size.st_size != 0:
                                    system("mkdir unpack")
                                    chdir('unpack')
                                    system(home+'\\.CGT\\programs\\gzip.exe -dcq '+home+'\\Desktop\\CGT-Files\\2\\repack_dependencies\\boot.img-ramdisk.gz | '+home+'\\.CGT\\programs\\cpio -i > NUL 2>&1')
                                    compress_repack_directory()
                                    _file_name = 'boot.img'
                                    file_name_ = open('CGT_435ed7e9f07f740abf511a62c00eef6e_CGT','w')
                                    file_name_.write(_file_name)
                                    file_name_.close()
                                    depen = ZipFile('repack_dependencies.zip','a')
                                    depen.write(home+'\\Desktop\\CGT-Files\\2\\CGT_435ed7e9f07f740abf511a62c00eef6e_CGT', 'CGT_435ed7e9f07f740abf511a62c00eef6e_CGT')
                                    depen.close()
                                    sleep(1)
                                    print(c.END+c.BLUE+'hazf ' + c.RED+'log ha' + c.BLUE + ' .' + c.GREEN + '.' + c.RED + '.')
                                    remove(home+'\\Desktop\\CGT-Files\\2\\boot.img')
                                    readme_unpack_write = '--- estekhraj shod boot.img az '+basename(file) + ' tavasote CGT ---'+'\n\n'+ '- lotfan [ file repack_dependencies.zip / poshe unpack ] ra hazf nakonid ya taghir name nadahid ...'
                                    readme_unpack = open(home + '\\Desktop\\CGT-Files\\2\\CGT.txt', 'w')
                                    readme_unpack.write(readme_unpack_write)
                                    readme_unpack.close()
                                    rmtree(home + "\\Desktop\\CGT-Files\\2\\repack_dependencies\\")
                                    rmtree(home + "\\Desktop\\CGT-Files\\2\\repack\\")
                                    remove(home + '\\Desktop\\CGT-Files\\2\\CGT_435ed7e9f07f740abf511a62c00eef6e_CGT')
                                    sleep(1)
                                    print(c.END+c.BLUE+'estekhraj shod '+c.RED+'boot.img'+c.BLUE+' az '+c.RED+basename(file)+c.BLUE+' in' + c.RED + ' : ' + c.YELLOW + 'CGT-Files\\2\\'+c.RED+'unpack')
                                    chdir(home)
                                    startfile(realpath(home+'\\Desktop\\CGT-Files\\2\\unpack\\'))
                                    startfile(home+'\\Desktop\\CGT-Files\\2\\CGT.txt')
                                elif ramdisk_size.st_size == 0:
                                    sleep(1)
                                    print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'6' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                    error(6)
                                    sleep(1)
                                    print(c.BLUE+'hazf'+c.RED+' log ha '+c.BLUE+'va'+c.RED+' khoroj '+c.BLUE+'.'+c.GREEN+'.'+c.RED+'.')
                                    chdir(home)
                                    try:
                                        rmtree(home + "\\Desktop\\CGT-Files\\2\\")
                                    except:
                                        sleep(1)
                                        print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'5' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                        error(5)
                                        sleep(1)
                                        print(c.BLUE+'hazf'+c.RED+' log ha '+c.BLUE+'va'+c.RED+' khoroj '+c.BLUE+'.'+c.GREEN+'.'+c.RED+'.')
                                        chdir(home)
                                        return
                            elif 'boot.img.lz4' in tar_file.getnames():
                                if isdir(home + "\\Desktop\\CGT-Files\\2\\"):
                                    try:
                                        sleep(1)
                                        print(c.END+c.RED+'poshe'+c.YELLOW+' 2 '+c.BLUE + 'vojod darad'+c.GREEN+' ; '+c.RED + 'hazf '+c.GREEN+'&'+c.RED+' sakht dobare ' + c.BLUE + '.' + c.GREEN + '.' + c.RED + '.')
                                        rmtree(home + "\\Desktop\\CGT-Files\\2\\")
                                    except:
                                        sleep(1)
                                        print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'5' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                        error(5)
                                        return
                                else:
                                    print(c.RED+'sakht'+c.BLUE+' poshe '+c.YELLOW+'2'+c.RED+' .'+c.GREEN+'.'+c.BLUE+'.')
                                system('mkdir '+home + '\\Desktop\\CGT-Files\\2\\')
                                chdir(home + '\\Desktop\\CGT-Files\\2\\')
                                sleep(1)
                                print(c.END+c.BLUE+'yaft shod'+c.RED+' boot.img.lz4'+c.BLUE+' dar '+c.RED+basename(file)+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                sleep(1)
                                print(c.END+c.BLUE+'estekhraj'+c.RED+' boot.img.lz4 '+c.BLUE+'az '+c.RED+basename(file)+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                tar_file.extract('boot.img.lz4')
                                sleep(1)
                                print(c.END+c.BLUE + 'tabdil '+c.RED + 'boot.img.lz4' + c.BLUE + ' be ' + c.RED + 'boot.img' + c.BLUE + ' .' + c.GREEN + '.' + c.RED + '.')
                                system(home +'\\.CGT\\programs\\lz4.exe -d boot.img.lz4')
                                img_lz4_size = stat(home+'\\Desktop\\CGT-Files\\2\\boot.img')
                                if img_lz4_size.st_size == 0:
                                  sleep(1)
                                  print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'4' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                  error(4)
                                  sleep(1)
                                  print(c.BLUE+'hazf'+c.RED+' log ha '+c.BLUE+'va'+c.RED+' khoroj '+c.BLUE+'.'+c.GREEN+'.'+c.RED+'.')
                                  chdir(home)
                                  try:
                                    rmtree(home + "\\Desktop\\CGT-Files\\2\\")
                                  except:
                                    print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'5' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                    error(5)
                                    return
                                  return
                                sleep(1)
                                print(c.END+c.BLUE + 'estekhraj ' + c.RED + 'boot.img'+c.BLUE + ' .' + c.GREEN + '.' + c.RED + '.')
                                system('mkdir '+home + '\\Desktop\\CGT-Files\\2\\repack_dependencies\\')
                                system(home+'\\.CGT\\programs\\unpackbootimg.exe' + ' -i ' + home+'\\Desktop\\CGT-Files\\2\\boot.img' + ' -o ' + home + '\\Desktop\\CGT-Files\\2\\repack_dependencies\\ > NUL')
                                sleep(1)
                                print(c.END+c.BLUE + 'estekhraj'+c.RED+' ramdisk ' + c.BLUE + '.' + c.GREEN + '.' + c.RED + '.')
                                ramdisk_size = stat(home+'\\Desktop\\CGT-Files\\2\\repack_dependencies\\boot.img-ramdisk.gz')
                                if ramdisk_size.st_size != 0:
                                    system("mkdir unpack")
                                    chdir('unpack')
                                    system(home+'\\.CGT\\programs\\gzip.exe -dcq '+home+'\\Desktop\\CGT-Files\\2\\repack_dependencies\\boot.img-ramdisk.gz | '+home+'\\.CGT\\programs\\cpio -i > NUL 2>&1')
                                    compress_repack_directory()
                                    _file_name = 'boot.img'
                                    file_name_ = open('CGT_435ed7e9f07f740abf511a62c00eef6e_CGT','w')
                                    file_name_.write(_file_name)
                                    file_name_.close()
                                    depen = ZipFile('repack_dependencies.zip','a')
                                    depen.write(home+'\\Desktop\\CGT-Files\\2\\CGT_435ed7e9f07f740abf511a62c00eef6e_CGT', 'CGT_435ed7e9f07f740abf511a62c00eef6e_CGT')
                                    depen.close()
                                    sleep(1)
                                    print(c.END+c.END+c.BLUE+'hazf ' + c.RED+'log ha' + c.BLUE + ' .' + c.GREEN + '.' + c.RED + '.')
                                    remove(home+'\\Desktop\\CGT-Files\\2\\boot.img')
                                    remove(home+'\\Desktop\\CGT-Files\\2\\boot.img.lz4')
                                    readme_unpack_write = '--- estekhraj shod boot.lz4 az '+basename(file) + ' tavasote CGT ---'+'\n\n'+ '- lotfan [ repack_dependencies.zip / poshe unpack ] ra hazf nakonid ya taghir name nadahid ...'
                                    readme_unpack = open(home + '\\Desktop\\CGT-Files\\2\\CGT.txt', 'w')
                                    readme_unpack.write(readme_unpack_write)
                                    readme_unpack.close()
                                    rmtree(home + "\\Desktop\\CGT-Files\\2\\repack_dependencies\\")
                                    rmtree(home + "\\Desktop\\CGT-Files\\2\\repack\\")
                                    remove(home + '\\Desktop\\CGT-Files\\2\\CGT_435ed7e9f07f740abf511a62c00eef6e_CGT')
                                    sleep(1)
                                    print(c.END+c.BLUE+'estekhraj shod '+c.RED+'boot.img.lz4'+c.BLUE+' az '+c.RED+basename(file)+c.BLUE+' dar' + c.RED + ' : ' + c.YELLOW + 'CGT-Files\\2\\'+c.RED+'unpack')
                                    chdir(home)
                                    startfile(realpath(home+'\\Desktop\\CGT-Files\\2\\unpack\\'))
                                    startfile(home+'\\Desktop\\CGT-Files\\2\\CGT.txt')
                                elif ramdisk_size.st_size == 0:
                                    sleep(1)
                                    print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'6' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                    error(6)
                                    sleep(1)
                                    print(c.BLUE+'hazf'+c.RED+' log ha '+c.BLUE+'va'+c.RED+' khoroj '+c.BLUE+'.'+c.GREEN+'.'+c.RED+'.')
                                    chdir(home)
                                    try:
                                        rmtree(home + "\\Desktop\\CGT-Files\\2\\")
                                    except:
                                        sleep(1)
                                        print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'5' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                        error(5)
                                        sleep(1)
                                        print(c.BLUE+'hazf'+c.RED+' log ha '+c.BLUE+'va'+c.RED+' khoroj '+c.BLUE+'.'+c.GREEN+'.'+c.RED+'.')
                                        chdir(home)
                                        return
                            else:
                                print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'14' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                error(14)
                        else:
                            print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'12' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                            error(12)
                else:
                    sleep(1)
                    print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'15' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                    error(15)
            elif exists(file) == False:
                print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'1' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                error(1)
    elif language == 'EN':
        print(c.END + c.BLUE+'drag' + c.RED + ' & ' + c.BLUE + 'drop ' + c.RED + c.YELLOW+'boot'+c.RED+' / ' + c.YELLOW+'recovery '+c.RED +'['+c.GREEN+'.img' + c.RED + '|' + c.GREEN + '.img.lz4'+c.RED+'|'+c.GREEN+'.tar'+c.RED+'|'+c.GREEN+'tar.md5'+c.RED+']'+c.BLUE+' and press'+c.RED+' enter ' + c.BLUE +'key'+ c.RED+' .'+c.GREEN+'.'+c.BLUE+'.')
        file = xinput(c.MAGENTA+'> '+c.YELLOW)
        file = file.replace("\"", "")
        file = file.replace("\'", "")
        file_name, file_extension = splitext(file)
        if ' ' in file:
            print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'2' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
            error(2)
        else:
            if exists(file) == True:
                if file_extension == '.lz4':
                    if (basename(file) == 'boot.img.lz4') or (basename(file) == 'recovery.img.lz4'):
                        file = file.replace(".lz4", "")
                        if isdir(home + "\\Desktop\\CGT-Files\\2\\"):
                            try:
                                sleep(1)
                                print(c.END+c.RED+'directory'+c.YELLOW+' 2 '+c.BLUE + 'already exists'+c.GREEN+' ; '+c.RED +'overwrite ' + c.BLUE + '.' + c.GREEN + '.' + c.RED + '.')
                                rmtree(home + "\\Desktop\\CGT-Files\\2\\")
                            except:
                                sleep(1)
                                print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'5' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                error(5)
                                return
                        else:
                            print(c.RED+'making'+c.BLUE+' directory '+c.YELLOW+'2'+c.RED+' .'+c.GREEN+'.'+c.BLUE+'.')
                        system('mkdir '+home + '\\Desktop\\CGT-Files\\2\\')
                        chdir(home + '\\Desktop\\CGT-Files\\2\\')
                        sleep(1)
                        print(c.END+c.BLUE + 'convert '+c.RED + basename(file+'.lz4') + c.BLUE + ' to ' + c.RED + basename(file) + c.BLUE + ' .' + c.GREEN + '.' + c.RED + '.')
                        system(home + '\\.CGT\\programs\\lz4.exe -d ' + file+'.lz4')
                        img_lz4_size = stat(file)
                        if img_lz4_size.st_size == 0:
                          sleep(1)
                          print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'4' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                          error(4)
                          sleep(1)
                          print(c.BLUE+'remove'+c.RED+' logs '+c.BLUE+'and'+c.RED+' break '+c.BLUE+'.'+c.GREEN+'.'+c.RED+'.')
                          chdir(home)
                          remove(file)
                          try:
                            rmtree(home + "\\Desktop\\CGT-Files\\2\\")
                          except:
                            print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'5' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                            error(5)
                          return
                        sleep(1)
                        print(c.END+c.BLUE + 'unpack '+c.RED+basename(file)+ c.BLUE + ' .' + c.GREEN + '.' + c.RED + '.')
                        system('mkdir '+home + '\\Desktop\\CGT-Files\\2\\repack_dependencies\\')
                        system(home+'\\.CGT\\programs\\unpackbootimg.exe' + ' -i ' + file + ' -o ' + home + '\\Desktop\\CGT-Files\\2\\repack_dependencies\\ > NUL')
                        sleep(1)
                        print(c.END+c.BLUE + 'unpack'+c.RED+' ramdisk ' + c.BLUE + '.' + c.GREEN + '.' + c.RED + '.')
                        try:
                            ramdisk_size = stat(home+'\\Desktop\\CGT-Files\\2\\repack_dependencies\\'+basename(file)+'-ramdisk.gz')
                        except:
                            sleep(1)
                            print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'8' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                            error(8)
                            sleep(1)
                            print(c.BLUE+'remove'+c.RED+' logs '+c.BLUE+'and'+c.RED+' break '+c.BLUE+'.'+c.GREEN+'.'+c.RED+'.')
                            chdir(home)
                            remove(file)
                            try:
                                rmtree(home + "\\Desktop\\CGT-Files\\2\\")
                            except:
                                print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'5' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                error(5)
                                return
                            return
                        ramdisk_size = stat(home+'\\Desktop\\CGT-Files\\2\\repack_dependencies\\'+basename(file)+'-ramdisk.gz')
                        if ramdisk_size.st_size != 0:
                            system('mkdir unpack')
                            chdir('unpack')
                            system(home+'\\.CGT\\programs\\gzip.exe -dcq '+home+'\\Desktop\\CGT-Files\\2\\repack_dependencies\\' + basename(file)+'-ramdisk.gz | '+home+'\\.CGT\\programs\\cpio -i > NUL 2>&1')
                            compress_repack_directory()
                            _file_name = basename(file)
                            file_name_ = open('CGT_435ed7e9f07f740abf511a62c00eef6e_CGT','w')
                            file_name_.write(_file_name)
                            file_name_.close()
                            depen = ZipFile('repack_dependencies.zip','a')
                            depen.write(home+'\\Desktop\\CGT-Files\\2\\CGT_435ed7e9f07f740abf511a62c00eef6e_CGT', 'CGT_435ed7e9f07f740abf511a62c00eef6e_CGT')
                            depen.close()
                            sleep(1)
                            print(c.END+c.BLUE+'remove'+c.RED+' logs '+c.BLUE+'.'+c.GREEN+'.'+c.RED+'.')
                            readme_unpack_write = '--- '+basename(file+'.lz4') + ' unpacked by CGT ---'+'\n\n'+'- please do not remove and rename [ repack_dependencies.zip file / unpack directory ] ...'
                            readme_unpack = open(home + '\\Desktop\\CGT-Files\\2\\CGT.txt', 'w')
                            readme_unpack.write(readme_unpack_write)
                            readme_unpack.close()
                            remove(file)
                            rmtree(home + "\\Desktop\\CGT-Files\\2\\repack_dependencies\\")
                            rmtree(home + "\\Desktop\\CGT-Files\\2\\repack\\")
                            remove(home + '\\Desktop\\CGT-Files\\2\\CGT_435ed7e9f07f740abf511a62c00eef6e_CGT')
                            sleep(1)
                            print(c.END+c.RED + basename(file+'.lz4') + c.BLUE+' unpacked in' + c.RED + ' : ' + c.YELLOW + 'CGT-Files\\2\\'+c.RED+'unpack')
                            chdir(home+'\\Desktop\\')
                            startfile(realpath(home+'\\Desktop\\CGT-Files\\2\\unpack\\'))
                            startfile(home+'\\Desktop\\CGT-Files\\2\\CGT.txt')
                        elif ramdisk_size.st_size == 0:
                            sleep(1)
                            print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'6' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                            error(6)
                            chdir(home)
                            remove(file)
                            print(c.BLUE+'remove'+c.RED+' logs '+c.BLUE+'and'+c.RED+' break '+c.BLUE+'.'+c.GREEN+'.'+c.RED+'.')
                            try:
                                rmtree(home + "\\Desktop\\CGT-Files\\2\\")
                            except:
                                print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'5' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                error(5)
                                return     
                    else:
                        print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'11' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                        error(11)
                elif file_extension == '.img':
                    if (basename(file) == 'boot.img') or (basename(file) == 'recovery.img'):
                        if isdir(home + "\\Desktop\\CGT-Files\\2\\"):
                            try:
                                sleep(1)
                                print(c.END+c.RED+'directory'+c.YELLOW+' 2 '+c.BLUE + 'already exists'+c.GREEN+' ; '+c.RED +'overwrite ' + c.BLUE + '.' + c.GREEN + '.' + c.RED + '.')
                                rmtree(home + "\\Desktop\\CGT-Files\\2\\")
                            except:
                                sleep(1)
                                print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'5' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                error(5)
                                return
                        else:
                            print(c.RED+'making'+c.BLUE+' directory '+c.YELLOW+'2'+c.RED+' .'+c.GREEN+'.'+c.BLUE+'.')
                        sleep(1)
                        print(c.END+c.BLUE + 'unpack '+c.RED+basename(file)+ c.BLUE + ' .' + c.GREEN + '.' + c.RED + '.')
                        system('mkdir '+home + '\\Desktop\\CGT-Files\\2\\')
                        chdir(home + '\\Desktop\\CGT-Files\\2\\')
                        system('mkdir '+home +
                                '\\Desktop\\CGT-Files\\2\\repack_dependencies\\')
                        system(home+'\\.CGT\\programs\\unpackbootimg.exe' + ' -i ' +
                                file + ' -o ' + home + '\\Desktop\\CGT-Files\\2\\repack_dependencies\\ > NUL')
                        sleep(1)
                        print(c.END+c.BLUE + 'unpack'+c.RED+' ramdisk ' +
                            c.BLUE + '.' + c.GREEN + '.' + c.RED + '.')
                        try:
                            ramdisk_size = stat(home+'\\Desktop\\CGT-Files\\2\\repack_dependencies\\'+basename(file)+'-ramdisk.gz')
                        except:
                            sleep(1)
                            print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'8' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                            error(8)
                            sleep(1)
                            print(c.BLUE+'remove'+c.RED+' logs '+c.BLUE+'and'+c.RED+' break '+c.BLUE+'.'+c.GREEN+'.'+c.RED+'.')
                            chdir(home)
                            try:
                                rmtree(home + "\\Desktop\\CGT-Files\\2\\")
                            except:
                                print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'5' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                error(5)
                            return
                        ramdisk_size = stat(home+'\\Desktop\\CGT-Files\\2\\repack_dependencies\\'+basename(file)+'-ramdisk.gz')
                        if ramdisk_size.st_size != 0:
                            system("mkdir unpack")
                            chdir('unpack')
                            system(home+'\\.CGT\\programs\\gzip.exe -dcq '+home+'\\Desktop\\CGT-Files\\2\\repack_dependencies\\' + basename(file)+'-ramdisk.gz | '+home+'\\.CGT\\programs\\cpio -i > NUL 2>&1')
                            compress_repack_directory()
                            _file_name = basename(file)
                            file_name_ = open('CGT_435ed7e9f07f740abf511a62c00eef6e_CGT','w')
                            file_name_.write(_file_name)
                            file_name_.close()
                            depen = ZipFile('repack_dependencies.zip','a')
                            depen.write(home+'\\Desktop\\CGT-Files\\2\\CGT_435ed7e9f07f740abf511a62c00eef6e_CGT', 'CGT_435ed7e9f07f740abf511a62c00eef6e_CGT')
                            depen.close()
                            sleep(1)
                            print(c.END+c.BLUE+'remove'+c.RED+' logs '+c.BLUE+'.'+c.GREEN+'.'+c.RED+'.')
                            readme_unpack_write = '--- '+basename(
                                file) + ' unpacked by CGT ---'+'\n\n'+'- please do not remove and rename repack_dependencies.zip file / unpack directory ...'
                            readme_unpack = open(
                                home + '\\Desktop\\CGT-Files\\2\\CGT.txt', 'w')
                            readme_unpack.write(readme_unpack_write)
                            readme_unpack.close()
                            rmtree(home + "\\Desktop\\CGT-Files\\2\\repack_dependencies\\")
                            rmtree(home + "\\Desktop\\CGT-Files\\2\\repack\\")
                            remove(home + '\\Desktop\\CGT-Files\\2\\CGT_435ed7e9f07f740abf511a62c00eef6e_CGT')
                            sleep(1)
                            print(c.END+c.RED + basename(file) + c.BLUE+' unpacked in' +
                                c.RED + ' : ' + c.YELLOW + 'CGT-Files\\2\\'+c.RED+'unpack')
                            chdir(home)
                            startfile(realpath(home+'\\Desktop\\CGT-Files\\2\\unpack\\'))
                            startfile(home+'\\Desktop\\CGT-Files\\2\\CGT.txt')
                        elif ramdisk_size.st_size == 0:
                            sleep(1)
                            print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'6' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                            error(6)
                            print(c.BLUE+'remove'+c.RED+' logs '+c.BLUE+'and'+c.RED+' break '+c.BLUE+'.'+c.GREEN+'.'+c.RED+'.')
                            chdir(home)
                            try:
                                rmtree(home + "\\Desktop\\CGT-Files\\2\\")
                            except:
                                print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'5' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                error(5)
                            return
                    else:
                        print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'10' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                        error(10)
                elif (file_extension == '.md5') or (file_extension == '.tar'):
                    tar_file = TarFileOpen(file)
                    if ('recovery.img' not in tar_file.getnames()) and ('recovery.img.lz4' not in tar_file.getnames()) and ('boot.img' not in tar_file.getnames()) and ('boot.img.lz4' not in tar_file.getnames()):
                        print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'9' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                        error(9)
                    else:
                        sleep(1)
                        print(c.END+c.YELLOW+'a'+c.GREEN+'.'+c.BLUE+'unpack '+c.RED+'recovery')
                        print(c.END+c.YELLOW+'b'+c.GREEN+'.'+c.BLUE+'unpack '+c.RED+'boot')
                        un = xinput(c.GREEN+'> '+c.YELLOW)
                        if un == 'a':
                            if 'recovery.img' in tar_file.getnames():
                                if isdir(home + "\\Desktop\\CGT-Files\\2\\"):
                                    try:
                                        sleep(1)
                                        print(c.END+c.RED+'directory'+c.YELLOW+' 2 '+c.BLUE + 'already exists'+c.GREEN+' ; '+c.RED +'overwrite ' + c.BLUE + '.' + c.GREEN + '.' + c.RED + '.')
                                        rmtree(home + "\\Desktop\\CGT-Files\\2\\")
                                    except:
                                        sleep(1)
                                        print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'5' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                        error(5)
                                        return
                                else:
                                    print(c.RED+'making'+c.BLUE+' directory '+c.YELLOW+'2'+c.RED+' .'+c.GREEN+'.'+c.BLUE+'.')
                                system('mkdir '+home + '\\Desktop\\CGT-Files\\2\\')
                                chdir(home + '\\Desktop\\CGT-Files\\2\\')
                                sleep(1)
                                print(c.END+c.BLUE+'find'+c.RED+' recovery.img'+c.BLUE+' in '+c.RED+basename(file)+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                sleep(1)
                                print(c.END+c.BLUE+'extract'+c.RED+' recovery.img '+c.BLUE+'from '+c.RED+basename(file)+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                tar_file.extract('recovery.img')
                                sleep(1)
                                print(c.END+c.BLUE + 'unpack ' + c.RED + 'recovery.img' + c.BLUE + ' .' + c.GREEN + '.' + c.RED + '.')
                                system('mkdir '+home + '\\Desktop\\CGT-Files\\2\\repack_dependencies\\')
                                system(home+'\\.CGT\\programs\\unpackbootimg.exe' + ' -i ' +
                                home+'\\Desktop\\CGT-Files\\2\\recovery.img' + ' -o ' + home + '\\Desktop\\CGT-Files\\2\\repack_dependencies\\ > NUL')
                                sleep(1)
                                print(c.END+c.BLUE + 'unpack'+c.RED+' ramdisk ' + c.BLUE + '.' + c.GREEN + '.' + c.RED + '.')
                                ramdisk_size = stat(home+'\\Desktop\\CGT-Files\\2\\repack_dependencies\\recovery.img-ramdisk.gz')
                                if ramdisk_size.st_size != 0:
                                    system("mkdir unpack")
                                    chdir('unpack')
                                    system(home+'\\.CGT\\programs\\gzip.exe -dcq '+home+'\\Desktop\\CGT-Files\\2\\repack_dependencies\\recovery.img-ramdisk.gz | '+home+'\\.CGT\\programs\\cpio -i > NUL 2>&1')
                                    compress_repack_directory()
                                    _file_name = 'recovery.img'
                                    file_name_ = open('CGT_435ed7e9f07f740abf511a62c00eef6e_CGT','w')
                                    file_name_.write(_file_name)
                                    file_name_.close()
                                    depen = ZipFile('repack_dependencies.zip','a')
                                    depen.write(home+'\\Desktop\\CGT-Files\\2\\CGT_435ed7e9f07f740abf511a62c00eef6e_CGT', 'CGT_435ed7e9f07f740abf511a62c00eef6e_CGT')
                                    depen.close()
                                    sleep(1)
                                    print(c.END+c.BLUE+'remove ' + c.RED+'logs' + c.BLUE + ' .' + c.GREEN + '.' + c.RED + '.')
                                    remove(home+'\\Desktop\\CGT-Files\\2\\recovery.img')
                                    readme_unpack_write = '--- unpacked recovery.img from '+basename(file)+' by CGT ---'+'\n\n'+'- please do not remove and rename [ repack_dependencies.zip / unpack directory ] ...'
                                    readme_unpack = open(home + '\\Desktop\\CGT-Files\\2\\CGT.txt', 'w')
                                    readme_unpack.write(readme_unpack_write)
                                    readme_unpack.close()
                                    rmtree(home + "\\Desktop\\CGT-Files\\2\\repack_dependencies\\")
                                    rmtree(home + "\\Desktop\\CGT-Files\\2\\repack\\")
                                    remove(home + '\\Desktop\\CGT-Files\\2\\CGT_435ed7e9f07f740abf511a62c00eef6e_CGT')
                                    sleep(1)
                                    print(c.END+c.BLUE+'unpacked '+c.RED+'recovery.img'+c.BLUE+' from '+c.RED+basename(file)+c.BLUE+' in' + c.RED + ' : ' + c.YELLOW + 'CGT-Files\\2\\'+c.RED+'unpack')
                                    chdir(home)
                                    startfile(realpath(home+'\\Desktop\\CGT-Files\\2\\unpack\\'))
                                    startfile(home+'\\Desktop\\CGT-Files\\2\\CGT.txt')
                                elif ramdisk_size.st_size == 0:
                                    sleep(1)
                                    print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'6' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                    error(6)
                                    sleep(1)
                                    print(c.BLUE+'remove'+c.RED+' logs '+c.BLUE+'and'+c.RED+' break '+c.BLUE+'.'+c.GREEN+'.'+c.RED+'.')
                                    chdir(home)
                                    try:
                                        rmtree(home + "\\Desktop\\CGT-Files\\2\\")
                                    except:
                                        print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'5' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                        error(5)
                                    return
                            elif 'recovery.img.lz4' in tar_file.getnames():
                                if isdir(home + "\\Desktop\\CGT-Files\\2\\"):
                                    try:
                                        sleep(1)
                                        print(c.END+c.RED+'directory'+c.YELLOW+' 2 '+c.BLUE + 'already exists'+c.GREEN+' ; '+c.RED +'overwrite ' + c.BLUE + '.' + c.GREEN + '.' + c.RED + '.')
                                        rmtree(home + "\\Desktop\\CGT-Files\\2\\")
                                    except:
                                        sleep(1)
                                        print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'5' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                        error(5)
                                        return
                                else:
                                    print(c.RED+'making'+c.BLUE+' directory '+c.YELLOW+'2'+c.RED+' .'+c.GREEN+'.'+c.BLUE+'.')
                                system('mkdir '+home + '\\Desktop\\CGT-Files\\2\\')
                                chdir(home + '\\Desktop\\CGT-Files\\2\\')
                                sleep(1)
                                print(c.END+c.BLUE+'find'+c.RED+' recovery.img.lz4'+c.BLUE+' in '+c.RED+basename(file)+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                sleep(1)
                                print(c.END+c.BLUE+'extract'+c.RED+' recovery.img.lz4 '+c.BLUE+'from '+c.RED+basename(file)+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                tar_file.extract('recovery.img.lz4')
                                sleep(1)
                                print(c.END+c.BLUE + 'convert '+c.RED + 'recovery.img.lz4' + c.BLUE + ' to ' +
                                    c.RED + 'recovery.img' + c.BLUE + ' .' + c.GREEN + '.' + c.RED + '.')
                                system(home +
                                        '\\.CGT\\programs\\lz4.exe -d recovery.img.lz4')
                                img_lz4_size = stat(home+'\\Desktop\\CGT-Files\\2\\recovery.img')
                                if img_lz4_size.st_size == 0:
                                  sleep(1)
                                  print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'4' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                  error(4)
                                  sleep(1)
                                  print(c.BLUE+'remove'+c.RED+' logs '+c.BLUE+'and'+c.RED+' break '+c.BLUE+'.'+c.GREEN+'.'+c.RED+'.')
                                  chdir(home)
                                  try:
                                    rmtree(home + "\\Desktop\\CGT-Files\\2\\")
                                  except:
                                    print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'5' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                    error(5)
                                  return
                                sleep(1)
                                print(c.END+c.BLUE + 'unpack ' + c.RED + 'recovery.img' + c.BLUE + ' .' + c.GREEN + '.' + c.RED + '.')
                                system('mkdir '+home + '\\Desktop\\CGT-Files\\2\\repack_dependencies\\')
                                system(home+'\\.CGT\\programs\\unpackbootimg.exe' + ' -i ' + home+'\\Desktop\\CGT-Files\\2\\recovery.img' + ' -o ' + home + '\\Desktop\\CGT-Files\\2\\repack_dependencies\\ > NUL')
                                sleep(1)
                                print(c.END+c.BLUE + 'unpack'+c.RED+' ramdisk ' + c.BLUE + '.' + c.GREEN + '.' + c.RED + '.')
                                ramdisk_size = stat(home+'\\Desktop\\CGT-Files\\2\\repack_dependencies\\recovery.img-ramdisk.gz')
                                if ramdisk_size.st_size != 0:
                                    system("mkdir unpack")
                                    chdir('unpack')
                                    system(home+'\\.CGT\\programs\\gzip.exe -dcq '+home+'\\Desktop\\CGT-Files\\2\\repack_dependencies\\recovery.img-ramdisk.gz | '+home+'\\.CGT\\programs\\cpio -i > NUL 2>&1')
                                    compress_repack_directory()
                                    _file_name = 'recovery.img'
                                    file_name_ = open('CGT_435ed7e9f07f740abf511a62c00eef6e_CGT','w')
                                    file_name_.write(_file_name)
                                    file_name_.close()
                                    depen = ZipFile('repack_dependencies.zip','a')
                                    depen.write(home+'\\Desktop\\CGT-Files\\2\\CGT_435ed7e9f07f740abf511a62c00eef6e_CGT', 'CGT_435ed7e9f07f740abf511a62c00eef6e_CGT')
                                    depen.close()
                                    sleep(1)
                                    print(c.END+c.BLUE+'remove ' + c.RED+'logs' + c.BLUE + ' .' + c.GREEN + '.' + c.RED + '.')
                                    remove(home+'\\Desktop\\CGT-Files\\2\\recovery.img')
                                    remove(home+'\\Desktop\\CGT-Files\\2\\recovery.img.lz4')
                                    readme_unpack_write = '--- unpacked recovery.img.lz4 from '+basename(file)+' by CGT ---'+'\n\n'+'- please do not remove and rename repack_dependencies.zip / unpack directory ...'
                                    readme_unpack = open(home + '\\Desktop\\CGT-Files\\2\\CGT.txt', 'w')
                                    readme_unpack.write(readme_unpack_write)
                                    readme_unpack.close()
                                    rmtree(home + "\\Desktop\\CGT-Files\\2\\repack_dependencies\\")
                                    rmtree(home + "\\Desktop\\CGT-Files\\2\\repack\\")
                                    remove(home + '\\Desktop\\CGT-Files\\2\\CGT_435ed7e9f07f740abf511a62c00eef6e_CGT')
                                    sleep(1)
                                    print(c.END+c.BLUE+'unpacked '+c.RED+'recovery.img.lz4'+c.BLUE+' from '+c.RED+basename(file)+c.BLUE+' in' + c.RED + ' : ' + c.YELLOW + 'CGT-Files\\2\\'+c.RED+'unpack')
                                    chdir(home)
                                    startfile(realpath(home+'\\Desktop\\CGT-Files\\2\\unpack\\'))
                                    startfile(home+'\\Desktop\\CGT-Files\\2\\CGT.txt')
                                elif ramdisk_size.st_size == 0:
                                    sleep(1)
                                    print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'6' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                    error(6)
                                    print(c.END+c.BLUE+'remove ' + c.RED+'logs' + c.BLUE + ' .' + c.GREEN + '.' + c.RED + '.')
                                    chdir(home)
                                    try:
                                        rmtree(home + "\\Desktop\\CGT-Files\\2\\")
                                    except:
                                        print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'5' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                        error(5)
                                    return
                            else:
                                print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'13' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')   
                                error(13)
                        elif un == 'b':
                            if 'boot.img' in tar_file.getnames():
                                if isdir(home + "\\Desktop\\CGT-Files\\2\\"):
                                    try:
                                        sleep(1)
                                        print(c.END+c.RED+'directory'+c.YELLOW+' 2 '+c.BLUE + 'already exists'+c.GREEN+' ; '+c.RED +'overwrite ' + c.BLUE + '.' + c.GREEN + '.' + c.RED + '.')
                                        rmtree(home + "\\Desktop\\CGT-Files\\2\\")
                                    except:
                                        sleep(1)
                                        print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'5' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                        error(5)
                                        return
                                else:
                                    print(c.RED+'making'+c.BLUE+' directory '+c.YELLOW+'2'+c.RED+' .'+c.GREEN+'.'+c.BLUE+'.')
                                system('mkdir '+home + '\\Desktop\\CGT-Files\\2\\')
                                chdir(home + '\\Desktop\\CGT-Files\\2\\')
                                sleep(1)
                                print(c.END+c.BLUE+'find'+c.RED+' boot.img'+c.BLUE+' in '+c.RED+basename(file)+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                sleep(1)
                                print(c.END+c.BLUE+'extract'+c.RED+' boot.img '+c.BLUE+'from '+c.RED+basename(file)+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                tar_file.extract('boot.img')
                                sleep(1)
                                print(c.END+c.BLUE + 'unpack ' + c.RED + 'boot.img' +c.BLUE + ' .' + c.GREEN + '.' + c.RED + '.')
                                system('mkdir '+home + '\\Desktop\\CGT-Files\\2\\repack_dependencies\\')
                                system(home+'\\.CGT\\programs\\unpackbootimg.exe' + ' -i ' +
                                home+'\\Desktop\\CGT-Files\\2\\boot.img' + ' -o ' + home + '\\Desktop\\CGT-Files\\2\\repack_dependencies\\ > NUL')
                                sleep(1)
                                print(c.END+c.BLUE + 'unpack'+c.RED+' ramdisk ' + c.BLUE + '.' + c.GREEN + '.' + c.RED + '.')
                                ramdisk_size = stat(home+'\\Desktop\\CGT-Files\\2\\repack_dependencies\\boot.img-ramdisk.gz')
                                if ramdisk_size.st_size != 0:
                                    system("mkdir unpack")
                                    chdir('unpack')
                                    system(home+'\\.CGT\\programs\\gzip.exe -dcq '+home+'\\Desktop\\CGT-Files\\2\\repack_dependencies\\boot.img-ramdisk.gz | '+home+'\\.CGT\\programs\\cpio -i > NUL 2>&1')
                                    compress_repack_directory()
                                    _file_name = 'boot.img'
                                    file_name_ = open('CGT_435ed7e9f07f740abf511a62c00eef6e_CGT','w')
                                    file_name_.write(_file_name)
                                    file_name_.close()
                                    depen = ZipFile('repack_dependencies.zip','a')
                                    depen.write(home+'\\Desktop\\CGT-Files\\2\\CGT_435ed7e9f07f740abf511a62c00eef6e_CGT', 'CGT_435ed7e9f07f740abf511a62c00eef6e_CGT')
                                    depen.close()
                                    sleep(1)
                                    print(c.BLUE+'remove'+c.RED+' logs '+c.BLUE+'.'+c.GREEN+'.'+c.RED+'.')
                                    remove(home+'\\Desktop\\CGT-Files\\2\\boot.img')
                                    readme_unpack_write = '--- unpacked boot.img from '+basename(file)+' by CGT ---'+'\n\n'+'- please do not remove and rename [ repack_dependencies.zip file / unpack directory ] ...'
                                    readme_unpack = open(home + '\\Desktop\\CGT-Files\\2\\CGT.txt', 'w')
                                    readme_unpack.write(readme_unpack_write)
                                    readme_unpack.close()
                                    rmtree(home + "\\Desktop\\CGT-Files\\2\\repack_dependencies\\")
                                    rmtree(home + "\\Desktop\\CGT-Files\\2\\repack\\")
                                    remove(home + '\\Desktop\\CGT-Files\\2\\CGT_435ed7e9f07f740abf511a62c00eef6e_CGT')
                                    sleep(1)
                                    print(c.END+c.BLUE+'unpacked '+c.RED+'boot.img'+c.BLUE+' from '+c.RED+basename(file)+c.BLUE+' in' + c.RED + ' : ' + c.YELLOW + 'CGT-Files\\2\\'+c.RED+'unpack')
                                    chdir(home)
                                    startfile(realpath(home+'\\Desktop\\CGT-Files\\2\\unpack\\'))
                                    startfile(home+'\\Desktop\\CGT-Files\\2\\CGT.txt')
                                elif ramdisk_size.st_size == 0:
                                    sleep(1)
                                    print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'6' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                    error(6)
                                    print(c.BLUE+'remove'+c.RED+' logs '+c.BLUE+'and'+c.RED+' break '+c.BLUE+'.'+c.GREEN+'.'+c.RED+'.')
                                    chdir(home)
                                    try:
                                        rmtree(home + "\\Desktop\\CGT-Files\\2\\")
                                    except:
                                        print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'5' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                        error(5)
                                    return
                            elif 'boot.img.lz4' in tar_file.getnames():
                                if isdir(home + "\\Desktop\\CGT-Files\\2\\"):
                                    try:
                                        sleep(1)
                                        print(c.END+c.RED+'directory'+c.YELLOW+' 2 '+c.BLUE + 'already exists'+c.GREEN+' ; '+c.RED +'overwrite ' + c.BLUE + '.' + c.GREEN + '.' + c.RED + '.')
                                        rmtree(home + "\\Desktop\\CGT-Files\\2\\")
                                    except:
                                        sleep(1)
                                        print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'5' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                        error(5)
                                        return
                                else:
                                    print(c.RED+'making'+c.BLUE+' directory '+c.YELLOW+'2'+c.RED+' .'+c.GREEN+'.'+c.BLUE+'.')
                                system('mkdir '+home + '\\Desktop\\CGT-Files\\2\\')
                                chdir(home + '\\Desktop\\CGT-Files\\2\\')
                                sleep(1)
                                print(c.END+c.BLUE+'find'+c.RED+' boot.img.lz4'+c.BLUE+' in '+c.RED+basename(file)+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                sleep(1)
                                print(c.END+c.BLUE+'extract'+c.RED+' boot.img.lz4 '+c.BLUE+'from '+c.RED+basename(file)+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                tar_file.extract('boot.img.lz4')
                                sleep(1)
                                print(c.END+c.BLUE + 'convert '+c.RED + 'boot.img.lz4' + c.BLUE + ' to ' +
                                    c.RED + 'boot.img' + c.BLUE + ' .' + c.GREEN + '.' + c.RED + '.')
                                system(home +
                                        '\\.CGT\\programs\\lz4.exe -d boot.img.lz4')
                                img_lz4_size = stat(home+'\\Desktop\\CGT-Files\\2\\boot.img')
                                if img_lz4_size.st_size == 0:
                                  sleep(1)
                                  print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'4' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                  error(4)
                                  sleep(1)
                                  print(c.BLUE+'remove'+c.RED+' logs '+c.BLUE+'and'+c.RED+' break '+c.BLUE+'.'+c.GREEN+'.'+c.RED+'.')
                                  chdir(home)
                                  try:
                                    rmtree(home + "\\Desktop\\CGT-Files\\2\\")
                                  except:
                                    print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'5' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                    error(5)
                                  return
                                sleep(1)
                                print(c.END+c.BLUE + 'unpack ' + c.RED + 'boot.img'+c.BLUE + ' .' + c.GREEN + '.' + c.RED + '.')
                                system('mkdir '+home + '\\Desktop\\CGT-Files\\2\\repack_dependencies\\')
                                system(home+'\\.CGT\\programs\\unpackbootimg.exe' + ' -i ' +
                                home+'\\Desktop\\CGT-Files\\2\\boot.img' + ' -o ' + home + '\\Desktop\\CGT-Files\\2\\repack_dependencies\\ > NUL')
                                sleep(1)
                                print(c.END+c.BLUE + 'unpack'+c.RED+' ramdisk ' + c.BLUE + '.' + c.GREEN + '.' + c.RED + '.')
                                ramdisk_size = stat(home+'\\Desktop\\CGT-Files\\2\\repack_dependencies\\boot.img-ramdisk.gz')
                                if ramdisk_size.st_size != 0:
                                    system("mkdir unpack")
                                    chdir('unpack')
                                    system(home+'\\.CGT\\programs\\gzip.exe -dcq '+home+'\\Desktop\\CGT-Files\\2\\repack_dependencies\\boot.img-ramdisk.gz | '+home+'\\.CGT\\programs\\cpio -i > NUL 2>&1')
                                    compress_repack_directory()
                                    _file_name = 'boot.img'
                                    file_name_ = open('CGT_435ed7e9f07f740abf511a62c00eef6e_CGT','w')
                                    file_name_.write(_file_name)
                                    file_name_.close()
                                    depen = ZipFile('repack_dependencies.zip','a')
                                    depen.write(home+'\\Desktop\\CGT-Files\\2\\CGT_435ed7e9f07f740abf511a62c00eef6e_CGT', 'CGT_435ed7e9f07f740abf511a62c00eef6e_CGT')
                                    depen.close()
                                    sleep(1)
                                    print(c.END+c.END+c.BLUE+'remove ' + c.RED+'logs' + c.BLUE + ' .' + c.GREEN + '.' + c.RED + '.')
                                    remove(home+'\\Desktop\\CGT-Files\\2\\boot.img')
                                    remove(home+'\\Desktop\\CGT-Files\\2\\boot.img.lz4')
                                    readme_unpack_write = '--- unpacked boot.img.lz4 from '+basename(file)+' by CGT ---'+'\n\n'+'- please do not remove and rename [ repack_dependencies.zip file / unpack directory ] ...'
                                    readme_unpack = open(home + '\\Desktop\\CGT-Files\\2\\CGT.txt', 'w')
                                    readme_unpack.write(readme_unpack_write)
                                    readme_unpack.close()
                                    rmtree(home + "\\Desktop\\CGT-Files\\2\\repack_dependencies\\")
                                    rmtree(home + "\\Desktop\\CGT-Files\\2\\repack\\")
                                    remove(home + '\\Desktop\\CGT-Files\\2\\CGT_435ed7e9f07f740abf511a62c00eef6e_CGT')
                                    sleep(1)
                                    print(c.END+c.BLUE+'unpacked '+c.RED+'boot.img.lz4'+c.BLUE+' from '+c.RED+basename(file)+c.BLUE+' in' + c.RED + ' : ' + c.YELLOW + 'CGT-Files\\2\\'+c.RED+'unpack')
                                    chdir(home)
                                    startfile(realpath(home+'\\Desktop\\CGT-Files\\2\\unpack\\'))
                                    startfile(home+'\\Desktop\\CGT-Files\\2\\CGT.txt')
                                elif ramdisk_size.st_size == 0:
                                    sleep(1)
                                    print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'6' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                    error(6)
                                    chdir(home)
                                    try:
                                        rmtree(home + "\\Desktop\\CGT-Files\\2\\")
                                    except:
                                        print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'5' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                        error(5)
                                        return
                            else:
                                print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'14' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                error(14)
                        else:
                            print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'12' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                            error(12)
                else:
                    sleep(1)
                    print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'15' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                    error(15)
            elif exists(file) == False:
                print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'1' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                error(1)

def if_2():
  if os_type().upper() == 'WINDOWS':
    windows()
  elif os_type().upper() == 'LINUX':
    linux()
  else:
    pass
