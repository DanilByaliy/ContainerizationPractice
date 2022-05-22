FROM golang:1.18-buster

WORKDIR /app

COPY go.mod .

RUN go mod download

COPY . .

RUN go build -o build/fizzbuzz.exe

CMD ["./build/fizzbuzz.exe", "serve"]