import pandas as pd
from flask import Flask,  render_template, request, redirect, url_for, send_from_directory,jsonify, Response
from json import dumps
import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory,jsonify

app = Flask(__name__)

app.config['DATA_FOLDER'] = os.path.join(app.root_path, 'static/database/clicks/')
click_files = [app.config['DATA_FOLDER'] + x for x in os.listdir(app.config['DATA_FOLDER'])]
click_files.sort()
list_click_file_to_df = [pd.read_csv(x, index_col=None, header=0) for x in click_files]
list_click_file_to_df_cleaned = [x.drop(columns = ['session_id',
                                                   'session_start',
                                                   'session_size',
                                                   'click_timestamp',
                                                   'click_environment',
                                                   'click_deviceGroup',
                                                   'click_os',
                                                   'click_country',
                                                   'click_region',
                                                   'click_referrer_type']) for x in list_click_file_to_df]
all_clicks_df = pd.concat(list_click_file_to_df_cleaned , axis=0, ignore_index=True)
usrlist=all_clicks_df['user_id'].unique()

def json ( response='', code=200, headers=None ) :
    return Response(dumps(response), code, mimetype='application/json', headers=headers)








@app.route("/")
def index () :
    return render_template('index.html', len=len(usrlist), usrlist=usrlist)



if __name__ == "__main__" :
    app.run()