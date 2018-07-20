#-*-coding:utf-8-*-

from __future__ import absolute_import
import nginx
import os
from pubstatus.models import instance

CONFIG_PATHS_TEST = [
    ""
]

GIT_PATH_TEST = ''


def _get_upstreams(config_file):
    c = nginx.loadf(config_file)
    servers = []
    for upstream in c.filter('Upstream'):
        servers += [key.as_dict["server"].split(' ')[0]
                    for key in upstream.keys if key.as_dict.has_key("server")]
    for location in c.filter('Server')[0].locations:
        if location.keys[0].as_dict.has_key("proxy_pass"):
            if len(location.keys[0].as_dict["proxy_pass"].split("://")[1].split(":"))==2:
                temp = location.keys[0].as_dict["proxy_pass"].split("://")[1]
                if location.keys[0].as_dict["proxy_pass"].split("://")[1][-1]=="/":
                    temp = temp[:-1]
                servers.append(temp)
    return servers


def _get_server_name(config_file):
    c = nginx.loadf(config_file)
    return filter(lambda x: x.as_dict.has_key('server_name'), c.filter('Server')[0].keys)[0].as_dict['server_name']


def _delete_remove_instance():
    '''
    当instance实例的env_flag环境设置为custom自定义时，将不会nginx检测自动删除
    '''
    files = _get_all_files()
    file_instances = []
    for file in files:
        server_name = _get_server_name(file)
        servers = _get_upstreams(file)
        for server in servers:
            file_instances.append(server_name+":"+server)
    obj_instances = [(i.server_name+":"+i.host+":"+str(i.port))
                     for i in instance.objects.filter(env_flag="test")]
    remove_instances = set(obj_instances)-set(file_instances)
    for ri in remove_instances:
       obj = instance.objects.get(server_name=ri.split(
           ":")[0], host=ri.split(":")[1], port=int(ri.split(":")[2]), env_flag="test")
       obj.delete()
    return True


def _get_all_files():
    files = []
    for config_path in CONFIG_PATHS_TEST:
        files += map(lambda x: config_path+x, os.listdir(config_path))
    return filter(lambda x: x.endswith(".conf"), files)


def _regedit_config_to_database(config_file):
    try:
        server_name = _get_server_name(config_file)
        servers = _get_upstreams(config_file)
        if len(server_name)<60:
            for server in servers:
                instance.objects.get_or_create(server_name=server_name, host=server.split(":")[
                                               0], port=server.split(":")[1], env_flag="test")
            return True
        return False
    except Exception as e:
        return str(e)


def git_pull_test():
    try:
        os.system("cd "+GIT_PATH_TEST+"&& git pull")
        return True
    except Exception as e:
        return str(e)


def main_pipeline_test():
    try:
        files = _get_all_files()
        _delete_remove_instance()
        for file in files:
            _regedit_config_to_database(file)
        return True
    except Exception as e:
        return str(e)


if __name__ == "__main__":
    # print _get_upstreams(
    #     '')
    # print _get_server_name(
    #     '')
    main_pipeline_test()
