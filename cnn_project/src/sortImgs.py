import pandas as pd
from shutil import move
from zipfile import ZipFile

path = "../data/chest_xray_data_set/"
path_test_zip = "../data/chest-xray-dataset-test/test/"
test_path = "../data/test_set/"
valid_path = "../data/valid_set/"
train_path = "../data/train_set/"
split_percent = 0.3


def move_imgs(dataframe, group: str):
    valid_len = round(len(dataframe.index) * split_percent)
    dest = valid_path + group
    for row in dataframe['X_ray_image_name'].iloc[:valid_len + 1]:
        src = path + row
        move(src, dest)
    print("Slike su prebacene u: " + dest)

    dest = train_path + group
    for row in dataframe['X_ray_image_name'].iloc[valid_len + 1:]:
        src = path + row
        move(src, dest)
    print("Slike su prebacene u: " + dest)


def move_test_imgs(dataframe, group: str):
    dest = test_path + group
    for row in dataframe['X_ray_image_name']:
        src = path_test_zip + row
        move(src, dest)
    print("Slike su prebacene u: " + dest)


def extract_from_zip(dir_name: str):
    fname = '../data/' + dir_name
    with ZipFile(fname, 'r') as zipObj:
        zipObj.extractall(path='../data')


if __name__ == '__main__':
    # ekstraktovanje fajlova iz zip datoteka
    extract_from_zip('chest_xray_data_set.zip')
    extract_from_zip('chest-xray-dataset-test.zip')

    # otvaranje fajla chest_xray_metadata.csv i izdvajanje grupa
    df = pd.read_csv("../data/chest_xray_data_set/metadata/chest_xray_metadata.csv")
    df_normal = df.loc[df['Label'] == 'Normal']
    df_pnemonia = df.loc[df['Label'] == 'Pnemonia']
    df_virus = df_pnemonia.loc[df_pnemonia['Label_1_Virus_category'] == 'Virus']
    df_bacteria = df_pnemonia.loc[df_pnemonia['Label_1_Virus_category'] == 'bacteria']

    move_imgs(df_normal, 'normal')
    move_imgs(df_virus, 'virus')
    move_imgs(df_bacteria, 'bacteria')

    # otvaranje fajla chest_xray_metadata.csv i izdvajanje grupa
    df2 = pd.read_csv("../data/chest-xray-dataset-test/chest_xray_test_dataset.csv")
    df2_normal = df2.loc[df2['Label'] == 'Normal']
    df2_pnemonia = df2.loc[df2['Label'] == 'Pnemonia']
    df2_virus = df2_pnemonia.loc[df2_pnemonia['Label_1_Virus_category'] == 'Virus']
    df2_bacteria = df2_pnemonia.loc[df2_pnemonia['Label_1_Virus_category'] == 'bacteria']

    move_test_imgs(df2_normal, 'normal')
    move_test_imgs(df2_virus, 'virus')
    move_test_imgs(df2_bacteria, 'bacteria')

    print("Zavrseno je prebacivanje slika.")
