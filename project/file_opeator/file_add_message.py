# // -------------------------------------------------------------------
# // Author: WANG GUN
# // Date: 2025/03/14
# // Description:
# // -------------------------------------------------------------------
import os
import pprint

folder_path='/Users/junwang/Downloads/lib'
batch_info= '''// -------------------------------------------------------------------
// Author: WANG JUN
// Date: 2025/03/14
// Description:
// -------------------------------------------------------------------

'''

for root,dirs, files in os.walk(folder_path):
    for filename in files:
        # ファイルのフルパスを作成
        file_path = os.path.join(root,filename)
        if os.path.isfile(file_path):
            # pprint.pprint(f"Processing file: {file_path}")
            try:

                with open(file_path, 'r') as file:
                    content = file.read()
                    if content.startswith("{") or content.startswith("//"):
                        continue
                    
                    pprint.pprint(f"Processing file: {file_path}")
                    new_content = batch_info + content
                    # 必要なら処理後にファイルを書き換える
                    with open(file_path, 'w') as file:
                        file.write(new_content)
            except Exception as e:
                pprint.pprint(f"Error processing {file_path}: {e}")
