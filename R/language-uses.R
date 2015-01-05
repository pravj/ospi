# load required libraries
library("ggplot2")
library("plyr")
library("reshape2")

# data.frame that contains language information of repositories
language.df <- read.csv("./data/repositories.csv")

# re-arrange the data.frame by extracting required columns only
language.df <- language.df[, c("organization", "language")]

# vector representing all the languages available
languages <- levels(language.df$language)

# vector representing all the organizations
organizations <- levels(language.df$organization)

# count of total organizations and languages
nlang <- length(languages)
norg <- length(organizations)

# count the occurance of different language for organizations
language.df <- ddply(language.df, .(organization, language), summarise, count = length(language))

# make a new data.frame that takes care of missing languages or each organization
new.language.df <- data.frame(
  organization = sort(rep(organizations, nlang)),
  language = rep(languages, norg),
  count = rep(0, norg * nlang)
)

# merge these two data.frames
# this is the **one should not do** way; but the class is calling me !!
for (i in 1:nrow(language.df)) {
  org <- language.df[i, 1]
  language <- language.df[i, 2]
  count <- language.df[i, 3]
  
  new.language.df[new.language.df$organization == org & new.language.df$language == language, 3] <- count
}

# re-arrange and rename the data.frame; for stacked bar chart
language.df <- melt(new.language.df)

# renders a stacked bar chart for organizations-repository-languages
gplot <- ggplot(language.df, aes(x = organization, y = value, fill = language))
gplot <- gplot + geom_bar(stat = "identity")