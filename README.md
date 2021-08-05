# 简介
根据`C`列信息，从网站[Pubchem](https://pubchem.ncbi.nlm.nih.gov/)下载3D结构的`sdf`文件，并且将文件命名为`A`列的名称，若`C`列数据为空，则另存`B`列对应的值为`txt`文件，并且将其命名为`A`列名称。
# 接口
[https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/2244/SDF?record_type=3d](https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/2244/SDF?record_type=3d)
# 安装
```bash
pip install pandas
pip install requests
pip install retrying
pip install alive_progress
```
# 用法
```bash
python main.py
```
# 打包
```bash
git clone https://github.com/XavierJiezou/pubchem-sdf-3d.git
cd pubchem-sdf-3d
pip install pipenv
pipenv install
pipenv shell
pip install pandas
pip install openpyxl
pip install requests
pip install retrying
pip install alive_progress
pip install pyinstaller
pyinstaller -F -i favicon.ico main.py
```
# 参考
> [https://pubchemdocs.ncbi.nlm.nih.gov/pug-rest](https://pubchemdocs.ncbi.nlm.nih.gov/pug-rest)