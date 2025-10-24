from flask import Flask, render_template_string
from calculator import sumar, restar, multiplicar, dividir

app = Flask(__name__)

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Calculadora - Anchapanta</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }
        .container {
            background: rgba(255, 255, 255, 0.1);
            padding: 30px;
            border-radius: 10px;
            backdrop-filter: blur(10px);
        }
        h1 {
            text-align: center;
            margin-bottom: 30px;
        }
        .operation {
            background: rgba(255, 255, 255, 0.2);
            padding: 15px;
            margin: 10px 0;
            border-radius: 5px;
        }
        .result {
            font-size: 24px;
            font-weight: bold;
            color: #4ade80;
        }
        .test-status {
            background: #10b981;
            padding: 20px;
            border-radius: 5px;
            margin-top: 20px;
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🧮 Calculadora Web - Mayte Anchapanta</h1>
        
        <div class="operation">
            <h3>➕ Suma: 10 + 5</h3>
            <p class="result">Resultado: {{ suma }}</p>
        </div>
        
        <div class="operation">
            <h3>➖ Resta: 10 - 5</h3>
            <p class="result">Resultado: {{ resta }}</p>
        </div>
        
        <div class="operation">
            <h3>✖️ Multiplicación: 10 × 5</h3>
            <p class="result">Resultado: {{ multiplicacion }}</p>
        </div>
        
        <div class="operation">
            <h3>➗ División: 10 ÷ 5</h3>
            <p class="result">Resultado: {{ division }}</p>
        </div>
        
        <div class="test-status">
            <h2> Aplicación funcionando correctamente</h2>
            <p>Todas las operaciones se ejecutaron exitosamente</p>
            <p>Docker Container: appanchapanta:1.0</p>
        </div>
    </div>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(
        HTML_TEMPLATE,
        suma=sumar(10, 5),
        resta=restar(10, 5),
        multiplicacion=multiplicar(10, 5),
        division=dividir(10, 5)
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=False)
