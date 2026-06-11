<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sair - HopLife</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    
    <style>
        body {
            background-color: #E0DED7;
            color: #000000;
        }
        
        .text-warm { 
            color: #E64500 !important; 
        }

        .card-login {
            max-width: 500px;
            width: 100%;
            background-color: #FFFFFF;
            border-radius: 1rem !important; 
        }

        /* Botão Laranja com Efeito 3D */
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
        
        /* Botão Secundário para Cancelar */
        .btn-cancelar {
            border-radius: 12px !important;
            padding: 0.8rem 2.2rem !important;
            font-weight: bold;
            border: 2px solid #E0DED7;
            color: #6c757d;
            background-color: transparent;
            transition: all 0.15s ease-in-out;
        }
        .btn-cancelar:hover {
            background-color: #f8f9fa;
            color: #343a40;
        }
    </style>
</head>
<body class="d-flex align-items-center justify-content-center min-vh-100">

    <div class="card p-4 p-md-5 shadow-sm border card-login text-center mx-3">
        
        <img src="${url.resourcesPath}/img/logo-hoplife.png" alt="Logo HopLife" height="85" class="mx-auto mb-4">

        <h1 class="display-6 fw-bold text-warm mb-3">Saindo do sistema...</h1>
        <p class="fs-5 text-muted mb-4">
            Tem certeza de que deseja encerrar a sua sessão?
        </p>

        <form action="${url.logoutConfirmAction}" method="POST">
            
            <input type="hidden" name="session_code" value="${logoutConfirm.code}">
            
            <div class="d-grid gap-3 mt-2">
                <button type="submit" name="confirmLogout" id="kc-logout" class="btn btn-warm btn-lg">
                    Sim, quero sair
                </button>
                
                <button type="button" class="btn btn-cancelar btn-lg" onclick="history.back()">
                    Cancelar
                </button>
            </div>
            
        </form>

    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>