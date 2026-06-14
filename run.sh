set -e

case "$1" in

  build_generator)
    docker build -t data-generator -f generator/Dockerfile .
    ;;

  run_generator)
    mkdir -p data
    docker run --rm -v "$(pwd)/data:/data" data-generator
    ;;

  create_local_data)
    mkdir -p local_data
    python3 generate.py local_data
    ;;

  build_reporter)
    docker build -t data-reporter -f reporter/Dockerfile .
    ;;

  run_reporter)
    mkdir -p data
    docker run --rm -v "$(pwd)/data:/data" data-reporter
    ;;

  structure)
    find . -not -path './.git*'
    ;;

  clear_data)
    rm -f data/*.csv data/*.html
    ;;

  inside_generator)
    docker run --rm -v "$(pwd)/data:/data" data-generator ls -la /data
    ;;

  inside_reporter)
    docker run --rm -v "$(pwd)/data:/data" data-reporter ls -la /data
    ;;

  report_server)
    docker run --rm -d -p 8080:80 -v "$(pwd)/data/report.html:/usr/share/nginx/html/index.html:ro" --name report_server nginx:alpine
    echo "Сервер запущен. Отчёт доступен на порту 8080"
    ;;


  *)
    echo "Неизвестная команда: $1"
    exit 1
    ;;
esac
