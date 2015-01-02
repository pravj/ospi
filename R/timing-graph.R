# load required libraries
library('ggplot2')
library('scales')

# some global variables used in the process
# GitHub's public launch date
github.created.at = "2008-04-10"

# source data date.frame
df <- read.csv("~/projects/ospi/data/organizations.csv")

# change the both date related columns
# from 'Factor' objects of date timestamps to native 'Date' objects
df$created_at <- as.Date(df$created_at)
df$founded_at <- as.Date(df$founded_at)

# initial ggplot instance with data source as 'sd'
gplot <- ggplot(df, aes(x = organization))
# use linerange geom for vertical bars
gplot <- gplot + geom_linerange(aes(ymin = created_at, ymax = founded_at))

# flip the co-ordinates and now 'dates' are on X-axis
# I saw a use of this because linerange geom doesn't have 'xmin' and 'xmax' args
gplot <- gplot + coord_flip()

# uses a custom time interval to show on X-axis
gplot <- gplot + scale_y_date(lim = c(as.Date("2007-01-01"), as.Date("2013-12-31")), breaks = date_breaks(width = "6 month"))

# add a dashed line that shows GitHub's appearance in the timeline
gplot <- gplot + geom_hline(aes(yintercept = as.numeric(as.Date(github.created.at))), linetype = "dotdash")

# mark points for the foundation time of organizations
gplot <- gplot + geom_point(aes(x = organization, y = founded_at), colour = "#188F57", size = 2.5)

# mark points for the creation time of organization account on GitHub
gplot <- gplot + geom_point(aes(x = organization, y = created_at), colour = "#273e9c", size = 2.5)
