import os

card_name_list = ['AncestralRecall', 'TimeWalk', 'TimeTwister', 'BlackRotus', 'MoxEmerald',
'MoxRuby', 'MoxSapphire', 'MoxJet', 'MoxPerl']

train_path = ('./train/')
test_path = ('./test/')
noize = 'null'

def create_train_path(jum,path):
    for name in card_name_list:
        # print(name)
        if not os.path.exists(jum):
            os.makedirs(path+name)
        else:
            print('Already exists!!!!')


def create_test_path(jum, path):
    for name in card_name_list:
        # print(name)
        if not os.path.exists(jum):
            os.makedirs(path+name)
        else:
            print('Already exists!!!!')


if __name__ == '__main__':
    create_train_path(noize,train_path)
    create_test_path(noize,test_path)