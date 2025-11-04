from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/calcular-frete", methods=['POST'])
def calcular_frete():
    
    data = request.get_json()
    
    if not data or not "dimensao" in data or not "peso" in data or not "tipo_frete" in data:
        
        return jsonify({"error": "campos não completos ou erro na sintaxe"}), 400
    
    try:
        tipo_frete = data['tipo_frete']
        altura = data['dimensao']['altura']
        largura = data['dimensao']['largura']
        peso = data['peso']
        
        
        if tipo_frete == "ninja":
            if (altura >= 5 and altura <=140) and (largura >= 13 and largura <= 125) and peso >= 0:
                
                valor_frete = (peso * 0.3) /10
                return jsonify({                       
                                    "nome":"Entrega Ninja",
                                    "valor_frete": f"{valor_frete:.2f}",
                                    "prazo_dias": 6            
                                })
            
            else:
                return jsonify([]),400
                
                
        elif tipo_frete == "kabum":   
            if (altura >= 10 and altura <=200) and (largura >= 6 and largura <= 140) and peso >= 0:
                
                valor_frete = (peso * 0.2) /10
                return jsonify({
                                                        
                                    "nome":"Entrega Kabum",
                                    "valor_frete": f"{valor_frete:.2f}",
                                    "prazo_dias": 4            
                                })
            
            else:
                return jsonify([]),400
            
    except Exception as e:
        return jsonify({"erro": f"{e}"})

            
            
if __name__ == '__main__':
    app.run(debug=True)