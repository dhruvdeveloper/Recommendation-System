import numpy as np
import pandas as pd

bookDF = pd.read_csv('input/books.csv')
bookDF = bookDF.drop(['small_image_url', 'title', 'best_book_id', 'isbn', 'isbn13','work_text_reviews_count','ratings_1','ratings_2','ratings_3','ratings_4','ratings_5'], axis=1)
ratingsDF = pd.read_csv('input/ratings.csv')

listOfDictonaries = []
indexMap = {}
reverseIndexMap = {}
ptr = 0
testdf = ratingsDF
testdf = testdf[['user_id', 'rating']].groupby(testdf['book_id'])
for groupKey in testdf.groups.keys():
    tempDict = {}

    groupDF = testdf.get_group(groupKey)
    for i in range(0, len(groupDF)):
        tempDict[groupDF.iloc[i, 0]] = groupDF.iloc[i, 1]
    indexMap[ptr] = groupKey
    reverseIndexMap[groupKey] = ptr
    ptr = ptr + 1
    listOfDictonaries.append(tempDict)

from sklearn.feature_extraction import DictVectorizer

dictVectorizer = DictVectorizer(sparse=True)
vector = dictVectorizer.fit_transform(listOfDictonaries)

from sklearn.metrics.pairwise import cosine_similarity

pairwiseSimilarity = cosine_similarity(vector)


returnDetail1 = {}
returnDetail2 = {}
returnDetail3 = {}
returnDetails = []
resultdict={}
count = []
def printBookDetails(bookID):
    returnDetail1['a' + str(len(count))] = (bookDF[bookDF['id'] == bookID]['original_title'].values[0])
    returnDetail2['b' + str(len(count))] = (bookDF[bookDF['id'] == bookID]['authors'].values[0])
    returnDetail3['c' + str(len(count))] = (bookDF[bookDF['id'] == bookID]['image_url'].values[0])
    count.append('1')


def getTopRecommandations(bookID):
    returnDetail1.clear()
    returnDetail2.clear()
    returnDetail3.clear()
    returnDetails.clear()
    count.clear()
    row = reverseIndexMap[bookID]
    print("------INPUT BOOK--------")
    printBookDetails(bookID)
    print("-------RECOMMENDATIONS----------")
    similarBookIDs = [printBookDetails(indexMap[i]) for i in np.argsort(pairwiseSimilarity[row])[-10:-1][::-1]]
    returnDetails.append(returnDetail1)
    returnDetails.append(returnDetail2)
    returnDetails.append(returnDetail3)
    return returnDetails
    # resultdict['original_title'] = returnDetail1
    # resultdict['authors'] = returnDetail2
    # resultdict['image_url'] = returnDetail2
    # print(resultdict)
    # return resultdict

a = getTopRecommandations(1245)
print(a)
