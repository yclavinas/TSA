setwd("~/Documents/SentimentAnalysis/TSA")
library(tm)
library(wordcloud)

text <- readLines("TsukubaShi_noUrl.txt", encoding="UTF-8")

corpus=Corpus(VectorSource(text))
corpus=tm_map(corpus,stripWhitespace)
##Convertetudoparaletraminuscula
corpus=tm_map(corpus,content_transformer(tolower))
##Removepontuacao
corpus<-tm_map(corpus,removePunctuation)
corpus=tm_map(corpus,removeWords,stopwords("english"))

corpus=tm_map(corpus,removeNumbers)
#term-documentmatrix
tdm=TermDocumentMatrix(corpus)
#Definetdmcomoumamatriz
m=as.matrix(tdm)
#Recuperaafrequenciadaspalavrasemordemdecrescente
palavras_freq=sort(rowSums(m),decreasing=TRUE) #Filtraparaficarapenascomaspalavrasmaisfrequentes
lim=quantile(palavras_freq,probs=0.25)
palavras_freq_top=palavras_freq[palavras_freq>lim]
palavras_freq_top=palavras_freq_top[c(-1, -2, -3)]

dm=data.frame(word=names(palavras_freq_top),freq=palavras_freq_top)
#Removeapalavramaisfrequente
wordcloud(dm$word,dm$freq,random.order= T, random.color = F,, colors=brewer.pal(8,"Dark2"))


palavras_freq_top

