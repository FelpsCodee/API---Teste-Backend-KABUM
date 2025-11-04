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
            if (altura >= 5 or altura <=140) or (largura >= 13 or largura <= 125) or peso >= 0:
                return jsonify({                       
                                    "nome":"Entrega Ninja",
                                    "valor_frete": f"{valor_frete:.2f}",
                                    "prazo_dias": 6            
                                }),
            
            else:
                return jsonify({"erro": "largura ou altura não corresponde ao tamanho permitido - altura máxima = 140, largura máxima = 125"}),400
                
                
        elif tipo_frete == "kabum":   
            if (altura >= 10 or altura <=200) or (largura >= 6 or largura <= 140) or peso >= 0:
            
                return jsonify({"erro": "largura ou altura não corresponde ao tamanho permitido - altura máxima = 200, largura máxima = 140"}),400
            else:
                valor_frete = (peso * 0.2) /10
                return jsonify({
                                                        
                                    "nome":"Entrega Ninja",
                                    "valor_frete": f"{valor_frete:.2f}",
                                    "prazo_dias": 4            
                                }),
    except Exception as e:
        print(f"{e}")

            
            
if __name__ == '__main__':
    app.run(debug=True)