# load required libraries
library("ggplot2")

# source data date.frame
repos.df <- read.csv("./data/repositories.csv")

# add repo index number for each repository
rows <- nrow(repos.df)
repos.df$repo_index <- seq(1:rows)

# plot a bar chart showing distribution of stars for each organization's repos
gplot <- ggplot(repos.df, aes(fill = organization))
gplot <- gplot + labs(y = "No. of Stars", title = "Distribution of stars on repositories", x = "")
gplot <- gplot + geom_bar(aes(x = repo_index, y = stars), stat = "identity")