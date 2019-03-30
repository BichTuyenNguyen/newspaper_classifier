from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import metrics
from sklearn.model_selection import train_test_split
import os, pickle, pandas as pd


###
# Vectorizer Function
###
def vectorizer_by_tfidf(dataset_train, dataset_test):
    v = TfidfVectorizer()
    vectors_train = v.fit_transform(dataset_train)
    vectors_test = v.transform(dataset_test)

    return vectors_train, vectors_test


###
# Load data function
###
def _load_dataset(path, cached_file="DATASET.sav"):
    if os.path.exists(cached_file):
        df_train = pickle.load(open(cached_file, "rb"))
    else:
        dataset = []
        os.chdir(path)
        for (dirpath, dirnames, filenames) in os.walk(path):
            for dirname in dirnames:
                rpath = os.path.join(path, dirname)
                os.chdir(rpath)
                for fname in os.listdir(rpath):
                    with open(fname, "r+", encoding="utf-8") as f:
                        item = {
                            "feature": f.read(),
                            "target": dirname,
                            "filename": fname
                        }
                        print(item)
                        dataset.append(item)
                    os.chdir(rpath)

        df_train = pd.DataFrame(dataset)

        pickle.dump(df_train, open(cached_file, "wb"))

    return df_train


###
#  Prediction Algorithm
###
def SVM_classifier(vectors_train, target_train, vectors_test, target_test):
    from sklearn import svm

    clf = svm.SVC(gamma='scale', decision_function_shape='ovo')
    clf.fit(vectors_train, target_train)
    pred = clf.predict(vectors_test)

    result = metrics.f1_score(target_test, pred, average="macro")
    print("F-measure (SVM): ", result)

    return pred


def logistic_input(vectors_train, target_train, vectors_test):
    from sklearn import svm

    clf = svm.SVC(gamma='scale', decision_function_shape='ovo')
    clf.fit(vectors_train, target_train)
    pred = clf.predict(vectors_test)

    return pred

def predict():
    print("loading, please waiting....")
    path = r"E:\OU\Project_Web_Recommand\newspaper_classification\data_token"
    cached_file = os.path.join(r"E:\OU\Project_Web_Recommand\newspaper_classification", "DATASET.sav")
    os.chdir(path)
    dataset = _load_dataset(path,cached_file)

    data_train, data_test, target_train, target_test = train_test_split(dataset['feature'], dataset['target'], test_size=0.3, random_state=42)
    vectors_train, vectors_test = vectorizer_by_tfidf(data_train, data_test)
    print("vector success....")
    pred1 = SVM_classifier(vectors_train=vectors_train,
                                           target_train=target_train,
                                           vectors_test=vectors_test,
                                           target_test=target_test)
    print(pred1)


def demo(sentence):
    from underthesea import word_tokenize
    path = r"E:\OU\Project_Web_Recommand\newspaper_classification\data_token"
    cached_file = os.path.join(r"E:\OU\Project_Web_Recommand\newspaper_classification", "DATASET.sav")
    os.chdir(path)
    dataset = _load_dataset(path, cached_file)

    sens = ''.join(sentence).lower().strip()
    token_sens = word_tokenize(sens, format="text")
    test_list = []
    test_list.append(token_sens)
    v = TfidfVectorizer()
    vectors_train = v.fit_transform(dataset["feature"])
    vectors_test = v.transform(test_list)

    pred = logistic_input(vectors_train=vectors_train,
                                           target_train=dataset['target'],
                                           vectors_test=vectors_test)
    print("Kết quả dự đoán là: ", pred)


# sentence = input("Nhập bài báo: ")
# demo(sentence)

predict()