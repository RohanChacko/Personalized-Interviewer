# Personalized Interviewer
Personalized Interview question generator based on intelligent resume parsing using the Stanford Parser server


## Link to presentation
[Google Drive Link](https://drive.google.com/file/d/1GBQjrUJ0pBEuZSbd8A3UT47PZ7_mfnCu/view?usp=sharing)

## Setting up the Parser servers
`cd QuestionGeneration`  
`bash runStanfordParserServer.sh`  
`bash runSSTServer.sh`

## Running the App
` python3 main3.py`

## Directory Structure

```
├── data
│   └── data.csv
├── docs
│   └── Megathon '18 - Joveo.pptx
├── main3.py
├── main.py
├── Original_Resumes
│   ├── 10Jonas.pdf
│   ├── 1Amy.pdf
│   ├── 2Ben.pdf
│   ├── 3Carrie.pdf
│   ├── 3M_Polo Yu_Finance Manager.pdf
│   ├── 4Dickson.pdf
│   ├── 5Edwardo.pdf
│   ├── 6Faye.pdf
│   ├── 7Giraffe.pdf
│   ├── 8Holly.pdf
│   ├── 9Ignatius.pdf
│   ├── a1.pdf
│   ├── a2.pdf
│   ├── Aberdeen_Bernice Tan_Compliance Assistant Manager.pdf
│   ├── Aberdeen_Lester Tan_Client Svcs Exec.pdf
│   ├── ABN AMRO_Husseyn Smili_Relationship Manager Director.pdf
│   ├── ABN_Joyce Shum_Accountant.pdf
│   ├── ABN_Yee Choon Kit_Relationship Manager.pdf
│   ├── Abraaj_Renny Chong_Fundraising Analyst.pdf
│   ├── Accorhotels_Sonya Vij_Legal Counsel.pdf
│   ├── Acion_Jayde Yip_Finance Director.pdf
│   └── Addleshaw_Treliza Li_Office Manager.pdf
├── Parsed_Resumes
├── pdf2txt.py
├── questiongeneration
│   ├── LICENSE
│   ├── QuestionGeneration
│   │   ├── build.sh
│   │   ├── config
│   │   │   ├── anc-v2-written.lm.gz
│   │   │   ├── database_properties.xml
│   │   │   ├── englishFactored.ser.gz
│   │   │   ├── englishPCFG.ser.gz
│   │   │   ├── factual-statement-extractor.properties
│   │   │   ├── file_properties.xml
│   │   │   ├── map_properties.xml
│   │   │   ├── NOUNS_WS_SS_P.gz
│   │   │   ├── QuestionTransducer.properties
│   │   │   ├── stopWordList.txt
│   │   │   ├── superSenseModelAllSemcor.ser.gz
│   │   │   ├── verbConjugations.txt
│   │   │   ├── VERBS_WS_SS.gz
│   │   │   └── wordlists
│   │   │       ├── dist.female.first
│   │   │       ├── dist.female.first.80percent
│   │   │       ├── dist.male.first
│   │   │       ├── dist.male.first.80percent
│   │   │       └── README-word-lists.txt
│   │   ├── dict
│   │   │   ├── adj.dat
│   │   │   ├── adj.exc
│   │   │   ├── adj.idx
│   │   │   ├── adv.dat
│   │   │   ├── adv.exc
│   │   │   ├── adv.idx
│   │   │   ├── cntlist
│   │   │   ├── cntlist.rev
│   │   │   ├── data.adj
│   │   │   ├── data.adv
│   │   │   ├── data.noun
│   │   │   ├── data.verb
│   │   │   ├── frames.vrb
│   │   │   ├── index.adj
│   │   │   ├── index.adv
│   │   │   ├── index.noun
│   │   │   ├── index.sense
│   │   │   ├── index.verb
│   │   │   ├── lexnames
│   │   │   ├── log.grind.3.0
│   │   │   ├── noun.dat
│   │   │   ├── noun.exc
│   │   │   ├── noun.idx
│   │   │   ├── sense.idx
│   │   │   ├── sentidx.vrb
│   │   │   ├── sents.vrb
│   │   │   ├── verb.dat
│   │   │   ├── verb.exc
│   │   │   ├── verb.Framestext
│   │   │   └── verb.idx
│   │   ├── lib
│   │   │   ├── arkref.jar
│   │   │   ├── commons-lang-2.4.jar
│   │   │   ├── commons-logging.jar
│   │   │   ├── junit-3.8.2.jar
│   │   │   ├── jwnl.jar
│   │   │   ├── stanford-parser-2008-10-26.jar
│   │   │   ├── supersense-tagger.jar
│   │   │   └── weka-3-6.jar
│   │   ├── licenses
│   │   │   ├── LICENSE-apache-commons-lang.txt
│   │   │   ├── LICENSE-apache-commons-logging.txt
│   │   │   ├── LICENSE-junit.txt
│   │   │   ├── LICENSE-jwnl.txt
│   │   │   ├── LICENSE-semcor.txt
│   │   │   ├── LICENSE-sst-light.txt
│   │   │   ├── LICENSE-stanfordparser.txt
│   │   │   ├── LICENSE.txt
│   │   │   ├── LICENSE-weka-3.6.txt
│   │   │   ├── LICENSE-wordnet.txt
│   │   │   ├── NOTICE.txt
│   │   │   ├── README-tregex.txt
│   │   │   └── README-tsurgeon.txt
│   │   ├── misc
│   │   │   └── prepare.sh
│   │   ├── models
│   │   │   ├── linear-regression-ranker-reg500.ser.gz
│   │   │   └── qg-training-31-aug-2010.dat
│   │   ├── question-generation.jar
│   │   ├── question_generator.py
│   │   ├── README.txt
│   │   ├── run.sh
│   │   ├── runSSTServer.sh
│   │   ├── runStanfordParserServer.sh
│   │   ├── simplify.sh
│   │   ├── src
│   │   │   └── edu
│   │   │       └── cmu
│   │   │           └── ark
│   │   │               ├── AnalysisUtilities.java
│   │   │               ├── BagOfWordsExtractor.java
│   │   │               ├── GlobalProperties.java
│   │   │               ├── InitialTransformationStep.java
│   │   │               ├── LanguageModel.java
│   │   │               ├── NPClarification.java
│   │   │               ├── ParseResult.java
│   │   │               ├── PorterStemmer.java
│   │   │               ├── QuestionAsker.java
│   │   │               ├── QuestionFeatureExtractor.java
│   │   │               ├── Question.java
│   │   │               ├── QuestionRanker.java
│   │   │               ├── QuestionTransducer.java
│   │   │               ├── ranking
│   │   │               │   ├── BaseRanker.java
│   │   │               │   ├── IRanker.java
│   │   │               │   ├── RandomRanker.java
│   │   │               │   ├── Rankable.java
│   │   │               │   ├── RankerFactory.java
│   │   │               │   ├── RankingEval.java
│   │   │               │   ├── RankingUtils.java
│   │   │               │   ├── RankScorer.java
│   │   │               │   └── WekaLinearRegressionRanker.java
│   │   │               ├── SentenceSimplifier.java
│   │   │               ├── SpecificityAnalyzer.java
│   │   │               ├── StanfordParserServer.java
│   │   │               ├── SuperSenseWrapper.java
│   │   │               ├── tests
│   │   │               │   ├── TestCheckForChanges.java
│   │   │               │   ├── TestNPClarification.java
│   │   │               │   ├── TestQuestions.java
│   │   │               │   ├── TestSentenceSimplifier.java
│   │   │               │   ├── TestSpecificityAnalyzer.java
│   │   │               │   └── TestWhPhraseGenerator.java
│   │   │               ├── TregexPatternFactory.java
│   │   │               ├── VerbConjugator.java
│   │   │               └── WhPhraseGenerator.java
│   │   ├── tests
│   │   │   ├── article461.Mary_II_of_England.txt
│   │   │   └── article461.Mary_II_of_England.txt.questions
│   │   └── train-model-cmd.sh
│   ├── QuestionGeneration.zip
│   ├── question_generator.py
│   ├── question.py
│   └── README.md
└── README.md
```

## Credits
<https://github.com/sumehta/question-generation>
