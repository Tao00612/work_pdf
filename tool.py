import hashlib
import os


def md5(src):
    m2 = hashlib.md5()
    m2.update(src.encode('utf-8'))
    return m2.hexdigest()


def func(path):
    s1 = ''
    with open(path, 'rb') as f:
        for j in f:
            s1 += str(j)
    obj = md5(s1)
    return obj


def main():
    d_file = []
    for i in range(1, 436):
        try:
            path = f'基美/{i}.pdf'
            obj = func(path)
            if obj in d_file:
                print('正在删除')
                os.remove(path)
            else:
                d_file.append(obj)
        except FileNotFoundError:
            print('无此文件')


if __name__ == '__main__':
    main()

