####loading package
library(nicheROVER)

##inout data sets
citrus<-read.csv("citrus.csv",sep=',',header = TRUE)
citrus.par <- tapply(1:nrow(citrus), citrus$species,function(ii) niw.post(nsamples = nsamples, X = citrus[ii,2:3]))###paried format
clrs <- c( "red", "blue") # colors for each species
over.stat <- overlap(citrus.par, nreps = nsamples, nprob = nsamples, alpha = .95)
overlap.plot(over.stat, col = clrs, mean.cred.col = "turquoise",equal.axis = TRUE,xlab = "Overlap Probability (%) -- Niche Region Size: 95%")