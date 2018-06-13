#
# Paul Evans
# 13 June 2018
#
setwd("~/Work/Noonan")
library(stylo)
stylo.results = stylo(
  gui = FALSE,
  corpus.lang = "Latin.corr"
)
summary(stylo.results)
print(stylo.results$features.actually.used)

