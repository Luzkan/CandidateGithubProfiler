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


extractRepoNames <-function(names) {
  toRet <- ""
  for (n in names) {
    toRet <- paste(toRet,n,";")
  }
  toRet
}

getLanguages <- function(languages) {
  toRet <- ""
  for (lang in languages) {
    for (l in lang$node$name){
      toRet <- paste(toRet,l,";")
    }
  }
  toRet
}

getCommitMsg <- function(commits, userName) {
  toRet <- ""
  for (p in commits) {
    tmp <- p$node$author$user$login
    for(i in 1:length(tmp)){
      if( !is.na(tmp[i]) && tmp[i] == userName){
        msg <- p$node$message[i]
        if(!is.na(msg)){
          toRet <- paste(toRet, msg,";" )
        }
        
      }
    }
  }
  toRet
}

calculateAVGCommitTime <- function(commits, userName) {
  if(is.null(commits)) return (NA)
  commitDates <- list()
  
  for(d in commits) {
    tmp <- d$node$author$user$login
    for(i in 1:length(tmp)){
      if( !is.na(tmp[i]) && tmp[i] == userName){
        commitDates <- c(commitDates,d$node$committedDate[i])
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
  if(is.null(json$data$repositoryOwner)){
    return (data.frame(userName, repos=NA,bio=NA,isHireable=NA,commitMessages=NA,languages=NA, avgCommitTime=NA))
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
             commitMessages = getCommitMsg(commitMsgE,userName),
             languages = getLanguages(languages),
             avgCommitTime=calculateAVGCommitTime(commitMsgE, userName))
}



repo_data <- read.csv('D:/Studia_mgr/Semestr_I/PBR/M1/data/cleaned_data.csv')

model_data<- data.frame(link = repo_data$ðŸ...Link.do.GitHuba,  dur = repo_data$âŒš.Jak.dÅ.ugo.to.trwaÅ.o., progDur = repo_data$ðŸ...Jak.dÅ.ugo.trwa.Twoja.przygoda.z.programowaniem.,
                        interviewPer = repo_data$ðŸ..â.ðŸ...Jaki.procent.pracodawcÃ³w.zaprosiÅ.o.CiÄ..na.rozmowÄ..technicznÄ..po.przesÅ.aniu.CV1.,
                        contactPer = repo_data$ðŸ..â.âš.ï..Jaki.procent.pracodawcÃ³w.siÄ..do.Ciebie.odezwaÅ.o.po.przesÅ.aniu.CV1.
)

model_data <- model_data[1:10,]

names <- strsplit(model_data$link, "/")
namesShort <- list()

for(n in names) {
  namesShort <- c(namesShort, tail(n, 1) )
}

resultFrame <- data.frame(userName=character(),bio=character(), isHireable=character())

for (n in namesShort){
  resultFrame <- rbind(resultFrame, getDataFromGitHub(n))
}

result <- cbind(model_data,resultFrame)

