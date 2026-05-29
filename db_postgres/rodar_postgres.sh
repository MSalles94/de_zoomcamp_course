# comando para rodar imagem do postgres 

docker run -it --rm \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="root" \
  -e POSTGRES_DB="ny_taxi" \
  -v ny_taxi_postgres_data:/var/lib/postgresql \
  -p 5432:5432 \
  postgres:18


# conectar com o postgres
uv run pgcli -h localhost -p 5432 -u root -d ny_taxi


# executar script de ingestão no banco com parametros
uv run python pipeline_sql.py \
  --pg-user=root \
  --pg-pass=root \
  --pg-host=localhost \
  --pg-port=5432 \
  --pg-db=ny_taxi \
  --target-table=yellow_taxi_data \
  --chunksize=100000 \
  --year=2021 \
  --month=2
