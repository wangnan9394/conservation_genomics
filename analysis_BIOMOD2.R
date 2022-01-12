library(BIOMOD)
###coords
CoorXY<-read.csv("CoorXY.txt",sep='\t',header=T)
###data inout
mydata<-read.csv("merge.withresults.keep.txt",sep='\t',header = T)
Initial.State(Response = mydata[,c(22,23)],Explanatory = mydata[,3:21],IndependentResponse =mydata[,c(22,23)],IndependentExplanatory =mydata[,3:21])

Models(GLM = T,TypeGLM = 'poly',Test = 'AIC',GBM = T,No.trees = 2000,GAM = F,Spline = 3,CTA = T,CV.tree = 50,ANN = T,CV.ann = 2,SRE = T,MARS = T,RF = T,NbRunEval =3,DataSplit = 80,Yweights=NULL,Roc=T,Optimized.Threshold.Roc=T,Kappa=T,TSS=T,KeepPredIndependent=T,VarImport=5,NbRepPA=2,strategy="circles",coor=CoorXY,distance=2,nb.absences=1000)

##wild
load("pred/Pred_wild")
load("pred/Pred_wild_indpdt")
level.plot(Pred_wild_indpdt[,"GLM",1,1], CoorXY,title='wild_GLM_indpdt',cex = 0.5)
level.plot(Pred_wild_indpdt[,"GBM",1,1], CoorXY,title='wild_GBM_indpdt',cex = 0.5)
level.plot(Pred_wild_indpdt[,"CTA",1,1], CoorXY,title='wild_CTA_indpdt',cex = 0.5)
level.plot(Pred_wild_indpdt[,"ANN",1,1], CoorXY,title='wild_ANN_indpdt',cex = 0.5)
level.plot(Pred_wild_indpdt[,"SRE",1,1], CoorXY,title='wild_SRE_indpdt',cex = 0.5)
level.plot(Pred_wild_indpdt[,"MARS",1,1], CoorXY,title='wild_MARS_indpdt',cex = 0.5)
level.plot(Pred_wild_indpdt[,"RF",1,1], CoorXY,title='wild_RF_indpdt',cex = 0.5)

##cultivated
load("pred/Pred_cultivated_indpdt")
level.plot(Pred_cultivated_indpdt[,"GLM",1,1], CoorXY,title='cultivated_GLM_indpdt',cex = 0.5)
level.plot(Pred_cultivated_indpdt[,"GBM",1,1], CoorXY,title='cultivated_GBM_indpdt',cex = 0.5)
level.plot(Pred_cultivated_indpdt[,"CTA",1,1], CoorXY,title='cultivated_CTA_indpdt',cex = 0.5)
level.plot(Pred_cultivated_indpdt[,"ANN",1,1], CoorXY,title='cultivated_ANN_indpdt',cex = 0.5)
level.plot(Pred_cultivated_indpdt[,"SRE",1,1], CoorXY,title='cultivated_SRE_indpdt',cex = 0.5)
level.plot(Pred_cultivated_indpdt[,"MARS",1,1], CoorXY,title='cultivated_MARS_indpdt',cex = 0.5)
level.plot(Pred_cultivated_indpdt[,"RF",1,1], CoorXY,title='cultivated_RF_indpdt',cex = 0.5)

#prediction analysis

###load prediction
load("models/wild_GLM_PA1")

###Summary
summary(wild_GLM_PA1)

###sort ANOVA variance 
wild_GLM_PA1$anova

###plotting
par(mfrow=c(2,2))
plot(wild_GLM_PA1)

##GLM
##load("models/Sp277_GLM_PA1")
##summary(Sp277_GLM_PA1)
##Sp277_GLM_PA1$anova##排序anova，方差
##par(mfrow=c(2,2))#排图
##plot(Sp277_GLM_PA1)#展示

##GBM
##library(gbm)
##load("models/Sp277_GBM_PA1")
##summary(Sp277_GBM_PA1)#出图
##plot(Sp277_GBM_PA1,i.var=1)#展示

##CTA
##load("models/Sp277_ANN_PA1")
##load("models/Sp277_CTA_PA1")
##names(Sp277_CTA_PA1)
##Sp277_CTA_PA1$frame
##plot(Sp277_CTA_PA1,margin=0.05)
##text(Sp277_CTA_PA1,use.n=T)



