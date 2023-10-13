import ipaddress

# 输入CIDR表示的子网
cidr_input = input("请输入CIDR表示的子网地址（例如，10.219.1.1/16）： ")

try:
    network = ipaddress.IPv4Network(cidr_input, strict=False)
except ipaddress.AddressValueError as e:
    print("无效的CIDR表示：", e)
except ValueError as e:
    print("无效的CIDR表示：", e)
else:
    # 生成IP地址列表
    ip_list = [str(ip) for ip in network.hosts()]

    # 将IP地址保存到文本文件
    filename = "ip_addresses.txt"
    with open(filename, 'w') as file:
        file.write("\n".join(ip_list))

    print(f"已将IP地址保存到 {filename} 文件中。")
