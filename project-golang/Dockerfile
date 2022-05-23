FROM golang:1.18-buster as build

WORKDIR /app

COPY go.mod .

RUN go mod download

COPY . .

RUN CGO_ENABLED=0 go build -o build/fizzbuzz.exe

FROM gcr.io/distroless/static-debian11

COPY --from=build /app/templates/index.html /templates/index.html

COPY --from=build /app/build/fizzbuzz.exe /build/fizzbuzz.exe

CMD ["./build/fizzbuzz.exe", "serve"]