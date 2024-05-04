# Pasaj üzerinden sipariş detaylarını aldık.
import orderData
orders = orderData.data


# chatbotun devreye girdiği kısım bu kısım

def control(request):
    # bu kısımda chatbot un yapay zeka ile istenilen bilgiyi doğru analiz etmesini sağlayacağız
    response = ""

    if ('nerde' in request) or ('konum' in request) or ('detay' in request) or ('sipar' in request) or ('bilgi' in request) or ('nerede' in request)  :
        
        for order in orders:
            if   str(order["name"]).lower() in request:

                if str(order["cargoStatu"]) == "Teslim Edildi":
                    response += f'{order["name"]} siparişiniz {order["price"]} tutarında {order["deliveryDate"]} tarihinde {order["cargoName"]} tarafından teslim edilmiştir \n'
                else:
                    response +=(f'{order["name"]} siparişiniz durumu {order["cargoStatu"]} olaran görünmektedir. {order["cargoName"]} tarafından {order["deliveryDate"]} tarihinde sizlere iletilecektir \n')
        

    

    elif ('ulaşmadı' in request) or ('gelmedi' in request) or ('varmadı' in request):
        for order in orders:
            if  str(order["name"]).lower() in request:
                if  str(order["cargoStatu"]) == "Teslim Edildi":
                    response += ("Teknik bir hata oluştu ürününüzü tekrar yolluyoruz. Anlayışınız için teşekkür ederiz")
                else:
                    response += (f'{order["name"]} siparişinşz şu anda {order["cargoStatu"]} durumundadır. ürününüz {order["deliveryDate"]} tarihinde teslim edilecektir')
    else:
        response = 'Ne söylediğini anlayamadım. Tekrar Eder misin'     

        
    
        
    return response

while True:

    request = input(str("Size Nasıl Yardımcı Olabilirim ? (Çıkmak İçin Q yazınız)=  "))
    if request.lower() == 'q':
        print("programdan çıkılıyor")
        break
    print(control(request.lower()))




