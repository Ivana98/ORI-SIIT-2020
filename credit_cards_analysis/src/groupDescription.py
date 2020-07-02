from matplotlib import pyplot as plt
import numpy as np

group_info ={}

# parametri su liste sa srednjim vrednostima za svaku posmatranu grupu po kolonama
def bar_plot(b, oop, ip, ca, oopf, ipf, cat, cl, p):
    labels = ['G1', 'G2', 'G3']

    # srednje vrednosti posmatranih kolona za svaku grupu

    balance = b  # stanje na računu dostupno za kupovinu
    # balance_frequency = bf  # koliko često se menja balans, vrednost između 0 i 1
    one_off_purchases = oop  # iznos potrošen na kupovinu jednokratno
    installments_purchases = ip  # iznos potrošen na kupovinu na rate
    cash_advance = ca  # iznos koji je korisnik uplatio unapred
    one_off_purchases_frequency = oopf  # koliko često kupuje jednokratno
    installments_purchases_frequency = ipf  # koliko često kupuje na rate
    cash_advance_trx = cat  # broj transakcija sa uplaćenim novcem unapred
    credit_limit = cl  # limit na kartici
    payments = p  # ukupan iznos uplacen na karticu
    # tenure = t  # koliko jos vaze usluge kartice

    x = np.arange(len(labels))  # the label locations
    # x_sm = np.arange(5)
    # x = np.arange(len(labels))
    width = 0.08  # the width of the bars

    fig1, ax = plt.subplots()
    fig1, ax_small = plt.subplots()

    ax.bar(x + 0.00, balance, width, label='Stanje')
    # ax_small.bar(x + 0.09, balance_frequency, width, label='Ucestalost promene stanja')
    ax.bar(x + 0.18, one_off_purchases, width, label='iznos - jednokratna kupovina')
    ax.bar(x + 0.27, installments_purchases, width, label='Iznos - kupovina na rate')
    ax.bar(x + 0.36, cash_advance, width, label='Iznos uplacen unapred')
    ax_small.bar(x + 0.45, one_off_purchases_frequency, width, label='Ucestalost jednokratne kupovine')
    ax_small.bar(x + 0.54, installments_purchases_frequency, width, label='Ucestalost kupovine na rate')
    ax_small.bar(x + 0.63, cash_advance_trx, width, label='Br. trans. uplacenih unapred')
    ax.bar(x + 0.72, credit_limit, width, label='Limit na kartici')
    ax.bar(x + 0.81, payments, width, label='Ukupno uplaceno na karticu')
    # ax_small.bar(x + 0.90, tenure, width, label='Vazenje kartice')

    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    ax_small.set_xticks(x)
    ax_small.set_xticklabels(labels)
    ax_small.legend()

    plt.title("Prikaz prosečnih vrednosti po grupama za svaku kolonu")
    plt.show()


# parametar je dataframe
def count(df):
    balance = []
    # balance_frequency = []
    one_off_purchases = []
    installments_purchases = []
    cash_advance = []
    one_off_purchases_frequency = []
    installments_purchases_frequency = []
    cash_advance_trx = []
    credit_limit = []
    payments = []
    # tenure = []

    for k in range(0, 3):
        group_frame = df.loc[df['CLUSTER'] == int(k)]

        balance.append(round(group_frame['BALANCE'].mean(), 2))
        # balance_frequency.append(round(group_frame['BALANCE_FREQUENCY'].mean(), 2))
        one_off_purchases.append(round(group_frame['ONEOFF_PURCHASES'].mean(), 2))
        installments_purchases.append(round(group_frame['INSTALLMENTS_PURCHASES'].mean(), 2))
        cash_advance.append(round(group_frame['CASH_ADVANCE'].mean(), 2))
        one_off_purchases_frequency.append(round(group_frame['ONEOFF_PURCHASES_FREQUENCY'].mean(), 2))
        installments_purchases_frequency.append(round(group_frame['PURCHASES_INSTALLMENTS_FREQUENCY'].mean(), 2))
        cash_advance_trx.append(round(group_frame['CASH_ADVANCE_TRX'].mean(), 2))
        credit_limit.append(round(group_frame['CREDIT_LIMIT'].mean(), 2))
        payments.append(round(group_frame['PAYMENTS'].mean(), 2))
        # tenure.append(round(group_frame['TENURE'].mean(), 2))

    set_description(balance)
    bar_plot(balance, one_off_purchases, installments_purchases,
             cash_advance, one_off_purchases_frequency, installments_purchases_frequency,
             cash_advance_trx, credit_limit, payments)


def describe_groups(df):

    for k in range(0, 3):
        group_frame = df.loc[df['CLUSTER'] == int(k)]

        print('Grupa: ' + str(k+1))
        print('---------------------------')
        print("Opis ponašnja grupe:")
        print(group_info.get(k))
        print_column_info('Stanje na računu dostupno za kupovinu:', group_frame['BALANCE'])
        # print_column_info('Koliko često se menja balans, vrednost između 0 i 1:', group_frame['BALANCE_FREQUENCY'])

        group_frame['sum_of_purchases'] = group_frame['ONEOFF_PURCHASES'] + group_frame['INSTALLMENTS_PURCHASES']
        print_column_info('Ukupan iznos potrošen na kupovinu:', group_frame['sum_of_purchases'])

        print_column_info('Iznos potrošen na kupovinu jednokratno:', group_frame['ONEOFF_PURCHASES'])
        print_column_info('Iznos potrošen na kupovinu na rate:', group_frame['INSTALLMENTS_PURCHASES'])
        print_column_info('Iznos koji je korisnik uplatio unapred:', group_frame['CASH_ADVANCE'])
        print_column_info('Koliko često korisnik kupuje jednokratno:', group_frame['ONEOFF_PURCHASES_FREQUENCY'])
        print_column_info('Koliko često korisnik kupuje na rate:', group_frame['PURCHASES_INSTALLMENTS_FREQUENCY'])
        print_column_info('Broj transakcija sa uplaćenim novcem unapred:', group_frame['CASH_ADVANCE_TRX'])
        print_column_info('Limit na kreditnoj kartici:', group_frame['CREDIT_LIMIT'])
        print_column_info('Ukupan iznos uplaćen na karticu:', group_frame['PAYMENTS'])
        print()


def print_column_info(col_name: str, col_df):
    print(col_name)
    print("\t Minimalna vrednost: " + str(round(col_df.min(), 2)))
    print("\t Minimalna vrednost (različita od nule): " + str(round(col_df[col_df > .01].min(), 2)))
    print("\t Maksimalna vrednost: " + str(round(col_df.max(), 2)))
    print("\t Prosečna vrednost: " + str(round(col_df.mean(), 2)))
    print("\t Mediana: " + str(round(col_df.median(), 2)))


def set_description(balance_list: []):
    min_val = min(balance_list)
    max_val = max(balance_list)

    descr1 = "Ova grupa ima najmanje novca na stanju na računu i najmanji limit na kreditnim karticama.\n" \
             "Retko kupuje i ne troši veliki iznos novca. Skoro podjednako novca troši na kupovinu na\n" \
             "rate kao i na jednokratnu kupovinu, ali skoro duplo češće kupuje na rate nego jednokratno.\n" \
             "Takođe, ne uplaćuje veliki iznos novca unapred, i mali broj transakcija vrši tim novcem."
    descr2 = "Ova grupa ima najveći limit na kreditnim karticama i najviše novca na računu,\n" \
             "ali retko kupuje i ne troši mnogo novca. Više novca troši na jednokratnu kupovinu\n" \
             "nego na kupovinu na rate, ali malo ređe kupuje jednokratno. Ova grupa uplaćuje veliki\n" \
             "iznos unapred na karticu i njime vrši najveći broj transakcija."
    descr3 = "Ova grupa ima veliki limit na kreditnim karticama i nema mnogo novca na stanju na računu.\n" \
             "Relativno često kupuje i to gotovo podjednako na rate i jednokratno, ali bar duplo više novca\n" \
             "koristi za jednokratnu kupovinu nego za kupovinu na rate. Najmanji iznos novca uplaćuje unapred,\n" \
             "i mali broj transakcija vrši tim novcem."

    for i in range(0, 3):
        if balance_list[i] == min_val:
            group_info[i] = descr1
        elif balance_list[i] == max_val:
            group_info[i] = descr2
        else:
            group_info[i] = descr3


