# Routeros脚本(ipv4)

    /tool fetch url=https://raw.githubusercontent.com/chengge9527/Mikrotik-CN/refs/heads/main/cn_ip_list/CN
    /system logging disable 0
    /import file-name=CN
    /system logging enable 0
    /file remove [find name="CN"]
    :local CN [:len [/ip firewall address-list find list="CN"]]
    :log info ("CN List Update:"."$CN"."Rules")
