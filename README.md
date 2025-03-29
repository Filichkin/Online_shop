# Разработка интернет-магазина

Для запуска проекта установите зависимости из файла:
```
requirements.txt
```

#### Установка и запуск брокера сообщений RabbitMQ
```
docker pull rabbitmq:3.13.1-management
```

```
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672
rabbitmq:3.13.1-management
```

#### Запуск Celery

```
pip install celery

celery -A myshop worker -l info
```

#### Отслеживание Celery с помощью Flower

```
pip install flower

celery -A myshop flower
```

#### Интеграция и отслеживание платежей

```
pip install stripe

brew install stripe/stripe-cli/stripe

stripe login

stripe listen --forward-to 127.0.0.1:8000/payment/webhook/

```