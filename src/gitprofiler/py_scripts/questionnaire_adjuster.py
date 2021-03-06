from dataclasses import dataclass
import pandas as pd
import numpy as np
import requests


@dataclass
class DataSource:
    """ Class handling CSV Load """
    name: str
    filepath: str
    separator: str

    def load_data(self) -> pd.DataFrame:
        return pd.read_csv(self.filepath, sep=self.separator)


class DataAnalyser:
    def __init__(self, loaded_csv):
        self.data = loaded_csv

    def check_data(self):
        print(f"N/A Columns: {self.get_na_columns()}")
        print(f"Object Columns: {self.get_object_columns()}")
        print(f"Float Columns: {self.get_float_columns()}")
        print(f"Int Columns: {self.get_int_columns()}")

    def get_na_columns(self):
        return [col for col in self.data.columns if self.data[col].isnull().any()]

    def get_object_columns(self):
        return [col for col in self.data.columns if self.data[col].dtype == "object"]

    def get_float_columns(self):
        return [col for col in self.data.columns if self.data[col].dtype == "float"]

    def get_int_columns(self):
        return [col for col in self.data.columns if self.data[col].dtype == "int"]


class DataAdjuster(DataAnalyser):
    def add_boolean_column(self, new_column_name: str, from_column_name: str, keyword: str):
        cond = self.data[from_column_name].str.contains(keyword)
        self.data[new_column_name] = np.where(cond, True, False)

    def set_float_collumn(self, column_name: str):
        self.data[column_name] = self.data[column_name].fillna(0.0)
        self.data[column_name] = self.data[column_name].astype(str).str.replace(",", ".").astype(float)

    def set_float_percentage_collumn(self, column_name: str):
        self.data[column_name] = self.data[column_name].fillna("0.0%")
        self.data[column_name] = self.data[column_name].astype(str).str[:-1].astype(float)

    def set_integer_collumn(self, column_name: str):
        self.data[column_name] = self.data[column_name].fillna(0)
        self.data[column_name] = self.data[column_name].astype(int)

    def set_string_collumn(self, column_name: str):
        self.data[column_name] = self.data[column_name].astype(str)
        self.data[column_name] = self.data[column_name].fillna(np.NaN)

    def set_datetime_collumn(self, column_name: str):
        self.data[column_name] = pd.to_datetime(self.data[column_name])

        # self.data[column_name] = self.data[column_name].astype(str).str.to_datetime()

    def set_boolean_column(self, column_name: str):
        self.data[column_name] = np.where(self.data[column_name].str.contains("Tak"), True, False)


def add_soft_skills_columns(da):
    """ Adds new column for each column filled with boolean values.

    Args:
        da ([DataAdjuster])
    """
    SOFT_SKILLS = ['Komunikatywno????', 'Organizacja', 'Umiej??tno??ci Analityczne', 'Kreatywno????',
                   'Zarz??dzanie Projektem', 'Dyscyplina', 'Ciekawo????', 'Zaradno????', 'Dost??pno???? Czasowa',
                   'Publiczne Przem??wienia', 'Prezentowanie', 'Negocjowanie', 'Innowacyjno????',
                   'Przyw??dztwo', 'Tolerancja na zmiany i niepewno????', 'Pisanie (reporty/dokumentacje)',
                   'Nie opisa??em ??adnych umiej??tno??ci mi??kkich i raczej te?? nie da si?? wydedukowa?? takich z mojego CV']

    for soft_skill in SOFT_SKILLS:
        da.add_boolean_column(soft_skill, '???? Umiej??tno??ci Mi??ciutkie ', soft_skill)
        print(da.data[[soft_skill]])

    da.data.drop(columns=["???? Umiej??tno??ci Mi??ciutkie "], inplace=True)


def add_exp_skills_columns(da):
    """ Adds new column for each column filled with boolean values.

    Args:
        da ([DataAdjuster])
    """

    EXP_SKILLS = ['Studia', 'Bootcamp', 'Kontrybuowanie do open-source', 'Stworzenie publicznej libki',
                  'Stworzenie w??asnego programu/apki', 'Freelancerskie zlecenia', 'Ciekawo????', 'Zaradno????', 'Dost??pno???? Czasowa',
                  'Uruchomienie w??asnego projektu', 'Kursy Online / Certyfikaty']

    for exp_skill in EXP_SKILLS:
        da.add_boolean_column(exp_skill, '??????????? Jakie mia??e??/a?? do??wiadczenie przed znalezieniem pracy?', exp_skill)
        print(da.data[[exp_skill]])

    da.data.drop(columns=["??????????? Jakie mia??e??/a?? do??wiadczenie przed znalezieniem pracy?"], inplace=True)


def standardize_column_values_self_rating(da):
    """ Merges identical answers to one value """

    ANSWERS = [('Tak', 'Tak - my??l??, ??e moje umiej??tno??ci mog?? by?? na niewyr????niaj??cym si?? poziomie, wi??c potrzebna by??a cierpliwo????'),
               ('Raczej Tak', 'Raczej tak - na to, co jestem w stanie sob?? zareprezentowa??, to mog??o to mniej wi??cej tyle trwa??'),
               ('Raczej Tak', 'Raczej tak - na to, co jestem w stanie sob?? zareprezentowa?? to mog??o to mniej wi??cej tyle trwa??'),
               ('Nie jestem pewien', 'Nie jestem pewien'),
               ('Raczej nie', 'Nie jestem nie wiadomo jakim ekspertem, ale jednak uwa??am, ??e umiem wystarczaj??co'),
               ('Raczej nie', 'Jestem w stanie sob?? co?? zaprezentowa??, ale nie uwa??am, ??eby to by??o sporo'),
               ('Nie', 'Z moimi umiej??tno??ciami powinienem znale???? prac?? du??o szybciej')]

    COLUMN_NAME = '??????? Oceniasz, ??e znalaz??e??/a?? prac?? w czasie adekwatnym do umiej??tno??ci?'

    for answer in ANSWERS:
        da.data.loc[da.data[COLUMN_NAME] == answer[1], COLUMN_NAME] = answer[0]


def standardize_column_values_time_experience(da):
    """ Merges identical answers to one value """

    ANSWERS = [('60', '5 lat+'),
               ('54', '4,5 roku'),
               ('48', '4 lata'),
               ('42', '3,5 roku'),
               ('36', '3 lata'),
               ('30', '2,5 roku'),
               ('24', '2 lata'),
               ('18', '1,5 roku'),
               ('12', '1 rok'),
               ('6', '0,5 roku')]

    COLUMN_NAME = '???? Jak d??ugo trwa Twoja przygoda z programowaniem?'

    for answer in ANSWERS:
        da.data.loc[da.data[COLUMN_NAME] == answer[1], COLUMN_NAME] = answer[0]


def standardize_column_values_job_search_time(da):
    """ Merges identical answers to one value """

    ANSWERS = [('1', '1 miesi??c'),
               ('2', '2 miesi??ce'),
               ('3', '3 miesi??ce'),
               ('4', '4 miesi??ce'),
               ('5', '5 miesi??cy'),
               ('6', '6 miesi??cy'),
               ('7', '7 miesi??cy'),
               ('8', '8 miesi??cy'),
               ('9', '9 miesi??cy'),
               ('10', '10 miesi??cy'),
               ('11', '11 miesi??cy'),
               ('12', '12 miesi??cy'),
               ('14', 'ponad 1 rok'),
               ('18', 'ponad 1,5 roku'),
               ('26', 'ponad 2 lata')]

    COLUMN_NAME = '??? Jak d??ugo to trwa??o?'

    for answer in ANSWERS:
        da.data.loc[da.data[COLUMN_NAME] == answer[1], COLUMN_NAME] = answer[0]


def change_polish_words_to_booleans(da):
    """ Maps polish words to corresponding boolean values """

    COLUMNS = ['??????????? Czy tworzy??e?? co?? "w??asnego"?',
               '???? Czy uda??o Ci si?? znale???? prac?? jako programista/tka?',
               '???? Zgoda na przetwarzanie informacji ']

    for column in COLUMNS:
        da.set_boolean_column(column)


def set_integer_columns_types(da):
    """ Maps polish words to corresponding boolean values """

    COLUMNS = ['??????????? Ile rozm??w kwalifikacyjnych musia??e??/a?? przej???? zanim uda??o Ci si?? znale???? prac???',
               '???? Do ilu pracodawc??w wys??a??e??/a?? CV (mniej wi??cej)?',
               '???? Jak oceniasz szybko???? znalezienia pracy?',
               '???? Jak d??ugo trwa Twoja przygoda z programowaniem?',
               '???? Ocena J??zyka #1',
               '???? Ocena J??zyka #2',
               '???? Ocena J??zyka #3', ]

    for column in COLUMNS:
        da.set_integer_collumn(column)


def set_float_columns_types(da):
    """ Maps polish words to corresponding boolean values """

    COLUMNS_PERCENTAGES = ['????????????? Jaki procent pracodawc??w si?? do Ciebie odezwa??o po przes??aniu CV1?',
                           '??????????? Jaki procent pracodawc??w zaprosi??o Ci?? na rozmow?? techniczn?? po przes??aniu CV1?']

    for column in COLUMNS_PERCENTAGES:
        da.set_float_percentage_collumn(column)


def set_string_columns_types(da):
    """ Maps polish words to corresponding boolean values """

    COLUMNS = ['???? J??zyk #1', '???? J??zyk #2', '???? J??zyk #3']

    for column in COLUMNS:
        da.set_string_collumn(column)


def merge_identical_columns(da):
    # df['Year'].astype(str) + df['quarter']

    da.data.loc[da.data['???? Do ilu pracodawc??w wys??a??e??/a?? CV (mniej wi??cej)?'].isnull(
    ), '???? Do ilu pracodawc??w wys??a??e??/a?? CV (mniej wi??cej)?'] = da.data['???? Do ilu pracodawc??w wys??a??e?? CV (mniej wi??cej)?']
    da.data.drop(columns=["???? Do ilu pracodawc??w wys??a??e?? CV (mniej wi??cej)?"], inplace=True)

    da.data.loc[da.data['??? Jak d??ugo to trwa??o?'].isnull(
    ), '??? Jak d??ugo to trwa??o?'] = da.data['??? Jak dawno rozpocz????e??/a?? poszukiwa?? pracy?']
    da.data.drop(columns=["??? Jak dawno rozpocz????e??/a?? poszukiwa?? pracy?"], inplace=True)

    da.data.loc[da.data['??????????? Ile rozm??w kwalifikacyjnych musia??e??/a?? przej???? zanim uda??o Ci si?? znale???? prac???'].isnull(
    ), '??????????? Ile rozm??w kwalifikacyjnych musia??e??/a?? przej???? zanim uda??o Ci si?? znale???? prac???'] = da.data['??????????? Ile rozm??w kwalifikacyjnych ju?? przeszed??e??/przesz??a???']
    da.data.drop(columns=["??????????? Ile rozm??w kwalifikacyjnych ju?? przeszed??e??/przesz??a???"], inplace=True)

    da.data.loc[da.data['???? Jak oceniasz szybko???? znalezienia pracy?'].isnull(
    ), '???? Jak oceniasz szybko???? znalezienia pracy?'] = da.data['???? Twoim zdaniem - jak oceniasz proces rekrutacji w zawodzie?']
    da.data.drop(columns=["???? Twoim zdaniem - jak oceniasz proces rekrutacji w zawodzie?"], inplace=True)

    da.data.loc[da.data['???? W kt??rym roku rozpocz????e??/a?? szuka?? pracy jako Entry / Junior programista?'].isnull(
    ), '???? W kt??rym roku rozpocz????e??/a?? szuka?? pracy jako Entry / Junior programista?'] = da.data['???? W kt??rym roku rozpocz????e??/a?? szuka?? prac?? jako Entry / Junior programista?']
    da.data.drop(columns=["???? W kt??rym roku rozpocz????e??/a?? szuka?? prac?? jako Entry / Junior programista?"], inplace=True)

    da.data.loc[da.data['??????? Oceniasz, ??e znalaz??e??/a?? prac?? w czasie adekwatnym do umiej??tno??ci?'].isnull(
    ), '??????? Oceniasz, ??e znalaz??e??/a?? prac?? w czasie adekwatnym do umiej??tno??ci?'] = da.data['??????? Jak oceniasz swoje umi??jetno??ci?']
    da.data.drop(columns=["??????? Jak oceniasz swoje umi??jetno??ci?"], inplace=True)

    da.data.loc[da.data['??????????? Jaki procent pracodawc??w zaprosi??o Ci?? na rozmow?? techniczn?? po przes??aniu CV1?'].isnull(
    ), '??????????? Jaki procent pracodawc??w zaprosi??o Ci?? na rozmow?? techniczn?? po przes??aniu CV1?'] = da.data['??????????? Jaki procent pracodawc??w zaprosi??o Ci?? na rozmow?? techniczn?? po przes??aniu CV2?']
    da.data.drop(columns=["??????????? Jaki procent pracodawc??w zaprosi??o Ci?? na rozmow?? techniczn?? po przes??aniu CV2?"], inplace=True)

    da.data.loc[da.data['????????????? Jaki procent pracodawc??w si?? do Ciebie odezwa??o po przes??aniu CV1?'].isnull(
    ), '????????????? Jaki procent pracodawc??w si?? do Ciebie odezwa??o po przes??aniu CV1?'] = da.data['????????????? Jaki procent pracodawc??w si?? do Ciebie odezwa??o po przes??aniu CV2?']
    da.data.drop(columns=["????????????? Jaki procent pracodawc??w si?? do Ciebie odezwa??o po przes??aniu CV2?"], inplace=True)


def fix_initial_data(da):

    # "Opcja1" -> 1
    da.data.at[2, '???? Do ilu pracodawc??w wys??a??e??/a?? CV (mniej wi??cej)?'] = 1

    # "Co najmniej kilkunastu" -> 10 < n < 20
    da.data.at[4, '???? Do ilu pracodawc??w wys??a??e??/a?? CV (mniej wi??cej)?'] = 11

    # "10-20" -> n = (10+20/2)
    da.data.at[43, '???? Do ilu pracodawc??w wys??a??e??/a?? CV (mniej wi??cej)?'] = 15

    # "20+" -> 20 < n < 25
    da.data.at[47, '???? Do ilu pracodawc??w wys??a??e??/a?? CV (mniej wi??cej)?'] = 21

    # "30-40" -> n = (30+40/2)
    da.data.at[50, '???? Do ilu pracodawc??w wys??a??e??/a?? CV (mniej wi??cej)?'] = 35

    # "4/5" -> 4
    da.data.at[51, '???? Do ilu pracodawc??w wys??a??e??/a?? CV (mniej wi??cej)?'] = 4

    # "60?" -> 60
    da.data.at[54, '???? Do ilu pracodawc??w wys??a??e??/a?? CV (mniej wi??cej)?'] = 60


def check_url_existance(url: str) -> bool:
    try:
        return requests.get(url).status_code != 404
    except requests.exceptions.MissingSchema:
        return requests.get(f"https://{url}").status_code != 404
    except requests.ConnectionError:
        return False


def validate_urls(da):
    result = [False if "github.com" not in url else check_url_existance(url) for url in da.data['???? Link do GitHuba']]
    da.data["Valid GitHub"] = result


def rename_columns(da):
    da.data.rename(columns={
        '???? Link do GitHuba': 'GithubLink',
        '???? Jak d??ugo trwa Twoja przygoda z programowaniem?': 'ProgrammingExp',
        '??????????? Czy tworzy??e?? co?? "w??asnego"?': 'PersonalWorkExp',
        '???? Czy uda??o Ci si?? znale???? prac?? jako programista/tka?': 'FoundWork',
        '???? W kt??rym roku rozpocz????e??/a?? szuka?? pracy jako Entry / Junior programista?': 'StartWorkSearchDate',
        '???? Jak oceniasz szybko???? znalezienia pracy?': 'SelfRateWorkFindTime',
        '??? Jak d??ugo to trwa??o?': 'WorkFindTime',
        '??????? Oceniasz, ??e znalaz??e??/a?? prac?? w czasie adekwatnym do umiej??tno??ci?': 'SelfRateAdequteTimeWorkFindTime',
        '??????????? Ile rozm??w kwalifikacyjnych musia??e??/a?? przej???? zanim uda??o Ci si?? znale???? prac???': 'InterviewsBeforeFoundWork',
        '???? Do ilu pracodawc??w wys??a??e??/a?? CV (mniej wi??cej)?': 'CVsSend',
        '????????????? Jaki procent pracodawc??w si?? do Ciebie odezwa??o po przes??aniu CV1?': 'CVsPercentRespondRate',
        '??????????? Jaki procent pracodawc??w zaprosi??o Ci?? na rozmow?? techniczn?? po przes??aniu CV1?': 'CVsTechInterviewPercentRespondRate',
        '???? Zgoda na przetwarzanie informacji ': 'Consent',
        '???? Jakby?? si?? zaklasyfikowa??/a?': 'SelfClassifiedRole',
        '???? Tech Stack': 'TechStack',
        '???? J??zyk #1': 'Language1',
        '???? Ocena J??zyka #1': 'LanguageRate1',
        '???? J??zyk #2': 'Language2',
        '???? Ocena J??zyka #2': 'LanguageRate2',
        '???? J??zyk #3': 'Language3',
        '???? Ocena J??zyka #3': 'LanguageRate3',
        'Komunikatywno????': 'Communicativeness',
        'Organizacja': 'SelfOrganization',
        'Umiej??tno??ci Analityczne': 'AnalyticalSkills',
        'Kreatywno????': 'Creativity',
        'Zarz??dzanie Projektem': 'ProjectManagement',
        'Dyscyplina': 'Discipline',
        'Ciekawo????': 'Curiosity',
        'Zaradno????': 'Resourcefulness',
        'Dost??pno???? Czasowa': 'TimeAvailability',
        'Publiczne Przem??wienia': 'PublicSpeeches',
        'Prezentowanie': 'Presenting',
        'Innowacyjno????': 'Innovation',
        'Przyw??dztwo': 'Leadership',
        'Tolerancja na zmiany i niepewno????': 'ToleranceToChangeAndUncertainty',
        'Pisanie (reporty/dokumentacje)': 'Writing',
        'Nie opisa??em ??adnych umiej??tno??ci mi??kkich i raczej te?? nie da si?? wydedukowa?? takich z mojego CV': 'NoDescribedSoftSkills',
        'Studia': 'Studies',
        'Bootcamp': 'Bootcamp',
        'Kontrybuowanie do open-source': 'OpenSourceContribution',
        'Stworzenie publicznej libki': 'PublicLibraryCreation',
        'Stworzenie w??asnego programu/apki': 'PersonalAppCreation',
        'Freelancerskie zlecenia': 'Freelancing',
        'Uruchomienie w??asnego projektu': 'PersonalProjectLaunching',
        'Kursy Online / Certyfikaty': 'OnlineCoursesCertificates',
        'Valid GitHub': 'ValidGitHub'
    }, inplace=True)


def remove_usernames(da):
    da.data.drop(['GithubLink'], axis=1, inplace=True)


def main():
    # Loading Data
    # data_source = DataSource("Questionnaire", "./data/questionnaire.csv", ",")
    data_source = DataSource("Questionnaire", "./data/questionnaire.csv", ",")
    git_table = data_source.load_data()
    da = DataAdjuster(git_table)

    # Adjusting Data
    merge_identical_columns(da)
    fix_initial_data(da)

    # Creating new columns out of checkbox question
    add_soft_skills_columns(da)
    add_exp_skills_columns(da)

    # Transforming string into numerical values
    standardize_column_values_self_rating(da)
    standardize_column_values_job_search_time(da)
    standardize_column_values_time_experience(da)

    # Changing polish word to boolean
    change_polish_words_to_booleans(da)

    # Setting type of columns
    set_integer_columns_types(da)
    set_float_columns_types(da)
    da.set_datetime_collumn("???? W kt??rym roku rozpocz????e??/a?? szuka?? pracy jako Entry / Junior programista?")

    # Check if given GitHub is valid
    validate_urls(da)

    # Rename column names to english language
    rename_columns(da)

    # Remove the column with usernames after the work is done
    # remove_usernames(da)

    # Check & Save
    da.check_data()
    da.data.to_csv('data/output.csv')


if __name__ == '__main__':
    main()
