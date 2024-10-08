def cpf_invalido(cpf):
    return len(cpf) != 11

def nome_invalido(nome):
    return not nome.isalpha()

def celular_invalido(celular):
    return len(celular) != 13

## Criando método para validações de CPF, nome, celular ##

    def validate(self, dados):
        if len(dados['cpf']) != 11:
            raise serializers.ValidationError({'CPF': 'O CPF deve ter 11 dígitos.'})
        
        if not dados['nome'].isalpha():
            raise serializers.ValidationError({'NOME': 'O nome só pode ter letras.'})
        
        if len(dados['celular']) != 13:
            raise serializers.ValidationError({'CELULAR:' 'O celular precisa ter 13 dígitos.'})
    
        return dados