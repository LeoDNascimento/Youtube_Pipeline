#YOUTUBE TRANDS PIPELINE

Pipeline Descritiva

Tecnologias Utilizadas:
- Youtube API
- AWS Lambda com Python 3.12
- AWS S3
- AWS RDS com PostgreSQL

Dependências:
- boto3 (para integração com o AWS S3)
- google-api-python-client (para integração com a Youtube API)

Caminho da Pipeline:
1. Consumir a Youtube API para obter os vídeos em tendência.
2. Utilizar uma função Lambda para processar e armazenar os dados dos vídeos em um formato JSON.
3. Armazenar os dados brutos (JSON) no Amazon S3 para posterior processamento.
4. Configurar uma função Lambda para ser acionada ao detectar um novo evento no S3.
5. Quando um novo arquivo é detectado no bucket do S3, a função Lambda é acionada para enviar o arquivo para o Data Warehouse (DW) no Amazon RDS.

![FLUXOGRAMA](https://ibb.co/g7xPkVD)

[Dados]
Campos obtidos da Youtube API:
- Id do vídeo
- Título do vídeo
- Duração do vídeo
- Id do canal
- Contagem de likes
- Contagem de compartilhamentos
- Data e hora de publicação
- Tags
``` javascript
{
  "video_id": "string",
  "title": "string",
  "duration": "string",
  "channel_id": "string",
  "likes": integer,
  "shares": integer,
  "tags": ["string"],
  "published_at": "string"
}
```

[Data Warehouse Final]
[Dados Armazenados no DW]
- Id do vídeo
- Título do vídeo
- Duração do vídeo
- Id do canal
- Contagem de likes
- Contagem de compartilhamentos
- Data e hora de publicação
- Tags

