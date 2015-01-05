# load required libraries
library("ggplot2")
library("plyr")
library("scales")

# data.frame that contains repository information
repos.df <- read.csv("./data/repositories.csv")

# data.frame that contains organization information
org.df <- read.csv("./data/organizations.csv")

# re-arrange the data.frames to exclude unnecessary columns 
repos.df <- ddply(repos.df, .(organization), summarise, created_at = as.Date(created_at))
org.df <- ddply(org.df, .(organization), summarise, created_at = as.Date(created_at))

# renders point graph; representing each repo creation as a point
gplot <- ggplot(repos.df, aes(x = created_at, y = organization))
gplot <- gplot + labs(x = "", y = "Organizations", title = "Repository Creation Timeline")
gplot <- gplot + geom_point()
gplot <- gplot + scale_x_date(lim = c(as.Date("2009-11-01"), as.Date("2015-01-01")), breaks = date_breaks(width = "6 month"))
gplot <- gplot + geom_point(data = org.df, aes(x = created_at, y = organization), colour = "#00cc00", size = 4, alpha = 0.6)