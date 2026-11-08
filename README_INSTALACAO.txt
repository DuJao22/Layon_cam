LAYON CAM — INSTALAÇÃO E USO
================================

O que é
-------
Aplicativo web instalável (PWA): o Celular X transmite câmera/áudio e o Celular Y
visualiza ao vivo. O Celular Y também envia o comando para iniciar/parar a gravação.
A gravação é criada e baixada no Celular X (formato WebM).

IMPORTANTE — HTTPS
------------------
Os navegadores Android exigem HTTPS (ou localhost) para liberar câmera e microfone.
O servidor Flask deste pacote inicia em HTTP para teste; portanto, para abrir a câmera
em outro aparelho, publique-o atrás de HTTPS. Opções:
- Hospedar em um serviço Python que ofereça HTTPS (Render, Railway ou VPS), ou
- Usar um túnel HTTPS como Cloudflare Tunnel/ngrok apontando para a porta 5000.
Não exponha o servidor publicamente sem configurar autenticação e controles de acesso.
Este MVP usa código de sala de 6 caracteres, mas ainda não tem login nem criptografia
adicional de aplicação. Use apenas para testes autorizados.

INSTALAÇÃO NO COMPUTADOR
------------------------
1. Instale Python 3.10 ou superior.
2. Extraia o ZIP.
3. Abra o terminal dentro da pasta layon_cam.
4. Instale as dependências:
      python -m venv .venv
   Windows:
      .venv\Scripts\activate
   Linux/macOS:
      source .venv/bin/activate
      pip install -r requirements.txt
5. Inicie:
      python app.py
6. Configure HTTPS para o endereço público apontando para a porta 5000.
7. Abra o endereço HTTPS no Chrome dos dois celulares.

INSTALAÇÃO NO TERMUX (ANDROID)
------------------------------
1. Instale Termux preferencialmente pelo F-Droid ou GitHub oficial.
2. Copie a pasta extraída para uma pasta acessível no Termux.
3. No Termux:
      pkg update
      pkg install python
      cd /caminho/para/layon_cam
      pip install -r requirements.txt
      python app.py
4. Para acessar de outro aparelho, configure um túnel HTTPS para a porta 5000
   ou hospede o servidor em um serviço com HTTPS.
5. Mantenha o Termux aberto enquanto usar o sistema.

HOSPEDAR NO RENDER
------------------
O arquivo render.yaml configura um serviço Web Python gratuito, instala as
dependências e inicia o app com Gunicorn. O Render gera a variável SECRET_KEY
e fornece HTTPS no endereço onrender.com.

1. Envie estes arquivos para um repositório Git no GitHub, GitLab ou Bitbucket.
2. No Render, escolha New > Blueprint e conecte esse repositório.
3. Confirme a criação do serviço definido em render.yaml e aguarde o deploy.
4. Abra o endereço onrender.com do serviço nos dois celulares.

O plano gratuito pode suspender o serviço após inatividade; a primeira abertura
depois disso pode demorar. As salas continuam em memória e desaparecem quando
o processo reinicia. Use apenas com dispositivos autorizados; ainda não há
autenticação para proteger salas e comandos.

COMO USAR
---------
CELULAR X (câmera):
1. Abra o endereço HTTPS no Chrome.
2. Escolha "Celular X · Câmera".
3. Toque em "Criar conexão" e anote o código de 6 caracteres.
4. Toque em "Ativar câmera" e permita câmera/microfone.
5. Deixe a tela aberta durante a transmissão.

CELULAR Y (monitor):
1. Abra o mesmo endereço HTTPS.
2. Escolha "Celular Y · Monitor".
3. Digite o código e toque em "Conectar ao celular X".
4. Aguarde o vídeo aparecer.
5. Use "Iniciar gravação no X" e "Parar gravação".
6. O arquivo WebM será baixado no celular X quando a gravação parar.

INSTALAR COMO APLICATIVO
------------------------
No Chrome Android, abra o endereço HTTPS, toque no menu ⋮ e escolha
"Instalar app" ou "Adicionar à tela inicial" (o texto pode variar).

LIMITAÇÕES DESTA VERSÃO
-----------------------
- MVP de demonstração; não é um sistema de segurança pronto para produção.
- O WebRTC usa STUN público; redes restritas podem exigir servidor TURN.
- A gravação fica no celular X, não na nuvem.
- A conexão depende de internet/rede e do navegador manter a página ativa.
- Fechar a página, bloquear o aparelho ou economizar bateria pode interromper vídeo.
- O servidor mantém salas em memória; reiniciar o servidor encerra as salas.
- O arquivo gravado usa WebM; compatibilidade de reprodução varia entre aparelhos.
- Não há gravação oculta: o navegador solicita permissões e a interface mostra o estado.

PRÓXIMOS PASSOS RECOMENDADOS ANTES DE USO REAL
---------------------------------------------
Adicionar autenticação, HTTPS obrigatório, salas com expiração, TURN privado,
limites de acesso, armazenamento seguro e testes em redes móveis diferentes.
