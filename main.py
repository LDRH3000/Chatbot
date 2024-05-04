# Pasaj üzerinden sipariş detaylarını aldık.
import orderData
orders = orderData.data


# chatbotun devreye girdiği kısım bu kısım

def control(request):
    # bu kısımda chatbot un yapay zeka ile istenilen bilgiyi doğru analiz etmesini sağlayacağız

    if ('nerde' in request) or ('konum' in request) or ('detay' in request) or ('sipar' in request) or ('bilgi' in request) or ('nerede' in request)  :
        x =0
        response = ""
        for order in orders:
            if   str(order["name"]).lower() in request:
                x += 1

                if str(order["cargoStatu"]) == "Teslim Edildi":
                    response += f'{order["name"]} siparişiniz {order["price"]} tutarında {order["deliveryDate"]} tarihinde {order["cargoName"]} tarafından teslim edilmiştir \n'
                else:
                    response +=(f'{order["name"]} siparişiniz durumu {order["cargoStatu"]} olaran görünmektedir. {order["cargoName"]} tarafından {order["deliveryDate"]} tarihinde sizlere iletilecektir \n')
        
        return response
    else:
        return "Ne söylediğini anlayamadım. Tekrar Eder misin"
    

while True:

    request = input(str("Size Nasıl Yardımcı Olabilirim ? (Çıkmak İçin Q yazınız)=  "))
    if request.lower() == 'q':
        print("programdan çıkılıyor")
        break
    print(control(request.lower()))




