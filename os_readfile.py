import os
import shutil
# 指定要查詢的路徑
Path = r'E:\car_pic\HOT_image'
# 列出指定路徑底下所有檔案(包含資料夾)
fileList = os.listdir(Path)
# 逐一查詢檔案清單
for file in fileList:
    #   這邊也可以視情況，做檔案的操作(複製、讀取...等)
    #   使用isdir檢查是否為目錄
    #   使用join的方式把路徑與檔案名稱串起來(等同filePath+fileName)
    if os.path.isdir(os.path.join(Path ,file)):
        print("directory: " + file)
    #   使用isfile判斷是否為檔案
    elif os.path.isfile(Path + file):
        print(file)
    else:
        print('ERROR!')

# 如果不存在該資料夾，建新資料夾
os.makedirs(r"E:\car_pic\hot_all",exist_ok=True)
Path_2 = r"E:\car_pic\hot_all"
# os.listdir將指定路徑底下當前的目錄和檔案列出來
# os.walk將指定路徑底下所有目錄和檔案列出來(包含子目錄以及子目錄底下的檔案)
allList = os.walk(Path)
# 列出所有子目錄與子目錄底下所有的檔案
for root, dirs, files in allList:
    # 列出目前讀取到的路徑
    # print("path：", root)
    # 列出在這個路徑下讀取到的資料夾(第一層讀完才會讀第二層)
    # print("directory：", dirs)
    # 列出在這個路徑下讀取到的所有檔案
    # print("file：", files)

    for i in files:
        # 複製所有檔案到新路徑Path_2
        shutil.copy(root+"\\"+i,Path_2)



