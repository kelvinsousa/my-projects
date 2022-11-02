from pathlib import Path
import os

path = 'C:\\Users\\kelvin.sousa\\downloads'
path_join = 'C:\\Users\\kelvin.sousa\\downloads\\'

folder_names = {
    
    'Excel':{'xlsx','csv'},
    'PDF':{'pdf'},
    'Docs': {'txt','tex','doc','docx','ppt','pptx'},
    'Ebooks': {'mobi', 'epub'},
    'Images': {'bmp','gif ico','jpeg','jpg','png','jfif','svg','tif','tiff'},
    'Softwares':{'apk','bat','bin', 'exe','jar','msi','py'},
    'Videos':{'3gp','avi','flv','h264','mkv','mov','mp4','mpg','mpeg','wmv'},
    'Zip':{'zip','gz','rar','rar','tgz','z'},
    'Others': {'NONE'},
    'Folders':{'NONE'}
}
if os.path.exists(path):

    dir_archives = list()
    only_files = list()
    only_folders = list()
        
    for i in os.listdir(path):
        dir_archives.append(os.path.join(path, i))
    
    for i in dir_archives:
        try:
            if os.path.isfile(i):
                only_files.append(i)
            else:
                only_folders.append(i)
                    
        except ValueError as e:
            print(e)
            print('Algo deu errado..')
                
        except:
            pass
        
    # mapeando as extenções, estamos criando um novo dicionario com a chave extension recebendo o value filetype. Esse dict está sendo criando por um laço for no dicionario folder_names que criamos na mão:
        
    extension_filetype_map = {
        extension: fileType 
        
        for fileType, extensions in folder_names.items() 
                for extension in extensions 
    }
    
    # Criando os caminhos das novas pastas
    folder_paths = [
        
        os.path.join(path_join, i)
        for i in folder_names.keys()           
        ]
            
    # [os.mkdir(folderPath) 
    #     for folderPath in folder_paths if not os.path.exists(folderPath)]
    
    # Criando as pastas apenas se as mesmas não existir:
    for folder in folder_paths:
        if not os.path.exists(folder):
            os.mkdir(folder)

    #outra forma de fazer o loop for:
    # [os.mkdir(folder) << criando dir da variável folder que vai ser uma iteração na lista abaixo se não existir
    # for folder in folder_paths if not os.path.exists(folderPath)]
    
    def new_path(old_path):
        
        extension = str(old_path).split('.')[-1]
        amplified_folder = extension_filetype_map[extension] if extension in extension_filetype_map.keys() else 'Others'
        final_path = os.path.join(path,amplified_folder, str(old_path).split('\\')[-1])
        
        return final_path
    
    
    # Movendo os arquivos para os novos diretorios iterando os arquivos por um loop na lista.
    try:
        # [Path(eachfile).rename(new_path(eachfile)) for eachfile in only_files] #other way to do loop above:

        for anyfile in only_files:
            Path(anyfile).rename(new_path(anyfile))
        
    except ValueError as e:
        print(e)
        print('Something went wrong with files..')
        
    except FileExistsError as e:
        print(e)
        print('The destination has a file with a same name!')
        
    except:
        print('No mapped error!')
        
    try:
        [Path(onlyfolder).rename(os.path.join(path,'Folders', str(onlyfolder).split('\\')[-1])) 
            for onlyfolder in only_folders 
                    if str(onlyfolder).split('\\')[-1] not in folder_names.keys()]
    except ValueError as e:
        print(e)
        print('Something went wrong with folders')
        
    except FileExistsError as e:
        print(e)
        print('The destination has a file with a same name!')
        
    except:
        print('No mapped error!')        
        
else:
    ('Path does not exist.')