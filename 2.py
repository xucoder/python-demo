import urllib
import urllib.request

def get_image(url):
    #request=urllib.request.Request(url)  #构建请求
    get_img=urllib.request.urlopen(url).read()
    with open('001.jpg','wb') as fp:
        fp.write(get_img)
    print('图片下载完成')
    return 

url='https://pic4.zhimg.com/80/v2-e516a4bbed23b80e54ea52bc4a49fd42_hd.jpg'
get_image(url)

#url(https://iknowpc.bdimg.com/static/common/pkg/common_z.48bf107.png)