<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Entrar - HopLife</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    
    <style>
        /* --- Trazendo a paleta da sua Home para o Keycloak --- */
        body {
            background-color: #E0DED7;
            color: #000000;
        }
        
        .text-warm { 
            color: #E64500 !important; 
        }

        /* --- Estilo do Card (Copiado da sua Home) --- */
        .card-login {
            max-width: 500px;
            width: 100%;
            background-color: #FFFFFF;
            border-radius: 1rem !important; /* Arredondado igual ao rounded-3 */
        }

        /* --- Botão Laranja com Efeito 3D (Copiado do seu Menu) --- */
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
        
        /* Inputs mais amigáveis e arredondados */
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
    </style>
</head>
<body class="d-flex align-items-center justify-content-center min-vh-100">

    <div class="card p-4 p-md-5 shadow-sm border card-login text-center mx-3">
        
        <img src="${url.resourcesPath}/img/logo-hoplife.png" alt="Logo HopLife" height="85" class="mx-auto mb-4">

        <h1 class="display-6 fw-bold text-warm mb-3">Bem-vindo ao HopLife!</h1>
        <p class="fs-5 text-muted mb-4">
            Entre no sistema para acompanhar suas metas diárias e registrar suas conquistas.
        </p>

        <form action="${url.loginAction}" method="post">
            
            <div class="mb-3 text-start">
                <label for="username" class="form-label fw-bold text-muted mb-1">Usuário</label>
                <input type="text" class="form-control form-control-lg" id="username" name="username" required autofocus>
            </div>
            
            <div class="mb-4 text-start">
                <label for="password" class="form-label fw-bold text-muted mb-1">Senha</label>
                <input type="password" class="form-control form-control-lg" id="password" name="password" required>
            </div>

            <button type="submit" class="btn btn-warm btn-lg w-100 mt-2">
                Entrar no Sistema
            </button>
            
        </form>

        <#if message?has_content && message.type == 'error'>
            <div class="alert alert-danger mt-4 fw-bold shadow-sm" style="border-radius: 10px; border: none;">
                ❌ Usuário ou senha incorretos. Tente novamente!
            </div>
        </#if>

    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>