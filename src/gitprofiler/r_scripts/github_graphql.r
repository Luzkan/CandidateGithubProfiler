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
          stargazers {
            totalCount
          }
        }
      }
    }
  }
}')

# Execute Query
(result <- connection$exec(new_query$queries$mydata))

# Parse to more human readable form
jsonlite::fromJSON(result)

# Writing to file
write(result, "output.json")
