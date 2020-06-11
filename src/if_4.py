# Copyright SYS113 2019. gpl v3.0 license , see readme file.

try:
    from os import startfile    
except:
    pass
from tarfile import open as TarFileOpen
from error import error
from fileinput import FileInput
from re import search
from time import sleep
from pathlib import Path
from shutil import rmtree , move
from os.path import isdir , isfile , splitext , exists , basename , realpath
from os import system , chdir , stat , remove , rename , listdir 
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

def window():
    def compress_repack_directory():
        sleep(1)
        if language == 'FA':
            print(c.BLUE+'feshorde kardan'+c.RED+' dependencies'+c.BLUE+' va tabdil an be '+c.RED+'repack_dependencies.zip '+c.BLUE+'.'+c.GREEN+'.'+c.RED+'.')
        else:
            print(c.BLUE+'packed'+c.RED+' dependencies'+c.BLUE+' to '+c.RED+'repack_dependencies.zip '+c.BLUE+'.'+c.GREEN+'.'+c.RED+'.')
        chdir(home + "\\Desktop\\CGT-Files\\4\\repack_dependencies\\")
        def kernel_file():
            FILE_DIRECTORY_PATH = home + '\\Desktop\\CGT-Files\\4\\repack_dependencies\\'
            FILE_PATTERN = ".+-zImage"
            for file_name in listdir(home + '\\Desktop\\CGT-Files\\4\\repack_dependencies\\'):
                if search(FILE_PATTERN, file_name):
                    return file_name
        def cmdline_file():
            FILE_DIRECTORY_PATH = home + '\\Desktop\\CGT-Files\\4\\repack_dependencies\\'
            FILE_PATTERN = ".+-cmdline"
            for file_name in listdir(home + '\\Desktop\\CGT-Files\\4\\repack_dependencies\\'):
                if search(FILE_PATTERN, file_name):
                    return file_name
        def base_file():
            FILE_DIRECTORY_PATH = home + '\\Desktop\\CGT-Files\\4\\repack_dependencies\\'
            FILE_PATTERN = ".+-base"
            for file_name in listdir(home + '\\Desktop\\CGT-Files\\4\\repack_dependencies\\'):
                if search(FILE_PATTERN, file_name):
                    return file_name
        def pagesize_file():
            FILE_DIRECTORY_PATH = home + '\\Desktop\\CGT-Files\\4\\repack_dependencies\\'
            FILE_PATTERN = ".+-pagesize"
            for file_name in listdir(home + '\\Desktop\\CGT-Files\\4\\repack_dependencies\\'):
                if search(FILE_PATTERN, file_name):
                    return file_name
        def dt_file():
            FILE_DIRECTORY_PATH = home + '\\Desktop\\CGT-Files\\4\\repack_dependencies\\'
            FILE_PATTERN = ".+-dtb"
            for file_name in listdir(home + '\\Desktop\\CGT-Files\\4\\repack_dependencies\\'):
                if search(FILE_PATTERN, file_name):
                    return file_name
        def kerneloffset_file():
            FILE_DIRECTORY_PATH = home + '\\Desktop\\CGT-Files\\4\\repack_dependencies\\'
            FILE_PATTERN = ".+-kerneloff"
            for file_name in listdir(home + '\\Desktop\\CGT-Files\\4\\repack_dependencies\\'):
                if search(FILE_PATTERN, file_name):
                    return file_name
        def ramdiskoffset_file():
            FILE_DIRECTORY_PATH = home + '\\Desktop\\CGT-Files\\4\\repack_dependencies\\'
            FILE_PATTERN = ".+-ramdiskoff"
            for file_name in listdir(home + '\\Desktop\\CGT-Files\\4\\repack_dependencies\\'):
                if search(FILE_PATTERN, file_name):
                    return file_name
        def secondoffset_file():
            FILE_DIRECTORY_PATH = home + '\\Desktop\\CGT-Files\\4\\repack_dependencies\\'
            FILE_PATTERN = ".+-secondoff"
            for file_name in listdir(home + '\\Desktop\\CGT-Files\\4\\repack_dependencies\\'):
                if search(FILE_PATTERN, file_name):
                    return file_name
        def tagsoffset_file():
            FILE_DIRECTORY_PATH = home + '\\Desktop\\CGT-Files\\4\\repack_dependencies\\'
            FILE_PATTERN = ".+-tagsoff"
            for file_name in listdir(home + '\\Desktop\\CGT-Files\\4\\repack_dependencies\\'):
                if search(FILE_PATTERN, file_name):
                    return file_name
        def hash_file():
            FILE_DIRECTORY_PATH = home + '\\Desktop\\CGT-Files\\4\\repack_dependencies\\'
            FILE_PATTERN = ".+-hash"
            for file_name in listdir(home + '\\Desktop\\CGT-Files\\4\\repack_dependencies\\'):
                if search(FILE_PATTERN, file_name):
                    return file_name
        old_kernel = home+'\\Desktop\\CGT-Files\\4\\repack_dependencies\\'+kernel_file()
        old_cmdline = home+'\\Desktop\\CGT-Files\\4\\repack_dependencies\\'+cmdline_file()
        old_base = home+'\\Desktop\\CGT-Files\\4\\repack_dependencies\\'+base_file()
        old_pagesize = home+'\\Desktop\\CGT-Files\\4\\repack_dependencies\\'+pagesize_file()
        if dt_file() != None:
            old_dt = home+'\\Desktop\\CGT-Files\\4\\repack_dependencies\\'+dt_file()
        old_kerneloffset = home+'\\Desktop\\CGT-Files\\4\\repack_dependencies\\'+kerneloffset_file()
        old_ramdiskoffset = home+'\\Desktop\\CGT-Files\\4\\repack_dependencies\\'+ramdiskoffset_file()
        old_secondoffset = home+'\\Desktop\\CGT-Files\\4\\repack_dependencies\\'+secondoffset_file()
        old_tagsoffset = home+'\\Desktop\\CGT-Files\\4\\repack_dependencies\\'+tagsoffset_file()
        old_hash = home+'\\Desktop\\CGT-Files\\4\\repack_dependencies\\'+hash_file()
        old_ramdisk = home+'\\Desktop\\CGT-Files\\4\\ramdisk.gz'
        new_kernel = home+'\\Desktop\\CGT-Files\\4\\repack_dependencies\\CGT_50484c19f1afdaf3841a0d821ed393d2_CGT'
        new_cmdline = home+'\\Desktop\\CGT-Files\\4\\repack_dependencies\\CGT_95f44086bc13f782435dd6356310e7bd_CGT'
        new_base = home+'\\Desktop\\CGT-Files\\4\\repack_dependencies\\CGT_593616de15330c0fb2d55e55410bf994_CGT'
        new_pagesize = home+'\\Desktop\\CGT-Files\\4\\repack_dependencies\\CGT_7525d528a3457f0227997c25239c4507_CGT'
        if dt_file() != None:
            new_dt = home+'\\Desktop\\CGT-Files\\4\\repack_dependencies\\CGT_3017d911efceb27d1de6a92b70979795_CGT'
        new_kerneloffset = home+'\\Desktop\\CGT-Files\\4\\repack_dependencies\\CGT_706cf6b230a6d77ee280a40b54246762_CGT'
        new_ramdiskoffset = home+'\\Desktop\\CGT-Files\\4\\repack_dependencies\\CGT_0e16d6f83afe32911816ef683ad5d639_CGT'
        new_secondoffset = home+'\\Desktop\\CGT-Files\\4\\repack_dependencies\\CGT_d753658059439ac8a93d411e68e5d66a_CGT'
        new_tagsoffset = home+'\\Desktop\\CGT-Files\\4\\repack_dependencies\\CGT_a4d756b70ed4593b8d0f2abd01694f39_CGT'
        new_hash = home+'\\Desktop\\CGT-Files\\4\\repack_dependencies\\CGT_0800fc577294c34e0b28ad2839435945_CGT'
        new_ramdisk = home+'\\Desktop\\CGT-Files\\4\\CGT_5c5f44ab0550487fbce8a2874ebaab6a_CGT.gz'
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
        rename(old_ramdisk , new_ramdisk)
        system('mkdir '+home + "\\Desktop\\CGT-Files\\4\\repack\\")
        rpk = home + "\\Desktop\\CGT-Files\\4\\repack\\"
        move(new_kernel,rpk)
        move(new_cmdline,rpk)
        move(new_base,rpk)
        move(new_pagesize,rpk)
        if isfile(home+'\\Desktop\\CGT-Files\\4\\repack_dependencies\\CGT_3017d911efceb27d1de6a92b70979795_CGT'):
            move(new_dt,rpk)
        move(new_kerneloffset,rpk)
        move(new_ramdiskoffset,rpk)
        move(new_secondoffset,rpk)
        move(new_tagsoffset,rpk)
        move(new_hash,rpk)
        move(new_ramdisk,rpk)
    if language == 'FA':
        sleep(0.5)
        print('\n'+c.RED+'nokte '+c.YELLOW+'1'+c.GREEN+' : '+c.BLUE+'dar in ravesh'+c.RED+' etela\'at '+c.BLUE+'hazf'+c.RED+' nmishavad '+c.BLUE+'az'+c.RED+' goshi '+c.BLUE+'.'+c.GREEN+'.'+c.RED+'.')
        sleep(0.5)
        print(c.RED+'nokte '+c.YELLOW+'2'+c.GREEN+' : '+c.BLUE+'in'+c.RED+' ravesh '+c.BLUE+'faght baraye '+c.RED+'goshi'+c.BLUE+' haye'+c.RED+' samsung '+c.BLUE+'ast '+c.RED + '.' + c.GREEN + '.' + c.BLUE + '.')
        sleep(0.5)
        print(c.RED+'nokte '+c.YELLOW+'3'+c.GREEN+' : '+c.RED+'boot asli\'i'+c.BLUE+' ke be '+c.YELLOW+'CGT'+c.BLUE+' midahid bayad haman '+c.RED+'boot feali'+c.BLUE+' goshi '+c.RED+'samsung'+c.BLUE+' bashad'+c.RED + ' .' + c.GREEN + '.' + c.BLUE + '.')
        sleep(0.5)
        print(c.RED+'nokte '+c.YELLOW+'4'+c.GREEN+' : '+c.BLUE+'in'+c.RED+' ravesh '+c.BLUE+'dar sorate '+c.RED+'faal'+c.BLUE+' bodan '+c.YELLOW+'frp'+c.GREEN+','+c.YELLOW+'oem'+c.GREEN+','+c.YELLOW+'crom'+c.GREEN+','+c.YELLOW+'reactivition '+c.BLUE+'ammal'+c.RED+' nakhahad '+c.BLUE+'kard '+c.BLUE + '.' + c.GREEN + '.' + c.RED + '.')
        sleep(0.5)
        print(c.RED+'nokte '+c.YELLOW+'5'+c.GREEN+' : '+c.BLUE+'in'+c.RED+' ravesh '+c.BLUE+'bar roye '+c.RED+'noskhe android '+c.BLUE+'bishtar az '+c.YELLOW+'8'+c.BLUE+' ammal'+c.RED+' nakhahad '+c.BLUE+'kard '+c.BLUE + '.' + c.GREEN + '.' + c.RED + '.'+'\n')
        sleep(1)
        print(c.END+c.GREEN+'drag'+c.RED+' & '+c.GREEN +'drop'+c.BLUE+' konid '+c.YELLOW+'boot asli'+c.RED+' ['+c.GREEN+'.img' + c.RED + '/' + c.GREEN + '.img.lz4'+c.RED+'/'+c.GREEN+'.tar'+c.RED+'/'+c.GREEN+'tar.md5'+c.RED+']'+c.BLUE+' ra va '+c.RED+'klid enter' + c.BLUE+' ra '+c.RED+'befesharid' + c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
        file = xinput(c.MAGENTA+'> '+c.YELLOW)
        file = file.replace("\"", "")
        file = file.replace("\'", "")
        file_name, file_extension = splitext(file)
        chdir(home)
        if ' ' in file:
            print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'2' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
            error(2)
        else:
            if exists(file) == True:
                if file_extension == '.lz4':
                    if (basename(file) == 'boot.img.lz4'):
                        remove_boot_img = file.replace(".lz4", "")
                        if isdir(home + "\\Desktop\\CGT-Files\\4\\"):
                            try:
                                sleep(1)
                                print(c.END+c.RED+'poshe'+c.YELLOW+' 4 '+c.BLUE + 'vojod darad'+c.GREEN+' ; '+c.RED + 'hazf '+c.GREEN+'&'+c.RED+' sakht dobare ' + c.BLUE + '.' + c.GREEN + '.' + c.RED + '.')
                                rmtree(home + "\\Desktop\\CGT-Files\\4\\")
                            except:
                                sleep(1)
                                print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'25' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                error(25)
                                return
                        else:
                            print(c.RED+'sakht'+c.BLUE+' poshe '+c.YELLOW+'4'+c.RED+' .'+c.GREEN+'.'+c.BLUE+'.')
                        system('mkdir '+home + '\\Desktop\\CGT-Files\\4\\')
                        chdir(home + '\\Desktop\\CGT-Files\\4\\')
                        sleep(1)
                        print(c.END+c.BLUE + 'tabdil '+c.RED + basename(remove_boot_img+'.lz4') + c.BLUE + ' be ' +
                            c.RED + basename(remove_boot_img) + c.BLUE + ' .' + c.GREEN + '.' + c.RED + '.')
                        system(home + '\\.CGT\\programs\\lz4.exe -d ' + file)
                        file = file.replace(".lz4", "")
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
                            rmtree(home + "\\Desktop\\CGT-Files\\4\\")
                          except:
                            print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'25' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                            error(25)
                          return
                        sleep(1)
                        print(c.END+c.BLUE + 'estekhraj '+c.RED+basename(file) + c.BLUE + ' .' + c.GREEN + '.' + c.RED + '.')
                        system('mkdir '+home + '\\Desktop\\CGT-Files\\4\\repack_dependencies\\')
                        system(home+'\\.CGT\\programs\\unpackbootimg.exe' + ' -i ' + file + ' -o ' + home + '\\Desktop\\CGT-Files\\4\\repack_dependencies\\ > NUL')
                        sleep(1)
                        print(c.END+c.BLUE + 'estekhraj'+c.RED+' ramdisk ' +
                            c.BLUE + '.' + c.GREEN + '.' + c.RED + '.')
                        try:
                            ramdisk_size = stat(home+'\\Desktop\\CGT-Files\\4\\repack_dependencies\\'+basename(file)+'-ramdisk.gz')
                        except:
                            try:
                                ramdisk_size = stat(home+'\\Desktop\\CGT-Files\\2\\repack_dependencies\\'+basename(file)+'-ramdisk.gz')
                            except:
                                sleep(1)
                                print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'8' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                error(8)
                                print(c.BLUE+'hazf'+c.RED+' log ha '+c.BLUE+'va'+c.RED+' khoroj '+c.BLUE+'.'+c.GREEN+'.'+c.RED+'.')
                                chdir(home)
                                remove(file)
                                try:
                                  rmtree(home + "\\Desktop\\CGT-Files\\4\\")
                                except:
                                  print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'25' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                  error(25)
                                return
                        if ramdisk_size.st_size != 0:
                            system('mkdir unpack')
                            chdir('unpack')
                            system(home+'\\.CGT\\programs\\gzip.exe -dcq '+home+'\\Desktop\\CGT-Files\\4\\repack_dependencies\\' + basename(file)+'-ramdisk.gz | '+home+'\\.CGT\\programs\\cpio -i > NUL 2>&1')
                            sleep(1)
                            print(c.BLUE+'taghir '+c.RED+'source'+c.BLUE+' baray '+c.RED +'dor zadan ghofl safhe'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                            if not '# Do not place files or directories in /data/local/tmp' in open(home+'\\Desktop\\CGT-Files\\4\\unpack\\init.rc','r').read():
                                sleep(1)
                                print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'27' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                error(27)
                                sleep(1)
                                print(c.BLUE+'hazf'+c.RED+' log ha '+c.BLUE+'va'+c.RED+' khoroj '+c.BLUE+'.'+c.GREEN+'.'+c.RED+'.')
                                chdir(home)
                                remove(remove_boot_img)
                                try:
                                    rmtree(home + "\\Desktop\\CGT-Files\\4\\")
                                except:
                                    print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'25' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                    error(25)
                                return
                            with FileInput(home+'\\Desktop\\CGT-Files\\4\\unpack\\init.rc', inplace=True) as file:
                                for line in file:
                                    print(line.replace('# Do not place files or directories in /data/local/tmp', '''
    # Do not place files or directories in /data/local/tmp

    # ---------- BYPASS SCREEN LOCK BY CGT ----------

    rm -f /data/system/locksettings.db 
    rm -f /data/system/locksettings.db-wal
    rm -f /data/system/locksettings.db-shm
    rm -f /data/system/gesture.key
    rm -f /data/system/password.key
    rm -f /data/system/signature.key
    rm -f /data/system/sparepassword.key
    rm /data/system/locksettings.db 
    rm /data/system/locksettings.db-wal
    rm /data/system/locksettings.db-shm
    rm /data/system/gesture.key
    rm /data/system/password.key
    rm /data/system/signature.key
    rm /data/system/sparepassword.key
    restorecon -R /data/system

    # ---------- BYPASS SCREEN LOCK BY CGT ----------
                    '''), end='')
                            sleep(1)
                            print(c.END + c.BLUE + 'tabdil'+c.RED+' ramdisk ' + c.BLUE+'be' +c.RED+' ramdisk.gz' + c.BLUE + ' .' + c.GREEN + '.' + c.RED + '.')
                            chdir(home+'\\Desktop\\CGT-Files\\4\\')
                            system(home+'\\.CGT\\programs\\mkbootfs.exe unpack | '+home+'\\.CGT\\programs\\minigzip.exe -c -9 > '+home+'\\Desktop\\CGT-Files\\4\\ramdisk.gz')
                            compress_repack_directory()
                            sleep(1)
                            print(c.END + c.BLUE + 'tabdil '+c.RED+'ramdisk.gz'+c.GREEN+' & '+c.RED+'baghi vabastegi ha' +c.BLUE+' be '+c.RED + 'boot.img ' + c.BLUE + '.' + c.GREEN + '.' + c.RED + '.')
                            chdir(home + "\\Desktop\\CGT-Files\\4\\")
                            class repack:
                                _mkboot = home+'\\.CGT\\programs\\mkbootimg.exe'
                                _kernel = home+'\\Desktop\\CGT-Files\\4\\repack\\CGT_50484c19f1afdaf3841a0d821ed393d2_CGT'
                                _ramdisk = home+'\\Desktop\\CGT-Files\\4\\repack\\CGT_5c5f44ab0550487fbce8a2874ebaab6a_CGT.gz'
                                _cmdline = open(home+'\\Desktop\\CGT-Files\\4\\repack\\CGT_95f44086bc13f782435dd6356310e7bd_CGT').read().replace('\n', '')
                                _cmdline = '\"'+_cmdline+'\"'
                                _base = open(home+'\\Desktop\\CGT-Files\\4\\repack\\CGT_593616de15330c0fb2d55e55410bf994_CGT').read().replace('\n', '')
                                _pagesize = open(home+'\\Desktop\\CGT-Files\\4\\repack\\CGT_7525d528a3457f0227997c25239c4507_CGT').read().replace('\n', '')
                                _dt = home+'\\Desktop\\CGT-Files\\4\\repack\\CGT_3017d911efceb27d1de6a92b70979795_CGT'
                                _kerneloffset = open(home+'\\Desktop\\CGT-Files\\4\\repack\\CGT_706cf6b230a6d77ee280a40b54246762_CGT').read().replace('\n', '')
                                _ramdiskoffset = open(home+'\\Desktop\\CGT-Files\\4\\repack\\CGT_0e16d6f83afe32911816ef683ad5d639_CGT').read().replace('\n', '')
                                _secondoffset = open(home+'\\Desktop\\CGT-Files\\4\\repack\\CGT_d753658059439ac8a93d411e68e5d66a_CGT').read().replace('\n', '')
                                _tagsoffset = open(home+'\\Desktop\\CGT-Files\\4\\repack\\CGT_a4d756b70ed4593b8d0f2abd01694f39_CGT').read().replace('\n', '')
                                _hash = open(home+'\\Desktop\\CGT-Files\\4\\repack\\CGT_0800fc577294c34e0b28ad2839435945_CGT').read().replace('\n', '')
                                _hash = '\"'+_hash+'\"'
                            if isfile(home+'\\Desktop\\CGT-Files\\4\\repack\\CGT_3017d911efceb27d1de6a92b70979795_CGT'):
                                system(repack._mkboot+' --kernel '+repack._kernel+' --ramdisk '+repack._ramdisk+' --cmdline '+repack._cmdline+' --base '+repack._base+' --pagesize '+repack._pagesize+' --dt '+repack._dt+' --kernel_offset '+repack._kerneloffset+' --ramdisk_offset '+repack._ramdiskoffset+' --second_offset '+repack._secondoffset+' --tags_offset '+repack._tagsoffset+' --hash '+repack._hash+' -o boot.img')
                            elif not isfile(home+'\\Desktop\\CGT-Files\\4\\repack\\CGT_3017d911efceb27d1de6a92b70979795_CGT'):
                                system(repack._mkboot+' --kernel '+repack._kernel+' --ramdisk '+repack._ramdisk+' --cmdline '+repack._cmdline+' --base '+repack._base+' --pagesize '+repack._pagesize+' --kernel_offset '+repack._kerneloffset+' --ramdisk_offset '+repack._ramdiskoffset+' --second_offset '+repack._secondoffset+' --tags_offset '+repack._tagsoffset+' --hash '+repack._hash+' -o boot.img')
                            sleep(1)
                            print(c.BLUE+'tabdil'+c.RED+' boot.img '+c.BLUE+'be'+c.RED+' CGT_SAM_BypassLockScreen_M1_CGT.tar '+c.BLUE + '.' + c.GREEN + '.' + c.RED + '.')
                            sleep(1)
                            print(c.END+c.BLUE+'hazf ' + c.RED+'log ha' + c.BLUE + ' .' + c.GREEN + '.' + c.RED + '.')
                            chdir(home+'\\Desktop\\')
                            rmtree(home + "\\Desktop\\CGT-Files\\4\\unpack")
                            rmtree(home + "\\Desktop\\CGT-Files\\4\\repack")
                            rmtree(home + "\\Desktop\\CGT-Files\\4\\repack_dependencies")
                            remove(remove_boot_img)
                            readme_unpack_write = '--- sakhteh shod CGT_SAM_BypassLockScreen_M1_CGT.tar tavasote CGT ---'+'\n\n'+'- chand nokte ...'+'\n\t'+"1 : dar in ravesh etela'at hazf nmishavad az goshi ..."+'\n\t'+"2 : boot asli'i ke be CGT midahid bayad haman boot feali goshi samsung bashad ..."+'\n\t' + '3 : in ravesh faght baraye goshi haye samsung ast ...'+'\n\t'+'4 : in ravesh dar sorate faal bodan frp,oem,crom,reactivition ammal nakhahad kard ...' + '\n\t'+'5 : in ravesh bar roye noskhe android bishtar az 8 ammal nakhahad kard ...'+'\n\t'+'6 : write konid CGT_SAM_BypassLockScreen_M1_CGT.tar ra dar AP odin ...'+'\n\t'+'7 : baad az write CGT_SAM_BypassLockScreen_M1_CGT.tar va dor zadan ghofl , az tamami dadeh haye goshi backup begirid va boot original ra write konid ...'+'\n\t'+'8 : agar goshi samsung shoma baad az write file va rah\'andazi mojadad bar roye logo samsung mand , dobareh boot asli ra write konid , in ravesh bar roye goshi samsung shoma kar nmikonad ...'+'\n\n'+'- download odin : https://github.com/sys113/CGT-dependencies/raw/master/Odin3_v3.13.1.zip'+'\n\n'+'- download goshi haye samsung : https://github.com/sys113/CGT-dependencies/raw/master/Samsung_USB_Driver_v1.5.60.0.zip'
                            readme_unpack = open(home + '\\Desktop\\CGT-Files\\4\\CGT.txt', 'w')
                            readme_unpack.write(readme_unpack_write)
                            readme_unpack.close()
                            sleep(1)
                            print(c.BLUE+'sakhte shod'+c.YELLOW+' CGT_SAM_BypassLockScreen_M1_CGT.tar '+c.BLUE+'dar' + c.RED+' : '+c.GREEN+'CGT-Files'+c.YELLOW+'/'+c.RED+'4'+c.YELLOW+'/')
                            chdir(home)
                            startfile(realpath(home+'\\Desktop\\CGT-Files\\4\\'))
                            startfile(home+'\\Desktop\\CGT-Files\\4\\CGT.txt')
                        elif ramdisk_size.st_size == 0:
                            sleep(1)
                            print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'6' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                            error(6)
                            chdir(home)
                            print(c.BLUE+'hazf'+c.RED+' log ha '+c.BLUE+'va'+c.RED+' khoroj '+c.BLUE+'.'+c.GREEN+'.'+c.RED+'.')
                            remove(remove_boot_img)
                            try:
                                rmtree(home + "\\Desktop\\CGT-Files\\4\\")
                            except:
                                print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'25' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                error(25)
                            return
                    else:
                        print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'26' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                        error(26)
                elif file_extension == '.img':
                    if (basename(file) == 'boot.img'):
                        if isdir(home + "\\Desktop\\CGT-Files\\4\\"):
                            try:
                                sleep(1)
                                print(c.END+c.RED+'poshe'+c.YELLOW+' 4 '+c.BLUE + 'vojod darad'+c.GREEN+' ; '+c.RED + 'hazf '+c.GREEN+'&'+c.RED+' sakht dobare ' + c.BLUE + '.' + c.GREEN + '.' + c.RED + '.')
                                rmtree(home + "\\Desktop\\CGT-Files\\4\\")
                            except:
                                sleep(1)
                                print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'25' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                error(25)
                                return
                        else:
                            print(c.RED+'sakht'+c.BLUE+' poshe '+c.YELLOW+'4'+c.RED+' .'+c.GREEN+'.'+c.BLUE+'.')
                        sleep(1)
                        print(c.END+c.BLUE + 'estekhraj '+c.RED+basename(file) + c.RED + ' .' + c.GREEN + '.' + c.BLUE + '.')
                        system('mkdir '+home + '\\Desktop\\CGT-Files\\4\\')
                        chdir(home + '\\Desktop\\CGT-Files\\4\\')
                        system('mkdir '+home + '\\Desktop\\CGT-Files\\4\\repack_dependencies\\')
                        system(home+'\\.CGT\\programs\\unpackbootimg.exe' + ' -i ' + file + ' -o ' + home + '\\Desktop\\CGT-Files\\4\\repack_dependencies\\ > NUL')
                        sleep(1)
                        print(c.END+c.BLUE + 'estekhraj'+c.RED+' ramdisk ' + c.BLUE + '.' + c.GREEN + '.' + c.RED + '.')
                        try:
                            ramdisk_size = stat(home+'\\Desktop\\CGT-Files\\4\\repack_dependencies\\'+basename(file)+'-ramdisk.gz')
                        except:
                            print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'8' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                            error(8)
                            print(c.BLUE+'hazf'+c.RED+' log ha '+c.BLUE+'va'+c.RED+' khoroj '+c.BLUE+'.'+c.GREEN+'.'+c.RED+'.')
                            chdir(home)
                            try:
                                rmtree(home + "\\Desktop\\CGT-Files\\4\\")
                            except:
                                print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'25' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                error(25)
                            return
                        if ramdisk_size.st_size != 0:
                            system('mkdir unpack')
                            chdir('unpack')
                            system(home+'\\.CGT\\programs\\gzip.exe -dcq '+home+'\\Desktop\\CGT-Files\\4\\repack_dependencies\\' + basename(file)+'-ramdisk.gz | '+home+'\\.CGT\\programs\\cpio -i > NUL 2>&1')
                            sleep(1)
                            print(c.BLUE+'taghir '+c.RED+'source'+c.BLUE+' baray '+c.RED +'dor zadan ghofl safhe'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                            if not '# Do not place files or directories in /data/local/tmp' in open(home+'\\Desktop\\CGT-Files\\4\\unpack\\init.rc','r').read():
                                sleep(1)
                                print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'27' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                error(27)
                                sleep(1)
                                print(c.BLUE+'hazf'+c.RED+' log ha '+c.BLUE+'va'+c.RED+' khoroj '+c.BLUE+'.'+c.GREEN+'.'+c.RED+'.')
                                chdir(home)
                                try:
                                    rmtree(home + "\\Desktop\\CGT-Files\\4\\")
                                except:
                                    print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'25' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                    error(25)
                                return
                            with FileInput(home+'\\Desktop\\CGT-Files\\4\\unpack\\init.rc', inplace=True) as file:
                                for line in file:
                                    print(line.replace('# Do not place files or directories in /data/local/tmp', '''
    # Do not place files or directories in /data/local/tmp

    # ---------- BYPASS SCREEN LOCK BY CGT ----------

    rm -f /data/system/locksettings.db 
    rm -f /data/system/locksettings.db-wal
    rm -f /data/system/locksettings.db-shm
    rm -f /data/system/gesture.key
    rm -f /data/system/password.key
    rm -f /data/system/signature.key
    rm -f /data/system/sparepassword.key
    rm /data/system/locksettings.db 
    rm /data/system/locksettings.db-wal
    rm /data/system/locksettings.db-shm
    rm /data/system/gesture.key
    rm /data/system/password.key
    rm /data/system/signature.key
    rm /data/system/sparepassword.key
    restorecon -R /data/system

    # ---------- BYPASS SCREEN LOCK BY CGT ----------
                    '''), end='')
                            sleep(1)
                            print(c.END + c.BLUE + 'tabdil'+c.RED+' ramdisk ' + c.BLUE+'be' +
                                  c.RED+' ramdisk.gz' + c.BLUE + ' .' + c.GREEN + '.' + c.RED + '.')
                            chdir(home+'\\Desktop\\CGT-Files\\4\\')
                            system(home+'\\.CGT\\programs\\mkbootfs.exe unpack | '+home+'\\.CGT\\programs\\minigzip.exe -c -9 > '+home+'\\Desktop\\CGT-Files\\4\\ramdisk.gz')
                            compress_repack_directory()
                            sleep(1)
                            print(c.END + c.BLUE + 'tabdil '+c.RED+'ramdisk.gz'+c.GREEN+' & '+c.RED+'baghi vabastegi ha' +c.BLUE+' be '+c.RED + 'boot.img ' + c.BLUE + '.' + c.GREEN + '.' + c.RED + '.')
                            chdir(home + "\\Desktop\\CGT-Files\\4\\")
                            class repack:
                                _mkboot = home+'\\.CGT\\programs\\mkbootimg.exe'
                                _kernel = home+'\\Desktop\\CGT-Files\\4\\repack\\CGT_50484c19f1afdaf3841a0d821ed393d2_CGT'
                                _ramdisk = home+'\\Desktop\\CGT-Files\\4\\repack\\CGT_5c5f44ab0550487fbce8a2874ebaab6a_CGT.gz'
                                _cmdline = open(home+'\\Desktop\\CGT-Files\\4\\repack\\CGT_95f44086bc13f782435dd6356310e7bd_CGT').read().replace('\n', '')
                                _cmdline = '\"'+_cmdline+'\"'
                                _base = open(home+'\\Desktop\\CGT-Files\\4\\repack\\CGT_593616de15330c0fb2d55e55410bf994_CGT').read().replace('\n', '')
                                _pagesize = open(home+'\\Desktop\\CGT-Files\\4\\repack\\CGT_7525d528a3457f0227997c25239c4507_CGT').read().replace('\n', '')
                                _dt = home+'\\Desktop\\CGT-Files\\4\\repack\\CGT_3017d911efceb27d1de6a92b70979795_CGT'
                                _kerneloffset = open(home+'\\Desktop\\CGT-Files\\4\\repack\\CGT_706cf6b230a6d77ee280a40b54246762_CGT').read().replace('\n', '')
                                _ramdiskoffset = open(home+'\\Desktop\\CGT-Files\\4\\repack\\CGT_0e16d6f83afe32911816ef683ad5d639_CGT').read().replace('\n', '')
                                _secondoffset = open(home+'\\Desktop\\CGT-Files\\4\\repack\\CGT_d753658059439ac8a93d411e68e5d66a_CGT').read().replace('\n', '')
                                _tagsoffset = open(home+'\\Desktop\\CGT-Files\\4\\repack\\CGT_a4d756b70ed4593b8d0f2abd01694f39_CGT').read().replace('\n', '')
                                _hash = open(home+'\\Desktop\\CGT-Files\\4\\repack\\CGT_0800fc577294c34e0b28ad2839435945_CGT').read().replace('\n', '')
                                _hash = '\"'+_hash+'\"'
                            if isfile(home+'\\Desktop\\CGT-Files\\4\\repack\\CGT_3017d911efceb27d1de6a92b70979795_CGT'):
                                system(repack._mkboot+' --kernel '+repack._kernel+' --ramdisk '+repack._ramdisk+' --cmdline '+repack._cmdline+' --base '+repack._base+' --pagesize '+repack._pagesize+' --dt '+repack._dt+' --kernel_offset '+repack._kerneloffset+' --ramdisk_offset '+repack._ramdiskoffset+' --second_offset '+repack._secondoffset+' --tags_offset '+repack._tagsoffset+' --hash '+repack._hash+' -o boot.img')
                            elif not isfile(home+'\\Desktop\\CGT-Files\\4\\repack\\CGT_3017d911efceb27d1de6a92b70979795_CGT'):
                                system(repack._mkboot+' --kernel '+repack._kernel+' --ramdisk '+repack._ramdisk+' --cmdline '+repack._cmdline+' --base '+repack._base+' --pagesize '+repack._pagesize+' --kernel_offset '+repack._kerneloffset+' --ramdisk_offset '+repack._ramdiskoffset+' --second_offset '+repack._secondoffset+' --tags_offset '+repack._tagsoffset+' --hash '+repack._hash+' -o boot.img')
                            sleep(1)
                            print(c.BLUE+'tabdil'+c.RED+' boot.img '+c.BLUE+'be'+c.RED+' CGT_SAM_BypassLockScreen_M1_CGT.tar '+c.BLUE + '.' + c.GREEN + '.' + c.RED + '.')
                            sleep(1)
                            print(c.END+c.BLUE+'hazf ' + c.RED+'log ha' + c.BLUE + ' .' + c.GREEN + '.' + c.RED + '.')
                            chdir(home+'\\Desktop\\')
                            rmtree(home + "\\Desktop\\CGT-Files\\4\\unpack")
                            rmtree(home + "\\Desktop\\CGT-Files\\4\\repack")
                            rmtree(home + "\\Desktop\\CGT-Files\\4\\repack_dependencies")
                            readme_unpack_write = '--- sakhteh shod CGT_SAM_BypassLockScreen_M1_CGT.tar tavasote CGT ---'+'\n\n'+'- chand nokte ...'+'\n\t'+"1 : dar in ravesh etela'at hazf nmishavad az goshi ..."+'\n\t'+"2 : boot asli'i ke be CGT midahid bayad haman boot feali goshi samsung bashad ..."+'\n\t' + '3 : in ravesh faght baraye goshi haye samsung ast ...'+'\n\t'+'4 : in ravesh dar sorate faal bodan frp,oem,crom,reactivition ammal nakhahad kard ...' + '\n\t'+'5 : in ravesh bar roye noskhe android bishtar az 8 ammal nakhahad kard ...'+'\n\t'+'6 : write konid CGT_SAM_BypassLockScreen_M1_CGT.tar ra dar AP odin ...'+'\n\t'+'7 : baad az write CGT_SAM_BypassLockScreen_M1_CGT.tar va dor zadan ghofl , az tamami dadeh haye goshi backup begirid va boot original ra write konid ...'+'\n\t'+'8 : agar goshi samsung shoma baad az write file va rah\'andazi mojadad bar roye logo samsung mand , dobareh boot asli ra write konid , in ravesh bar roye goshi samsung shoma kar nmikonad ...'+'\n\n'+'- download odin : https://github.com/sys113/CGT-dependencies/raw/master/Odin3_v3.13.1.zip'+'\n\n'+'- download goshi haye samsung : https://github.com/sys113/CGT-dependencies/raw/master/Samsung_USB_Driver_v1.5.60.0.zip'
                            readme_unpack = open(home + '\\Desktop\\CGT-Files\\4\\CGT.txt', 'w')
                            readme_unpack.write(readme_unpack_write)
                            readme_unpack.close()
                            sleep(1)
                            print(c.BLUE+'sakhte shod'+c.YELLOW+' CGT_SAM_BypassLockScreen_M1_CGT.tar '+c.BLUE+'dar' + c.RED+' : '+c.GREEN+'CGT-Files'+c.YELLOW+'/'+c.RED+'4'+c.YELLOW+'/')
                            chdir(home)
                            startfile(realpath(home+'\\Desktop\\CGT-Files\\4\\'))
                            startfile(home+'\\Desktop\\CGT-Files\\4\\CGT.txt')
                        elif ramdisk_size.st_size == 0:
                            sleep(1)
                            print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'6' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                            error(6)
                            chdir(home)
                            print(c.BLUE+'hazf'+c.RED+' log ha '+c.BLUE+'va'+c.RED+' khoroj '+c.BLUE+'.'+c.GREEN+'.'+c.RED+'.')
                            chdir(home)
                            try:
                                rmtree(home + "\\Desktop\\CGT-Files\\4\\")
                            except:
                                print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'25' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                error(25)
                            return
                    else:
                        print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'28' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                        error(28)
                elif (file_extension == '.md5') or (file_extension == '.tar'):
                    tar_file = TarFileOpen(file)
                    if ('boot.img' not in tar_file.getnames()) and ('boot.img.lz4' not in tar_file.getnames()):
                        print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'14' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                        error(14)
                    else:
                        if 'boot.img' in tar_file.getnames():
                            if isdir(home + "\\Desktop\\CGT-Files\\4\\"):
                                try:
                                    sleep(1)
                                    print(c.END+c.RED+'poshe'+c.YELLOW+' 4 '+c.BLUE + 'vojod darad'+c.GREEN+' ; '+c.RED + 'hazf '+c.GREEN+'&'+c.RED+' sakht dobare ' + c.BLUE + '.' + c.GREEN + '.' + c.RED + '.')
                                    rmtree(home + "\\Desktop\\CGT-Files\\4\\")
                                except:
                                    sleep(1)
                                    print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'25' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                    error(25)
                                    return
                            else:
                                print(c.RED+'sakht'+c.BLUE+' poshe '+c.YELLOW+'4'+c.RED+' .'+c.GREEN+'.'+c.BLUE+'.')
                            system('mkdir '+home + '\\Desktop\\CGT-Files\\4\\')
                            chdir(home + '\\Desktop\\CGT-Files\\4\\')
                            sleep(1)
                            print(c.END+c.BLUE+'yaft shod'+c.RED+' boot.img'+c.BLUE+' dar '+c.RED+basename(file)+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                            sleep(1)
                            print(c.END+c.BLUE+'estekhraj'+c.RED+' boot.img '+c.BLUE+'az '+c.RED+basename(file)+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                            tar_file.extract('boot.img')
                            sleep(1)
                            print(c.END+c.BLUE + 'estekhraj ' + c.RED + 'boot.img ' + c.BLUE + '.' + c.GREEN + '.' + c.RED + '.')
                            system('mkdir '+home + '\\Desktop\\CGT-Files\\4\\repack_dependencies\\')
                            system(home+'\\.CGT\\programs\\unpackbootimg.exe' + ' -i ' + home+'\\Desktop\\CGT-Files\\4\\boot.img' + ' -o ' + home + '\\Desktop\\CGT-Files\\4\\repack_dependencies\\ > NUL')
                            rename(home+'\\Desktop\\CGT-Files\\4\\boot.img',home+'\\Desktop\\CGT-Files\\4\\stock_boot.img')
                            sleep(1)
                            print(c.END+c.BLUE + 'estekhraj'+c.RED+' ramdisk ' + c.BLUE + '.' + c.GREEN + '.' + c.RED + '.')
                            ramdisk_size = stat(home+'\\Desktop\\CGT-Files\\4\\repack_dependencies\\boot.img-ramdisk.gz')
                            if ramdisk_size.st_size != 0:
                                system('mkdir unpack')
                                chdir('unpack')
                                system(home+'\\.CGT\\programs\\gzip.exe -dcq '+home+'\\Desktop\\CGT-Files\\4\\repack_dependencies\\boot.img-ramdisk.gz | '+home+'\\.CGT\\programs\\cpio -i > NUL 2>&1')
                                sleep(1)
                                print(c.BLUE+'taghir '+c.RED+'source'+c.BLUE+' baray '+c.RED +'dor zadan ghofl safhe'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                if not '# Do not place files or directories in /data/local/tmp' in open(home+'\\Desktop\\CGT-Files\\4\\unpack\\init.rc','r').read():
                                    sleep(1)
                                    print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'27' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                    error(27)
                                    sleep(1)
                                    print(c.BLUE+'hazf'+c.RED+' log ha '+c.BLUE+'va'+c.RED+' khoroj '+c.BLUE+'.'+c.GREEN+'.'+c.RED+'.')
                                    chdir(home)
                                    try:
                                        rmtree(home + "\\Desktop\\CGT-Files\\4\\")
                                    except:
                                        print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'25' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                        error(25)
                                    return
                                with FileInput(home+'\\Desktop\\CGT-Files\\4\\unpack\\init.rc', inplace=True) as file:
                                    for line in file:
                                        print(line.replace('# Do not place files or directories in /data/local/tmp', '''
    # Do not place files or directories in /data/local/tmp

    # ---------- BYPASS SCREEN LOCK BY CGT ----------

    rm -f /data/system/locksettings.db 
    rm -f /data/system/locksettings.db-wal
    rm -f /data/system/locksettings.db-shm
    rm -f /data/system/gesture.key
    rm -f /data/system/password.key
    rm -f /data/system/signature.key
    rm -f /data/system/sparepassword.key
    rm /data/system/locksettings.db 
    rm /data/system/locksettings.db-wal
    rm /data/system/locksettings.db-shm
    rm /data/system/gesture.key
    rm /data/system/password.key
    rm /data/system/signature.key
    rm /data/system/sparepassword.key
    restorecon -R /data/system

    # ---------- BYPASS SCREEN LOCK BY CGT ----------
                        '''), end='')
                                sleep(1)
                                print(c.END + c.BLUE + 'tabdil'+c.RED+' ramdisk ' + c.BLUE+'be' +
                                      c.RED+' ramdisk.gz' + c.BLUE + ' .' + c.GREEN + '.' + c.RED + '.')
                                chdir(home+'\\Desktop\\CGT-Files\\4\\')
                                system(home+'\\.CGT\\programs\\mkbootfs.exe unpack | '+home+'\\.CGT\\programs\\minigzip.exe -c -9 > '+home+'\\Desktop\\CGT-Files\\4\\ramdisk.gz')
                                compress_repack_directory()
                                sleep(1)
                                print(c.END + c.BLUE + 'tabdil '+c.RED+'ramdisk.gz'+c.GREEN+' & '+c.RED+'baghi va ha' +c.BLUE+' be '+c.RED + 'boot.img ' + c.BLUE + '.' + c.GREEN + '.' + c.RED + '.')
                                chdir(home + "\\Desktop\\CGT-Files\\4\\")
                                class repack:
                                    _mkboot = home+'\\.CGT\\programs\\mkbootimg.exe'
                                    _kernel = home+'/Desktop/CGT-Files/4/repack/CGT_50484c19f1afdaf3841a0d821ed393d2_CGT'
                                    _ramdisk = home+'/Desktop/CGT-Files/4/repack/CGT_5c5f44ab0550487fbce8a2874ebaab6a_CGT.gz'
                                    _cmdline = open(home+'/Desktop/CGT-Files/4/repack/CGT_95f44086bc13f782435dd6356310e7bd_CGT').read().replace('\n', '')
                                    _cmdline = '\"'+_cmdline+'\"'
                                    _base = open(home+'/Desktop/CGT-Files/4/repack/CGT_593616de15330c0fb2d55e55410bf994_CGT').read().replace('\n', '')
                                    _pagesize = open(home+'/Desktop/CGT-Files/4/repack/CGT_7525d528a3457f0227997c25239c4507_CGT').read().replace('\n', '')
                                    _dt = home+'/Desktop/CGT-Files/4/repack/CGT_3017d911efceb27d1de6a92b70979795_CGT'
                                    _kerneloffset = open(home+'/Desktop/CGT-Files/4/repack/CGT_706cf6b230a6d77ee280a40b54246762_CGT').read().replace('\n', '')
                                    _ramdiskoffset = open(home+'/Desktop/CGT-Files/4/repack/CGT_0e16d6f83afe32911816ef683ad5d639_CGT').read().replace('\n', '')
                                    _secondoffset = open(home+'/Desktop/CGT-Files/4/repack/CGT_d753658059439ac8a93d411e68e5d66a_CGT').read().replace('\n', '')
                                    _tagsoffset = open(home+'/Desktop/CGT-Files/4/repack/CGT_a4d756b70ed4593b8d0f2abd01694f39_CGT').read().replace('\n', '')
                                    _hash = open(home+'/Desktop/CGT-Files/4/repack/CGT_0800fc577294c34e0b28ad2839435945_CGT').read().replace('\n', '')
                                    _hash = '\"'+_hash+'\"'
                                if isfile(home+'\\Desktop\\CGT-Files\\4\\repack\\CGT_3017d911efceb27d1de6a92b70979795_CGT'):
                                    system(repack._mkboot+' --kernel '+repack._kernel+' --ramdisk '+repack._ramdisk+' --cmdline '+repack._cmdline+' --base '+repack._base+' --pagesize '+repack._pagesize+' --dt '+repack._dt+' --kernel_offset '+repack._kerneloffset+' --ramdisk_offset '+repack._ramdiskoffset+' --second_offset '+repack._secondoffset+' --tags_offset '+repack._tagsoffset+' --hash '+repack._hash+' -o boot.img')
                                elif not isfile(home+'\\Desktop\\CGT-Files\\4\\repack\\CGT_3017d911efceb27d1de6a92b70979795_CGT'):
                                    system(repack._mkboot+' --kernel '+repack._kernel+' --ramdisk '+repack._ramdisk+' --cmdline '+repack._cmdline+' --base '+repack._base+' --pagesize '+repack._pagesize+' --kernel_offset '+repack._kerneloffset+' --ramdisk_offset '+repack._ramdiskoffset+' --second_offset '+repack._secondoffset+' --tags_offset '+repack._tagsoffset+' --hash '+repack._hash+' -o boot.img')
                                sleep(1)
                                print(c.BLUE+'tabdil'+c.RED+' boot.img '+c.BLUE+'be'+c.RED+' CGT_SAM_BypassLockScreen_M1_CGT.tar '+c.BLUE + '.' + c.GREEN + '.' + c.RED + '.')
                                sleep(1)
                                print(c.END+c.BLUE+'hazf ' + c.RED+'log ha' + c.BLUE + ' .' + c.GREEN + '.' + c.RED + '.')
                                chdir(home+'\\Desktop\\')
                                rmtree(home + "\\Desktop\\CGT-Files\\4\\unpack")
                                rmtree(home + "\\Desktop\\CGT-Files\\4\\repack")
                                rmtree(home + "\\Desktop\\CGT-Files\\4\\repack_dependencies")
                                remove(home + "\\Desktop\\CGT-Files\\4\\stock_boot.img")
                                readme_unpack_write = '--- sakhteh shod CGT_SAM_BypassLockScreen_M1_CGT.tar tavasote CGT ---'+'\n\n'+'- chand nokte ...'+'\n\t'+"1 : dar in ravesh etela'at hazf nmishavad az goshi ..."+'\n\t'+"2 : boot asli'i ke be CGT midahid bayad haman boot feali goshi samsung bashad ..."+'\n\t' + '3 : in ravesh faght baraye goshi haye samsung ast ...'+'\n\t'+'4 : in ravesh dar sorate faal bodan frp,oem,crom,reactivition ammal nakhahad kard ...' + '\n\t'+'5 : in ravesh bar roye noskhe android bishtar az 8 ammal nakhahad kard ...'+'\n\t'+'6 : write konid CGT_SAM_BypassLockScreen_M1_CGT.tar ra dar AP odin ...'+'\n\t'+'7 : baad az write CGT_SAM_BypassLockScreen_M1_CGT.tar va dor zadan ghofl , az tamami dadeh haye goshi backup begirid va boot original ra write konid ...'+'\n\t'+'8 : agar goshi samsung shoma baad az write file va rah\'andazi mojadad bar roye logo samsung mand , dobareh boot asli ra write konid , in ravesh bar roye goshi samsung shoma kar nmikonad ...'+'\n\n'+'- download odin : https://github.com/sys113/CGT-dependencies/raw/master/Odin3_v3.13.1.zip'+'\n\n'+'- download goshi haye samsung : https://github.com/sys113/CGT-dependencies/raw/master/Samsung_USB_Driver_v1.5.60.0.zip'
                                readme_unpack = open(home + '\\Desktop\\CGT-Files\\4\\CGT.txt', 'w')
                                readme_unpack.write(readme_unpack_write)
                                readme_unpack.close()
                                sleep(1)
                                print(c.BLUE+'sakhte shod'+c.YELLOW+' CGT_SAM_BypassLockScreen_M1_CGT.tar '+c.BLUE+'dar' + c.RED+' : '+c.GREEN+'CGT-Files'+c.YELLOW+'/'+c.RED+'4'+c.YELLOW+'/')
                                chdir(home)
                                startfile(realpath(home+'\\Desktop\\CGT-Files\\4\\'))
                                startfile(home+'\\Desktop\\CGT-Files\\4\\CGT.txt')
                            elif ramdisk_size.st_size == 0:
                                sleep(1)
                                print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'6' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                error(6)
                                sleep(1)
                                print(c.BLUE+'hazf'+c.RED+' log ha '+c.BLUE+'va'+c.RED+' khoroj '+c.BLUE+'.'+c.GREEN+'.'+c.RED+'.')
                                chdir(home)
                                try:
                                    rmtree(home + "\\Desktop\\CGT-Files\\4\\")
                                except:
                                    print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'25' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                    error(25)
                                return
                        elif 'boot.img.lz4' in tar_file.getnames():
                            if isdir(home + "\\Desktop\\CGT-Files\\4\\"):
                                try:
                                    sleep(1)
                                    print(c.END+c.RED+'poshe'+c.YELLOW+' 4 '+c.BLUE + 'vojod darad'+c.GREEN+' ; '+c.RED + 'hazf '+c.GREEN+'&'+c.RED+' sakht dobare ' + c.BLUE + '.' + c.GREEN + '.' + c.RED + '.')
                                    rmtree(home + "\\Desktop\\CGT-Files\\4\\")
                                except:
                                    sleep(1)
                                    print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'25' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                    error(25)
                                    return
                            else:
                                print(c.RED+'sakht'+c.BLUE+' poshe '+c.YELLOW+'4'+c.RED+' .'+c.GREEN+'.'+c.BLUE+'.')
                            system('mkdir '+home + '\\Desktop\\CGT-Files\\4\\')
                            chdir(home + '\\Desktop\\CGT-Files\\4\\')
                            sleep(1)
                            print(c.END+c.BLUE+'yaft shod'+c.RED+' boot.img.lz4'+c.BLUE+' dar '+c.RED+basename(file)+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                            sleep(1)
                            print(c.END+c.BLUE+'estekhraj'+c.RED+' boot.img.lz4 '+c.BLUE+'az '+c.RED+basename(file)+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                            tar_file.extract('boot.img.lz4')
                            sleep(1)
                            print(c.END+c.BLUE + 'tabdil '+c.RED + 'boot.img.lz4' + c.BLUE + ' be ' +
                                c.RED + 'boot.img' + c.BLUE + ' .' + c.GREEN + '.' + c.RED + '.')
                            system(home +'\\.CGT\\programs\\lz4.exe -d boot.img.lz4')
                            img_lz4_size = stat(home+'\\Desktop\\CGT-Files\\4\\boot.img')
                            if img_lz4_size.st_size == 0:
                              sleep(1)
                              print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'4' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                              error(4)
                              sleep(1)
                              print(c.BLUE+'hazf'+c.RED+' log ha '+c.BLUE+'va'+c.RED+' khoroj '+c.BLUE+'.'+c.GREEN+'.'+c.RED+'.')
                              chdir(home)
                              try:
                                rmtree(home + "\\Desktop\\CGT-Files\\4\\")
                              except:
                                print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'25' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                error(25)
                              return
                            sleep(1)
                            print(c.END+c.BLUE + 'estekhraj ' + c.RED + 'boot.img ' + c.BLUE + '.' + c.GREEN + '.' + c.RED + '.')
                            system('mkdir '+home + '\\Desktop\\CGT-Files\\4\\repack_dependencies\\')
                            system(home+'\\.CGT\\programs\\unpackbootimg.exe' + ' -i ' + home+'\\Desktop\\CGT-Files\\4\\boot.img' + ' -o ' + home + '\\Desktop\\CGT-Files\\4\\repack_dependencies\\ > NUL')
                            rename(home+'\\Desktop\\CGT-Files\\4\\boot.img',home+'\\Desktop\\CGT-Files\\4\\stock_boot.img')
                            sleep(1)
                            print(c.END+c.BLUE + 'estekhraj'+c.RED+' ramdisk ' + c.BLUE + '.' + c.GREEN + '.' + c.RED + '.')
                            try:
                                ramdisk_size = stat(home+'\\Desktop\\CGT-Files\\4\\repack_dependencies\\boot.img-ramdisk.gz')
                            except:
                                print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'8' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                error(8)
                                return
                            if ramdisk_size.st_size != 0:
                                system('mkdir unpack')
                                chdir('unpack')
                                system(home+'\\.CGT\\programs\\gzip.exe -dcq '+home+'\\Desktop\\CGT-Files\\4\\repack_dependencies\\boot.img-ramdisk.gz | '+home+'\\.CGT\\programs\\cpio -i > NUL 2>&1')
                                sleep(1)
                                print(c.BLUE+'taghir '+c.RED+'source'+c.BLUE+' baray '+c.RED +'dor zadan ghofl safhe'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                if not '# Do not place files or directories in /data/local/tmp' in open(home+'\\Desktop\\CGT-Files\\4\\unpack\\init.rc','r').read():
                                    sleep(1)
                                    print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'27' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                    error(27)
                                    sleep(1)
                                    print(c.BLUE+'hazf'+c.RED+' log ha '+c.BLUE+'va'+c.RED+' khoroj '+c.BLUE+'.'+c.GREEN+'.'+c.RED+'.')
                                    chdir(home)
                                    try:
                                        rmtree(home + "\\Desktop\\CGT-Files\\4\\")
                                    except:
                                        print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'25' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                        error(25)
                                    return
                                with FileInput(home+'\\Desktop\\CGT-Files\\4\\unpack\\init.rc', inplace=True) as file:
                                    for line in file:
                                        print(line.replace('# Do not place files or directories in /data/local/tmp', '''
    # Do not place files or directories in /data/local/tmp

    # ---------- BYPASS SCREEN LOCK BY CGT ----------

    rm -f /data/system/locksettings.db 
    rm -f /data/system/locksettings.db-wal
    rm -f /data/system/locksettings.db-shm
    rm -f /data/system/gesture.key
    rm -f /data/system/password.key
    rm -f /data/system/signature.key
    rm -f /data/system/sparepassword.key
    rm /data/system/locksettings.db 
    rm /data/system/locksettings.db-wal
    rm /data/system/locksettings.db-shm
    rm /data/system/gesture.key
    rm /data/system/password.key
    rm /data/system/signature.key
    rm /data/system/sparepassword.key
    restorecon -R /data/system

    # ---------- BYPASS SCREEN LOCK BY CGT ----------
                        '''), end='')
                                sleep(1)
                                print(c.END + c.BLUE + 'tabdil'+c.RED+' ramdisk ' + c.BLUE+'be' +c.RED+' ramdisk.gz' + c.BLUE + ' .' + c.GREEN + '.' + c.RED + '.')
                                chdir(home+'\\Desktop\\CGT-Files\\4\\')
                                system(home+'\\.CGT\\programs\\mkbootfs.exe unpack | '+home+'\\.CGT\\programs\\minigzip.exe -c -9 > '+home+'\\Desktop\\CGT-Files\\4\\ramdisk.gz')
                                compress_repack_directory()
                                sleep(1)
                                print(c.END + c.BLUE + 'tabdil '+c.RED+'ramdisk.gz'+c.GREEN+' & '+c.RED+'baghi vabastegi ha' +c.BLUE+' be '+c.RED + 'boot.img ' + c.BLUE + '.' + c.GREEN + '.' + c.RED + '.')
                                chdir(home + "\\Desktop\\CGT-Files\\4\\")
                                class repack:
                                    _mkboot = home+'\\.CGT\\programs\\mkbootimg.exe'
                                    _kernel = home+'/Desktop/CGT-Files/4/repack/CGT_50484c19f1afdaf3841a0d821ed393d2_CGT'
                                    _ramdisk = home+'/Desktop/CGT-Files/4/repack/CGT_5c5f44ab0550487fbce8a2874ebaab6a_CGT.gz'
                                    _cmdline = open(home+'/Desktop/CGT-Files/4/repack/CGT_95f44086bc13f782435dd6356310e7bd_CGT').read().replace('\n', '')
                                    _cmdline = '\"'+_cmdline+'\"'
                                    _base = open(home+'/Desktop/CGT-Files/4/repack/CGT_593616de15330c0fb2d55e55410bf994_CGT').read().replace('\n', '')
                                    _pagesize = open(home+'/Desktop/CGT-Files/4/repack/CGT_7525d528a3457f0227997c25239c4507_CGT').read().replace('\n', '')
                                    _dt = home+'/Desktop/CGT-Files/4/repack/CGT_3017d911efceb27d1de6a92b70979795_CGT'
                                    _kerneloffset = open(home+'/Desktop/CGT-Files/4/repack/CGT_706cf6b230a6d77ee280a40b54246762_CGT').read().replace('\n', '')
                                    _ramdiskoffset = open(home+'/Desktop/CGT-Files/4/repack/CGT_0e16d6f83afe32911816ef683ad5d639_CGT').read().replace('\n', '')
                                    _secondoffset = open(home+'/Desktop/CGT-Files/4/repack/CGT_d753658059439ac8a93d411e68e5d66a_CGT').read().replace('\n', '')
                                    _tagsoffset = open(home+'/Desktop/CGT-Files/4/repack/CGT_a4d756b70ed4593b8d0f2abd01694f39_CGT').read().replace('\n', '')
                                    _hash = open(home+'/Desktop/CGT-Files/4/repack/CGT_0800fc577294c34e0b28ad2839435945_CGT').read().replace('\n', '')
                                    _hash = '\"'+_hash+'\"'
                                if isfile(home+'\\Desktop\\CGT-Files\\4\\repack\\CGT_3017d911efceb27d1de6a92b70979795_CGT'):
                                    system(repack._mkboot+' --kernel '+repack._kernel+' --ramdisk '+repack._ramdisk+' --cmdline '+repack._cmdline+' --base '+repack._base+' --pagesize '+repack._pagesize+' --dt '+repack._dt+' --kernel_offset '+repack._kerneloffset+' --ramdisk_offset '+repack._ramdiskoffset+' --second_offset '+repack._secondoffset+' --tags_offset '+repack._tagsoffset+' --hash '+repack._hash+' -o boot.img')
                                elif not isfile(home+'\\Desktop\\CGT-Files\\4\\repack\\CGT_3017d911efceb27d1de6a92b70979795_CGT'):
                                    system(repack._mkboot+' --kernel '+repack._kernel+' --ramdisk '+repack._ramdisk+' --cmdline '+repack._cmdline+' --base '+repack._base+' --pagesize '+repack._pagesize+' --kernel_offset '+repack._kerneloffset+' --ramdisk_offset '+repack._ramdiskoffset+' --second_offset '+repack._secondoffset+' --tags_offset '+repack._tagsoffset+' --hash '+repack._hash+' -o boot.img')
                                sleep(1)
                                print(c.BLUE+'tabdil'+c.RED+' boot.img '+c.BLUE+'be'+c.RED+' CGT_SAM_BypassLockScreen_M1_CGT.tar '+c.BLUE + '.' + c.GREEN + '.' + c.RED + '.')
                                sleep(1)
                                print(c.END+c.BLUE+'hazf ' + c.RED+'log ha' + c.BLUE + ' .' + c.GREEN + '.' + c.RED + '.')
                                chdir(home+'\\Desktop\\')
                                rmtree(home + "\\Desktop\\CGT-Files\\4\\unpack")
                                rmtree(home + "\\Desktop\\CGT-Files\\4\\repack")
                                rmtree(home + "\\Desktop\\CGT-Files\\4\\repack_dependencies\\")
                                remove(home + "\\Desktop\\CGT-Files\\4\\stock_boot.img")
                                remove(home + "\\Desktop\\CGT-Files\\4\\boot.img.lz4")
                                readme_unpack_write = '--- sakhteh shod CGT_SAM_BypassLockScreen_M1_CGT.tar tavasote CGT ---'+'\n\n'+'- chand nokte ...'+'\n\t'+"1 : dar in ravesh etela'at hazf nmishavad az goshi ..."+'\n\t'+"2 : boot asli'i ke be CGT midahid bayad haman boot feali goshi samsung bashad ..."+'\n\t' + '3 : in ravesh faght baraye goshi haye samsung ast ...'+'\n\t'+'4 : in ravesh dar sorate faal bodan frp,oem,crom,reactivition ammal nakhahad kard ...' + '\n\t'+'5 : in ravesh bar roye noskhe android bishtar az 8 ammal nakhahad kard ...'+'\n\t'+'6 : write konid CGT_SAM_BypassLockScreen_M1_CGT.tar ra dar AP odin ...'+'\n\t'+'7 : baad az write CGT_SAM_BypassLockScreen_M1_CGT.tar va dor zadan ghofl , az tamami dadeh haye goshi backup begirid va boot original ra write konid ...'+'\n\t'+'8 : agar goshi samsung shoma baad az write file va rah\'andazi mojadad bar roye logo samsung mand , dobareh boot asli ra write konid , in ravesh bar roye goshi samsung shoma kar nmikonad ...'+'\n\n'+'- download odin : https://github.com/sys113/CGT-dependencies/raw/master/Odin3_v3.13.1.zip'+'\n\n'+'- download goshi haye samsung : https://github.com/sys113/CGT-dependencies/raw/master/Samsung_USB_Driver_v1.5.60.0.zip'
                                readme_unpack = open(home + '\\Desktop\\CGT-Files\\4\\CGT.txt', 'w')
                                readme_unpack.write(readme_unpack_write)
                                readme_unpack.close()
                                sleep(1)
                                print(c.BLUE+'sakhte shod'+c.YELLOW+' CGT_SAM_BypassLockScreen_M1_CGT.tar '+c.BLUE+'dar' + c.RED+' : '+c.GREEN+'CGT-Files'+c.YELLOW+'/'+c.RED+'4'+c.YELLOW+'/')
                                chdir(home)
                                startfile(realpath(home+'\\Desktop\\CGT-Files\\4\\'))
                                startfile(home+'\\Desktop\\CGT-Files\\4\\CGT.txt')
                            elif ramdisk_size.st_size == 0:
                                        print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'6' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                        error(6)
                                        print(c.END+c.BLUE+'hazf ' + c.RED+'log ha' + c.BLUE + ' .' + c.GREEN + '.' + c.RED + '.')
                                        chdir(home)
                                        try:
                                            rmtree(home + "\\Desktop\\CGT-Files\\4\\")
                                        except:
                                            print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'25' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                            error(25)
                                        return
                else:
                    print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'15' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                    error(15)
            elif exists(file) == False:
                print(c.RED+'khata'+c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'1' + c.GREEN+' | '+c.BLUE+'lotfan bbinid '+c.RED+'CGT-Files/FA-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                error(1)
        if exists(home+"\\Desktop\\CGT-Files\\4\\boot.img"):
            chdir(home+"\\Desktop\\CGT-Files\\4\\")
            with TarFileOpen("CGT_SAM_BypassLockScreen_M1_CGT.tar", "w") as tar:
                tar.add('boot.img')
            remove(home+'\\Desktop\\CGT-Files\\4\\boot.img')
            chdir(home+'\\Desktop\\')
    elif language == 'EN':
        sleep(0.5)
        print('\n'+c.RED+'tip '+c.YELLOW+'1'+c.GREEN+' : '+c.BLUE+'this method'+c.RED+' not delete data '+c.BLUE+'from the'+c.RED+' phone'+c.BLUE+' .'+c.GREEN+'.'+c.BLUE+'.')
        sleep(0.5)
        print(c.RED+'tip '+c.YELLOW+'2'+c.GREEN+' : '+c.BLUE+'this'+c.RED+' method '+c.BLUE+'only for'+c.RED+' samsung phones '+c.BLUE + '.' + c.GREEN + '.' + c.RED + '.')
        sleep(0.5)
        print(c.RED+'tip '+c.YELLOW+'3'+c.GREEN+' : '+c.RED+'original boot'+c.BLUE+' imported to '+c.YELLOW+'CGT'+c.BLUE+' it should be equal '+c.RED+'current boot'+c.BLUE+' samsung phone'+c.RED + ' .' + c.GREEN + '.' + c.BLUE + '.')
        sleep(0.5)
        print(c.RED+'tip '+c.YELLOW+'4'+c.GREEN+' : '+c.BLUE+'this'+c.RED+' method '+c.BLUE+'will '+c.RED+'not work '+c.BLUE+'if '+c.YELLOW+'frp'+c.GREEN+','+c.YELLOW+'oem'+c.GREEN+','+c.YELLOW+'crom'+c.GREEN+','+c.YELLOW+'reactivition '+c.BLUE+'is'+c.RED+' enabled '+c.BLUE + '.' + c.GREEN + '.' + c.RED + '.')
        sleep(0.5)
        print(c.RED+'tip '+c.YELLOW+'5'+c.GREEN+' : '+c.BLUE+'this'+c.RED+' method '+c.BLUE+'will '+c.RED+'not work '+c.BLUE+'in '+c.RED+'android version'+c.BLUE+' more than'+c.YELLOW+' 8 '+c.BLUE + '.' + c.GREEN + '.' + c.RED + '.'+'\n')
        sleep(1)
        print(c.END + c.BLUE+'drag' + c.RED + ' & ' + c.BLUE + 'drop ' + c.RED + c.YELLOW+'original boot '+c.RED +'['+c.GREEN+'.img' + c.RED + '/' + c.GREEN + '.img.lz4' + c.RED + '/' + c.GREEN + '.tar' + c.RED + '/' + c.GREEN + '.tar.md5'+c.RED+']'+c.BLUE + ' and press' + c.RED+' enter ' + c.BLUE +'key'+ c.RED+' .'+c.GREEN+'.'+c.BLUE+'.')
        file = xinput(c.MAGENTA+'> '+c.YELLOW)
        file = file.replace("\"", "")
        file = file.replace("\'", "")
        file_name, file_extension = splitext(file)
        chdir(home)
        if ' ' in file:
            print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'2' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
            error(2)
        else:
            if exists(file) == True:
                if file_extension == '.lz4':
                    if (basename(file) == 'boot.img.lz4'):
                        remove_boot_img = file.replace(".lz4", "")
                        if isdir(home + "\\Desktop\\CGT-Files\\4\\"):
                            try:
                                sleep(1)
                                print(c.END+c.RED+'directory'+c.YELLOW+' 4 '+c.BLUE + 'already exists'+c.GREEN+' ; '+c.RED +'overwrite ' + c.BLUE + '.' + c.GREEN + '.' + c.RED + '.')
                                rmtree(home + "\\Desktop\\CGT-Files\\4\\")
                            except:
                                sleep(1)
                                print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'25' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                error(25)
                                return
                        else:
                            print(c.RED+'making'+c.BLUE+' directory '+c.YELLOW+'4'+c.RED+' .'+c.GREEN+'.'+c.BLUE+'.')
                        system('mkdir '+home + '\\Desktop\\CGT-Files\\4\\')
                        chdir(home + '\\Desktop\\CGT-Files\\4\\')
                        sleep(1)
                        print(c.END+c.BLUE + 'conevert '+c.RED + basename(remove_boot_img+'.lz4') + c.BLUE + ' to ' +
                            c.RED + basename(remove_boot_img) + c.BLUE + ' .' + c.GREEN + '.' + c.RED + '.')
                        system(home + '\\.CGT\\programs\\lz4.exe -d ' + file)
                        file = file.replace(".lz4", "")
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
                            rmtree(home + "\\Desktop\\CGT-Files\\4\\")
                          except:
                            print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'25' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                            error(25)
                          return
                        sleep(1)
                        print(c.END+c.BLUE + 'unpack '+c.RED+basename(file) + c.BLUE + ' .' + c.GREEN + '.' + c.RED + '.')
                        system('mkdir '+home +
                                '\\Desktop\\CGT-Files\\4\\repack_dependencies\\')
                        system(home+'\\.CGT\\programs\\unpackbootimg.exe' + ' -i ' +
                                file + ' -o ' + home + '\\Desktop\\CGT-Files\\4\\repack_dependencies\\ > NUL')
                        sleep(1)
                        print(c.END+c.BLUE + 'unpack'+c.RED+' ramdisk ' +
                            c.BLUE + '.' + c.GREEN + '.' + c.RED + '.')
                        try:
                            ramdisk_size = stat(home+'\\Desktop\\CGT-Files\\4\\repack_dependencies\\'+basename(file)+'-ramdisk.gz')
                        except:
                            try:
                                ramdisk_size = stat(home+'\\Desktop\\CGT-Files\\2\\repack_dependencies\\'+basename(file)+'-ramdisk.gz')
                            except:
                                sleep(1)
                                print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'8' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                error(8)
                                print(c.BLUE+'ramove'+c.RED+' logs '+c.BLUE+'and'+c.RED+' break '+c.BLUE+'.'+c.GREEN+'.'+c.RED+'.')
                                chdir(home)
                                remove(file)
                                try:
                                  rmtree(home + "\\Desktop\\CGT-Files\\4\\")
                                except:
                                  print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'25' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                  error(25)
                                return
                        if ramdisk_size.st_size != 0:
                            system('mkdir unpack')
                            chdir('unpack')
                            system(home+'\\.CGT\\programs\\gzip.exe -dcq '+home+'\\Desktop\\CGT-Files\\4\\repack_dependencies\\' + basename(file)+'-ramdisk.gz | '+home+'\\.CGT\\programs\\cpio -i > NUL 2>&1')
                            sleep(1)
                            print(c.BLUE+'edit '+c.RED+'source'+c.BLUE+' to '+c.RED +'bypass lock screen'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                            if not '# Do not place files or directories in /data/local/tmp' in open(home+'\\Desktop\\CGT-Files\\4\\unpack\\init.rc','r').read():
                                sleep(1)
                                print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'27' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                error(27)
                                sleep(1)
                                print(c.BLUE+'remove'+c.RED+' logs '+c.BLUE+'and'+c.RED+' break '+c.BLUE+'.'+c.GREEN+'.'+c.RED+'.')
                                chdir(home)
                                remove(remove_boot_img)
                                try:
                                    rmtree(home + "\\Desktop\\CGT-Files\\4\\")
                                except:
                                    print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'25' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                    error(25)
                                return
                            with FileInput(home+'\\Desktop\\CGT-Files\\4\\unpack\\init.rc', inplace=True) as file:
                                for line in file:
                                    print(line.replace('# Do not place files or directories in /data/local/tmp', '''
    # Do not place files or directories in /data/local/tmp

    # ---------- BYPASS SCREEN LOCK BY CGT ----------

    rm -f /data/system/locksettings.db 
    rm -f /data/system/locksettings.db-wal
    rm -f /data/system/locksettings.db-shm
    rm -f /data/system/gesture.key
    rm -f /data/system/password.key
    rm -f /data/system/signature.key
    rm -f /data/system/sparepassword.key
    rm /data/system/locksettings.db 
    rm /data/system/locksettings.db-wal
    rm /data/system/locksettings.db-shm
    rm /data/system/gesture.key
    rm /data/system/password.key
    rm /data/system/signature.key
    rm /data/system/sparepassword.key
    restorecon -R /data/system

    # ---------- BYPASS SCREEN LOCK BY CGT ----------
                    '''), end='')
                            sleep(1)
                            print(c.END + c.BLUE + 'packed'+c.RED+' ramdisk ' + c.BLUE+'to' +c.RED+' ramdisk.gz' + c.BLUE + ' .' + c.GREEN + '.' + c.RED + '.')
                            chdir(home+'\\Desktop\\CGT-Files\\4\\')
                            system(home+'\\.CGT\\programs\\mkbootfs.exe unpack | '+home+'\\.CGT\\programs\\minigzip.exe -c -9 > '+home+'\\Desktop\\CGT-Files\\4\\ramdisk.gz')
                            compress_repack_directory()
                            sleep(1)
                            print(c.END + c.BLUE + 'packed '+c.RED+'ramdisk.gz'+c.GREEN+' & '+c.RED+'another dependencies' +c.BLUE+' to '+c.RED + 'boot.img ' + c.BLUE + '.' + c.GREEN + '.' + c.RED + '.')
                            chdir(home + "\\Desktop\\CGT-Files\\4\\")
                            class repack:
                                _mkboot = home+'\\.CGT\\programs\\mkbootimg.exe'
                                _kernel = home+'\\Desktop\\CGT-Files\\4\\repack\\CGT_50484c19f1afdaf3841a0d821ed393d2_CGT'
                                _ramdisk = home+'\\Desktop\\CGT-Files\\4\\repack\\CGT_5c5f44ab0550487fbce8a2874ebaab6a_CGT.gz'
                                _cmdline = open(home+'\\Desktop\\CGT-Files\\4\\repack\\CGT_95f44086bc13f782435dd6356310e7bd_CGT').read().replace('\n', '')
                                _cmdline = '\"'+_cmdline+'\"'
                                _base = open(home+'\\Desktop\\CGT-Files\\4\\repack\\CGT_593616de15330c0fb2d55e55410bf994_CGT').read().replace('\n', '')
                                _pagesize = open(home+'\\Desktop\\CGT-Files\\4\\repack\\CGT_7525d528a3457f0227997c25239c4507_CGT').read().replace('\n', '')
                                _dt = home+'\\Desktop\\CGT-Files\\4\\repack\\CGT_3017d911efceb27d1de6a92b70979795_CGT'
                                _kerneloffset = open(home+'\\Desktop\\CGT-Files\\4\\repack\\CGT_706cf6b230a6d77ee280a40b54246762_CGT').read().replace('\n', '')
                                _ramdiskoffset = open(home+'\\Desktop\\CGT-Files\\4\\repack\\CGT_0e16d6f83afe32911816ef683ad5d639_CGT').read().replace('\n', '')
                                _secondoffset = open(home+'\\Desktop\\CGT-Files\\4\\repack\\CGT_d753658059439ac8a93d411e68e5d66a_CGT').read().replace('\n', '')
                                _tagsoffset = open(home+'\\Desktop\\CGT-Files\\4\\repack\\CGT_a4d756b70ed4593b8d0f2abd01694f39_CGT').read().replace('\n', '')
                                _hash = open(home+'\\Desktop\\CGT-Files\\4\\repack\\CGT_0800fc577294c34e0b28ad2839435945_CGT').read().replace('\n', '')
                                _hash = '\"'+_hash+'\"'
                            if isfile(home+'\\Desktop\\CGT-Files\\4\\repack\\CGT_3017d911efceb27d1de6a92b70979795_CGT'):
                                system(repack._mkboot+' --kernel '+repack._kernel+' --ramdisk '+repack._ramdisk+' --cmdline '+repack._cmdline+' --base '+repack._base+' --pagesize '+repack._pagesize+' --dt '+repack._dt+' --kernel_offset '+repack._kerneloffset+' --ramdisk_offset '+repack._ramdiskoffset+' --second_offset '+repack._secondoffset+' --tags_offset '+repack._tagsoffset+' --hash '+repack._hash+' -o boot.img')
                            elif not isfile(home+'\\Desktop\\CGT-Files\\4\\repack\\CGT_3017d911efceb27d1de6a92b70979795_CGT'):
                                system(repack._mkboot+' --kernel '+repack._kernel+' --ramdisk '+repack._ramdisk+' --cmdline '+repack._cmdline+' --base '+repack._base+' --pagesize '+repack._pagesize+' --kernel_offset '+repack._kerneloffset+' --ramdisk_offset '+repack._ramdiskoffset+' --second_offset '+repack._secondoffset+' --tags_offset '+repack._tagsoffset+' --hash '+repack._hash+' -o boot.img')
                            sleep(1)
                            print(c.BLUE+'convert'+c.RED+' boot.img '+c.BLUE+'to'+c.RED+' CGT_SAM_BypassLockScreen_M1_CGT.tar '+c.BLUE + '.' + c.GREEN + '.' + c.RED + '.')
                            sleep(1)
                            print(c.END+c.BLUE+'remove ' + c.RED+'logs' + c.BLUE + ' .' + c.GREEN + '.' + c.RED + '.')
                            chdir(home+'\\Desktop\\')
                            rmtree(home + "\\Desktop\\CGT-Files\\4\\unpack")
                            rmtree(home + "\\Desktop\\CGT-Files\\4\\repack")
                            rmtree(home + "\\Desktop\\CGT-Files\\4\\repack_dependencies")
                            remove(remove_boot_img)
                            readme_unpack_write = '--- maked CGT_SAM_BypassLockScreen_M1_CGT.tar by CGT ---'+'\n\n'+'- Several tips ...'+'\n\t'+'1 : this method not delete data from the phone ...'+'\n\t'+'2 : this method only for samsung phones ...'+'\n\t' + '3 : original boot imported to CGT it should be equal current boot samsung phone ...'+'\n\t'+'4 : this method will not work if frp,oem,crom,reactivition is enabled ...' + '\n\t'+'5 : this method will not work in android version more than 8 ...'+'\n\t'+'6 : write CGT_SAM_BypassLockScreen_M1_CGT.tar in AP odin ...'+'\n\t'+'7 : after CGT_SAM_BypassLockScreen_M1_CGT.tar and bypass lock screen , backup all data and write again original boot to phone ...'+'\n\t'+'8 : if samsung phone after reboot stays on samsung logo write again original boot and This method does not work on your samsung phone ...'+'\n\n'+'- download odin : https://github.com/sys113/CGT-dependencies/raw/master/Odin3_v3.13.1.zip'+'\n\n'+'- download samsung phone driver : https://github.com/sys113/CGT-dependencies/raw/master/Samsung_USB_Driver_v1.5.60.0.zip'
                            readme_unpack = open(home + '\\Desktop\\CGT-Files\\4\\CGT.txt', 'w')
                            readme_unpack.write(readme_unpack_write)
                            readme_unpack.close()
                            sleep(1)
                            print(c.BLUE+'maked'+c.YELLOW+' CGT_SAM_BypassLockScreen_M1_CGT.tar '+c.BLUE+'in' + c.RED+' : '+c.GREEN+'CGT-Files'+c.YELLOW+'/'+c.RED+'4'+c.YELLOW+'/')
                            chdir(home)
                            startfile(realpath(home+'\\Desktop\\CGT-Files\\4\\'))
                            startfile(home+'\\Desktop\\CGT-Files\\4\\CGT.txt')
                        elif ramdisk_size.st_size == 0:
                            sleep(1)
                            print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'6' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                            error(6)
                            chdir(home)
                            print(c.BLUE+'ramove'+c.RED+' logs '+c.BLUE+'and'+c.RED+' break '+c.BLUE+'.'+c.GREEN+'.'+c.RED+'.')
                            remove(remove_boot_img)
                            try:
                                rmtree(home + "\\Desktop\\CGT-Files\\4\\")
                            except:
                                print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'25' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                error(25)
                            return
                    else:
                        print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'26' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                        error(26)
                elif file_extension == '.img':
                    if (basename(file) == 'boot.img'):
                        if isdir(home + "\\Desktop\\CGT-Files\\4\\"):
                            try:
                                sleep(1)
                                print(c.END+c.RED+'directory'+c.YELLOW+' 4 '+c.BLUE + 'already exists'+c.GREEN+' ; '+c.RED +'overwrite ' + c.BLUE + '.' + c.GREEN + '.' + c.RED + '.')
                                rmtree(home + "\\Desktop\\CGT-Files\\4\\")
                            except:
                                sleep(1)
                                print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'25' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                error(25)
                                return
                        else:
                            print(c.RED+'making'+c.BLUE+' directory '+c.YELLOW+'4'+c.RED+' .'+c.GREEN+'.'+c.BLUE+'.')
                        sleep(1)
                        print(c.END+c.BLUE + 'unpack '+c.RED+basename(file) + c.BLUE + ' .' + c.GREEN + '.' + c.RED + '.')
                        system('mkdir '+home + '\\Desktop\\CGT-Files\\4\\')
                        chdir(home + '\\Desktop\\CGT-Files\\4\\')
                        system('mkdir '+home +
                                '\\Desktop\\CGT-Files\\4\\repack_dependencies\\')
                        system(home+'\\.CGT\\programs\\unpackbootimg.exe' + ' -i ' + file + ' -o ' + home + '\\Desktop\\CGT-Files\\4\\repack_dependencies\\ > NUL')
                        sleep(1)
                        print(c.END+c.BLUE + 'unpack'+c.RED+' ramdisk ' + c.BLUE + '.' + c.GREEN + '.' + c.RED + '.')
                        try:
                            ramdisk_size = stat(home+'\\Desktop\\CGT-Files\\4\\repack_dependencies\\'+basename(file)+'-ramdisk.gz')
                        except:
                            print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'8' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                            error(8)
                            print(c.BLUE+'remove'+c.RED+' logs '+c.BLUE+'and'+c.RED+' break '+c.BLUE+'.'+c.GREEN+'.'+c.RED+'.')
                            chdir(home)
                            try:
                                rmtree(home + "\\Desktop\\CGT-Files\\4\\")
                            except:
                                print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'25' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                error(25)
                            return
                        if ramdisk_size.st_size != 0:
                            system('mkdir unpack')
                            chdir('unpack')
                            system(home+'\\.CGT\\programs\\gzip.exe -dcq '+home+'\\Desktop\\CGT-Files\\4\\repack_dependencies\\' + basename(file)+'-ramdisk.gz | '+home+'\\.CGT\\programs\\cpio -i > NUL 2>&1')
                            sleep(1)
                            print(c.BLUE+'edit '+c.RED+'source'+c.BLUE+' to '+c.RED +'bypass lock screen'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                            if not '# Do not place files or directories in /data/local/tmp' in open(home+'\\Desktop\\CGT-Files\\4\\unpack\\init.rc','r').read():
                                sleep(1)
                                print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'27' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                error(27)
                                sleep(1)
                                print(c.BLUE+'remove'+c.RED+' logs '+c.BLUE+'and'+c.RED+' break '+c.BLUE+'.'+c.GREEN+'.'+c.RED+'.')
                                chdir(home)
                                try:
                                    rmtree(home + "\\Desktop\\CGT-Files\\4\\")
                                except:
                                    print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'25' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                    error(25)
                                return
                            with FileInput(home+'\\Desktop\\CGT-Files\\4\\unpack\\init.rc', inplace=True) as file:
                                for line in file:
                                    print(line.replace('# Do not place files or directories in /data/local/tmp', '''
    # Do not place files or directories in /data/local/tmp

    # ---------- BYPASS SCREEN LOCK BY CGT ----------

    rm -f /data/system/locksettings.db 
    rm -f /data/system/locksettings.db-wal
    rm -f /data/system/locksettings.db-shm
    rm -f /data/system/gesture.key
    rm -f /data/system/password.key
    rm -f /data/system/signature.key
    rm -f /data/system/sparepassword.key
    rm /data/system/locksettings.db 
    rm /data/system/locksettings.db-wal
    rm /data/system/locksettings.db-shm
    rm /data/system/gesture.key
    rm /data/system/password.key
    rm /data/system/signature.key
    rm /data/system/sparepassword.key
    restorecon -R /data/system

    # ---------- BYPASS SCREEN LOCK BY CGT ----------
                    '''), end='')
                            sleep(1)
                            print(c.END + c.BLUE + 'packed'+c.RED+' ramdisk ' + c.BLUE+'to' +
                                  c.RED+' ramdisk.gz' + c.BLUE + ' .' + c.GREEN + '.' + c.RED + '.')
                            chdir(home+'\\Desktop\\CGT-Files\\4\\')
                            system(home+'\\.CGT\\programs\\mkbootfs.exe unpack | '+home+'\\.CGT\\programs\\minigzip.exe -c -9 > '+home+'\\Desktop\\CGT-Files\\4\\ramdisk.gz')
                            compress_repack_directory()
                            sleep(1)
                            print(c.END + c.BLUE + 'packed '+c.RED+'ramdisk.gz'+c.GREEN+' & '+c.RED+'another dependencies' +c.BLUE+' to '+c.RED + 'boot.img ' + c.BLUE + '.' + c.GREEN + '.' + c.RED + '.')
                            chdir(home + "\\Desktop\\CGT-Files\\4\\")
                            class repack:
                                _mkboot = home+'\\.CGT\\programs\\mkbootimg.exe'
                                _kernel = home+'\\Desktop\\CGT-Files\\4\\repack\\CGT_50484c19f1afdaf3841a0d821ed393d2_CGT'
                                _ramdisk = home+'\\Desktop\\CGT-Files\\4\\repack\\CGT_5c5f44ab0550487fbce8a2874ebaab6a_CGT.gz'
                                _cmdline = open(home+'\\Desktop\\CGT-Files\\4\\repack\\CGT_95f44086bc13f782435dd6356310e7bd_CGT').read().replace('\n', '')
                                _cmdline = '\"'+_cmdline+'\"'
                                _base = open(home+'\\Desktop\\CGT-Files\\4\\repack\\CGT_593616de15330c0fb2d55e55410bf994_CGT').read().replace('\n', '')
                                _pagesize = open(home+'\\Desktop\\CGT-Files\\4\\repack\\CGT_7525d528a3457f0227997c25239c4507_CGT').read().replace('\n', '')
                                _dt = home+'\\Desktop\\CGT-Files\\4\\repack\\CGT_3017d911efceb27d1de6a92b70979795_CGT'
                                _kerneloffset = open(home+'\\Desktop\\CGT-Files\\4\\repack\\CGT_706cf6b230a6d77ee280a40b54246762_CGT').read().replace('\n', '')
                                _ramdiskoffset = open(home+'\\Desktop\\CGT-Files\\4\\repack\\CGT_0e16d6f83afe32911816ef683ad5d639_CGT').read().replace('\n', '')
                                _secondoffset = open(home+'\\Desktop\\CGT-Files\\4\\repack\\CGT_d753658059439ac8a93d411e68e5d66a_CGT').read().replace('\n', '')
                                _tagsoffset = open(home+'\\Desktop\\CGT-Files\\4\\repack\\CGT_a4d756b70ed4593b8d0f2abd01694f39_CGT').read().replace('\n', '')
                                _hash = open(home+'\\Desktop\\CGT-Files\\4\\repack\\CGT_0800fc577294c34e0b28ad2839435945_CGT').read().replace('\n', '')
                                _hash = '\"'+_hash+'\"'
                            if isfile(home+'\\Desktop\\CGT-Files\\4\\repack\\CGT_3017d911efceb27d1de6a92b70979795_CGT'):
                                system(repack._mkboot+' --kernel '+repack._kernel+' --ramdisk '+repack._ramdisk+' --cmdline '+repack._cmdline+' --base '+repack._base+' --pagesize '+repack._pagesize+' --dt '+repack._dt+' --kernel_offset '+repack._kerneloffset+' --ramdisk_offset '+repack._ramdiskoffset+' --second_offset '+repack._secondoffset+' --tags_offset '+repack._tagsoffset+' --hash '+repack._hash+' -o boot.img')
                            elif not isfile(home+'\\Desktop\\CGT-Files\\4\\repack\\CGT_3017d911efceb27d1de6a92b70979795_CGT'):
                                system(repack._mkboot+' --kernel '+repack._kernel+' --ramdisk '+repack._ramdisk+' --cmdline '+repack._cmdline+' --base '+repack._base+' --pagesize '+repack._pagesize+' --kernel_offset '+repack._kerneloffset+' --ramdisk_offset '+repack._ramdiskoffset+' --second_offset '+repack._secondoffset+' --tags_offset '+repack._tagsoffset+' --hash '+repack._hash+' -o boot.img')
                            sleep(1)
                            print(c.BLUE+'convert'+c.RED+' boot.img '+c.BLUE+'to'+c.RED+' CGT_SAM_BypassLockScreen_M1_CGT.tar '+c.BLUE + '.' + c.GREEN + '.' + c.RED + '.')
                            sleep(1)
                            print(c.END+c.BLUE+'remove ' + c.RED+'logs' + c.BLUE + ' .' + c.GREEN + '.' + c.RED + '.')
                            chdir(home+'\\Desktop\\')
                            rmtree(home + "\\Desktop\\CGT-Files\\4\\unpack")
                            rmtree(home + "\\Desktop\\CGT-Files\\4\\repack")
                            rmtree(home + "\\Desktop\\CGT-Files\\4\\repack_dependencies")
                            readme_unpack_write = '--- maked CGT_SAM_BypassLockScreen_M1_CGT.tar by CGT ---'+'\n\n'+'- Several tips ...'+'\n\t'+'1 : this method not delete data from the phone ...'+'\n\t'+'2 : this method only for samsung phones ...'+'\n\t' + '3 : original boot imported to CGT it should be equal current boot samsung phone ...'+'\n\t'+'4 : this method will not work if frp,oem,crom,reactivition is enabled ...' + '\n\t'+'5 : this method will not work in android version more than 8 ...'+'\n\t'+'6 : write CGT_SAM_BypassLockScreen_M1_CGT.tar in AP odin ...'+'\n\t'+'7 : after CGT_SAM_BypassLockScreen_M1_CGT.tar and bypass lock screen , backup all data and write again original boot to phone ...'+'\n\t'+'8 : if samsung phone after reboot stays on samsung logo write again original boot and This method does not work on your samsung phone ...'+'\n\n'+'- download odin : https://github.com/sys113/CGT-dependencies/raw/master/Odin3_v3.13.1.zip'+'\n\n'+'- download samsung phone driver : https://github.com/sys113/CGT-dependencies/raw/master/Samsung_USB_Driver_v1.5.60.0.zip'
                            readme_unpack = open(home + '\\Desktop\\CGT-Files\\4\\CGT.txt', 'w')
                            readme_unpack.write(readme_unpack_write)
                            readme_unpack.close()
                            sleep(1)
                            print(c.BLUE+'maked'+c.YELLOW+' CGT_SAM_BypassLockScreen_M1_CGT.tar '+c.BLUE+'in' + c.RED+' : '+c.GREEN+'CGT-Files'+c.YELLOW+'/'+c.RED+'4'+c.YELLOW+'/')
                            chdir(home)
                            startfile(realpath(home+'\\Desktop\\CGT-Files\\4\\'))
                            startfile(home+'\\Desktop\\CGT-Files\\4\\CGT.txt')
                        elif ramdisk_size.st_size == 0:
                            sleep(1)
                            print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'6' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                            error(6)
                            chdir(home)
                            print(c.BLUE+'remove'+c.RED+' logs '+c.BLUE+'and'+c.RED+' break '+c.BLUE+'.'+c.GREEN+'.'+c.RED+'.')
                            chdir(home)
                            try:
                                rmtree(home + "\\Desktop\\CGT-Files\\4\\")
                            except:
                                print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'25' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                error(25)
                            return
                    else:
                        print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'28' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                        error(28)
                elif (file_extension == '.md5') or (file_extension == '.tar'):
                    tar_file = TarFileOpen(file)
                    if ('boot.img' not in tar_file.getnames()) and ('boot.img.lz4' not in tar_file.getnames()):
                        print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'14' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                        error(14)
                    else:
                        if 'boot.img' in tar_file.getnames():
                            if isdir(home + "\\Desktop\\CGT-Files\\4\\"):
                                try:
                                    sleep(1)
                                    print(c.END+c.RED+'directory'+c.YELLOW+' 4 '+c.BLUE + 'already exists'+c.GREEN+' ; '+c.RED +'overwrite ' + c.BLUE + '.' + c.GREEN + '.' + c.RED + '.')
                                    rmtree(home + "\\Desktop\\CGT-Files\\4\\")
                                except:
                                    sleep(1)
                                    print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'25' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                    error(25)
                                    return
                            else:
                                print(c.RED+'making'+c.BLUE+' directory '+c.YELLOW+'4'+c.RED+' .'+c.GREEN+'.'+c.BLUE+'.')
                            system('mkdir '+home + '\\Desktop\\CGT-Files\\4\\')
                            chdir(home + '\\Desktop\\CGT-Files\\4\\')
                            sleep(1)
                            print(c.END+c.BLUE+'find'+c.RED+' boot.img'+c.BLUE+' in '+c.RED+basename(file)+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                            sleep(1)
                            print(c.END+c.BLUE+'extract'+c.RED+' boot.img '+c.BLUE+'from '+c.RED+basename(file)+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                            tar_file.extract('boot.img')
                            sleep(1)
                            print(c.END+c.BLUE + 'unpack ' + c.RED + 'boot.img' + c.BLUE + ' .' + c.GREEN + '.' + c.RED + '.')
                            system('mkdir '+home + '\\Desktop\\CGT-Files\\4\\repack_dependencies\\')
                            system(home+'\\.CGT\\programs\\unpackbootimg.exe' + ' -i ' + home+'\\Desktop\\CGT-Files\\4\\boot.img' + ' -o ' + home + '\\Desktop\\CGT-Files\\4\\repack_dependencies\\ > NUL')
                            rename(home+'\\Desktop\\CGT-Files\\4\\boot.img',home+'\\Desktop\\CGT-Files\\4\\stock_boot.img')
                            sleep(1)
                            print(c.END+c.BLUE + 'unpack'+c.RED+' ramdisk ' + c.BLUE + '.' + c.GREEN + '.' + c.RED + '.')
                            ramdisk_size = stat(home+'\\Desktop\\CGT-Files\\4\\repack_dependencies\\boot.img-ramdisk.gz')
                            if ramdisk_size.st_size != 0:
                                system('mkdir unpack')
                                chdir('unpack')
                                system(home+'\\.CGT\\programs\\gzip.exe -dcq '+home+'\\Desktop\\CGT-Files\\4\\repack_dependencies\\boot.img-ramdisk.gz | '+home+'\\.CGT\\programs\\cpio -i > NUL 2>&1')
                                sleep(1)
                                print(c.BLUE+'edit '+c.RED+'source'+c.BLUE+' to '+c.RED +'bypass lock screen'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                if not '# Do not place files or directories in /data/local/tmp' in open(home+'\\Desktop\\CGT-Files\\4\\unpack\\init.rc','r').read():
                                    sleep(1)
                                    print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'27' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                    error(27)
                                    sleep(1)
                                    print(c.BLUE+'remove'+c.RED+' logs '+c.BLUE+'and'+c.RED+' break '+c.BLUE+'.'+c.GREEN+'.'+c.RED+'.')
                                    chdir(home)
                                    try:
                                        rmtree(home + "\\Desktop\\CGT-Files\\4\\")
                                    except:
                                        print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'25' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                        error(25)
                                    return
                                with FileInput(home+'\\Desktop\\CGT-Files\\4\\unpack\\init.rc', inplace=True) as file:
                                    for line in file:
                                        print(line.replace('# Do not place files or directories in /data/local/tmp', '''
    # Do not place files or directories in /data/local/tmp

    # ---------- BYPASS SCREEN LOCK BY CGT ----------

    rm -f /data/system/locksettings.db 
    rm -f /data/system/locksettings.db-wal
    rm -f /data/system/locksettings.db-shm
    rm -f /data/system/gesture.key
    rm -f /data/system/password.key
    rm -f /data/system/signature.key
    rm -f /data/system/sparepassword.key
    rm /data/system/locksettings.db 
    rm /data/system/locksettings.db-wal
    rm /data/system/locksettings.db-shm
    rm /data/system/gesture.key
    rm /data/system/password.key
    rm /data/system/signature.key
    rm /data/system/sparepassword.key
    restorecon -R /data/system

    # ---------- BYPASS SCREEN LOCK BY CGT ----------
                        '''), end='')
                                sleep(1)
                                print(c.END + c.BLUE + 'packed'+c.RED+' ramdisk ' + c.BLUE+'to' +
                                      c.RED+' ramdisk.gz' + c.BLUE + ' .' + c.GREEN + '.' + c.RED + '.')
                                chdir(home+'\\Desktop\\CGT-Files\\4\\')
                                system(home+'\\.CGT\\programs\\mkbootfs.exe unpack | '+home+'\\.CGT\\programs\\minigzip.exe -c -9 > '+home+'\\Desktop\\CGT-Files\\4\\ramdisk.gz')
                                compress_repack_directory()
                                sleep(1)
                                print(c.END + c.BLUE + 'packed '+c.RED+'ramdisk.gz'+c.GREEN+' & '+c.RED+'another dependencies' +c.BLUE+' to '+c.RED + 'boot.img ' + c.BLUE + '.' + c.GREEN + '.' + c.RED + '.')
                                chdir(home + "\\Desktop\\CGT-Files\\4\\")
                                class repack:
                                    _mkboot = home+'\\.CGT\\programs\\mkbootimg.exe'
                                    _kernel = home+'/Desktop/CGT-Files/4/repack/CGT_50484c19f1afdaf3841a0d821ed393d2_CGT'
                                    _ramdisk = home+'/Desktop/CGT-Files/4/repack/CGT_5c5f44ab0550487fbce8a2874ebaab6a_CGT.gz'
                                    _cmdline = open(home+'/Desktop/CGT-Files/4/repack/CGT_95f44086bc13f782435dd6356310e7bd_CGT').read().replace('\n', '')
                                    _cmdline = '\"'+_cmdline+'\"'
                                    _base = open(home+'/Desktop/CGT-Files/4/repack/CGT_593616de15330c0fb2d55e55410bf994_CGT').read().replace('\n', '')
                                    _pagesize = open(home+'/Desktop/CGT-Files/4/repack/CGT_7525d528a3457f0227997c25239c4507_CGT').read().replace('\n', '')
                                    _dt = home+'/Desktop/CGT-Files/4/repack/CGT_3017d911efceb27d1de6a92b70979795_CGT'
                                    _kerneloffset = open(home+'/Desktop/CGT-Files/4/repack/CGT_706cf6b230a6d77ee280a40b54246762_CGT').read().replace('\n', '')
                                    _ramdiskoffset = open(home+'/Desktop/CGT-Files/4/repack/CGT_0e16d6f83afe32911816ef683ad5d639_CGT').read().replace('\n', '')
                                    _secondoffset = open(home+'/Desktop/CGT-Files/4/repack/CGT_d753658059439ac8a93d411e68e5d66a_CGT').read().replace('\n', '')
                                    _tagsoffset = open(home+'/Desktop/CGT-Files/4/repack/CGT_a4d756b70ed4593b8d0f2abd01694f39_CGT').read().replace('\n', '')
                                    _hash = open(home+'/Desktop/CGT-Files/4/repack/CGT_0800fc577294c34e0b28ad2839435945_CGT').read().replace('\n', '')
                                    _hash = '\"'+_hash+'\"'
                                if isfile(home+'\\Desktop\\CGT-Files\\4\\repack\\CGT_3017d911efceb27d1de6a92b70979795_CGT'):
                                    system(repack._mkboot+' --kernel '+repack._kernel+' --ramdisk '+repack._ramdisk+' --cmdline '+repack._cmdline+' --base '+repack._base+' --pagesize '+repack._pagesize+' --dt '+repack._dt+' --kernel_offset '+repack._kerneloffset+' --ramdisk_offset '+repack._ramdiskoffset+' --second_offset '+repack._secondoffset+' --tags_offset '+repack._tagsoffset+' --hash '+repack._hash+' -o boot.img')
                                elif not isfile(home+'\\Desktop\\CGT-Files\\4\\repack\\CGT_3017d911efceb27d1de6a92b70979795_CGT'):
                                    system(repack._mkboot+' --kernel '+repack._kernel+' --ramdisk '+repack._ramdisk+' --cmdline '+repack._cmdline+' --base '+repack._base+' --pagesize '+repack._pagesize+' --kernel_offset '+repack._kerneloffset+' --ramdisk_offset '+repack._ramdiskoffset+' --second_offset '+repack._secondoffset+' --tags_offset '+repack._tagsoffset+' --hash '+repack._hash+' -o boot.img')
                                sleep(1)
                                print(c.BLUE+'convert'+c.RED+' boot.img '+c.BLUE+'to'+c.RED+' CGT_SAM_BypassLockScreen_M1_CGT.tar '+c.BLUE + '.' + c.GREEN + '.' + c.RED + '.')
                                sleep(1)
                                print(c.END+c.BLUE+'remove ' + c.RED+'logs' + c.BLUE + ' .' + c.GREEN + '.' + c.RED + '.')
                                chdir(home+'\\Desktop\\')
                                rmtree(home + "\\Desktop\\CGT-Files\\4\\unpack")
                                rmtree(home + "\\Desktop\\CGT-Files\\4\\repack")
                                rmtree(home + "\\Desktop\\CGT-Files\\4\\repack_dependencies")
                                remove(home + "\\Desktop\\CGT-Files\\4\\stock_boot.img")
                                readme_unpack_write = '--- maked CGT_SAM_BypassLockScreen_M1_CGT.tar by CGT ---'+'\n\n'+'- Several tips ...'+'\n\t'+'1 : this method not delete data from the phone ...'+'\n\t'+'2 : this method only for samsung phones ...'+'\n\t' + '3 : original boot imported to CGT it should be equal current boot samsung phone ...'+'\n\t'+'4 : this method will not work if frp,oem,crom,reactivition is enabled ...' + '\n\t'+'5 : this method will not work in android version more than 8 ...'+'\n\t'+'6 : write CGT_SAM_BypassLockScreen_M1_CGT.tar in AP odin ...'+'\n\t'+'7 : after CGT_SAM_BypassLockScreen_M1_CGT.tar and bypass lock screen , backup all data and write again original boot to phone ...'+'\n\t'+'8 : if samsung phone after reboot stays on samsung logo write again original boot and This method does not work on your samsung phone ...'+'\n\n'+'- download odin : https://github.com/sys113/CGT-dependencies/raw/master/Odin3_v3.13.1.zip'+'\n\n'+'- download samsung phone driver : https://github.com/sys113/CGT-dependencies/raw/master/Samsung_USB_Driver_v1.5.60.0.zip'
                                readme_unpack = open(home + '\\Desktop\\CGT-Files\\4\\CGT.txt', 'w')
                                readme_unpack.write(readme_unpack_write)
                                readme_unpack.close()
                                sleep(1)
                                print(c.BLUE+'maked'+c.YELLOW+' CGT_SAM_BypassLockScreen_M1_CGT.tar '+c.BLUE+'in' + c.RED+' : '+c.GREEN+'CGT-Files'+c.YELLOW+'/'+c.RED+'4'+c.YELLOW+'/')
                                chdir(home)
                                startfile(realpath(home+'\\Desktop\\CGT-Files\\4\\'))
                                startfile(home+'\\Desktop\\CGT-Files\\4\\CGT.txt')
                            elif ramdisk_size.st_size == 0:
                                sleep(1)
                                print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'6' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                error(6)
                                sleep(1)
                                print(c.BLUE+'remove'+c.RED+' logs '+c.BLUE+'and'+c.RED+' break '+c.BLUE+'.'+c.GREEN+'.'+c.RED+'.')
                                chdir(home)
                                try:
                                    rmtree(home + "\\Desktop\\CGT-Files\\4\\")
                                except:
                                    print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'25' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                    error(25)
                                return
                        elif 'boot.img.lz4' in tar_file.getnames():
                            if isdir(home + "\\Desktop\\CGT-Files\\4\\"):
                                try:
                                    sleep(1)
                                    print(c.END+c.RED+'directory'+c.YELLOW+' 4 '+c.BLUE + 'already exists'+c.GREEN+' ; '+c.RED +'overwrite ' + c.BLUE + '.' + c.GREEN + '.' + c.RED + '.')
                                    rmtree(home + "\\Desktop\\CGT-Files\\4\\")
                                except:
                                    sleep(1)
                                    print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'25' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                    error(25)
                                    return
                            else:
                                print(c.RED+'making'+c.BLUE+' directory '+c.YELLOW+'4'+c.RED+' .'+c.GREEN+'.'+c.BLUE+'.')
                            system('mkdir '+home + '\\Desktop\\CGT-Files\\4\\')
                            chdir(home + '\\Desktop\\CGT-Files\\4\\')
                            sleep(1)
                            print(c.END+c.BLUE+'find'+c.RED+' boot.img.lz4'+c.BLUE+' in '+c.RED+basename(file)+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                            sleep(1)
                            print(c.END+c.BLUE+'extract'+c.RED+' boot.img.lz4 '+c.BLUE+'from '+c.RED+basename(file)+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                            tar_file.extract('boot.img.lz4')
                            sleep(1)
                            print(c.END+c.BLUE + 'conevert '+c.RED + 'boot.img.lz4' + c.BLUE + ' to ' +
                                c.RED + 'boot.img' + c.BLUE + ' .' + c.GREEN + '.' + c.RED + '.')
                            system(home +'\\.CGT\\programs\\lz4.exe -d boot.img.lz4')
                            img_lz4_size = stat(home+'\\Desktop\\CGT-Files\\4\\boot.img')
                            if img_lz4_size.st_size == 0:
                              sleep(1)
                              print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'4' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                              error(4)
                              sleep(1)
                              print(c.BLUE+'remove'+c.RED+' logs '+c.BLUE+'and'+c.RED+' break '+c.BLUE+'.'+c.GREEN+'.'+c.RED+'.')
                              chdir(home)
                              try:
                                rmtree(home + "\\Desktop\\CGT-Files\\4\\")
                              except:
                                print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'25' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                error(25)
                              return
                            sleep(1)
                            print(c.END+c.BLUE + 'unpack ' + c.RED + 'boot.img' + c.BLUE + ' .' + c.GREEN + '.' + c.RED + '.')
                            system('mkdir '+home + '\\Desktop\\CGT-Files\\4\\repack_dependencies\\')
                            system(home+'\\.CGT\\programs\\unpackbootimg.exe' + ' -i ' + home+'\\Desktop\\CGT-Files\\4\\boot.img' + ' -o ' + home + '\\Desktop\\CGT-Files\\4\\repack_dependencies\\ > NUL')
                            rename(home+'\\Desktop\\CGT-Files\\4\\boot.img',home+'\\Desktop\\CGT-Files\\4\\stock_boot.img')
                            sleep(1)
                            print(c.END+c.BLUE + 'unpack'+c.RED+' ramdisk ' + c.BLUE + '.' + c.GREEN + '.' + c.RED + '.')
                            try:
                                ramdisk_size = stat(home+'\\Desktop\\CGT-Files\\4\\repack_dependencies\\boot.img-ramdisk.gz')
                            except:
                                print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'8' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                error(8)
                                return
                            if ramdisk_size.st_size != 0:
                                system('mkdir unpack')
                                chdir('unpack')
                                system(home+'\\.CGT\\programs\\gzip.exe -dcq '+home+'\\Desktop\\CGT-Files\\4\\repack_dependencies\\boot.img-ramdisk.gz | '+home+'\\.CGT\\programs\\cpio -i > NUL 2>&1')
                                sleep(1)
                                print(c.BLUE+'edit '+c.RED+'source'+c.BLUE+' to '+c.RED +'bypass lock screen'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                if not '# Do not place files or directories in /data/local/tmp' in open(home+'\\Desktop\\CGT-Files\\4\\unpack\\init.rc','r').read():
                                    sleep(1)
                                    print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'27' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                    error(27)
                                    sleep(1)
                                    print(c.BLUE+'remove'+c.RED+' logs '+c.BLUE+'and'+c.RED+' break '+c.BLUE+'.'+c.GREEN+'.'+c.RED+'.')
                                    chdir(home)
                                    try:
                                        rmtree(home + "\\Desktop\\CGT-Files\\4\\")
                                    except:
                                        print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'25' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                        error(25)
                                    return
                                with FileInput(home+'\\Desktop\\CGT-Files\\4\\unpack\\init.rc', inplace=True) as file:
                                    for line in file:
                                        print(line.replace('# Do not place files or directories in /data/local/tmp', '''
    # Do not place files or directories in /data/local/tmp

    # ---------- BYPASS SCREEN LOCK BY CGT ----------

    rm -f /data/system/locksettings.db 
    rm -f /data/system/locksettings.db-wal
    rm -f /data/system/locksettings.db-shm
    rm -f /data/system/gesture.key
    rm -f /data/system/password.key
    rm -f /data/system/signature.key
    rm -f /data/system/sparepassword.key
    rm /data/system/locksettings.db 
    rm /data/system/locksettings.db-wal
    rm /data/system/locksettings.db-shm
    rm /data/system/gesture.key
    rm /data/system/password.key
    rm /data/system/signature.key
    rm /data/system/sparepassword.key
    restorecon -R /data/system

    # ---------- BYPASS SCREEN LOCK BY CGT ----------
                        '''), end='') 
                                sleep(1)
                                print(c.END + c.BLUE + 'packed'+c.RED+' ramdisk ' + c.BLUE+'to' +c.RED+' ramdisk.gz' + c.BLUE + ' .' + c.GREEN + '.' + c.RED + '.')
                                chdir(home+'\\Desktop\\CGT-Files\\4\\')
                                system(home+'\\.CGT\\programs\\mkbootfs.exe unpack | '+home+'\\.CGT\\programs\\minigzip.exe -c -9 > '+home+'\\Desktop\\CGT-Files\\4\\ramdisk.gz')
                                compress_repack_directory()
                                sleep(1)
                                print(c.END + c.BLUE + 'packed '+c.RED+'ramdisk.gz'+c.GREEN+' & '+c.RED+'another dependencies' +c.BLUE+' to '+c.RED + 'boot.img ' + c.BLUE + '.' + c.GREEN + '.' + c.RED + '.')
                                chdir(home + "\\Desktop\\CGT-Files\\4\\")
                                class repack:
                                    _mkboot = home+'\\.CGT\\programs\\mkbootimg.exe'
                                    _kernel = home+'/Desktop/CGT-Files/4/repack/CGT_50484c19f1afdaf3841a0d821ed393d2_CGT'
                                    _ramdisk = home+'/Desktop/CGT-Files/4/repack/CGT_5c5f44ab0550487fbce8a2874ebaab6a_CGT.gz'
                                    _cmdline = open(home+'/Desktop/CGT-Files/4/repack/CGT_95f44086bc13f782435dd6356310e7bd_CGT').read().replace('\n', '')
                                    _cmdline = '\"'+_cmdline+'\"'
                                    _base = open(home+'/Desktop/CGT-Files/4/repack/CGT_593616de15330c0fb2d55e55410bf994_CGT').read().replace('\n', '')
                                    _pagesize = open(home+'/Desktop/CGT-Files/4/repack/CGT_7525d528a3457f0227997c25239c4507_CGT').read().replace('\n', '')
                                    _dt = home+'/Desktop/CGT-Files/4/repack/CGT_3017d911efceb27d1de6a92b70979795_CGT'
                                    _kerneloffset = open(home+'/Desktop/CGT-Files/4/repack/CGT_706cf6b230a6d77ee280a40b54246762_CGT').read().replace('\n', '')
                                    _ramdiskoffset = open(home+'/Desktop/CGT-Files/4/repack/CGT_0e16d6f83afe32911816ef683ad5d639_CGT').read().replace('\n', '')
                                    _secondoffset = open(home+'/Desktop/CGT-Files/4/repack/CGT_d753658059439ac8a93d411e68e5d66a_CGT').read().replace('\n', '')
                                    _tagsoffset = open(home+'/Desktop/CGT-Files/4/repack/CGT_a4d756b70ed4593b8d0f2abd01694f39_CGT').read().replace('\n', '')
                                    _hash = open(home+'/Desktop/CGT-Files/4/repack/CGT_0800fc577294c34e0b28ad2839435945_CGT').read().replace('\n', '')
                                    _hash = '\"'+_hash+'\"'
                                if isfile(home+'\\Desktop\\CGT-Files\\4\\repack\\CGT_3017d911efceb27d1de6a92b70979795_CGT'):
                                    system(repack._mkboot+' --kernel '+repack._kernel+' --ramdisk '+repack._ramdisk+' --cmdline '+repack._cmdline+' --base '+repack._base+' --pagesize '+repack._pagesize+' --dt '+repack._dt+' --kernel_offset '+repack._kerneloffset+' --ramdisk_offset '+repack._ramdiskoffset+' --second_offset '+repack._secondoffset+' --tags_offset '+repack._tagsoffset+' --hash '+repack._hash+' -o boot.img')
                                elif not isfile(home+'\\Desktop\\CGT-Files\\4\\repack\\CGT_3017d911efceb27d1de6a92b70979795_CGT'):
                                    system(repack._mkboot+' --kernel '+repack._kernel+' --ramdisk '+repack._ramdisk+' --cmdline '+repack._cmdline+' --base '+repack._base+' --pagesize '+repack._pagesize+' --kernel_offset '+repack._kerneloffset+' --ramdisk_offset '+repack._ramdiskoffset+' --second_offset '+repack._secondoffset+' --tags_offset '+repack._tagsoffset+' --hash '+repack._hash+' -o boot.img')
                                sleep(1)
                                print(c.BLUE+'convert'+c.RED+' boot.img '+c.BLUE+'to'+c.RED+' CGT_SAM_BypassLockScreen_M1_CGT.tar '+c.BLUE + '.' + c.GREEN + '.' + c.RED + '.')
                                sleep(1)
                                print(c.END+c.BLUE+'remove ' + c.RED+'logs' + c.BLUE + ' .' + c.GREEN + '.' + c.RED + '.')
                                chdir(home+'\\Desktop\\')
                                rmtree(home + "\\Desktop\\CGT-Files\\4\\unpack")
                                rmtree(home + "\\Desktop\\CGT-Files\\4\\repack")
                                rmtree(home + "\\Desktop\\CGT-Files\\4\\repack_dependencies\\")
                                remove(home + "\\Desktop\\CGT-Files\\4\\stock_boot.img")
                                remove(home + "\\Desktop\\CGT-Files\\4\\boot.img.lz4")
                                readme_unpack_write = '--- maked CGT_SAM_BypassLockScreen_M1_CGT.tar by CGT ---'+'\n\n'+'- Several tips ...'+'\n\t'+'1 : this method not delete data from the phone ...'+'\n\t'+'2 : this method only for samsung phones ...'+'\n\t' + '3 : original boot imported to CGT it should be equal current boot samsung phone ...'+'\n\t'+'4 : this method will not work if frp,oem,crom,reactivition is enabled ...' + '\n\t'+'5 : this method will not work in android version more than 8 ...'+'\n\t'+'6 : write CGT_SAM_BypassLockScreen_M1_CGT.tar in AP odin ...'+'\n\t'+'7 : after CGT_SAM_BypassLockScreen_M1_CGT.tar and bypass lock screen , backup all data and write again original boot to phone ...'+'\n\t'+'8 : if samsung phone after reboot stays on samsung logo write again original boot and This method does not work on your samsung phone ...'+'\n\n'+'- download odin : https://github.com/sys113/CGT-dependencies/raw/master/Odin3_v3.13.1.zip'+'\n\n'+'- download samsung phone driver : https://github.com/sys113/CGT-dependencies/raw/master/Samsung_USB_Driver_v1.5.60.0.zip'
                                readme_unpack = open(home + '\\Desktop\\CGT-Files\\4\\CGT.txt', 'w')
                                readme_unpack.write(readme_unpack_write)
                                readme_unpack.close()
                                sleep(1)
                                print(c.BLUE+'maked'+c.YELLOW+' CGT_SAM_BypassLockScreen_M1_CGT.tar '+c.BLUE+'in' + c.RED+' : '+c.GREEN+'CGT-Files'+c.YELLOW+'/'+c.RED+'4'+c.YELLOW+'/')
                                chdir(home)
                                startfile(realpath(home+'\\Desktop\\CGT-Files\\4\\'))
                                startfile(home+'\\Desktop\\CGT-Files\\4\\CGT.txt')
                                chdir(home+'\\Desktop\\')
                            elif ramdisk_size.st_size == 0:
                                        print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'6' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                        error(6)
                                        print(c.BLUE+'ramove'+c.RED+' logs '+c.BLUE+'and'+c.RED+' break '+c.BLUE+'.'+c.GREEN+'.'+c.RED+'.')
                                        chdir(home)
                                        try:
                                            rmtree(home + "\\Desktop\\CGT-Files\\4\\")
                                        except:
                                            print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'25' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                                            error(25)
                                        return
                else:
                    print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'15' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                    error(15)
            elif exists(file) == False:
                print(c.END + c.RED + 'error' + c.GREEN+' : ' + c.BLUE + 'code '+c.YELLOW+'1' + c.GREEN+' | '+c.BLUE+'please see '+c.RED+'CGT-Files/EN-ErrorList.png'+c.BLUE+' .'+c.GREEN+'.'+c.RED+'.')
                error(1)
        if exists(home+"\\Desktop\\CGT-Files\\4\\boot.img"):
            chdir(home+"\\Desktop\\CGT-Files\\4\\")
            with TarFileOpen("CGT_SAM_BypassLockScreen_M1_CGT.tar", "w") as tar:
                tar.add('boot.img')
            remove(home+'\\Desktop\\CGT-Files\\4\\boot.img')
            chdir(home+'\\Desktop\\')
def if_4():
    if os_type().upper() == 'WINDOWS':
        window()
    elif os_type().upper() == 'LINUX':
        linux()
    else:
        pass
