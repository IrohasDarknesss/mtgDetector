import os
import shutil
import glob
import random

card_name_list = ['AncestralRecall', 'TimeWalk', 'TimeTwister', 'BlackRotus', 'MoxEmerald',
'MoxRuby', 'MoxSapphire', 'MoxJet', 'MoxPerl']

def sep_train_and_test(spl, names):
    for name in names:
        try:
            os.makedirs('./dataset/test/{}'.format(name))
        except:
            pass

        train_path_list = glob.glob('./dataset/train/{}/*'.format(name))

        list_len = len(train_path_list)
        sep = int(list_len*spl)
        rand = random.sample(train_path_list, list_len)
        train_list = rand[:sep]
        test_list  = rand[sep:]

        test_path_list = './dataset/test/{}/'

        print(test_path_list.format(name))
        print(len(train_path_list))
        print(len(train_list))
        print(len(test_list))
        
        # for test_path in test_list:
        #     shutil.move(test_path, test_path_list.format(name)+os.path.basename(test_path))
        # return [train_list, test_list]

def create_path_list(path):
    for name in path:
        train_names = name + '_train_list'
        test_names = name + '_test_list'
        return train_names, test_names

if __name__ == '__main__':
    path_name = create_path_list(card_name_list)
    train_and_test_list  = sep_train_and_test(0.7,card_name_list)