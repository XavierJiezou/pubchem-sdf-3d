from alive_progress import alive_bar
import concurrent.futures as cf
from retrying import retry
import os, requests, time
import pandas as pd


class PubchemSdf():
    def __init__(self):
        self.inp_path = input('Please enter the path of the file in xlsx format: ')
        self.out_path = input('Please enter the name of output-dir to save data: ')

    def get_txt(self, name, c2):
        if not os.path.exists(name):
            with open(name, 'w') as f:
                f.write(c2)
        else:
            pass

    @retry(wait_fixed=3000)
    def get_sdf(self, name, cid, c2):
        if not os.path.exists(name):
            api = f'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{cid}/SDF?record_type=3d'
            res = requests.get(api)
            if res.status_code == 200:
                with open(name, 'wb') as f:
                    f.write(res.content)
            elif res.status_code == 404: # PUGREST.NotFound
                name = f'{name[:-3]}txt'
                self.get_txt(name, c2)
            elif res.status_code == 503: # PUGREST.ServerBusy
                raise RuntimeError('Raise an exception to call retry')
            else:
                raise RuntimeError('Raise an exception to call retry')
        else:
            pass

    def save_file(self, c1, c2, c3):
        if pd.isnull(c3):
            name = f'{self.out_path}/{c1}.txt'
            self.get_txt(name, c2)
        else:
            name = f'{self.out_path}/{c1}.sdf'
            self.get_sdf(name, int(c3), c2)

    def __main__(self):
        df = pd.read_excel(self.inp_path)
        os.makedirs(self.out_path, exist_ok=True)
        with alive_bar(df.shape[0]) as bar:
            with cf.ThreadPoolExecutor() as tp:
                for ind, row in df.iterrows():
                    c1 = row[0]
                    c2 = row[1]
                    c3 = row[2]
                    tp.submit(self.save_file, c1, c2, c3).add_done_callback(lambda func: bar())
        os.system('pause')


if __name__ == '__main__':
    PubchemSdf().__main__()
