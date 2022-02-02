import pandas as pd


def read_csv(name: str):
    df = pd.read_csv(name, sep=';', skiprows=range(0, 3), low_memory=False)
    df["Расход (руб.)"] = pd.to_numeric(df["Расход (руб.)"].replace(',', '.', regex=True))
    return df


def viev_company(dataframe: pd.DataFrame):
    df = dataframe.groupby("Кампания")
    name = ''
    for item in df:
        name = f'{name} {item[0]} \n'
    with open('company.txt', 'w', encoding='utf8') as doc:
        doc.write(name)
    return df


# функция вычисляющая CTR CPC CPM
def calculations(dataframe: pd.DataFrame):
    df = dataframe.groupby("Кампания")
    company = str(input(f'Введите название компании, вы можете их посмотреть в файле company.txt '))
    df = df.get_group(company)
    df['CTR'] = df["Клики"].sum() / df["Показы"].sum()
    df['CPC'] = df["Расход (руб.)"].sum() / df["Клики"].sum()
    df['CPM'] = df["Расход (руб.)"].sum() / (df["Показы"].sum() / 1000)
    return df


if __name__ == '__main__':
    data = 'month.csv'
    data = read_csv(data)
    viev_company(data)
    print(calculations(data))
