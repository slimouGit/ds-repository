# dataset source: http://www.math.umd.edu/~slud/s430.old/Data/ESOPH.dat

#Load required libraries
library(tidyverse)

library(ggplot2)
library(ggcorrplot)

#config local source
setwd ("F:/studium/Master/17_2021_SS/DataScience_SS_21/ds-repository/Exercise_05")
esoph <- read.table ("esoph-data.csv")
head(esoph, 10)

print("-----------------------------------------------------")
#number of rows
print(nrow(esoph))
#number of columns
print(ncol(esoph))
print("-----------------------------------------------------")
#Computing statistics for each column
print("summary(esoph)")
summary(esoph)
print("-----------------------------------------------------")
#
print("str(esoph)")
str(esoph)

print("-----------------------------------------------------")
print("mask <- esoph$agegp ==  25-34")
mask <- esoph$agegp == "25-34"
esoph[ mask , ]

print("-----------------------------------------------------")
print("mask <- esoph$agegp ==  35-44")
mask <- esoph$agegp == "35-44"
esoph[ mask , ]

print("-----------------------------------------------------")
print("mask <- esoph$agegp ==  45-54")
mask <- esoph$agegp == "45-54"
esoph[ mask , ]

print("-----------------------------------------------------")
print("mask <- esoph$agegp ==  55-64")
mask <- esoph$agegp == "55-64"
esoph[ mask , ]

print("-----------------------------------------------------")
print("mask <- esoph$agegp ==  65-74")
mask <- esoph$agegp == "65-74"
esoph[ mask , ]

print("-----------------------------------------------------")
print("mask <- esoph$agegp ==  75+")
mask <- esoph$agegp == "75+"
esoph[ mask , ]

print("-----------------------------------------------------")
print("mask <- esoph$ncases > 5")
mask <- esoph$ncases > 5
esoph[ mask , ]
print("-----------------------------------------------------")

#plott some stats
hist(esoph$ncases, xlab="Number of cases")
hist(esoph$ncontrols, xlab="Number of controlls")

#scatterplots
plot (esoph$ncases, esoph$ncontrols)

plot(esoph$ncases, esoph$ncontrols, xlab="Cases", ylab="Controls",
     main="Cases vs Controls", pch=15, col="red")

boxplot (esoph$ncases ~ esoph$agegp,main="Esoph dataset",
         border="gray",lwd=1,col=rainbow(5))


#Grouping by age group, calculate percentage by sum of cases divided by sum of control counts
d1<- esoph %>%  group_by(agegp) %>%
    summarise(count = n(), total_cases = sum(ncases), total_controls = sum(ncontrols),
              percentage=total_cases*100/total_controls)

ggplot(d1, aes(x=d1$agegp, y=d1$percentage,fill=d1$agegp)) +
   geom_bar(stat="identity", position = "dodge") +
   scale_fill_brewer(palette ="Set1")+
   labs(x= 'Age Groups', y= 'Percentage Of Cancer Cases')+
   guides(fill=guide_legend(title="Age Groups"))

#Group by both age and tobacco consumption groups
d2<- esoph %>%  group_by(agegp,tobgp) %>%
    summarise(count = n(), total_cases = sum(ncases), total_controls = sum(ncontrols),
              percentage=total_cases*100/total_controls)

ggplot(d2, aes(x=d2$agegp, y=d2$percentage,fill=d2$tobgp)) +
   geom_bar(stat="identity", position = "dodge") +
   scale_fill_brewer(palette ="Set1")+
   labs(x= 'Age Groups', y= 'Percentage Of Cancer Cases')+
   guides(fill=guide_legend(title="Tobacco Consumption Groups Per Age Group"))


#Group by both age and alcohol consumption groups
d3<- esoph %>%  group_by(agegp,alcgp) %>%
     summarise(count = n(), total_cases = sum(ncases), total_controls = sum(ncontrols),
               percentage=total_cases*100/total_controls)
ggplot(d3, aes(x=d3$agegp, y=d3$percentage,fill=d3$alcgp)) +
   geom_bar(stat="identity", position = "dodge") +
   scale_fill_brewer(palette ="Set1")+
   labs(x= 'Age Groups', y= 'Percentage Of Cancer Cases')+
   guides(fill=guide_legend(title="Alcohol Consumption Groups Per Age Group"))



#effects of both alcohol and tobacco consumption for the whole observations
ggplot(esoph, aes(factor(esoph$alcgp), esoph$ncases*100/esoph$ncontrols, fill = esoph$tobgp)) +
  geom_bar(stat="identity", position = "dodge") +
  scale_fill_brewer(palette ="Set1")+
  labs(x= 'Alcohol Consumption Groups', y= 'Percentage Of Cancer Cases')+
  guides(fill=guide_legend(title="Tobacco Consumption Groups"))