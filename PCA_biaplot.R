#####intalling the ggbiplot
library(devtools) 
install_github("vqv/ggbiplot")


###loading ggbiplot
library(ggbiplot)
te<-read.csv("five-siginificant-PCA.txt",sep='\t',header=T)##input complete file
te.pca <- prcomp(te, scale. = TRUE)
ggbiplot(te.pca, obs.scale = 1, var.scale = 1, groups = te2$species, ellipse = TRUE, circle = TRUE) + scale_color_discrete(name = '') + theme(legend.direction = 'horizontal', legend.position = 'top')+theme_bw()