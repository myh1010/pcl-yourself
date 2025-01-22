import nbtlib
import os
import zlib
import io
import sys

def read_servers_dat(filepath):
    try:
        nbt_file = nbtlib.load(filepath, gzipped=False)

        # 存储解析结果的列表
        servers_list = []

        if 'servers' in nbt_file:
            servers = nbt_file['servers']
            #print(f"共找到 {len(servers)} 个服务器：")
            for i, server in enumerate(servers):
                name = server.get('name', 'N/A')
                ip = server.get('ip', 'N/A')
                servers_list.append(f"{name};{ip}")
        else:
            servers_list.append("未找到服务器列表。")

        return servers_list

    except Exception as e:
        print(f"读取文件时出错: {e}")
        print("尝试作为gzip压缩文件读取")
        try:
            with open(filepath, 'rb') as f:
                compressed_data = f.read()
            decompressed_data = zlib.decompress(compressed_data)
            nbt_file = nbtlib.File.load(fileobj=io.BytesIO(decompressed_data), gzipped=False)
            # 存储解析结果的列表
            servers_list = []

            if 'servers' in nbt_file:
                servers = nbt_file['servers']
                #print(f"共找到 {len(servers)} 个服务器：")
                for i, server in enumerate(servers):
                    name = server.get('name', 'N/A')
                    ip = server.get('ip', 'N/A')
                    servers_list.append(f"{name};{ip}")
            else:
                servers_list.append("未找到服务器列表。")

            return servers_list
        except Exception as e:
            print(f"作为gzip压缩文件读取失败: {e}")

if __name__ == "__main__":
    # 检查是否提供了 filepath 参数


    filepath = "../.minecraft/servers.dat"
    # 调用 read_servers_dat 函数并获取返回的服务器列表
    servers_list = read_servers_dat(filepath)

    # 打印服务器列表，每个服务器信息占一行
    ft = open("servers.txt","w+")
    a=0
    for server_info in servers_list:
        ft.write(server_info)
        ft.write('\n')
    ft.close()
