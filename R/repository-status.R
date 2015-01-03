library("ggplot2")
library("plyr")

# data.frame of organizations.csv content
org.df <- read.csv("./data/organizations.csv")

# bar chart representing total public repositories
gplot <- ggplot(org.df, aes(x = organization, y = public_repos))
gplot <- gplot + geom_bar(stat = "identity")

# mean of the group, Avg. public repos
avg.repos <- mean(org.df$public_repos)

# Add the mean of this group as a horizontal line
gplot <- gplot + geom_hline(aes(yintercept = as.numeric(avg.repos)), linetype = "dotdash")
gplot + geom_text(aes(y=avg.repos, x=0.67, label="Avg. Repos", angle=90))
