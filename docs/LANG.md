# 1

## Pre

```latex
What distinguishes this paper among others - as we mentioned - we do recognise that majority of recruiters does not have skills that could examine the technicality of a candidate. For example in the \emph{"Mining the Technical Roles of GitHub Users"} the survey was conducted among recruiters from \footnote{StackOverflow Website URL: https://stackoverflow.com/} - strictly developer collaboration \& knowledge sharing website. Thus, it can be concluded that the surveyed sample was exceptional among global population of recruiters as they were interested to create an account and browse an IT-technical website. As far as we know there are examples of few not developed recommendation systems based on user Github profile but there are many papers which focus on mining data from repositories.
```

## Post

What distinguishes this paper among others — as we mentioned — we do **recognize** that **the** majority of recruiters does not have skills that could examine the technicality of a candidate. For example in the \emph{"Mining the Technical Roles of GitHub Users"} the survey was conducted among recruiters from **StackOverflow website** \footnote{StackOverflow Website URL: https://stackoverflow.com/} - which is **primarily used by developers for the purposes of collaboration \& knowledge sharing**. Thus, it can be concluded that the surveyed sample was exceptional among global population of recruiters **as they have made extra efforts to create an account on** IT-technical website **and not only that - they were actively browsing it and even possibly creating extra content which made them visible and reachable by researchers**. **Based on the research we have conducted, there are only a few unfinished recommendation systems that use the user GitHub profile but at the same time there is some research that focuses on mining the data from the repositories.**

## End

```latex
What distinguishes this paper among others — as we mentioned — we do recognize that the majority of recruiters does not have skills that could examine the technicality of a candidate. For example in the \emph{"Mining the Technical Roles of GitHub Users"} the survey was conducted among recruiters from StackOverflow website \footnote{StackOverflow Website URL: https://stackoverflow.com/} - which is primarily used by developers for the purposes of collaboration \& knowledge sharing. Thus, it can be concluded that the surveyed sample was exceptional among global population of recruiters as they have made extra efforts to create an account on IT-technical website and not only that - they were actively browsing it and even possibly creating extra content which made them visible and reachable by researchers. Based on the research we have conducted, there are only a few unfinished recommendation systems that use the user GitHub profile but at the same time there is some research that focuses on mining the data from the repositories.
```

# 2

## Pre

```latex
Research questions presented below should help to understand the importance of creating such tool and also provide an information about functionality which is needed by potential future users - recruiters. What is more they should explore the general topic of recruiment and repositories as well.

Hence, we defined four research questions.

- \emph{RQ1: What skills are common when a company is looking for a developer?}\\
  Our system needs to determine wheather developer should be considered as worthy of attention. This question help to find out which skills are considered important among companies.
- \emph{RQ2: How repository make a good impression?}\\
  One way of assesing developer expertise is to analyse his projects. Thus, we should determine which features of repositories are the most representative ones.
- \emph{RQ3: How should recruitment process look like in IT?}\\
  As a result this question should porvide us with information wheater recomendation system based on repsitories is worth devoting time.
- \emph{RQ4: Is Github repository used only for programming purposes?}\\
  As we all know not every object is used with authors purpose. Same situation might occure with the repositories. It is not required for them to be used only for developing purposes (some are used are a storage or for the experimental porpouses).
```

## Post

Research questions presented below should **explain** **[d] to help understand [/d]** the importance of **[d] creating [/d]** such tool and also provide an information about **the** functionalities which **potential end user might need (i.e. - recruiters, developers themselves).** **Furthermore we also explore issues related to the recruitment itself, as well as the quality of repositories**.

Hence, we defined four research questions.

- \emph{RQ1: **What are the most common skills the company is looking for among the candidates?**}\\
  Our system needs to determine **whether** **developer is worthy of attention and if he should be considered further in the recruitment process.** **The answer to this question should explain what** skills are considered important among companies.
- \emph{RQ2: How **a given** repository **makes** a good impression?}\\
  One way of **assessing** developer expertise is to analyse his projects. Thus, we should determine which features of repositories are the most representative ones.
- \emph{RQ3: **Is it possible to get a good enough information about the candidate's potential based on the GitHub profile?**}\\
  **This** question should **provide** us with information **whether** **the recommendation** system based on **repositories** is worth devoting time.
- \emph{RQ4: Is Github repository used only for programming purposes?}\\
  **It often happens that an item is used contrary to the original intention of the author.** Same situation might **occur** with the repositories. **There is no compulsion to prohibit the use of a repository for purposes other than development.**

## End

```latex
Research questions presented below should explain to help understand the importance of creating such tool and also provide an information about the functionalities which potential end user might need (i.e. - recruiters, developers themselves). Furthermore we also explore issues related to the recruitment itself, as well as the quality of repositories.

Hence, we defined four research questions.
\begin{itemize}
- \emph{RQ1: What are the most common skills the company is looking for among the candidates?}\\
  Our system needs to determine whether developer is worthy of attention and if he should be considered further in the recruitment process. The answer to this question should explain what skills are considered important among companies.
- \emph{RQ2: How a given repository makes a good impression?}\\
  One way of assessing developer expertise is to analyse his projects. Thus, we should determine which features of repositories are the most representative ones.
- \emph{RQ3: Is it possible to get a good enough information about the candidate's potential based on the GitHub profile?}\\
  This question should provide us with information whether the recommendation system based on repositories is worth devoting time.
- \emph{RQ4: Is Github repository used only for programming purposes?}\\
  It often happens that an item is used contrary to the original intention of the author. Same situation might occur with the repositories. There is no compulsion to prohibit the use of a repository for purposes other than development.
\end{itemize}
```

# 3

## Pre

```latex
Search engines used to the proces of finding proper resoures are Google Scholar and Scoupus. Results were provided with the usage of a defined search string which presents as follows :
\begin{itemize}
    \item Google Schoolar : (skill and repository) or ( (recruitment or hiring OR interview))
or ((github OR gitlab ) AND repository AND (programming purpose)) AND ("Mining Software Repositories" or "Computer science")
    \item  Scopus : ( skill AND repository ) OR ( ( recruitment OR hiring OR interview ) ) OR ( ( github OR gitlab ) AND repository AND ( programming AND purpose ) ) AND "Mining Software Repositories" AND "Computer science" AND ( LIMIT-TO ( PUBYEAR , 2021 ) OR LIMIT-TO ( PUBYEAR , 2020 ) OR LIMIT-TO ( PUBYEAR , 2019 ) OR LIMIT-TO ( PUBYEAR , 2018 ) OR LIMIT-TO ( PUBYEAR , 2017 ) ) AND ( LIMIT-TO ( EXACTKEYWORD , "Software Engineering" ) ) - Because of enormous number of results in Scopus we decided to add another limitations such as exact keyword: "Software Engineering" and years of publication: 2017-2021.
\end{itemize}
They gave us a good amount of publications which needed to be filtered. Unfortunately many of them did not answear to the questions that we established and also were not in English. As shown on the Fig. 1 search engines provided us with over two hundred publication. Finally we sticked with only ten valuable articles.
```

## Post

**We used search engines (Google Scholar and Scopus) in order to find proper resources and currently available papers on the subject that is investigated by our paper.** **We searched the studies we received using pre-defined search string which is given below~\ref{lst:search-string-google}~\ref{lst:search-string-scopus}.**

**\begin{itemize}
\item Google Scholar: \\
\begin{lstlisting}[language=Python, label={lst:search-string-google}]
(skill and repository) or
(recruitment or hiring OR interview) or
(
(github OR gitlab) AND
repository AND
(programming purpose)
) AND
("Mining Software Repositories" or "Computer science")
\end{lstlisting}
\item Scopus: \\
\begin{lstlisting}[language=Python, label={lst:search-string-scopus}]
( skill AND repository ) OR
( recruitment OR hiring OR interview ) OR
(
( github OR gitlab ) AND
repository AND
( programming AND purpose )
) AND
"Mining Software Repositories" AND
"Computer science" AND
(
LIMIT-TO ( PUBYEAR , 2021 ) OR
LIMIT-TO ( PUBYEAR , 2020 ) OR
LIMIT-TO ( PUBYEAR , 2019 ) OR
LIMIT-TO ( PUBYEAR , 2018 ) OR
LIMIT-TO ( PUBYEAR , 2017 )
) AND
( LIMIT-TO ( EXACTKEYWORD , "Software Engineering" ) )
\end{lstlisting}** \\
Because of enormous number of results **obtained via** Scopus we decided to add **additional constraints** such as **exact presence of keyword** "Software Engineering" and **limit the publication year to**: 2017-2021.
**\end{itemize}**

This gave us a good amount of publications which needed to be further **filtered by hand**. **Unfortunately, many** of them did not answer the **previously established research** questions and also **many of them** were not in English **language**. As shown on **the~\ref{fig:literature-identification}** search engines provided us with over two hundred **publications**. **In the end, we've identified ten of the most important studies that are helpful in our topic.**

\begin{figure}[htp]
\centering
\includegraphics[width=11cm]{searchProcess11}
\caption{Literature identification}
**\label{fig:literature-identification}**
\end{figure}

## End

```latex
We used search engines (Google Scholar and Scopus) in order to find proper resources and currently available papers on the subject that is investigated by our paper. We searched the studies we received using pre-defined search string which is given below~\ref{lst:search-string-google}~\ref{lst:search-string-scopus}.

\begin{itemize}
\item Google Scholar: \\
\begin{lstlisting}[language=Python, label={lst:search-string-google}]
(skill and repository) or
(recruitment or hiring OR interview) or
(
    (github OR gitlab) AND
    repository AND
    (programming purpose)
) AND
("Mining Software Repositories" or "Computer science")
\end{lstlisting}
\item Scopus: \\
\begin{lstlisting}[language=Python, label={lst:search-string-scopus}]
( skill AND repository ) OR
( recruitment OR hiring OR interview ) OR
(
    ( github OR gitlab ) AND
    repository AND
    ( programming AND purpose )
) AND
"Mining Software Repositories" AND
"Computer science" AND
(
    LIMIT-TO ( PUBYEAR , 2021 ) OR
    LIMIT-TO ( PUBYEAR , 2020 ) OR
    LIMIT-TO ( PUBYEAR , 2019 ) OR
    LIMIT-TO ( PUBYEAR , 2018 ) OR
    LIMIT-TO ( PUBYEAR , 2017 )
) AND
( LIMIT-TO ( EXACTKEYWORD , "Software Engineering" ) )
\end{lstlisting} \\
Because of enormous number of results in Scopus we decided to add another limitations such as exact keyword: "Software Engineering" and years of publication: 2017-2021.
\end{itemize}

This gave us a good amount of publications which needed to be further filtered by hand. Unfortunately, many of them did not answer the previously established research questions and also many of them were not in English language. As shown on the~\ref{fig:literature-identification} search engines provided us with over two hundred publications. In the end, we've identified ten of the most important studies that are helpful in our topic.

\begin{figure}[htp]
\centering
\includegraphics[width=11cm]{searchProcess11}
\caption{Literature identification}
\label{fig:literature-identification}
\end{figure}
```
