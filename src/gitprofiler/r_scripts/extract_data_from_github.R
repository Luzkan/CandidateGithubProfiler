library("ghql")
library("jsonlite")
library("dplyr")
rm(list=ls())

queryString1 <- '{
  repositoryOwner(login:"' 

queryString2 <-  '") {
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
}'

# Function extracts reposiotires names from json retrived from github request
# Example usage : extractRepoNames(list(name1, name2, name3))
extractRepoNames <-function(names) {
  toRet <- ""
  for (n in names) {
    toRet <- paste(toRet,n,";")
  }
  toRet
}

#Function extracts languages from json retrived from github request
#Exampleusage : getLanguages(languagesList)
getLanguages <- function(languages) {
  toRet <- ""
  for (lang in languages) {
    for (l in lang$node$name){
      toRet <- paste(toRet,l,";")
    }
  }
  toRet
}

#Function extracts commits messages from json retrived from github request
#Example usage : getCommitMsg(commitsList, "Username")
getCommitMsg <- function(commits, userName) {
  toRet <- ""
  if(!is.null(commits)){
    for (p in commits) {
      tmp <- p$node$author$user
      
      if(!is.null(tmp) && !is.na(tmp)){
        for(i in 1:length(tmp$login)){
          if( !is.na(tmp$login[i]) && !is.null(tmp$login[i]) && tmp$login[i] == userName){
            msg <- p$node$message[i]
            if(!is.na(msg)){
              toRet <- paste(toRet, msg,";" )
            }
            
          }
        }
      }
    }
  }
  toRet
}

#Function calculates average time between commits based on data from github request
#Example usage : calculateAVGCommitTime(commmitsList, "username")
calculateAVGCommitTime <- function(commits, userName) {
  if(is.null(commits)) return (NA)
  commitDates <- list()
  
  for(d in commits) {
    tmp <- d$node$author$user
    if(!is.null(tmp) && !is.na(tmp)){
    for(i in 1:length(tmp$login)){
      if( !is.na(tmp$login[i]) && !is.null(tmp$login[i]) && tmp$login[i] == userName){
        commitDates <- c(commitDates,d$node$committedDate[i])
      }
    }
    }
  }
  time_between_commits <- list()
  average_time_between_commit <- NA
  
  for(idx in seq_along(commitDates)){
    if (idx+1 > length(commitDates)){
      break
    }
    dateOne<-as.POSIXct(commitDates[[idx]], format = "%Y-%m-%dT%H:%M:%SZ")
    dateTwo<-as.POSIXct(commitDates[[idx+1]], format = "%Y-%m-%dT%H:%M:%SZ")
    time_between_commits[[idx]]<- as.numeric(difftime(dateOne,dateTwo, units="mins"))
  }
  average_time_between_commit <- mean(unlist(time_between_commits))
  average_time_between_commit
}

#Function retrives data from github based on provided username and then collects it to data.frame
#Example usage : getDataFromGitHub("Username")
getDataFromGitHub <- function(userName) {
  token <- "f927a6de5f6c2edfd93743bb299ecd11f3f011d7"
  connection <- GraphqlClient$new(
    url = "https://api.github.com/graphql",
    headers = list(Authorization = paste0("Bearer ", token))
  )
  connection$load_schema()
  new_query <- Query$new()
  queryString <- paste(queryString1, userName , queryString2, sep = "")
  new_query$query('mydata', queryString)
  json <- fromJSON(connection$exec(new_query$queries$mydata))
  
  #CheckIfExecuted query
  if(is.null(json$data$repositoryOwner) || length(json$data$repositoryOwner$repositories$edges) < 1){
    return (data.frame(userName, repos=NA,bio=NA,isHireable=NA,languages=NA, avgCommitTime=NA))
  }
  
  #Data from JSON
  repositoriesList <- json$data$repositoryOwner$repositories$edges$node$name
  bio <- json$data$repositoryOwner$bio
  isHireable <- json$data$repositoryOwner$isHireable
  commitMsgE <- json$data$repositoryOwner$repositories$edges$node$defaultBranchRef$target$history$edges
  languages <- json$data$repositoryOwner$repositories$edges$node$languages$edges
  
  #NullCheck
  if(is.null(bio)){
    bio <- NA
  }
  
  data.frame(userName = userName,
             repos = extractRepoNames(repositoriesList),
             bio = bio, 
             isHireable = isHireable,
             languages = getLanguages(languages),
             avgCommitTime=calculateAVGCommitTime(commitMsgE, userName))
}


#Reading data from CSV file provided from questionare
repo_data <- read.csv('D:/Studia_mgr/Semestr_I/PBR/M1/data/cleaned_data.csv', encoding = "UTF-8")

model_data<- data.frame(link = repo_data$X.U.0001F431..Link.do.GitHuba,
                        dur = repo_data$X.U.231A..Jak.d³ugo.to.trwa³o.,
                        progDur = repo_data$X.U.0001F9ED..Jak.d³ugo.trwa.Twoja.przygoda.z.programowaniem.,
                        interviewPer = repo_data$X.U.0001F468..U.200D..U.0001F527..Jaki.procent.pracodawców.zaprosi³o.Ciê.na.rozmowê.techniczn¹.po.przes³aniu.CV1.,
                        contactPer = repo_data$X.U.0001F468..U.200D..U.2696..U.FE0F..Jaki.procent.pracodawców.siê.do.Ciebie.odezwa³o.po.przes³aniu.CV1.
)



#Extracting usernames from CSV file
names <- strsplit(repo_data$X.U.0001F431..Link.do.GitHuba, "/")
namesShort <- list()

for(n in names) {
  namesShort <- c(namesShort, tail(n, 1) )
}

#Creation of empty dataframe
resultFrame <- data.frame(userName=character(),bio=character(), isHireable=character())

#Collecting data for every nickname from github
for (n in namesShort){
  resultFrame <- rbind(resultFrame, getDataFromGitHub(n))
}


#Concat of data from google form and github request
result <- cbind(repo_data,resultFrame)

write.csv(x=result, file="Results.csv")
