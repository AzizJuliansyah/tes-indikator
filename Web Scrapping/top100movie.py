import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/"

response = requests.get(url)

if response.status_code == 200:
    print("Permintaan berhasil (Status 200 OK)")
    soup = BeautifulSoup(response.text, "lxml")

    body = soup.find("body")
    div = soup.find("div", id="__next")
    div1 = soup.find("main", class_="ipc-page-wrapper ipc-page-wrapper--baseAlt")
    div2 = soup.find("div", class_="ipc-page-content-container ipc-page-content-container--center sc-383f2ac5-0 bfcGjo")
    div3 = soup.find("div", class_="ipc-page-content-container ipc-page-content-container--center")
    div4 = soup.find("section", class_="ipc-page-background ipc-page-background--base sc-29b01cb5-0 gmWwif")
    div5 = soup.find("div", class_="chart-layout-parent")
    div6 = soup.find("div", class_="ipc-page-grid ipc-page-grid--bias-left")
    div7 = soup.find("div", class_="sc-29b01cb5-3 dSNKnk ipc-page-grid__item ipc-page-grid__item--span-2")

    if body and div and div1 and div2 and div3 and div4 and div5 and div6 and div7:
        lister_list = div1.find("ul", class_="ipc-metadata-list ipc-metadata-list--dividers-between sc-9d2f6de0-0 ckQYbL compact-list-view ipc-metadata-list--base")

        if lister_list:
            movie_items = lister_list.find_all("li", class_="ipc-metadata-list-summary-item sc-59b6048d-0 jemTre cli-parent")

            for movie_item in movie_items:
                title_div = movie_item.find("div", class_="ipc-metadata-list-summary-item__c")
                anchor = title_div.find("a")
                h3 = anchor.find("h3")
                title = h3.text.strip()

                print(f"{title}")
        else:
            print("Elemen lister_list tidak ditemukan.")
    else:
        print("Elemen div yang sesuai tidak ditemukan.")
else:
    print(f"Gagal. Status kode: {response.status_code}")
