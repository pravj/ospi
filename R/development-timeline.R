# load required libraries
library("ggplot2")
library("plyr")
library("reshape2")

# data.frame that contains weekly commit activity for repositories
timeline.df <- read.csv("./data/timeline.csv")

# update lables that shows week number on X-axis to manage space 
colnames(timeline.df) <- c("organization", "repository", paste(seq(1:52), rep("", 52), sep = ""))

# remove a repo(flipkart/linux)'s activity to render things more clear
temp.timeline.df <- timeline.df[-c(71), ]

# re-arrange the data.frames
timeline.df <- melt(timeline.df)
temp.timeline.df <- melt(temp.timeline.df)

# calculates the sum of each week's commits for each organization
timeline.df <- ddply(timeline.df, .(organization, variable), summarise, commits = sum(value))
temp.timeline.df <- ddply(temp.timeline.df, .(organization, variable), summarise, commits = sum(value))

# plot with commit activity of all the repositories
gplot <- ggplot(timeline.df, aes(x = variable, y = commits, group = organization, colour = organization, alpha = 0.5))
gplot <- gplot + labs(x = "Week Index", y = "No. of Commits", title = "Weekly Commit Activity")
gplot <- gplot + geom_line()

# zoom plot of original plot to make things more clear
temp.gplot <- ggplot(temp.timeline.df, aes(x = variable, y = commits, group = organization, colour = organization, alpha = 0.5))
temp.gplot <- temp.gplot + labs(x = "Week Index", y = "No. of Commits", title = "Weekly Commit Activity")
temp.gplot <- temp.gplot + geom_line()