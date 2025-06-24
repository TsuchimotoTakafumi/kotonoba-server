# kotonoba_server.py
from flask import Flask, request, jsonify
import wikipedia
import flask_cors

app = Flask(__name__)
flask_cors.CORS(app)  # CORS対応（Xcodeからのアクセス許可）

wikipedia.set_lang("ja")  # 日本語に設定

@app.route('/api/kotonoba')
def get_word_meaning():
    word = request.args.get('word', '')
    try:
        summary = wikipedia.summary(word, sentences=2)
        result = summary
    except wikipedia.exceptions.DisambiguationError as e:
        result = f"複数の意味があります。例: {', '.join(e.options[:3])}"
    except wikipedia.exceptions.PageError:
        result = "意味が見つかりませんでした。"
    except Exception as e:
        result = f"エラーが発生しました: {str(e)}"

    return jsonify({'result': result})

if __name__ == '__main__':
    # ポート5001でFlaskを起動
    app.run(debug=True, host='0.0.0.0', port=5001)
