# Language (v1)

This file notes all the corrections I made in the language _(spelling / grammar / language / changed sentences / general improvements)_ used in the paper so the original thought behind a sentence can be easily tracked back in case I'll twist the original message. This also contains various `LaTeX` improvements such as added formatting, references, labels, additional use of commands from additional packages and etc.

This file covers:

- Systematic Review
- Research Questions
- Resources to Be Searched
- Results Selection Process
- Literature Review
- Methodology
- Data Collection
- Data Preprocessing

---

# 1 - Systematic Review

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

# 2 - Research Questions

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

# 3 - Resources to Be Searched

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

# 4 - Results Selection Process

## Pre

```latex
Having selected a large number of studies with the search engines we screened titles and abstracts so as to exclude irrelevant papers. Subsequently, we eliminated duplicates. In consequence we obtained 28 results. Eventually, we managed to analyse all of filtered studies and choose 10 the most appropriate ones.
```

## Post

**After running the search string query, we were presented with a large number of results.** **We have went through the results list and discarded all duplicate entries and simultaneously discarded those papers whose titles or abstracts were not related to the topic of our research.** **Thus, we ended up with 28 papers which we further examined. Finally, we have chosen 10 papers which are closely related to the subject of this paper.**

## End

```latex
After running the search string query, we were presented with a large number of results. We have went through the results list and discarded all duplicate entries and simultaneously discarded those papers whose titles or abstracts were not related to the topic of our research. Thus, we ended up with 28 papers which we further examined. Finally, we have chosen 10 papers which are closely related to the subject of this paper.
```

# 5 - Literature Review

## Pre

```latex
Choosed literature gives us answears to the questions asked earlier in this paper and provide us some useful informations. \\Skills which are needed from IT specialists descirbes \cite{StackOverflowStudies} based on job offers posted on Stack Overflow. They extract needed data and then define which hard and soft skills are welcome among recruiters. This study helps us to depict usefull skills and also can help young programmers to find their first dream job as a software engineer. Paper \cite{DoOnBoardingProgramsWork} gives us a very interesting look on boarding programs. It aware us that not every contribiutor to the open source systems is going to be a skilled programer. Based on this article many contributors are people who took part in a boarding program which are mentored by some master. Master gives participants many tips and helps them with their problems. Having that information we should be careful looking at repository contributors because not everyone is going to be professional. Article \cite{GitHubProfilesToJobAdv} shows us how skills extracted from job offers can be matched with developers skills extracted from repositories. Description of data scraping and how matching can be done should be useful in system which is presented in this paper.
\\Subject of repositories is discussed in \cite{MiningGitHub}, they take a deep look into the structure and usage of repositiories. This paper points out that not every repository is used for programming porpuses. Many of the repositories are abandonded few weeks after creation which causes very large actvity in first weeks but with the time passing, activity is decreasing drastically. A good amount of peple are using repositories as a storage or they simply have empty repositories as an effect of some experiments or attempts of learning.
\\Recruitment process is described by the developers in paper \cite{HiringIsBroken} where authors collected data from actuall developers who posted their opinions on social networks. There is said that recruiment process casues a lot of stress and is not liked among developers. Programmers say that during the interview they can not show their whole potential and they are served with excercises which are not useful during normal work and do not check their actuall knowleadge. Developers criticise big companies for their ease of rejecting canditates beacause there are going to be much more candidates and it is not going to be a big mistake if they reject someone good - simply they will find someone else.
\\In recent years there have been carried out a various similar types of research concerning issues related to our study. For instance, there was created an online developer profiling tool assessing developer expertise \cite{GitLabProfilingTool}. The tool considers factors such as code quality, code quantity, contribution to rank  software engineer’s repositories and his skills as well. Evaluations of developers using greater number of features were determined as more accurate ones. However, weight of all of the indicators was equivalent, so none of them could be chosen as the most significant. Moreover, the tool is based on analysis of repositories created on GitLab which is definitely less popular than GitHub.[przypis?]
\\Furthermore, a relation between technical and social skills \cite{WhatMakesGoodDev} was explored also. In the study which aims at finding out what makes developer good we discovered that there is a lack of strong association between above types of skills, so doubtless it is extremely tough to assess soft and social skills mining GitHub repositories.
\\Generally, candidate selection process might be based on LinkedIn profile, CV and Github Profile as well \cite{CandidateSelection}. Although it could be complicated to obtain information about non-technical skills using above resources, personality traits of candidates could be accessed from analyzed transcription of a phone call.
\\In terms of identifying experts in software libraries and frameworks \cite{SoftwareLibraries} it was analyzed which features best distinguish library specialists. First of all, it was explored that the feature values are different for experts in each library. Nevertheless, the features such as number of commits are always relevant.
```

## Post

## End

```latex

```

# 6 - Methodology

## Pre

```latex
In this section we defined methods, techniques, tools and processes referring to the main part of our research.
```

## Post

## End

```latex

```

# 7 - Data Collection

## Pre

```latex
Process of data collection was divided into two steps. First step was to collect github users and data about their skills and job experiences. To do that we used Google Form in which creation of form was very easy and clear. Collected data was saved to CSV file and then properly prepared with R script. Second step was to collect data from repositories. We used usernames provided in the from and then with usage of GitHub GraphQL API we were able get to information which were considered interesting for us.
```

## Post

Our main goal during the data collection process was to obtain GitHub Usernames along with as many answers to questions related to the subject of the recruitment process, assessment of own skills as well as some additional information which could help in the reconstruction of results found in other papers. We have created a Google Form questionnaire and then posted it on two programming-related Facebook Groups.

In both groups, one can find people with a full range of professional experience but based on the activity (posts and comments), one of them is mainly characterized by highly qualified employees (Seniors) while the other seems evenly distributed.

To collect data from GitHub we used GraphQL Queries. The query takes only the username on input and on output puts only the information precisely specified within the query itself.

## End

```latex
\subsubsection{Questionnaire}

Our main goal during the data collection process was to obtain GitHub Usernames along with as many answers to questions related to the subject of the recruitment process, assessment of own skills as well as some additional information which could help in the reconstruction of results found in other papers. We have created a Google Form questionnaire and then posted it on two programming-related Facebook Groups.

In both groups, one can find people with a full range of professional experience but based on the activity (posts and comments), one of them is mainly characterized by highly qualified employees (Seniors) while the other seems evenly distributed.

\subsubsection{Parsing GitHub Information}

To collect data from GitHub we used GraphQL Queries \footnote{GraphQL GitHub API: https://docs.github.com/en/graphql}. The query takes only the username on input and on output puts only the information precisely specified within the query itself. GraphQL Query is presented in~\ref{lst:graphql-query} and output format in~\ref{lst:graphql-output-json}.

\begin{lstlisting}[language=R, label={lst:graphql-query}]
{
  repositoryOwner(login:"<USER_NAME>") {
    repositories(first: 5, orderBy: {field:PUSHED_AT,direction:DESC}, isFork:false) {
      edges {
        node {
          name
          diskUsage
          forkCount
          isEmpty
          languages (first : 10){
            edges{
              size
              node{
                name
              }
            }
          }
          labels (first : 50){
            totalCount
            nodes{
              name
              description
              updatedAt
            }
          }
          issues (first : 20){
            totalCount
            edges{
              node{
                body
                author{
                  login
                }
              }
            }
          }
          stargazers {
            totalCount
          }
          description
          defaultBranchRef{
            target{
              ... on Commit {
                history(first : 10){
                  totalCount
                  edges{
                    node{
                      ... on Commit {
                        message
                        committedDate
                        author{
                          user{
                            login
                          }
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
    ... on User {
      bio
      company
      isHireable
      isViewer
    }
  }
}
\end{lstlisting}

\begin{lstlisting}[language=Python, label={lst:graphql-output-json}]
<OUTPUT_JSON_DAJ_KTOŚ_TU>
\end{lstlisting} \\

```

# 8 - Data Preprocessing

## Pre

```latex
Having collected dataset which was going to be used in a further phase of research we decided to preprocess the data. First and foremost,  we had to reject useless survey answers with no information about GitHub username. Subsequently, we needed to determine which features, obtained from github profiles, can be identified as the most appropriate ones.  After screening the features we also used a special tool called Mega-Linter in order to achieve more indicators about users’s repositories quality. In the end, we prepared a csv file with preprocessed data containing multiple pieces of information about GitHub users and selected features.
```

## Post

## End

```latex

```
