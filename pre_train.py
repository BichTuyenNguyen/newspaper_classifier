import os
from underthesea import word_tokenize

main_path = os.getcwd()
root_path = os.path.join(main_path, "data")
dest_path = os.path.join(main_path, "data_token")


class Token:
    def __init__(self, root_path, dest_path):
        self.root_path = root_path
        self.dest_path = dest_path
        pass

    def create_dest_dir(self):
        if not os.path.exists(self.dest_path):
            os.mkdir(self.dest_path)
        for (dirpath, dirnames, filenames) in os.walk(self.root_path):
            for dname in dirnames:
                if not os.path.exists(os.path.join(self.dest_path, dname)):
                    os.makedirs(os.path.join(self.dest_path, dname))


    def token_folder(self):
        print("start...")
        os.chdir(self.root_path)
        for (dirpath, dirnames, filenames) in os.walk(self.root_path):
            for dirname in dirnames:
                rpath = os.path.join(self.root_path, dirname)
                dpath = os.path.join(self.dest_path, dirname)
                os.chdir(rpath)
                for fname in os.listdir(rpath):
                    with open(fname, "r+", encoding="utf-8") as f:
                        sentence = f.readlines()
                        sens = ''.join(sentence).lower().strip()
                        token_string = word_tokenize(sens, format="text")
                        os.chdir(dpath)
                        with open(fname, "w+", encoding="utf-8") as w:
                            w.write(token_string)
                    os.chdir(rpath)
        print("finish!")

# to = token(root_path,dest_path)
