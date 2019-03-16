import requests
def main():
    url = 'https://apidata.mos.ru/v1/datasets/1488/rows?api_key=41196be4f1cfbe741166345f7fddbb93'
    json = requests.get(url=url).json()
    for i in range(1, len(json)):
        print(json[i]['Cells']['Station']+" - "+str(json[i]['Cells']['ID'])+" - "+str(json[i]['Cells']['Status']))
if __name__ == '__main__':
    main()
