<h1>Chat Python - Plataforma Impact</h1>

<p>Este projeto é um sistema de <strong>chat</strong> desenvolvido em <strong>Python</strong> que faz consumo de uma <strong>API</strong> para enviar e receber mensagens entre os alunos da plataforma <strong>Impact</strong>, dentro de uma <strong>VM</strong> (Máquina Virtual) do servidor do <strong>Rafael Fino</strong>, Arquiteto de Software do banco C6 e mentor do curso. O chat é atualizado periodicamente, permitindo a comunicação em tempo real.</p>

<h2>📋 Funcionalidades</h2>
<ul>
  <li><strong>Envio e recebimento de mensagens</strong>: O chat utiliza uma API para conectar e realizar a troca de mensagens entre os usuários.</li>
  <li><strong>Atualização periódica</strong>: O sistema verifica novas mensagens em intervalos regulares, garantindo que as conversas estejam sempre atualizadas.</li>
  <li><strong>Autenticação</strong>: Os usuários precisam autenticar-se na API antes de enviar ou receber mensagens.</li>
  <li><strong>Execução em VM</strong>: O projeto roda dentro de uma VM configurada no servidor de Rafael Fino, usada para testar e desenvolver as funcionalidades.</li>
</ul>

<h2>🚀 Tecnologias Utilizadas</h2>
<ul>
  <li><strong>Python 3</strong>: Linguagem de programação usada para o desenvolvimento do chat.</li>
  <li><strong>API REST</strong>: Para enviar e receber mensagens entre os alunos.</li>
  <li><strong>Biblioteca Requests</strong>: Para fazer as requisições HTTP à API.</li>
  <li><strong>Threading</strong>: Utilizado para permitir que a aplicação receba atualizações de mensagens periodicamente sem bloquear a interface do usuário.</li>
</ul>

<h2>⚙️ Como Funciona</h2>
<ol>
  <li><strong>Autenticação</strong>: O usuário faz login no sistema utilizando suas credenciais.</li>
  <li><strong>Envio de Mensagens</strong>: Após autenticado, o usuário pode enviar mensagens para outros alunos conectados à API.</li>
  <li><strong>Recebimento de Mensagens</strong>: O sistema verifica periodicamente a API para atualizar o feed de mensagens em tempo real.</li>
</ol>

<h2>🛠️ Configuração e Execução</h2>

<h3>1. Pré-requisitos</h3>
<ul>
  <li>Python 3.x instalado na VM.</li>
  <li>Instalar as dependências necessárias:</li>
</ul>

<pre><code>pip install requests</code></pre>

<h3>2. Configuração da API</h3>
<p>No código, configure a URL da API e as credenciais de login para se conectar ao sistema:</p>

<pre><code>server_url = "URL_DA_API"
user_data = {
    'name': "SeuNome",
    'password': "SuaSenha"
}</code></pre>

<h3>3. Executando o Chat</h3>
<p>Para executar o chat, rode o seguinte comando:</p>

<pre><code>python3 nome_do_arquivo.py</code></pre>

<h2>📈 Atualizações Futuras</h2>
<ul>
  <li>Adicionar criptografia nas mensagens para maior segurança.</li>
  <li>Implementar suporte a múltiplos canais de chat.</li>
  <li>Melhorar a interface com suporte a uma interface gráfica.</li>
</ul>

<h2>👨‍🏫 Mentor</h2>
<p>Este projeto foi desenvolvido sob a mentoria de <strong>Rafael Fino</strong>, Arquiteto de Software do banco C6, como parte dos estudos na plataforma <strong>Impact</strong>.</p>

<h2>📝 Licença</h2>
<p>Este projeto está sob a licença <a href="LICENSE">MIT</a>.</p>
