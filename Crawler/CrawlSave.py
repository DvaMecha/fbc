import os
import Model.MainModel
import time

model = Model.MainModel.MainModel.GetInstance()


def saveData():
    if "odds500" in model['getData']:
        saveFile(model.getData['odds500'])
        model.view["main"].outPutText(model.datamodel['info']['output'])
    else:
        model.view["main"].outPutText(model.datamodel['info']['nodata'], True)


def saveFile(self,d):
    s = str(d)
    time_str = time.strftime("%H-%M-%S", time.localtime())
    cur_dir = 'output'
    folder_name = time.strftime("%Y-%m-%d", time.localtime())
    folder_path = ''
    if os.path.isdir(cur_dir):
        folder_path = os.path.join(cur_dir, folder_name)
        if not os.path.isdir(folder_path):
            os.mkdir(folder_path)

    save_path = os.path.join(folder_path, 'webout' + time_str + '.txt')
    f_obj = open(save_path, 'w', encoding='utf-8')
    f_obj.write(s)
    f_obj.close()