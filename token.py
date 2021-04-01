from itsdangerous import JSONWebSignatureSerializer as Serializer

s = Serializer("sdhfkwhy48y27843784y783sdnfjksdfjk", expires_in=2)

token = s.dumps({"user_id": 14}).decode("utf-8")


s.loads(token).get('user_id')
