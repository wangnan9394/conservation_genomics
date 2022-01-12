###denpend on R package-dismo

###prepared datasets of kumquat collection (Lon and Lat) and WorldClim database tif1-19

if (maxent()) {
     # get predictor variables
     fnames <- list.files(path=paste(system.file(package="dismo"), '/clim', sep=''),###climates-bil-files
                          pattern='bil', full.names=TRUE )
     predictors <- stack(fnames)
     #plot(predictors)
     # file with presence points
     ####NOTE!! input your data, my data set as 'sjg' here
     # witholding a 20% sample for testing
     fold <- kfold(sjg, k=5)
     occtest <- sjg[fold == 1, ]
     occtrain <- sjg[fold != 1, ]
     # fit model, biome is a categorical variable
      me <- maxent(predictors, occtrain,factors=c('tif1',"tif2",'tif3',"tif4",'tif5',"tif6",'tif7',"tif8",'tif9',"tif10","tif11","tif12","tif13",'tif14',"tif15",'tif16',"tif17",'tif18',"tif19"))###factors
     # see the maxent results in a browser:
     me
     # use "args"
     # me2 <- maxent(predictors, occtrain, factors=c("bio_1"), args=c("-J", "-P"))
     # plot showing importance of each variable
     plot(me)
     # response curves
     # response(me)
     # predict to entire dataset
     r <- predict(me, predictors)
     # with some options:
     # r <- predict(me, predictors, args=c("outputformat=raw"), progress='text',
     # filename='maxent_prediction.grd')
     plot(r)
     
}

## The grd file was transformed to tif for downstream analysis