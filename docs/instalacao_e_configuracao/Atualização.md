# Atualizando o TIMTec para uma nova versão

As versões do TIMTec estão disponíveis aqui: https://github.com/institutotim/timtec/releases

Cada versão do TIMTec é uma tag no repositório git.

## Verificando repositório

O primeiro passo é verificar se o repositório do código fonte é `https://github.com/institutotim/timtec.git`.

Para verificar qual a origem do código é necessário executar o comando `git remote -v`, e o resultado deve ser parecido com este:

```
$ git remote -v
origin	https://github.com/institutotim/timtec.git (fetch)
origin	https://github.com/institutotim/timtec.git (push)
```

Se o endereço do repositório que aparecer for igual ao que está acima, basta ir para o próximo passo.

Caso o endereço do repositório for diferente deste, será necessário alterá-lo. Para efetuar a alteração é necessário utilizar a seguinte linha de comando:

```
$ git remote set-url origin https://github.com/institutotim/timtec.git
```

Depois de executar o comando acima, basta a url do repositório utilizando novamente o ocmando `git remote -v`

```
$ git remote -v
origin	https://github.com/institutotim/timtec.git (fetch)
origin	https://github.com/institutotim/timtec.git (push)
```

## Atualizando o código

Após confirmar o repositório de origem da aplicação, O próximo passo é atualizar o código. Dentro da raiz do repositório, com o usuário criado para instalação do software, execute:

```
$ git pull
$ git checkout NOME-DA-VERSAO
```

Onde o NOME-DA-VERSAO deve ser substítuido pela tag da versão desejada. Exemplo: `git checkout v3.1.1`.

Ainda na raiz do repositório, basta executar o comando `make update` para efetuar a alteração da instalação.

`$ make update`

Feito isso, o software estará atualizado.
