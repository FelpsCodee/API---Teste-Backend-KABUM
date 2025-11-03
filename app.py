from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/calcular-frete", methods=['POST'])
def calcular_frete():
    print("passo1")
    data = request.get_json()
    print("passo2")
    if not data or not "dimensao" in data or not "peso" in data or not "tipo_frete" in data:
        print("passo3")
        return jsonify({"error": "campos não completos ou erro na sintaxe"}), 400
    
    try:
        print("passo4")
        tipo_frete = data['tipo_frete']
        altura = data['dimensao']['altura']
        largura = data['dimensao']['largura']
        peso = data['peso']
        
        print(valor_frete)
        if peso <= 0 :
            return jsonify({[]})
        
        #ENTREGA NINJA
        if (altura < 10 or altura > 200) or (largura < 6 or largura > 140):
            print("passo5")
            return jsonify({"erro": "largura ou altura não corresponde ao tamanho permitido - largura = 200, largura = 140"})
        else:
            print("passoEXTRA")
            return jsonify({
                                                    
                                "nome":"Entrega Ninja",
                                "valor_frete": f"{valor_frete:.2f}",
                                "prazo_dias": 6            
                            })
            
    except Exception as e:
        print(f"{e}")


    if tipo_frete == "Ninja":   
        if (altura < 10 or altura > 200) or (largura < 6 or largura > 140):
        
            return jsonify({"erro": "largura ou altura não corresponde ao tamanho permitido - largura = 200, largura = 140"})
        else:
            valor_frete = (peso * 0.3) /10
            return jsonify({
                                                    
                                "nome":"Entrega Ninja",
                                "valor_frete": f"{valor_frete:.2f}",
                                "prazo_dias": 6            
                            })
            
            
if __name__ == '__main__':
    app.run(debug=True)