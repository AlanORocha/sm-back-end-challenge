def verify_version(request):
    # Extrai o prefixo da URL para obter a versão ("/api/vX/")
    path_segments = request.path.strip("/").split("/")

    # Verifica se o segundo segmento da URL é uma versão válida
    if len(path_segments) >= 2 and path_segments[0] == "api":
        api_version = path_segments[1]

        # Validação de versões suportadas
        supported_versions = ["v1", "v2"]
        if api_version not in supported_versions:
            return None
        else:
            return api_version
