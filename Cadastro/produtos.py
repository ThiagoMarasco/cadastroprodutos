def produtos(nome,ean,preco,ncm,descricao,marca,anexo1,anexo2,anexo3):
    sep = {
        "produtos": [
            {
                "produto": {
                    "sequencia": 1,
                    "nome": nome,
                    "codigo": ean,
                    "unidade": "unid",
                    "preco": preco,
                    "preco_promocional": 0,
                    "ncm": ncm,
                    "origem": "0",
                    "gtin": ean,
                    "gtin_embalagem": ean,
                    "localizacao": "",
                    "peso_liquido": 0.500,
                    "peso_bruto": 0.500,
                    "estoque_minimo": 1,
                    "estoque_maximo": 0,
                    "estoque_atual": 0,
                    "id_fornecedor": 0,
                    "codigo_fornecedor": "",
                    "codigo_pelo_fornecedor": "",
                    "unidade_por_caixa": "1",
                    "preco_custo": 0,
                    "situacao": "A",
                    "tipo": "P",
                    "cod_lista_servicos": "",
                    "descricao_complementar": descricao,
                    "obs": descricao,
                    "cest": "19.021.00",
                    "valor_max": 0.0,
                    "dias_preparacao": 0,
                    "marca": marca,
                    "tipo_embalagem": 1,
                    "altura_embalagem": 0.0,
                    "largura_embalagem": 0.0,
                    "comprimento_embalagem": 0.0,
                    "diametro_embalagem": 0.0,
                    "categoria": "Cadastros",
                    "anexos": [                   
                        {
                            "anexo": anexo1
                        },
                        {
                            "anexo": anexo2
                        },
                        {
                            "anexo": anexo3
                        }
                    ],
                    "classe_produto": "S",
                    "kit": [],
                    "variacoes": [],
                    "tags": [],
                    "seo": {
                        "seo_title": "",
                        "seo_keywords": "",
                        "link_video": "",
                        "seo_description": "",
                        "slug": ""
                    },

                }
            }
        ]
    }
    return sep
