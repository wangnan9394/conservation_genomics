###usage: Rscript Tif_2_csv.R <input.tif>

library("raster")
r<-raster(file=args[1])
df= as.data.frame(r,xy=T)
write.csv(df,"bio1.csv")
p <- ggplot()+geom_tile(data=df,aes(x=x,y=y,fill=df$pop_den_1995_0.50x0.50))+scale_fill_gradientn(colors=c("white","#A5DEE4","#E83015"))+theme_bw()+xlim(2500,3500)+ylim(1000,1500)
dev.off()