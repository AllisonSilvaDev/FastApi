fetch('http://127.0.0.1:8000/vendas/1') 
    .then(response => {
        if (!response.ok) {
            throw new Error('Erro na requisição');
        }
        return response.json(); 
    })
    .then(data => {
        console.log(data);
        const dadosDiv = document.getElementById('dados-api');
        dadosDiv.innerHTML = `<p>${data}</p>`;


        dadosDiv.innerHTML = `
                <p>Item: ${data.Item}</p>
                <p>R$${data.preco_uni}</p>
                <p>Quantidade: ${data.quantidade}</p>
            `;
    })
    .catch(error => {
        console.error('Erro:', error);
    });