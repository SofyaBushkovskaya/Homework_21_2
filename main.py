from http.server import BaseHTTPRequestHandler, HTTPServer


hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    """
        Специальный класс, который отвечает за
        обработку входящих запросов от клиентов
    """
    def do_GET(self):
        """ Метод для обработки входящих GET-запросов """
        self.send_response(200)  # Отправка кода ответа
        self.send_header("Content-type", "text/html")  # Отправка типа данных
        self.end_headers()  # Завершение формирования заголовков ответа

        # Чтение содержимого HTML-файла и отправка в теле ответа
        try:
            with open("contact.html", "r", encoding="utf-8") as file:
                content = file.read()
            self.wfile.write(content.encode("utf-8"))
        except FileNotFoundError:
            self.send_error(404, "File Not Found")


if __name__ == "__main__":
    # Инициализация веб-сервера
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print(f"Server started http://{hostName}:{serverPort}")

    try:
        # Запуск веб-сервера
        webServer.serve_forever()
    except KeyboardInterrupt:
        # Остановка сервера при прерывании
        pass

    # Корректная остановка веб-сервера
    webServer.server_close()
    print("Server stopped.")
