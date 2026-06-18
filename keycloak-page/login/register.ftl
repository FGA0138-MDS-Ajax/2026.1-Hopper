<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Registrar - HopLife</title>
    
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@latest/tabler-icons.min.css">
    
    <style>
        /* --- Paleta e Fundo --- */
        body {
            background-color: #E0DED7;
            color: #000000;
        }

        /* --- Estilo do Card Principal --- */
        .card-login {
            max-width: 500px;
            width: 100%;
            background-color: #FFFFFF;
            border-radius: 1rem !important;
        }

        /* --- Botão Laranja 3D --- */
        .btn-warm {
            background-color: #E64500 !important;
            color: #FFFFFF !important;
            border-radius: 12px !important;
            padding: 0.8rem 2.2rem !important;
            font-weight: 700;
            border: none;
            box-shadow: 0 4px 0 #B33600 !important;
            transition: all 0.15s ease-in-out;
        }
        .btn-warm:hover {
            transform: translateY(2px);
            box-shadow: 0 2px 0 #B33600 !important;
            color: #FFFFFF !important;
        }
        .btn-warm:active {
            transform: translateY(4px);
            box-shadow: 0 0 0 transparent !important;
        }
        
        /* --- Inputs --- */
        .form-control {
            border-radius: 10px;
            border: 2px solid #E0DED7;
            background-color: #F9F9F8;
        }
        .form-control:focus {
            border-color: #3A5A50;
            box-shadow: 0 0 0 0.25rem rgba(58, 90, 80, 0.25);
            background-color: #FFFFFF;
        }

        /* --- Ajustes do Olhinho da Senha --- */
        .hl-pass-wrap { position: relative; }
        .hl-eye {
            position: absolute;
            right: 15px;
            top: 50%;
            transform: translateY(-50%);
            cursor: pointer;
            color: #888780;
            font-size: 22px;
            background: none;
            border: none;
            padding: 0;
            line-height: 1;
        }
        .hl-eye:hover { color: #E64500; }

        /* --- Barras de Força da Senha --- */
        .hl-strength {
            display: flex;
            gap: 4px;
            margin-top: 8px;
        }
        .hl-strength-bar {
            flex: 1;
            height: 6px;
            border-radius: 3px;
            background: #E0DED7;
            transition: background 0.2s;
        }
        .hl-strength-label {
            font-size: 13px;
            font-weight: bold;
            color: #888780;
            text-align: right;
            margin-top: 4px;
            margin-bottom: 0;
        }
    </style>
</head>
<body class="d-flex align-items-center justify-content-center min-vh-100 py-4">

    <div class="card p-4 p-md-5 shadow-sm border card-login text-center mx-3">
        
        <img src="${url.resourcesPath}/img/logo-hoplife.png" alt="Logo HopLife" height="85" class="mx-auto mb-4">

        <h1 class="display-6 fw-bold text-warm mb-3">Crie sua conta</h1>
        <p class="fs-5 text-muted mb-4">
            Registre-se para começar a acompanhar suas metas e conquistas diárias.
        </p>

        <form action="${url.registrationAction}" method="post" id="registerForm">
            
            <div class="row text-start mb-3">
                <div class="col-12 col-sm-6 mb-3 mb-sm-0">
                    <label for="firstName" class="form-label fw-bold text-muted mb-1">Nome</label>
                    <input type="text" class="form-control form-control-lg" id="firstName" name="firstName" value="${(register.formData.firstName!'')}" placeholder="João" required autofocus>
                </div>
                <div class="col-12 col-sm-6">
                    <label for="lastName" class="form-label fw-bold text-muted mb-1">Sobrenome</label>
                    <input type="text" class="form-control form-control-lg" id="lastName" name="lastName" value="${(register.formData.lastName!'')}" placeholder="Silva" required>
                </div>
            </div>

            <div class="mb-3 text-start">
                <label for="email" class="form-label fw-bold text-muted mb-1">E-mail</label>
                <input type="email" class="form-control form-control-lg" id="email" name="email" value="${(register.formData.email!'')}" placeholder="joao@email.com" required>
            </div>

            <div class="mb-3 text-start">
                <label for="username" class="form-label fw-bold text-muted mb-1">Nome de usuário</label>
                <input type="text" class="form-control form-control-lg" id="username" name="username" value="${(register.formData.username!'')}" placeholder="joao.silva" required>
                <small class="text-muted d-block mt-1 fw-bold" style="font-size: 0.8rem;">Somente letras minúsculas, números, pontos (.), hifens (-) e underlines (_).</small>
            </div>

            <div class="mb-3 text-start">
                <label for="password" class="form-label fw-bold text-muted mb-1">Senha</label>
                <div class="hl-pass-wrap">
                    <input type="password" class="form-control form-control-lg" id="password" name="password" placeholder="••••••••" oninput="checkStrength()" style="padding-right:3rem;" required>
                    <button type="button" class="hl-eye" onclick="togglePass('password','eye1')" aria-label="Mostrar senha">
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

            <div class="mb-4 text-start">
                <label for="password-confirm" class="form-label fw-bold text-muted mb-1">Confirmar senha</label>
                <div class="hl-pass-wrap">
                    <input type="password" class="form-control form-control-lg" id="password-confirm" name="password-confirm" placeholder="••••••••" style="padding-right:3rem;" required>
                    <button type="button" class="hl-eye" onclick="togglePass('password-confirm','eye2')" aria-label="Mostrar senha">
                        <i class="ti ti-eye" id="eye2"></i>
                    </button>
                </div>
            </div>

            <button type="submit" class="btn btn-warm btn-lg w-100 mt-2">
                Criar conta
            </button>
            
        </form>

        <#if message?has_content && message.type == 'error'>
            <div class="alert alert-danger mt-4 fw-bold shadow-sm text-start" style="border-radius: 10px; border: none;">
                ❌ 
                <#if message.summary?contains("Email") || message.summary?contains("email")>
                    Este e-mail já está cadastrado. Tente outro.
                <#elseif message.summary?contains("Username") || message.summary?contains("username")>
                    Este nome de usuário já está em uso. Escolha outro.
                <#elseif message.summary?contains("character") || message.summary?contains("Character") || message.summary?contains("invalid")>
                    Caractere inválido no nome de usuário. Não use espaços no meio.
                <#elseif message.summary?contains("match")>
                    As senhas digitadas não coincidem.
                <#else>
                    ${message.summary}
                </#if>
            </div>
        </#if>

        <div class="mt-4 pt-3 border-top">
            <p class="text-muted fw-bold mb-2">Já tem uma conta?</p>
            <a href="${url.loginUrl}" class="btn btn-light w-100 py-2" 
               style="border-radius: 12px; font-weight: bold; border: 2px solid #E0DED7; color: #374151;">
                Entrar no sistema
            </a>
        </div>

    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
    <script>
        document.addEventListener("DOMContentLoaded", function() {
            const usernameInput = document.getElementById('username');
            
            // 1. Quando o usuário sai do campo, o JS "limpa" os espaços no final e no início (trim)
            usernameInput.addEventListener('blur', function() {
                this.value = this.value.trim();
                checkUsernameValidity(this);
            });

            // 2. Lógica central de validação do Nome de Usuário
            function checkUsernameValidity(input) {
                if (input.validity.valueMissing) {
                    input.setCustomValidity('Por favor, preencha este campo.');
                } else if (/[^a-z0-9.\-_]/.test(input.value)) {
                    // Se tiver espaços no meio ou símbolos proibidos, ele avisa!
                    input.setCustomValidity('Caractere inválido no nome de usuário. Não use espaços no meio.');
                } else {
                    input.setCustomValidity(''); // Se estiver limpo, passa!
                }
            }

            // Tradução das mensagens de validação nativas e tratamento dos campos
            const inputs = document.querySelectorAll('input[required]');
            inputs.forEach(input => {
                input.addEventListener('invalid', function(e) {
                    if (e.target.type === 'email') {
                        if (e.target.validity.valueMissing) {
                            e.target.setCustomValidity('Por favor, preencha este campo.');
                        } else {
                            e.target.setCustomValidity('Por favor, inclua um domínio após o "@".');
                        }
                    } else if (e.target.id === 'username') {
                        checkUsernameValidity(e.target);
                    } else {
                        e.target.setCustomValidity('Por favor, preencha este campo.');
                    }
                });

                input.addEventListener('input', function(e) {
                    if (e.target.id === 'username') {
                        e.target.value = e.target.value.toLowerCase(); // Força minúsculo dinamicamente
                        checkUsernameValidity(e.target); // Valida enquanto digita
                    } else {
                        e.target.setCustomValidity('');
                    }
                });
            });

            // Trim de segurança caso o usuário envie direto com o Enter sem sair do campo
            document.getElementById('registerForm').addEventListener('submit', function() {
                usernameInput.value = usernameInput.value.trim();
            });
        });

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
            const v = document.getElementById('password').value;
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
    </script>
</body>
</html>