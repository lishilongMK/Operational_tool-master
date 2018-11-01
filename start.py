#/usr/bin/python
#-*- coding:utf-8 -*-


import os
import sys;sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from lib.create_html import creat_html_v2
from lib.from_zabbixv2 import  GetImages
from lib.create_word import creat_w
import configparser

filter_dict = {
                "key_":["vm.memory.size[available]",
                        "system.cpu.util[,user]",
                        "vfs.fs.size[/,free]",
                        "vfs.fs.size[/,total]",]
                }





def main(stime, filter_dic={}):

    #初始化配置
    Bash_Dir = os.path.dirname(os.path.abspath(__file__))
    config_file = '%s%s%s%s%s' % (Bash_Dir, os.sep, 'config', os.sep, 'project_config.cfg')
    images_dir = '%s%s%s' % (Bash_Dir, os.sep, 'images')
    pro_hostname_dir = '%s%s%s' % (Bash_Dir, os.sep, 'project_host')
    config = configparser.RawConfigParser()
    config.read(config_file)
    # pro_list = ['womai','feihe','carrefour','beiguo','songshu']
    pro_list = ['beiguo']
    stime = '20180501'
    for pro_iterm in pro_list:
        host = config.get(pro_iterm, 'host')
        images_path = '%s%s%s' % (images_dir, os.sep,config.get(pro_iterm, 'images_path'))
        user = config.get(pro_iterm, 'user')
        password = str(config.get(pro_iterm, 'password'))
        hostname_path = '%s%s%s' % (pro_hostname_dir, os.sep, config.get(pro_iterm, 'hostname_path'))
        get_images = GetImages(host, images_path, user, password, stime, hostname_path)

        #获取host iterm number
        get_images.list_graphsid()



        #获取get host iterm graphs
        # server_iterm = get_images.get_graphs()


        #获取趋势数据的ID，get itemid list
        get_images.list_itermsid(filter_dic)


        #获取趋势数据
        # if pro_iterm == 'songshu' or pro_iterm == 'womai':
        #     trends_d = get_images.get_table_data()
        # else:
        #     trends_d = {}


        #创建文件
        # creat_w(pro_iterm, Bash_Dir,server_iterm, trends_d)
        # if pro_iterm == 'beiguo' or pro_iterm == 'carrefour':
        #    creat_html_v2(pro_iterm, server_iterm)

if __name__ == '__main__':
    stime = '20180201'
    main(stime)