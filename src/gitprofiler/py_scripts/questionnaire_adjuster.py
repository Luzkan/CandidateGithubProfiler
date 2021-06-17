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
    SOFT_SKILLS = ['Komunikatywność', 'Organizacja', 'Umiejętności Analityczne', 'Kreatywność',
                   'Zarządzanie Projektem', 'Dyscyplina', 'Ciekawość', 'Zaradność', 'Dostępność Czasowa',
                   'Publiczne Przemówienia', 'Prezentowanie', 'Negocjowanie', 'Innowacyjność',
                   'Przywództwo', 'Tolerancja na zmiany i niepewność', 'Pisanie (reporty/dokumentacje)',
                   'Nie opisałem żadnych umiejętności miękkich i raczej też nie da się wydedukować takich z mojego CV']

    for soft_skill in SOFT_SKILLS:
        da.add_boolean_column(soft_skill, '🐻 Umiejętności Mięciutkie ', soft_skill)
        print(da.data[[soft_skill]])

    da.data.drop(columns=["🐻 Umiejętności Mięciutkie "], inplace=True)


def add_exp_skills_columns(da):
    """ Adds new column for each column filled with boolean values.

    Args:
        da ([DataAdjuster])
    """

    EXP_SKILLS = ['Studia', 'Bootcamp', 'Kontrybuowanie do open-source', 'Stworzenie publicznej libki',
                  'Stworzenie własnego programu/apki', 'Freelancerskie zlecenia', 'Ciekawość', 'Zaradność', 'Dostępność Czasowa',
                  'Uruchomienie własnego projektu', 'Kursy Online / Certyfikaty']

    for exp_skill in EXP_SKILLS:
        da.add_boolean_column(exp_skill, '👨‍🔬 Jakie miałeś/aś doświadczenie przed znalezieniem pracy?', exp_skill)
        print(da.data[[exp_skill]])

    da.data.drop(columns=["👨‍🔬 Jakie miałeś/aś doświadczenie przed znalezieniem pracy?"], inplace=True)


def standardize_column_values_self_rating(da):
    """ Merges identical answers to one value """

    ANSWERS = [('Tak', 'Tak - myślę, że moje umiejętności mogą być na niewyróżniającym się poziomie, więc potrzebna była cierpliwość'),
               ('Raczej Tak', 'Raczej tak - na to, co jestem w stanie sobą zareprezentować, to mogło to mniej więcej tyle trwać'),
               ('Raczej Tak', 'Raczej tak - na to, co jestem w stanie sobą zareprezentować to mogło to mniej więcej tyle trwać'),
               ('Nie jestem pewien', 'Nie jestem pewien'),
               ('Raczej nie', 'Nie jestem nie wiadomo jakim ekspertem, ale jednak uważam, że umiem wystarczająco'),
               ('Raczej nie', 'Jestem w stanie sobą coś zaprezentować, ale nie uważam, żeby to było sporo'),
               ('Nie', 'Z moimi umiejętnościami powinienem znaleźć pracę dużo szybciej')]

    COLUMN_NAME = '🕰️ Oceniasz, że znalazłeś/aś pracę w czasie adekwatnym do umiejętności?'

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

    COLUMN_NAME = '🧭 Jak długo trwa Twoja przygoda z programowaniem?'

    for answer in ANSWERS:
        da.data.loc[da.data[COLUMN_NAME] == answer[1], COLUMN_NAME] = answer[0]


def standardize_column_values_job_search_time(da):
    """ Merges identical answers to one value """

    ANSWERS = [('1', '1 miesiąc'),
               ('2', '2 miesiące'),
               ('3', '3 miesiące'),
               ('4', '4 miesiące'),
               ('5', '5 miesięcy'),
               ('6', '6 miesięcy'),
               ('7', '7 miesięcy'),
               ('8', '8 miesięcy'),
               ('9', '9 miesięcy'),
               ('10', '10 miesięcy'),
               ('11', '11 miesięcy'),
               ('12', '12 miesięcy'),
               ('14', 'ponad 1 rok'),
               ('18', 'ponad 1,5 roku'),
               ('26', 'ponad 2 lata')]

    COLUMN_NAME = '⌚ Jak długo to trwało?'

    for answer in ANSWERS:
        da.data.loc[da.data[COLUMN_NAME] == answer[1], COLUMN_NAME] = answer[0]


def change_polish_words_to_booleans(da):
    """ Maps polish words to corresponding boolean values """

    COLUMNS = ['👨‍💻 Czy tworzyłeś coś "własnego"?',
               '🔨 Czy udało Ci się znaleźć pracę jako programista/tka?',
               '🔏 Zgoda na przetwarzanie informacji ']

    for column in COLUMNS:
        da.set_boolean_column(column)


def set_integer_columns_types(da):
    """ Maps polish words to corresponding boolean values """

    COLUMNS = ['👨‍💼 Ile rozmów kwalifikacyjnych musiałeś/aś przejść zanim udało Ci się znaleźć pracę?',
               '📬 Do ilu pracodawców wysłałeś/aś CV (mniej więcej)?',
               '🚶 Jak oceniasz szybkość znalezienia pracy?',
               '🧭 Jak długo trwa Twoja przygoda z programowaniem?',
               '🟢 Ocena Języka #1',
               '🔵 Ocena Języka #2',
               '🟣 Ocena Języka #3', ]

    for column in COLUMNS:
        da.set_integer_collumn(column)


def set_float_columns_types(da):
    """ Maps polish words to corresponding boolean values """

    COLUMNS_PERCENTAGES = ['👨‍⚖️ Jaki procent pracodawców się do Ciebie odezwało po przesłaniu CV1?',
                           '👨‍🔧 Jaki procent pracodawców zaprosiło Cię na rozmowę techniczną po przesłaniu CV1?']

    for column in COLUMNS_PERCENTAGES:
        da.set_float_percentage_collumn(column)


def set_string_columns_types(da):
    """ Maps polish words to corresponding boolean values """

    COLUMNS = ['🟢 Język #1', '🔵 Język #2', '🟣 Język #3']

    for column in COLUMNS:
        da.set_string_collumn(column)


def merge_identical_columns(da):
    # df['Year'].astype(str) + df['quarter']

    da.data.loc[da.data['📬 Do ilu pracodawców wysłałeś/aś CV (mniej więcej)?'].isnull(
    ), '📬 Do ilu pracodawców wysłałeś/aś CV (mniej więcej)?'] = da.data['📬 Do ilu pracodawców wysłałeś CV (mniej więcej)?']
    da.data.drop(columns=["📬 Do ilu pracodawców wysłałeś CV (mniej więcej)?"], inplace=True)

    da.data.loc[da.data['⌚ Jak długo to trwało?'].isnull(
    ), '⌚ Jak długo to trwało?'] = da.data['⌚ Jak dawno rozpocząłeś/aś poszukiwać pracy?']
    da.data.drop(columns=["⌚ Jak dawno rozpocząłeś/aś poszukiwać pracy?"], inplace=True)

    da.data.loc[da.data['👨‍💼 Ile rozmów kwalifikacyjnych musiałeś/aś przejść zanim udało Ci się znaleźć pracę?'].isnull(
    ), '👨‍💼 Ile rozmów kwalifikacyjnych musiałeś/aś przejść zanim udało Ci się znaleźć pracę?'] = da.data['👨‍💼 Ile rozmów kwalifikacyjnych już przeszedłeś/przeszłaś?']
    da.data.drop(columns=["👨‍💼 Ile rozmów kwalifikacyjnych już przeszedłeś/przeszłaś?"], inplace=True)

    da.data.loc[da.data['🚶 Jak oceniasz szybkość znalezienia pracy?'].isnull(
    ), '🚶 Jak oceniasz szybkość znalezienia pracy?'] = da.data['🚶 Twoim zdaniem - jak oceniasz proces rekrutacji w zawodzie?']
    da.data.drop(columns=["🚶 Twoim zdaniem - jak oceniasz proces rekrutacji w zawodzie?"], inplace=True)

    da.data.loc[da.data['📅 W którym roku rozpocząłeś/aś szukać pracy jako Entry / Junior programista?'].isnull(
    ), '📅 W którym roku rozpocząłeś/aś szukać pracy jako Entry / Junior programista?'] = da.data['📅 W którym roku rozpocząłeś/aś szukać pracę jako Entry / Junior programista?']
    da.data.drop(columns=["📅 W którym roku rozpocząłeś/aś szukać pracę jako Entry / Junior programista?"], inplace=True)

    da.data.loc[da.data['🕰️ Oceniasz, że znalazłeś/aś pracę w czasie adekwatnym do umiejętności?'].isnull(
    ), '🕰️ Oceniasz, że znalazłeś/aś pracę w czasie adekwatnym do umiejętności?'] = da.data['🕰️ Jak oceniasz swoje umięjetności?']
    da.data.drop(columns=["🕰️ Jak oceniasz swoje umięjetności?"], inplace=True)

    da.data.loc[da.data['👨‍🔧 Jaki procent pracodawców zaprosiło Cię na rozmowę techniczną po przesłaniu CV1?'].isnull(
    ), '👨‍🔧 Jaki procent pracodawców zaprosiło Cię na rozmowę techniczną po przesłaniu CV1?'] = da.data['👨‍🔧 Jaki procent pracodawców zaprosiło Cię na rozmowę techniczną po przesłaniu CV2?']
    da.data.drop(columns=["👨‍🔧 Jaki procent pracodawców zaprosiło Cię na rozmowę techniczną po przesłaniu CV2?"], inplace=True)

    da.data.loc[da.data['👨‍⚖️ Jaki procent pracodawców się do Ciebie odezwało po przesłaniu CV1?'].isnull(
    ), '👨‍⚖️ Jaki procent pracodawców się do Ciebie odezwało po przesłaniu CV1?'] = da.data['👨‍⚖️ Jaki procent pracodawców się do Ciebie odezwało po przesłaniu CV2?']
    da.data.drop(columns=["👨‍⚖️ Jaki procent pracodawców się do Ciebie odezwało po przesłaniu CV2?"], inplace=True)


def fix_initial_data(da):

    # "Opcja1" -> 1
    da.data.at[2, '📬 Do ilu pracodawców wysłałeś/aś CV (mniej więcej)?'] = 1

    # "Co najmniej kilkunastu" -> 10 < n < 20
    da.data.at[4, '📬 Do ilu pracodawców wysłałeś/aś CV (mniej więcej)?'] = 11

    # "10-20" -> n = (10+20/2)
    da.data.at[43, '📬 Do ilu pracodawców wysłałeś/aś CV (mniej więcej)?'] = 15

    # "20+" -> 20 < n < 25
    da.data.at[47, '📬 Do ilu pracodawców wysłałeś/aś CV (mniej więcej)?'] = 21

    # "30-40" -> n = (30+40/2)
    da.data.at[50, '📬 Do ilu pracodawców wysłałeś/aś CV (mniej więcej)?'] = 35

    # "4/5" -> 4
    da.data.at[51, '📬 Do ilu pracodawców wysłałeś/aś CV (mniej więcej)?'] = 4

    # "60?" -> 60
    da.data.at[54, '📬 Do ilu pracodawców wysłałeś/aś CV (mniej więcej)?'] = 60


def check_url_existance(url: str) -> bool:
    try:
        return requests.get(url).status_code != 404
    except requests.exceptions.MissingSchema:
        return requests.get(f"https://{url}").status_code != 404
    except requests.ConnectionError:
        return False


def validate_urls(da):
    result = [False if "github.com" not in url else check_url_existance(url) for url in da.data['🐱 Link do GitHuba']]
    da.data["Valid GitHub"] = result


def rename_columns(da):
    da.data.rename(columns={
        '🐱 Link do GitHuba': 'GithubLink',
        '🧭 Jak długo trwa Twoja przygoda z programowaniem?': 'ProgrammingExp',
        '👨‍💻 Czy tworzyłeś coś "własnego"?': 'PersonalWorkExp',
        '🔨 Czy udało Ci się znaleźć pracę jako programista/tka?': 'FoundWork',
        '📅 W którym roku rozpocząłeś/aś szukać pracy jako Entry / Junior programista?': 'StartWorkSearchDate',
        '🚶 Jak oceniasz szybkość znalezienia pracy?': 'SelfRateWorkFindTime',
        '⌚ Jak długo to trwało?': 'WorkFindTime',
        '🕰️ Oceniasz, że znalazłeś/aś pracę w czasie adekwatnym do umiejętności?': 'SelfRateAdequteTimeWorkFindTime',
        '👨‍💼 Ile rozmów kwalifikacyjnych musiałeś/aś przejść zanim udało Ci się znaleźć pracę?': 'InterviewsBeforeFoundWork',
        '📬 Do ilu pracodawców wysłałeś/aś CV (mniej więcej)?': 'CVsSend',
        '👨‍⚖️ Jaki procent pracodawców się do Ciebie odezwało po przesłaniu CV1?': 'CVsPercentRespondRate',
        '👨‍🔧 Jaki procent pracodawców zaprosiło Cię na rozmowę techniczną po przesłaniu CV1?': 'CVsTechInterviewPercentRespondRate',
        '🔏 Zgoda na przetwarzanie informacji ': 'Consent',
        '😶 Jakbyś się zaklasyfikował/a?': 'SelfClassifiedRole',
        '📦 Tech Stack': 'TechStack',
        '🟢 Język #1': 'Language1',
        '🟢 Ocena Języka #1': 'LanguageRate1',
        '🔵 Język #2': 'Language2',
        '🔵 Ocena Języka #2': 'LanguageRate2',
        '🟣 Język #3': 'Language3',
        '🟣 Ocena Języka #3': 'LanguageRate3',
        'Komunikatywność': 'Communicativeness',
        'Organizacja': 'SelfOrganization',
        'Umiejętności Analityczne': 'AnalyticalSkills',
        'Kreatywność': 'Creativity',
        'Zarządzanie Projektem': 'ProjectManagement',
        'Dyscyplina': 'Discipline',
        'Ciekawość': 'Curiosity',
        'Zaradność': 'Resourcefulness',
        'Dostępność Czasowa': 'TimeAvailability',
        'Publiczne Przemówienia': 'PublicSpeeches',
        'Prezentowanie': 'Presenting',
        'Innowacyjność': 'Innovation',
        'Przywództwo': 'Leadership',
        'Tolerancja na zmiany i niepewność': 'ToleranceToChangeAndUncertainty',
        'Pisanie (reporty/dokumentacje)': 'Writing',
        'Nie opisałem żadnych umiejętności miękkich i raczej też nie da się wydedukować takich z mojego CV': 'NoDescribedSoftSkills',
        'Studia': 'Studies',
        'Bootcamp': 'Bootcamp',
        'Kontrybuowanie do open-source': 'OpenSourceContribution',
        'Stworzenie publicznej libki': 'PublicLibraryCreation',
        'Stworzenie własnego programu/apki': 'PersonalAppCreation',
        'Freelancerskie zlecenia': 'Freelancing',
        'Uruchomienie własnego projektu': 'PersonalProjectLaunching',
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
    da.set_datetime_collumn("📅 W którym roku rozpocząłeś/aś szukać pracy jako Entry / Junior programista?")

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
