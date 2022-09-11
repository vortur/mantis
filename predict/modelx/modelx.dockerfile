FROM alpine:latest as root-ca
RUN apk update && apk add git ca-certificates

FROM golang:alpine as builder
ARG ARCH=amd64
ENV GOARCH=${ARCH}
ARG OS=linux
ENV GOOS=${OS}
COPY . /go/app
WORKDIR /go/app
RUN CGO_ENABLED=0 go build -o /go/bin/service -ldflags '-extldflags "-static"' cmd/main.go

FROM alpine:latest as alpine-with-tz
RUN apk --no-cache add tzdata zip ca-certificates
WORKDIR /usr/share/zoneinfo

RUN zip -q -r -0 /zoneinfo.zip .

FROM scratch
WORKDIR /
COPY --from=builder /go/bin/service /service
COPY --from=builder /go/app/config /config
COPY --from=builder /go/app/epsapi/migrations /migrations

ENV ZONEINFO /zoneinfo.zip
COPY --from=alpine-with-tz /zoneinfo.zip /
COPY --from=root-ca /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/

ENTRYPOINT ["/service", "service"]