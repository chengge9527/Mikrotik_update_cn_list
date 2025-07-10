import requests
import os

def main():
    # 目标URL
    url = "https://www.iwik.org/ipcountry/mikrotik/CN"
    
    try:
        # 下载IP列表
        response = requests.get(url)
        response.raise_for_status()  # 检查HTTP错误
        
        # 创建输出目录
        os.makedirs("cn_ip_list", exist_ok=True)
        
        # 保存为固定文件名 CN
        with open("cn_ip_list/CN", "w") as f:
            f.write(response.text)
        
        print("成功保存中国IP列表到 CN")
        
    except Exception as e:
        print(f"错误: {e}")
        exit(1)

if __name__ == "__main__":
    main()
