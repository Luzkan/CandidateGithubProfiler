# Removing currently stored variables (ex.: from previous sessions)
rm(list=ls())

# Importing Libraries
library("ghql")
library("jsonlite")
library("dplyr")

# Private GitHub Token ( create your own here: https://github.com/settings/tokens/new )
token <- "<token>"

# GraphQL Connection Object (GitHub)
connection <- GraphqlClient$new(
  url = "https://api.github.com/graphql",
  headers = list(Authorization = paste0("Bearer ", token))
)

# GitHub Server doesn't has a schema at the base URL, have to manually load the schema in this case
connection$load_schema()

# Creating new Query
new_query <- Query$new()

# GraphQL Query
new_query$query('mydata', '{
  repositoryOwner(login:"Luzkan") {
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
}')
# Execute Query

(result <- connection$exec(new_query$queries$mydata))

# Parse to more human readable form
jsonlite::fromJSON(result)

# Writing to file
write(result, "output.json")

json <- fromJSON(result)


repositoriesNames <- json$data$repositoryOwner$repositories$edges$node$name
bio <- json$data$repositoryOwner$bio
isHireable <- json$data$repositoryOwner$isHireable
emptyRepos <- json$data$repositoryOwner$repositories$edges$node$isEmpty
commitMsgE <- json$data$repositoryOwner$repositories$edges$node$defaultBranchRef$target$history$edges
commitMSGList <- list()
commitDates <- list()


for(d in commitMsgE) {
  tmp <- d$node$author$user$login
  for(i in 1:length(tmp)){
    if( !is.na(tmp[i]) && tmp[i] == "Luzkan"){
      commitDates <- c(commitDates,d$node$committedDate[i])
    }
  }
}

for (p in commitMsgE) {
  tmp <- d$node$author$user$login
  for(i in 1:length(tmp)){
    if( !is.na(tmp[i]) && tmp[i] == "Luzkan"){
      msg <- p$node$message[i]
      if(!is.na(msg)){
        commitMSGList <- c(commitMSGList, msg )
      }
      
    }
  }
}

languages <- json$data$repositoryOwner$repositories$edges$node$languages$edges
languagesList <- list()

for (l in languages) {
  print(l)
  languagesList <- c(languagesList, l$node$name )
}

#Calculating average time between commits
time_between_commits <- list()

for(idx in seq_along(commitDates)){
  if (idx+1 > length(commitDates)){
    break
  }
  dateOne<-as.POSIXct(commitDates[[idx]], format = "%Y-%m-%dT%H:%M:%SZ")
  dateTwo<-as.POSIXct(commitDates[[idx+1]], format = "%Y-%m-%dT%H:%M:%SZ")
  time_between_commits[[idx]]<- as.numeric(difftime(dateOne,dateTwo, units="mins"))
}

average_time_between_commit <- mean(unlist(time_between_commits))

df <- data.frame(bio, emptyRepos, isHireable,average_time_between_commit,
                 c(repositoriesNames), c(languagesList), c(commitDates), c(commitMSGList))

rm(new_query)

write(result, "output.json")