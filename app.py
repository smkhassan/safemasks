from safe_masks_crawler import alibaba_module
from safe_masks_transformer import azure_storage_table

##Global Variables

url_test_local = 'https://www.alibaba.com/product-detail/5Layers-Multifunctional-Face-Masks-KN95-Respirator_62532136916.html?spm=a2700.galleryofferlist.0.0.125c66d3DbeLJk&s=p'


# flag = True
# while flag:
alibaba_product = alibaba_module.crawler.crawl(url_test_local)
azure_storage_table.Storage.WriteToStorage(products=alibaba_product)



