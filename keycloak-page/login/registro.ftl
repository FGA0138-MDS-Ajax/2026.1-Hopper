<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Registrar - HopLife</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@latest/tabler-icons.min.css">
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      min-height: 100vh;
      background-color: #E0DED7;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 2rem 1rem;
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    }

    .hl-card {
      background: #FFFFFF;
      border-radius: 1rem;
      border: 0.5px solid rgba(0,0,0,0.08);
      padding: 2.5rem 2.5rem 2rem;
      width: 100%;
      max-width: 480px;
      text-align: center;
    }

    .hl-logo {
      width: 64px;
      height: 64px;
      background: #E64500;
      border-radius: 16px;
      display: flex;
      align-items: center;
      justify-content: center;
      margin: 0 auto 1.5rem;
      box-shadow: 0 4px 0 #B33600;
    }
    .hl-logo i { font-size: 32px; color: #fff; }

    .hl-title {
      font-size: 22px;
      font-weight: 600;
      color: #E64500;
      margin: 0 0 0.4rem;
    }

    .hl-sub {
      font-size: 14px;
      color: #888780;
      margin: 0 0 1.8rem;
      line-height: 1.5;
    }

    .hl-row {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 12px;
    }

    .hl-group { margin-bottom: 1rem; text-align: left; }

    .hl-label {
      display: block;
      font-size: 13px;
      font-weight: 600;
      color: #5F5E5A;
      margin-bottom: 6px;
    }

    .hl-field {
      width: 100%;
      border: 2px solid #E0DED7;
      border-radius: 10px;
      background: #F9F9F8;
      padding: 0.65rem 0.85rem;
      font-size: 15px;
      color: #2C2C2A;
      outline: none;
      transition: border-color 0.15s, background 0.15s;
      font-family: inherit;
    }
    .hl-field:focus {
      border-color: #3A5A50;
      background: #fff;
      box-shadow: 0 0 0 3px rgba(58,90,80,0.15);
    }

    .hl-pass-wrap { position: relative; }
    .hl-eye {
      position: absolute;
      right: 12px;
      top: 50%;
      transform: translateY(-50%);
      cursor: pointer;
      color: #888780;
      font-size: 18px;
      background: none;
      border: none;
      padding: 0;
      line-height: 1;
    }
    .hl-eye:hover { color: #E64500; }

    .hl-strength {
      display: flex;
      gap: 4px;
      margin-top: 6px;
    }
    .hl-strength-bar {
      flex: 1;
      height: 4px;
      border-radius: 2px;
      background: #E0DED7;
      transition: background 0.2s;
    }
    .hl-strength-label {
      font-size: 11px;
      color: #888780;
      text-align: right;
      margin-top: 3px;
    }

    .hl-hint {
      font-size: 11px;
      color: #B4B2A9;
      margin-top: 4px;
    }

    .hl-btn {
      width: 100%;
      background: #E64500;
      color: #fff;
      border: none;
      border-radius: 12px;
      padding: 0.75rem 1.5rem;
      font-size: 15px;
      font-weight: 700;
      cursor: pointer;
      box-shadow: 0 4px 0 #B33600;
      transition: transform 0.12s, box-shadow 0.12s;
      margin-top: 0.5rem;
      font-family: inherit;
    }
    .hl-btn:hover { transform: translateY(2px); box-shadow: 0 2px 0 #B33600; }
    .hl-btn:active { transform: translateY(4px); box-shadow: 0 0 0 #B33600; }

    .hl-error {
      background: #FCEBEB;
      color: #791F1F;
      border-radius: 10px;
      padding: 0.7rem 1rem;
      font-size: 13px;
      font-weight: 600;
      margin-top: 1rem;
      display: flex;
      align-items: center;
      gap: 8px;
      text-align: left;
    }
    .hl-success {
      background: #EAF3DE;
      color: #27500A;
      border-radius: 10px;
      padding: 0.7rem 1rem;
      font-size: 13px;
      font-weight: 600;
      margin-top: 1rem;
      display: flex;
      align-items: center;
      gap: 8px;
      text-align: left;
    }

    .hl-divider {
      border: none;
      border-top: 0.5px solid #E0DED7;
      margin: 1.5rem 0 1rem;
    }

    .hl-footer {
      font-size: 12px;
      color: #B4B2A9;
    }

    .hl-link {
      color: #E64500;
      font-weight: 600;
      text-decoration: none;
      cursor: pointer;
    }
    .hl-link:hover { text-decoration: underline; }

    .hl-check-row {
      display: flex;
      align-items: center;
      gap: 8px;
      text-align: left;
      margin-bottom: 1rem;
    }
    .hl-check-row input[type=checkbox] {
      accent-color: #E64500;
      width: 16px;
      height: 16px;
      cursor: pointer;
      flex-shrink: 0;
    }
    .hl-check-row label { font-size: 13px; color: #5F5E5A; cursor: pointer; }
  </style>
</head>
<body>

  <div class="hl-card">

    <div class="hl-logo">
      <i class="ti ti-leaf"></i>
    </div>
    <h1 class="hl-title">Crie sua conta</h1>
    <p class="hl-sub">Registre-se para começar a acompanhar suas metas e conquistas diárias.</p>

    <div class="hl-row">
      <div class="hl-group">
        <label class="hl-label" for="nome">Nome</label>
        <input class="hl-field" type="text" id="nome" placeholder="João">
      </div>
      <div class="hl-group">
        <label class="hl-label" for="sobrenome">Sobrenome</label>
        <input class="hl-field" type="text" id="sobrenome" placeholder="Silva">
      </div>
    </div>

    <div class="hl-group">
      <label class="hl-label" for="email">E-mail</label>
      <input class="hl-field" type="email" id="email" placeholder="joao@email.com">
    </div>

    <div class="hl-group">
      <label class="hl-label" for="usuario">Nome de usuário</label>
      <input class="hl-field" type="text" id="usuario" placeholder="joao.silva" oninput="checkUser()">
      <p class="hl-hint">Somente letras, números e pontos. Sem espaços.</p>
    </div>

    <div class="hl-group">
      <label class="hl-label" for="senha">Senha</label>
      <div class="hl-pass-wrap">
        <input class="hl-field" type="password" id="senha" placeholder="••••••••" oninput="checkStrength()" style="padding-right:2.5rem;">
        <button class="hl-eye" onclick="togglePass('senha','eye1')" aria-label="Mostrar senha">
          <i class="ti ti-eye" id="eye1"></i>
        </button>
      </div>
      <div class="hl-strength">
        <div class="hl-strength-bar" id="b1"></div>
        <div class="hl-strength-bar" id="b2"></div>
        <div class="hl-strength-bar" id="b3"></div>
        <div class="hl-strength-bar" id="b4"></div>
      </div>
      <p class="hl-strength-label" id="strength-label"></p>
    </div>

    <div class="hl-group">
      <label class="hl-label" for="confirmar">Confirmar senha</label>
      <div class="hl-pass-wrap">
        <input class="hl-field" type="password" id="confirmar" placeholder="••••••••" style="padding-right:2.5rem;">
        <button class="hl-eye" onclick="togglePass('confirmar','eye2')" aria-label="Mostrar senha">
          <i class="ti ti-eye" id="eye2"></i>
        </button>
      </div>
    </div>

    <div class="hl-check-row">
      <input type="checkbox" id="termos">
      <label for="termos">Concordo com os <a class="hl-link" href="#">termos de uso</a> e a <a class="hl-link" href="#">política de privacidade</a></label>
    </div>

    <button class="hl-btn" onclick="handleRegister()">Criar conta</button>

    <div id="msg" style="display:none;"></div>

    <hr class="hl-divider">
    <p class="hl-footer">Já tem uma conta? <a class="hl-link" href="#">Entrar no sistema</a></p>

  </div>

  <script>
    function togglePass(id, iconId) {
      const inp = document.getElementById(id);
      const icon = document.getElementById(iconId);
      if (inp.type === 'password') {
        inp.type = 'text';
        icon.className = 'ti ti-eye-off';
      } else {
        inp.type = 'password';
        icon.className = 'ti ti-eye';
      }
    }

    function checkStrength() {
      const v = document.getElementById('senha').value;
      const bars = ['b1','b2','b3','b4'].map(id => document.getElementById(id));
      const label = document.getElementById('strength-label');
      bars.forEach(b => b.style.background = '#E0DED7');
      let score = 0;
      if (v.length >= 8) score++;
      if (/[A-Z]/.test(v)) score++;
      if (/[0-9]/.test(v)) score++;
      if (/[^A-Za-z0-9]/.test(v)) score++;
      const colors = ['#E24B4A','#EF9F27','#639922','#3A5A50'];
      const labels = ['Muito fraca','Fraca','Boa','Forte'];
      if (v.length === 0) { label.textContent = ''; return; }
      for (let i = 0; i < score; i++) bars[i].style.background = colors[score - 1];
      label.textContent = labels[score - 1];
      label.style.color = colors[score - 1];
    }

    function checkUser() {
      const inp = document.getElementById('usuario');
      inp.value = inp.value.replace(/[^a-zA-Z0-9.]/g, '');
    }

    function showMsg(type, text) {
      const el = document.getElementById('msg');
      el.className = type === 'error' ? 'hl-error' : 'hl-success';
      const icon = type === 'error' ? 'ti-alert-circle' : 'ti-circle-check';
      el.innerHTML = `<i class="ti ${icon}"></i>${text}`;
      el.style.display = 'flex';
    }

    function handleRegister() {
      const nome     = document.getElementById('nome').value.trim();
      const sobrenome= document.getElementById('sobrenome').value.trim();
      const email    = document.getElementById('email').value.trim();
      const usuario  = document.getElementById('usuario').value.trim();
      const senha    = document.getElementById('senha').value;
      const confirmar= document.getElementById('confirmar').value;
      const termos   = document.getElementById('termos').checked;

      if (!nome || !sobrenome || !email || !usuario || !senha || !confirmar) {
        showMsg('error', 'Preencha todos os campos obrigatórios.'); return;
      }
      if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
        showMsg('error', 'Informe um e-mail válido.'); return;
      }
      if (senha.length < 6) {
        showMsg('error', 'A senha deve ter pelo menos 6 caracteres.'); return;
      }
      if (senha !== confirmar) {
        showMsg('error', 'As senhas não coincidem.'); return;
      }
      if (!termos) {
        showMsg('error', 'Você precisa aceitar os termos para continuar.'); return;
      }
      showMsg('success', 'Conta criada com sucesso! Bem-vindo ao HopLife.');
    }
  </script>

</body>
</html>