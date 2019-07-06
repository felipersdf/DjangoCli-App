const cep = document.querySelector('#id_cep')
const logradouro = document.querySelector('#id_logradouro')
const bairro = document.querySelector('#id_bairro')
const cidade = document.querySelector('#id_cidade')
const estado = document.querySelector('#id_estado')

if(cep) {
    cep.addEventListener('blur', function() {
        let cep2 = cep.value
        let url = `https://viacep.com.br/ws/${cep2}/json/`
            fetch(url)
                .then(response => response.json())
                .then(data => {
                    logradouro.value = data.logradouro
                    bairro.value = data.bairro
                    estado.value = data.uf
                    cidade.value = data.localidade
                })
    })
}