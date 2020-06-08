# Copyright SYS113 2019. gpl v3.0 license , see readme file.

try:
    from os import startfile    
except:
    pass
from error import error
from pathlib import Path
from os.path import isdir , isfile , realpath
from os import chdir , system , remove
from platform import system as os_type
from time import sleep
from shutil import rmtree , make_archive
from zipfile import ZipFile

home = (str(Path.home()))

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

if os_type().upper() == 'WINDOWS':
    if isfile(home+'\\.CGT\\files\\LANGUAGE'):
        language = open(home + '\\.CGT\\files\\LANGUAGE', 'r').read()
elif os_type().upper() == 'LINUX':
    if isfile(home+'/.CGT/files/LANGUAGE'):
        language = open(home + '/.CGT/files/LANGUAGE', 'r').read()
else:
    pass

def windows():
    if language == 'FA':
        if isdir(home + '\\Desktop\\CGT-Files\\2\\'):
            if isfile(home + '\\Desktop\\CGT-Files\\2\\repack_dependencies.zip'):
                if isdir(home + '\\Desktop\\CGT-Files\\2\\unpack\\'):
                    if isdir(home + "\\Desktop\\CGT-Files\\3\\"):
                        try:
                            sleep(1)
                            print(c.END+c.RED+'poshe'+c.YELLOW+' 3 '+c.BLUE + 'vojod darad'+c.GREEN+' ; '+c.RED + 'hazf '+c.GREEN+'&'+c.RED+' sakht dobare ' + c.BLUE + '.' + c.GREEN + '.' + c.RED + '.')
                            rmtree(home + "\\Desktop\\CGT-Files\\3\\")
                        except:
                            sleep(1)
                            print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'16' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                            error(16)
                            return
                    else:
                        print(c.RED+'sakht'+c.BLUE+' poshe '+c.YELLOW+'3'+c.RED+' .'+c.GREEN+'.'+c.BLUE+'.')
                    sleep(1)
                    print(c.END + c.RED + 'feshorde'+c.BLUE+' kardan '+c.RED+'poshe'+c.YELLOW+' unpack'+ c.BLUE+' va '+c.RED+'tabdil'+c.BLUE+' an be' +c.RED+' ramdisk' + c.BLUE + ' .' + c.GREEN + '.' + c.RED + '.')
                    chdir(home+'\\Desktop\\CGT-Files\\2\\')
                    system(home+'\\.CGT\\programs\\mkbootfs.exe unpack | '+home+'\\.CGT\\programs\\minigzip.exe -c -9 > '+home + '\\Desktop\\CGT-Files\\2\\CGT_5c5f44ab0550487fbce8a2874ebaab6a_CGT.gz 2>NUL')
                    sleep(1)
                    print(c.END + c.BLUE + 'ezafe kardan '+c.RED+'ramdisk'+c.BLUE+' be '+c.RED+'repack_dependencies.zip ' + c.BLUE + '.' + c.GREEN + '.' + c.RED + '.')
                    with ZipFile('repack_dependencies.zip', 'a') as zipf:
                        zipf.write(home + '\\Desktop\\CGT-Files\\2\\CGT_5c5f44ab0550487fbce8a2874ebaab6a_CGT.gz' , 'CGT_5c5f44ab0550487fbce8a2874ebaab6a_CGT.gz')
                    sleep(1)
                    print(c.END + c.BLUE + 'estekhraj '+c.RED+'repack_dependencies.zip ' + c.BLUE + '.' + c.GREEN + '.' + c.RED + '.')
                    system('mkdir '+home + '\\Desktop\\CGT-Files\\2\\repack\\')
                    with ZipFile(home + '\\Desktop\\CGT-Files\\2\\repack_dependencies.zip', 'r') as zip_ref:
                        zip_ref.extractall(home + '\\Desktop\\CGT-Files\\2\\repack\\')
                    new_kernel = home+'\\Desktop\\CGT-Files\\2\\repack\\CGT_50484c19f1afdaf3841a0d821ed393d2_CGT'
                    new_cmdline = home+'\\Desktop\\CGT-Files\\2\\repack\\CGT_95f44086bc13f782435dd6356310e7bd_CGT'
                    new_base = home+'\\Desktop\\CGT-Files\\2\\repack\\CGT_593616de15330c0fb2d55e55410bf994_CGT'
                    new_pagesize = home+'\\Desktop\\CGT-Files\\2\\repack\\CGT_7525d528a3457f0227997c25239c4507_CGT'
                    new_dt = home+'\\Desktop\\CGT-Files\\2\\repack\\CGT_3017d911efceb27d1de6a92b70979795_CGT'
                    new_kerneloffset = home+'\\Desktop\\CGT-Files\\2\\repack\\CGT_706cf6b230a6d77ee280a40b54246762_CGT'
                    new_ramdiskoffset = home+'\\Desktop\\CGT-Files\\2\\repack\\CGT_0e16d6f83afe32911816ef683ad5d639_CGT'
                    new_secondoffset = home+'\\Desktop\\CGT-Files\\2\\repack\\CGT_d753658059439ac8a93d411e68e5d66a_CGT'
                    new_tagsoffset = home+'\\Desktop\\CGT-Files\\2\\repack\\CGT_a4d756b70ed4593b8d0f2abd01694f39_CGT'
                    new_hash = home+'\\Desktop\\CGT-Files\\2\\repack\\CGT_0800fc577294c34e0b28ad2839435945_CGT'
                    class repack:
                            _filename = open(home+'\\Desktop\\CGT-Files\\2\\repack\\CGT_435ed7e9f07f740abf511a62c00eef6e_CGT').read()
                            _mkboot = home+'\\.CGT\\programs\\mkbootimg.exe'
                            _kernel = home+'\\Desktop\\CGT-Files\\2\\repack\\CGT_50484c19f1afdaf3841a0d821ed393d2_CGT'
                            _ramdisk = home+'\\Desktop\\CGT-Files\\2\\repack\\CGT_5c5f44ab0550487fbce8a2874ebaab6a_CGT.gz'
                            _cmdline = open(home+'\\Desktop\\CGT-Files\\2\\repack\\CGT_95f44086bc13f782435dd6356310e7bd_CGT').read().replace('\n', '')
                            _cmdline = '\"'+_cmdline+'\"'
                            _base = open(home+'\\Desktop\\CGT-Files\\2\\repack\\CGT_593616de15330c0fb2d55e55410bf994_CGT').read().replace('\n', '')
                            _pagesize = open(home+'\\Desktop\\CGT-Files\\2\\repack\\CGT_7525d528a3457f0227997c25239c4507_CGT').read().replace('\n', '')
                            _dt = home+'\\Desktop\\CGT-Files\\2\\repack\\CGT_3017d911efceb27d1de6a92b70979795_CGT'
                            _kerneloffset = open(home+'\\Desktop\\CGT-Files\\2\\repack\\CGT_706cf6b230a6d77ee280a40b54246762_CGT').read().replace('\n', '')
                            _ramdiskoffset = open(home+'\\Desktop\\CGT-Files\\2\\repack\\CGT_0e16d6f83afe32911816ef683ad5d639_CGT').read().replace('\n', '')
                            _secondoffset = open(home+'\\Desktop\\CGT-Files\\2\\repack\\CGT_d753658059439ac8a93d411e68e5d66a_CGT').read().replace('\n', '')
                            _tagsoffset = open(home+'\\Desktop\\CGT-Files\\2\\repack\\CGT_a4d756b70ed4593b8d0f2abd01694f39_CGT').read().replace('\n', '')
                            _hash = open(home+'\\Desktop\\CGT-Files\\2\\repack\\CGT_0800fc577294c34e0b28ad2839435945_CGT').read().replace('\n', '')
                            _hash = '\"'+_hash+'\"'
                    sleep(1)
                    print(c.END + c.BLUE + 'tabdil '+c.RED+'ramdisk'+c.BLUE+' & '+c.RED+'dependencies' + c.BLUE+' be '+c.RED + repack._filename + c.BLUE + ' .' + c.GREEN + '.' + c.RED + '.')
                    system('mkdir '+home + '\\Desktop\\CGT-Files\\3\\')
                    chdir(home + '\\Desktop\\CGT-Files\\3\\')
                    if isfile(new_dt):
                        system(repack._mkboot+' --kernel '+repack._kernel+' --ramdisk '+repack._ramdisk+' --cmdline '+repack._cmdline+' --base '+repack._base+' --pagesize '+repack._pagesize+' --dt '+repack._dt+' --kernel_offset '+repack._kerneloffset+' --ramdisk_offset '+repack._ramdiskoffset+' --second_offset '+repack._secondoffset+' --tags_offset '+repack._tagsoffset+' --hash '+repack._hash+' -o '+repack._filename)
                    elif not isfile(new_dt):
                        system(repack._mkboot+' --kernel '+repack._kernel+' --ramdisk '+repack._ramdisk+' --cmdline '+repack._cmdline+' --base '+repack._base+' --pagesize '+repack._pagesize+' --kernel_offset '+repack._kerneloffset+' --ramdisk_offset '+repack._ramdiskoffset+' --second_offset '+repack._secondoffset+' --tags_offset '+repack._tagsoffset+' --hash '+repack._hash+' -o '+repack._filename)
                    sleep(1)
                    print(c.END+c.BLUE+'hazf ' + c.RED+'log ha' + c.BLUE + ' .' + c.GREEN + '.' + c.RED + '.')
                    remove(home+'\\Desktop\\CGT-Files\\2\\CGT_5c5f44ab0550487fbce8a2874ebaab6a_CGT.gz')
                    remove(home+'\\Desktop\\CGT-Files\\2\\repack_dependencies.zip')
                    remove(home + '\\Desktop\\CGT-Files\\2\\repack\\CGT_5c5f44ab0550487fbce8a2874ebaab6a_CGT.gz')
                    make_archive(home+'\\Desktop\\CGT-Files\\2\\repack_dependencies\\', 'zip', home+'\\Desktop\\CGT-Files\\2\\repack\\')
                    rmtree(home + "\\Desktop\\CGT-Files\\2\\repack\\")
                    readme_repack_write = '--- tabdil dobare be '+repack._filename+' tavasote CGT ---'
                    readme_repack = open(
                        home + '\\Desktop\\CGT-Files\\3\\CGT.txt', 'w')
                    readme_repack.write(readme_repack_write)
                    readme_repack.close()
                    sleep(1)
                    print(c.END + c.RED + 'poshe ' +c.YELLOW+'unpack ' + c.BLUE + 'tabdil shod be ' + c.GREEN+repack._filename +c.RED+' : '+c.GREEN+"CGT-Files\\3\\"+c.RED+repack._filename)
                    chdir(home+'\\Desktop\\')
                    startfile(realpath(home+'\\Desktop\\CGT-Files\\3\\'))
                    startfile(home+'\\Desktop\\CGT-Files\\3\\CGT.txt')
                else:
                    sleep(1)
                    print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'17' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                    error(17)
            else:
                sleep(1)
                print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'19' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                error(19)
        else:
            sleep(1)
            print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'18' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
            error(18)
    elif language == 'EN':
        if isdir(home + '\\Desktop\\CGT-Files\\2\\'):
            if isfile(home + '\\Desktop\\CGT-Files\\2\\repack_dependencies.zip'):
                if isdir(home + '\\Desktop\\CGT-Files\\2\\unpack\\'):
                    if isdir(home + "\\Desktop\\CGT-Files\\3\\"):
                        try:
                            sleep(1)
                            print(c.END+c.RED+'directory'+c.YELLOW+' 3 '+c.BLUE + 'already exists'+c.GREEN+' ; '+c.RED +'overwrite ' + c.BLUE + '.' + c.GREEN + '.' + c.RED + '.')
                            rmtree(home + "\\Desktop\\CGT-Files\\3\\")
                        except:
                            sleep(1)
                            print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'16' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                            error(16)
                            return
                    else:
                        print(c.RED+'making'+c.BLUE+' directory '+c.YELLOW+'3'+c.RED+' .'+c.GREEN+'.'+c.BLUE+'.')
                    sleep(1)
                    print(c.END + c.BLUE + 'packed'+c.RED+c.YELLOW+' unpack'+c.RED+' directory ' + c.BLUE+'to' +c.RED+' ramdisk' + c.BLUE + ' .' + c.GREEN + '.' + c.RED + '.')
                    chdir(home+'\\Desktop\\CGT-Files\\2\\')
                    system(home+'\\.CGT\\programs\\mkbootfs.exe unpack | '+home+'\\.CGT\\programs\\minigzip.exe -c -9 > '+home + '\\Desktop\\CGT-Files\\2\\CGT_5c5f44ab0550487fbce8a2874ebaab6a_CGT.gz 2>NUL')
                    sleep(1)
                    print(c.END + c.BLUE + 'add '+c.RED+'ramdisk'+c.BLUE+' to '+c.RED+'repack_dependencies.zip ' + c.BLUE + '.' + c.GREEN + '.' + c.RED + '.')
                    with ZipFile('repack_dependencies.zip', 'a') as zipf:
                        zipf.write(home + '\\Desktop\\CGT-Files\\2\\CGT_5c5f44ab0550487fbce8a2874ebaab6a_CGT.gz' , 'CGT_5c5f44ab0550487fbce8a2874ebaab6a_CGT.gz')
                    sleep(1)
                    print(c.END + c.BLUE + 'decompress '+c.RED+'repack_dependencies.zip ' + c.BLUE + '.' + c.GREEN + '.' + c.RED + '.')
                    system('mkdir '+home + '\\Desktop\\CGT-Files\\2\\repack\\')
                    with ZipFile(home + '\\Desktop\\CGT-Files\\2\\repack_dependencies.zip', 'r') as zip_ref:
                        zip_ref.extractall(home + '\\Desktop\\CGT-Files\\2\\repack\\')
                    new_kernel = home+'\\Desktop\\CGT-Files\\2\\repack\\CGT_50484c19f1afdaf3841a0d821ed393d2_CGT'
                    new_cmdline = home+'\\Desktop\\CGT-Files\\2\\repack\\CGT_95f44086bc13f782435dd6356310e7bd_CGT'
                    new_base = home+'\\Desktop\\CGT-Files\\2\\repack\\CGT_593616de15330c0fb2d55e55410bf994_CGT'
                    new_pagesize = home+'\\Desktop\\CGT-Files\\2\\repack\\CGT_7525d528a3457f0227997c25239c4507_CGT'
                    new_dt = home+'\\Desktop\\CGT-Files\\2\\repack\\CGT_3017d911efceb27d1de6a92b70979795_CGT'
                    new_kerneloffset = home+'\\Desktop\\CGT-Files\\2\\repack\\CGT_706cf6b230a6d77ee280a40b54246762_CGT'
                    new_ramdiskoffset = home+'\\Desktop\\CGT-Files\\2\\repack\\CGT_0e16d6f83afe32911816ef683ad5d639_CGT'
                    new_secondoffset = home+'\\Desktop\\CGT-Files\\2\\repack\\CGT_d753658059439ac8a93d411e68e5d66a_CGT'
                    new_tagsoffset = home+'\\Desktop\\CGT-Files\\2\\repack\\CGT_a4d756b70ed4593b8d0f2abd01694f39_CGT'
                    new_hash = home+'\\Desktop\\CGT-Files\\2\\repack\\CGT_0800fc577294c34e0b28ad2839435945_CGT'
                    class repack:
                            _filename = open(home+'\\Desktop\\CGT-Files\\2\\repack\\CGT_435ed7e9f07f740abf511a62c00eef6e_CGT').read()
                            _mkboot = home+'\\.CGT\\programs\\mkbootimg.exe'
                            _kernel = home+'\\Desktop\\CGT-Files\\2\\repack\\CGT_50484c19f1afdaf3841a0d821ed393d2_CGT'
                            _ramdisk = home+'\\Desktop\\CGT-Files\\2\\repack\\CGT_5c5f44ab0550487fbce8a2874ebaab6a_CGT.gz'
                            _cmdline = open(home+'\\Desktop\\CGT-Files\\2\\repack\\CGT_95f44086bc13f782435dd6356310e7bd_CGT').read().replace('\n', '')
                            _cmdline = '\"'+_cmdline+'\"'
                            _base = open(home+'\\Desktop\\CGT-Files\\2\\repack\\CGT_593616de15330c0fb2d55e55410bf994_CGT').read().replace('\n', '')
                            _pagesize = open(home+'\\Desktop\\CGT-Files\\2\\repack\\CGT_7525d528a3457f0227997c25239c4507_CGT').read().replace('\n', '')
                            _dt = home+'\\Desktop\\CGT-Files\\2\\repack\\CGT_3017d911efceb27d1de6a92b70979795_CGT'
                            _kerneloffset = open(home+'\\Desktop\\CGT-Files\\2\\repack\\CGT_706cf6b230a6d77ee280a40b54246762_CGT').read().replace('\n', '')
                            _ramdiskoffset = open(home+'\\Desktop\\CGT-Files\\2\\repack\\CGT_0e16d6f83afe32911816ef683ad5d639_CGT').read().replace('\n', '')
                            _secondoffset = open(home+'\\Desktop\\CGT-Files\\2\\repack\\CGT_d753658059439ac8a93d411e68e5d66a_CGT').read().replace('\n', '')
                            _tagsoffset = open(home+'\\Desktop\\CGT-Files\\2\\repack\\CGT_a4d756b70ed4593b8d0f2abd01694f39_CGT').read().replace('\n', '')
                            _hash = open(home+'\\Desktop\\CGT-Files\\2\\repack\\CGT_0800fc577294c34e0b28ad2839435945_CGT').read().replace('\n', '')
                            _hash = '\"'+_hash+'\"'
                    sleep(1)
                    print(c.END + c.BLUE + 'packed '+c.RED+'ramdisk'+c.BLUE+' & '+c.RED+'dependencies directory' + c.BLUE+' to '+c.RED + repack._filename + c.BLUE + ' .' + c.GREEN + '.' + c.RED + '.')
                    system('mkdir '+home + '\\Desktop\\CGT-Files\\3\\')
                    chdir(home + '\\Desktop\\CGT-Files\\3\\')
                    if isfile(new_dt):
                        system(repack._mkboot+' --kernel '+repack._kernel+' --ramdisk '+repack._ramdisk+' --cmdline '+repack._cmdline+' --base '+repack._base+' --pagesize '+repack._pagesize+' --dt '+repack._dt+' --kernel_offset '+repack._kerneloffset+' --ramdisk_offset '+repack._ramdiskoffset+' --second_offset '+repack._secondoffset+' --tags_offset '+repack._tagsoffset+' --hash '+repack._hash+' -o '+repack._filename+' 2>NUL')
                    elif not isfile(new_dt):
                        system(repack._mkboot+' --kernel '+repack._kernel+' --ramdisk '+repack._ramdisk+' --cmdline '+repack._cmdline+' --base '+repack._base+' --pagesize '+repack._pagesize+' --kernel_offset '+repack._kerneloffset+' --ramdisk_offset '+repack._ramdiskoffset+' --second_offset '+repack._secondoffset+' --tags_offset '+repack._tagsoffset+' --hash '+repack._hash+' -o '+repack._filename+' 2>NUL')
                    sleep(1)
                    print(c.END+c.BLUE+'remove ' + c.RED+'logs' + c.BLUE + ' .' + c.GREEN + '.' + c.RED + '.')
                    remove(home+'\\Desktop\\CGT-Files\\2\\CGT_5c5f44ab0550487fbce8a2874ebaab6a_CGT.gz')
                    remove(home+'\\Desktop\\CGT-Files\\2\\repack_dependencies.zip')
                    remove(home + '\\Desktop\\CGT-Files\\2\\repack\\CGT_5c5f44ab0550487fbce8a2874ebaab6a_CGT.gz')
                    make_archive(home+'\\Desktop\\CGT-Files\\2\\repack_dependencies\\', 'zip', home+'\\Desktop\\CGT-Files\\2\\repack\\')
                    rmtree(home + "\\Desktop\\CGT-Files\\2\\repack\\")
                    readme_repack_write = '--- repack to '+repack._filename+' by CGT ---'
                    readme_repack = open(
                        home + '\\Desktop\\CGT-Files\\3\\CGT.txt', 'w')
                    readme_repack.write(readme_repack_write)
                    readme_repack.close()
                    sleep(1)
                    print(c.END + c.YELLOW+'unpack ' + c.RED + 'directory ' + c.BLUE + 'repacked to ' + c.RED+repack._filename+c.BLUE+' file'+c.RED+' : '+c.GREEN+"CGT-Files\\3\\"+c.RED+repack._filename)
                    chdir(home+'\\Desktop\\')
                    startfile(realpath(home+'\\Desktop\\CGT-Files\\3\\'))
                    startfile(home+'\\Desktop\\CGT-Files\\3\\CGT.txt')
                else:
                    sleep(1)
                    print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'17' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                    error(17)
            else:
                sleep(1)
                print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'19' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.') 
                error(19)
        else:
            sleep(1)
            print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'18' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
            error(18)

def linux():
    if isdir(home + '/Desktop/CGT-Files/2/'):
        if isfile(home + '/Desktop/CGT-Files/2/repack_dependencies.zip'):
            if isdir(home + '/Desktop/CGT-Files/2/unpack/'):
                sleep(1)
                print(c.END + c.BLUE + 'packed'+c.RED+c.YELLOW+' unpack'+c.RED+' directory ' + c.BLUE+'to' +c.RED+' ramdisk' + c.BLUE + ' .' + c.GREEN + '.' + c.RED + '.')
                chdir(home+'/Desktop/CGT-Files/2/unpack/')
                system('find . | '+home+'/.CGT/dependencies/./cpio --quiet -o -H newc | '+home+'/.CGT/dependencies/./gzip > ../CGT_5c5f44ab0550487fbce8a2874ebaab6a_CGT.cpio.gz')
                chdir(home+'/Desktop/CGT-Files/2/')
                sleep(1)
                print(c.END + c.BLUE + 'add '+c.RED+'ramdisk'+c.BLUE+' to '+c.RED+'repack_dependencies.zip ' + c.BLUE + '.' + c.GREEN + '.' + c.RED + '.')
                with ZipFile('repack_dependencies.zip', 'a') as zipf:
                    zipf.write(home + '/Desktop/CGT-Files/2/CGT_5c5f44ab0550487fbce8a2874ebaab6a_CGT.cpio.gz' , 'CGT_5c5f44ab0550487fbce8a2874ebaab6a_CGT.cpio.gz')
                sleep(1)
                print(c.END + c.BLUE + 'decompress '+c.RED+'repack_dependencies.zip ' + c.BLUE + '.' + c.GREEN + '.' + c.RED + '.')
                mkdir(home + '/Desktop/CGT-Files/2/repack/')
                with ZipFile(home + '/Desktop/CGT-Files/2/repack_dependencies.zip', 'r') as zip_ref:
                    zip_ref.extractall(home + '/Desktop/CGT-Files/2/repack/')
                sleep(1)
                print(c.END + c.BLUE + 'packed '+c.RED+'ramdisk'+c.BLUE+' & '+c.RED+'dependencies' + c.BLUE+' to '+c.RED + 'new.img ' + c.BLUE + '.' + c.GREEN + '.' + c.RED + '.')
                if isfile(home + "/Desktop/CGT-Files/3/new.img"):
                    sleep(1)
                    print(c.END+c.RED + 'new.img'+c.BLUE + ' already exists'+c.GREEN+' ; '+c.RED + 'overwrite ' + c.BLUE + '.' + c.GREEN + '.' + c.RED + '.')
                    system('rm -r '+home + "/Desktop/CGT-Files/3/")
                new_kernel = home+'/Desktop/CGT-Files/2/repack/CGT_50484c19f1afdaf3841a0d821ed393d2_CGT'
                new_cmdline = home+'/Desktop/CGT-Files/2/repack/CGT_95f44086bc13f782435dd6356310e7bd_CGT'
                new_base = home+'/Desktop/CGT-Files/2/repack/CGT_593616de15330c0fb2d55e55410bf994_CGT'
                new_pagesize = home+'/Desktop/CGT-Files/2/repack/CGT_7525d528a3457f0227997c25239c4507_CGT'
                new_dt = home+'/Desktop/CGT-Files/2/repack/CGT_3017d911efceb27d1de6a92b70979795_CGT'
                new_kerneloffset = home+'/Desktop/CGT-Files/2/repack/CGT_706cf6b230a6d77ee280a40b54246762_CGT'
                new_ramdiskoffset = home+'/Desktop/CGT-Files/2/repack/CGT_0e16d6f83afe32911816ef683ad5d639_CGT'
                new_secondoffset = home+'/Desktop/CGT-Files/2/repack/CGT_d753658059439ac8a93d411e68e5d66a_CGT'
                new_tagsoffset = home+'/Desktop/CGT-Files/2/repack/CGT_a4d756b70ed4593b8d0f2abd01694f39_CGT'
                new_hash = home+'/Desktop/CGT-Files/2/repack/CGT_0800fc577294c34e0b28ad2839435945_CGT'
                class repack:
                        _mkboot = home+'/.CGT/dependencies/./mkbootimg'
                        _kernel = home+'/Desktop/CGT-Files/2/repack/CGT_50484c19f1afdaf3841a0d821ed393d2_CGT'
                        _ramdisk = home+'/Desktop/CGT-Files/2/repack/CGT_5c5f44ab0550487fbce8a2874ebaab6a_CGT.cpio.gz'
                        _cmdline = open(home+'/Desktop/CGT-Files/2/repack/CGT_95f44086bc13f782435dd6356310e7bd_CGT').read().replace('\n', '')
                        _cmdline = '\"'+_cmdline+'\"'
                        _base = open(home+'/Desktop/CGT-Files/2/repack/CGT_593616de15330c0fb2d55e55410bf994_CGT').read().replace('\n', '')
                        _pagesize = open(home+'/Desktop/CGT-Files/2/repack/CGT_7525d528a3457f0227997c25239c4507_CGT').read().replace('\n', '')
                        _dt = home+'/Desktop/CGT-Files/2/repack/CGT_3017d911efceb27d1de6a92b70979795_CGT'
                        _kerneloffset = open(home+'/Desktop/CGT-Files/2/repack/CGT_706cf6b230a6d77ee280a40b54246762_CGT').read().replace('\n', '')
                        _ramdiskoffset = open(home+'/Desktop/CGT-Files/2/repack/CGT_0e16d6f83afe32911816ef683ad5d639_CGT').read().replace('\n', '')
                        _secondoffset = open(home+'/Desktop/CGT-Files/2/repack/CGT_d753658059439ac8a93d411e68e5d66a_CGT').read().replace('\n', '')
                        _tagsoffset = open(home+'/Desktop/CGT-Files/2/repack/CGT_a4d756b70ed4593b8d0f2abd01694f39_CGT').read().replace('\n', '')
                        _hash = open(home+'/Desktop/CGT-Files/2/repack/CGT_0800fc577294c34e0b28ad2839435945_CGT').read().replace('\n', '')
                        _hash = '\"'+_hash+'\"'
                if isdir(home + "/Desktop/CGT-Files/3/"):
                        sleep(1)
                        print(c.END+c.YELLOW+'3 '+c.RED+'directory'+c.BLUE + ' already exists'+c.GREEN+' ; '+c.RED +
                            'overwrite ' + c.BLUE + '.' + c.GREEN + '.' + c.RED + '.')
                        system('rm -rf '+home + "/Desktop/CGT-Files/3/")
                mkdir(home + '/Desktop/CGT-Files/3/')
                chdir(home + '/Desktop/CGT-Files/3/')
                system(repack._mkboot+' --kernel '+repack._kernel+' --ramdisk '+repack._ramdisk+' --cmdline '+repack._cmdline+' --base '+repack._base+' --pagesize '+repack._pagesize+' --dt '+repack._dt+' --kernel_offset '+repack._kerneloffset+' --ramdisk_offset '+repack._ramdiskoffset+' --second_offset '+repack._secondoffset+' --tags_offset '+repack._tagsoffset+' --hash '+repack._hash+' -o new.img')
                sleep(1)
                print(c.END+c.BLUE+'remove ' + c.RED+'logs' + c.BLUE + ' .' + c.GREEN + '.' + c.RED + '.')
                remove(home+'/Desktop/CGT-Files/2/repack_dependencies.zip')
                remove(home + '/Desktop/CGT-Files/2/CGT_5c5f44ab0550487fbce8a2874ebaab6a_CGT.cpio.gz')
                make_archive(home+'/Desktop/CGT-Files/2/repack_dependencies/', 'zip', home+'/Desktop/CGT-Files/2/repack/')
                rmtree(home + "/Desktop/CGT-Files/2/repack/")
                readme_repack_write = '--- repack [boot/recovery] by CGT ---'
                readme_repack = open(
                    home + '/Desktop/CGT-Files/3/CGT.txt', 'w')
                readme_repack.write(readme_repack_write)
                readme_repack.close()
                sleep(1)
                print(c.END + c.YELLOW+'unpack ' + c.RED + 'directory ' + c.BLUE + 'repacked to ' + c.RED+'new.img'+c.BLUE+' file'+c.RED+' : '+c.GREEN+"3/"+c.RED+"new.img")
                chdir(home+'/Desktop/')
            else:
                sleep(1)
                print(c.END + c.RED + 'error'+c.GREEN + ' : ' + c.BLUE + 'can\'t find' + c.RED +
                      ' unpack ' + c.BLUE + 'directory' + c.RED + ' .' + c.GREEN + '.' + c.BLUE + '.')
                sleep(1)
                print(c.END + c.RED+'error' + c.GREEN + ' : ' + c.BLUE + 'failed to make ' +c.RED + 'new.img' + c.BLUE + ' .' + c.GREEN + '.' + c.RED + '.')
        else:
            sleep(1)
            print(c.END + c.RED + 'error'+c.GREEN + ' : ' + c.BLUE + 'can\'t find' + c.RED +
                  ' repack_dependencies.zip' + c.RED + ' .' + c.GREEN + '.' + c.BLUE + '.')
            sleep(1)
            print(c.END + c.RED + 'error'+c.GREEN + ' : ' + c.BLUE + 'failed to make ' +
                  c.RED + 'new.img' + c.BLUE + ' .' + c.GREEN + '.' + c.RED + '.')
    else:
        sleep(1)
        print(c.END + c.RED + 'error' + c.GREEN + ' : ' + c.BLUE + 'can\'t find' +
              c.RED + ' 2 ' + c.BLUE + 'directory' + c.RED + ' .' + c.GREEN + '.' + c.BLUE + '.')
        sleep(1)
        print(c.END + c.RED+'error' + c.GREEN + ' : ' + c.BLUE + 'failed to make ' +
              c.RED + 'new.img' + c.BLUE + ' .' + c.GREEN + '.' + c.RED + '.')
        
def if_3():
  if os_type().upper() == 'WINDOWS':
    windows()
  elif os_type().upper() == 'LINUX':
    linux()
  else:
    pass