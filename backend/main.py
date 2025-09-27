import gspread
import pandas as pd
from google.oauth2.service_account import Credentials
from flask import Flask, jsonify, send_from_directory
import os
import re
import json


SPREADSHEET_ID = '1OO7gDKXv4YJiDfpfrIHaXIa_XUgDhl3rG2FQImQ-ixY' 
SHEET_NAME = 'Sessões de Cadastros' 
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']



def validar_e_formatar_cpf(cpf):
    cpf_str = str(cpf)
    cpf_limpo = re.sub(r'\D', '', cpf_str)

    if len(cpf_limpo) != 11 or len(set(cpf_limpo)) == 1:
        return "CPF Inválido"

    try:
        soma = sum(int(cpf_limpo[i]) * (10 - i) for i in range(9))
        digito_1 = (soma * 10) % 11
        if digito_1 == 10: digito_1 = 0
        if digito_1 != int(cpf_limpo[9]):
            return "CPF Inválido"

        soma = sum(int(cpf_limpo[i]) * (11 - i) for i in range(10))
        digito_2 = (soma * 10) % 11
        if digito_2 == 10: digito_2 = 0
        if digito_2 != int(cpf_limpo[10]):
            return "CPF Inválido"
        
        return f"{cpf_limpo[:3]}.{cpf_limpo[3:6]}.{cpf_limpo[6:9]}-{cpf_limpo[9:]}"

    except (ValueError, IndexError):
        return "CPF Inválido"

def validar_e_formatar_telefone(numero):
    num_str = str(numero)
    num_limpo = re.sub(r'\D', '', num_str)

    if len(num_limpo) != 13 or not num_limpo.startswith('55') or num_limpo[4] != '9':
        return "Telefone Inválido"

    codigo_pais = num_limpo[:2]
    ddd = num_limpo[2:4]
    primeira_parte = num_limpo[5:9]
    segunda_parte = num_limpo[9:]
    
    return f"+{codigo_pais} ({ddd}) 9{primeira_parte}-{segunda_parte}"

app = Flask(__name__, static_folder='../frontend', static_url_path='/')

def get_data_from_sheet():
    try:
       
        gcp_credentials_str = os.environ.get('GCP_CREDENTIALS')

        
        if not gcp_credentials_str:
            print("ERRO: Variável de ambiente GCP_CREDENTIALS não encontrada.")
            return None
        
      
        gcp_credentials_dict = json.loads(gcp_credentials_str)
        
      
        creds = Credentials.from_service_account_info(gcp_credentials_dict, scopes=SCOPES)
        

        client = gspread.authorize(creds)
        sheet = client.open_by_key(SPREADSHEET_ID).worksheet(SHEET_NAME)
        
        data = sheet.get_all_records()
        df = pd.DataFrame(data)

        df.dropna(how='all', inplace=True)

        if 'timestamp' in df.columns:
            df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce').dt.strftime('%d/%m/%Y %H:%M:%S')

        if 'cpf' in df.columns:
            df['cpf'] = df['cpf'].apply(validar_e_formatar_cpf)

        if 'numero' in df.columns:
            df['numero'] = df['numero'].apply(validar_e_formatar_telefone)
        
        df.fillna('N/A', inplace=True)
        return df

    except Exception as e:
        print(f"ERRO ao buscar dados da planilha: {e}")
        return None

@app.route('/api/data')
def get_data():
    df = get_data_from_sheet()
    if df is not None:
        return jsonify(df.to_dict(orient='records'))
    else:
        return jsonify({"error": "Não foi possível buscar os dados"}), 500

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)