# load required libraries
library("ggplot2")
library("plyr")

# data.frame for repository information
repos.df <- read.csv("./data/repositories.csv")
# data.frame for forked repository's information
forked.repos.df <- read.csv("./data/forked_repo_stats.csv")

# count forked repository for each  organization
forks.df <- ddply(repos.df, .(organization), summarise, forks = sum(is_fork))
forks <- forks.df$forks

# count source(original; not a fork) repository for each organization
sources.df <- ddply(repos.df, .(organization), summarise, sources = sum(!is_fork))
sources <- sources.df$sources

# count unactive fork repository for each organization
unactive.forks.df <- ddply(forked.repos.df, .(organization), summarise, unactive_forks = sum(!commits))
unactive.forks <- unactive.forks.df$unactive_forks

# cover missing values for organizations without any forked repo
unactive.forks <- c(unactive.forks[1:8], 0, unactive.forks[9:11], 0, unactive.forks[12])

# count active fork repositories for each organization
active.forks <- forks - unactive.forks

# resultant data frame with repository attribute stats of all organization's repos
result.df <- data.frame(
  organization = forks.df$organization,
  active_forks = active.forks,
  unactive_forks = unactive.forks,
  sources = sources
)