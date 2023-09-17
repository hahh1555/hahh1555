#读取文件---删除标点符号---分词---函数计算---输出
import os
import jieba
import gensim
import re
from time import * #引入时间库




#获取指定路径的文件内容
def get_message(path):
    str=''
    f=open(path,'r',encoding='UTF-8')
    line=f.readline()
    while line:
        str=str+line
        line=f.read()
    f.close()
    return str

#使用正则运算过滤特殊字符，再使用结巴分词
def j_file(str):
    #过滤特殊符号
    str=re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])", "", str)
    #结巴分词
    result=jieba.lcut(str)
    return result

# 计算余弦相似度
def calc_similarity(text1, text2):
    texts = [text1, text2]
    dictionary = gensim.corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]
    similarity = gensim.similarities.Similarity('-Similarity-index', corpus, num_features=len(dictionary))
    test_corpus_1 = dictionary.doc2bow(text1)
    cosine_sim = similarity[test_corpus_1][1]
    return cosine_sim

#主函数
def main(path1,path2):
    #开始
    startT=time()
    #保存输出结果文件的绝对路径
    #save_path='D:/python/_text/result.txt'
    str1=get_message(path1)
    str2=get_message(path2)
    t1=j_file(str1)
    t2=j_file(str2)
    similarity=calc_similarity(t1,t2)
    # 结束
    endT = time()
    print('文章重复率为：%.2f' %similarity)
    print("time=%.2g 秒" % (endT - startT))
        # 将结果写入指定文件
    f = open('save.txt', 'w', encoding="utf-8")
    f.write('文章重复率为：%.2f' %similarity)
    f.write('\n')
    f.write("time=%.2g 秒" % (endT - startT))
    f.close()


if __name__ == '__main__':
    #输入原文文件的绝对路径
    path1="D:\python\_text\orig.txt"
    #输入抄袭文件的绝对路径
    path2="D:\python\_text\orig_0.8_add.txt"

    if not os.path.exists(path1):
        print("原文文件不存在！")
        exit()
    if not os.path.exists(path2):
         print("抄袭文件不存在！")
         exit()
    #执行
    main(path1,path2)










