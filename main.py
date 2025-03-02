from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta

integras_xpath = "//yt-formatted-string[@id='video-title' and contains(text(), 'Assista à íntegra do Jornal da Record') ]"

driver = Chrome()
driver.get("https://www.youtube.com/@JornaldaRecord/videos")
integras_titulos = driver.find_elements(By.XPATH, integras_xpath)
print(integras_titulos)

data_atual = datetime.now().strftime("%d/%m/%Y")
ontem = (datetime.now() - timedelta(days=1)).strftime("%d/%m/%Y")

for titulo in integras_titulos:
    data = titulo.text.split(" | ")[1]
    if data == data_atual or data == ontem:
        tempo_lancamento = titulo.find_elements(By.XPATH, "../../..//span[@class='inline-metadata-item style-scope ytd-video-meta-block']")[1]
        numero_tempo, tipo_tempo = tempo_lancamento.text.split(" ")[1:]
        if tipo_tempo == "minutos" and int(numero_tempo) <= 30:
            print("Enviando notificação")
