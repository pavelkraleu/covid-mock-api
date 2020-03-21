# COVID Mock API


## POST /api/v1/start

```
curl --header "Content-Type: application/json" --request POST --data '{"login": "aaa","password": "bbb","location": "123"}' http://localhost:8080/api/v1/start
```

```json
{
  "result": "success",
  "token": "djE6MTU4NDcxOTcxNzoxMjM0NTpoYXNoCg=="
}
```

## GET /api/v1/material

```
curl http://localhost:8080/api/v1/material
```

```json
{
  "material": [
    {
      "id": 10,
      "name": "Rou\u0161ka (Batist)"
    },
    {
      "id": 13,
      "name": "\u00dastenka (Panep)"
    }
  ],
  "result": "success"
}
```

## POST /api/v1/validate

```
curl --header "Content-Type: application/json" --request POST --data '{"idcardno": "12345678"}' http://localhost:8080/api/v1/validate
```

```json
{
  "result": "success",
  "message": "V pořádku.",
  "limits": [
      {"id": 10, "limit": 20},
      {"id": 13, "limit": 15}
  ]
}
```

## POST /api/v1/dispense

```
curl --header "Content-Type: application/json" --request POST --data '{"idcardno": "12345", "material": [{"id": 10, "quantity": 10},{"id": 13, "quantity": 10}]}' http://localhost:8080/api/v1/dispense
```
```json
{
  "result": "success"
}
```
