document.addEventListener('DOMContentLoaded', () => {
    const table = document.getElementById('data-table');
    const tableHead = table.querySelector('thead');
    const tableBody = table.querySelector('tbody');
    const loadingDiv = document.getElementById('loading');

    async function fetchDataAndBuildTable() {
        loadingDiv.style.display = 'block'; 
        table.style.display = 'none';

        try {
            const response = await fetch('/api/data');
            const data = await response.json();

            if (data.error) {
                throw new Error(data.error);
            }

            tableHead.innerHTML = "";
            tableBody.innerHTML = "";

            if (data.length > 0) {
                const headers = Object.keys(data[0]);
                const headerRow = document.createElement('tr');
                headers.forEach(headerText => {
                    const th = document.createElement('th');
                    th.textContent = headerText;
                    headerRow.appendChild(th);
                });
                tableHead.appendChild(headerRow);

                data.forEach(item => {
                    const row = document.createElement('tr');
                    headers.forEach(header => {
                        const cell = document.createElement('td');
                        cell.textContent = item[header];
                        row.appendChild(cell);
                    });
                    tableBody.appendChild(row);
                });
            } else {
                 tableBody.innerHTML = '<tr><td colspan="100%">Nenhum dado encontrado.</td></tr>';
            }

        } catch (error) {
            console.error('Erro ao buscar dados:', error);
            tableBody.innerHTML = `<tr><td colspan="100%">Falha ao carregar os dados. Tente novamente mais tarde.</td></tr>`;
        } finally {
            loadingDiv.style.display = 'none';
            table.style.display = 'table';
        }
    }

    fetchDataAndBuildTable();

    setInterval(fetchDataAndBuildTable, 60000);
});