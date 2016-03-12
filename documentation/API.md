MS Registry REST API Resources
==============================

Welcome to the MS Registry REST API. Below, you’ll find a full listing of all 
the available  endpoints. As we add more endpoints, they will be automatically 
documented here.

The endpoint’s documentation section includes what query parameters the endpoint
will accept, what the JSON object’s parameters will be in the response, and an 
example query/response.

This documentation is for most recent version of the MS Registry REST API, 
version v0.1.1.

GET /auth/test
--------------

Test Bearer Token authentication.

### Resource Information

>     Method                     GET
>     URL                        /auth/test
>     Requires authentication?   Yes

### Resource Errors

These are the possible errors returned by this endpoint.

+---------------+----------------------+---------------------------------------+
| **HTTP Code** | **Error Identifier** | **Error Message**                     |
+===============+======================+=======================================+
| 403           |authorization_required| Authorization header is expected      |
|               |                      |                                       |
+---------------+----------------------+---------------------------------------+
| 401           |invalid_header        | Authorization header must start with  |
|               |                      | Bearer                                |
|               |                      |                                       |
+---------------+----------------------+---------------------------------------+
| 401           |invalid_header        | Token not found                       |
|               |                      |                                       |
+---------------+----------------------+---------------------------------------+
| 401           |invalid_header        | Authorization header must be Bearer + |
|               |                      | token                                 |
|               |                      |                                       |
+---------------+----------------------+---------------------------------------+
| 400           |token_expired         | Token is expired                      |
|               |                      |                                       |
+---------------+----------------------+---------------------------------------+
| 400           |invalid_audience      | Incorrect audience                    |
|               |                      |                                       |
+---------------+----------------------+---------------------------------------+
| 400           |invalid_signature     | Token signature is invalid            |
|               |                      |                                       |
+---------------+----------------------+---------------------------------------+
| 500           |internal_server_error | An error occurred while adding this   |
|               |                      | user                                  |
|               |                      |                                       |
+---------------+----------------------+---------------------------------------+

### Example

```bash
curl \
 -H 'authorization: Bearer YOUR_API_TOKEN' \
 'https://ws.msregistry.s3it.uzh.ch/auth/test'
```

#### Response

```json
{
  "code": "authorization_success", 
  "description": "All good. You only get this message if you're authenticated."
}

```

GET /user
---------

Get metadata about the current user.

### Resource Information

>     Method                     GET
>     URL                        /api/v1.0/user
>     Requires authentication?   Yes

### Response Parameters

+---------------------+-----------------+--------------------------------------+
| **Parameter**       | **Type**        | **Description**                      |
+=====================+=================+======================================+
| **uniqueID**        | `(string)`      | That's the  unique ID of the user,   |
|                     |                 | received from OAuth server           |
|                     |                 |                                      |
+---------------------+-----------------+--------------------------------------+
| **consent**         | `(bool)`        | Has the Informed Consent been        |
|                     |                 | accepted?                            |
|                     |                 |                                      |
+---------------------+-----------------+--------------------------------------+
| **member\_since**   | `(iso 8601`     | Datetime the user joined             |
|                     | `datetime)`     |                                      |
|                     |                 |                                      |
+---------------------+-----------------+--------------------------------------+
| **last\_seen**      | `(iso 8601`     | Datetime last seen user. This field  |
|                     | `datetime)`     | is updated on every user interaction |
|                     |                 |                                      |
+---------------------+-----------------+--------------------------------------+

### Resource Errors

These are the possible errors returned by this endpoint.

+---------------+----------------------+---------------------------------------+
| **HTTP Code** | **Error Identifier** | **Error Message**                     |
+===============+======================+=======================================+
| 403           |authorization_required| Authorization header is expected      |
|               |                      |                                       |
+---------------+----------------------+---------------------------------------+
| 401           |invalid_header        | Authorization header must start with  |
|               |                      | Bearer                                |
|               |                      |                                       |
+---------------+----------------------+---------------------------------------+
| 401           |invalid_header        | Token not found                       |
|               |                      |                                       |
+---------------+----------------------+---------------------------------------+
| 401           |invalid_header        | Authorization header must be Bearer + |
|               |                      | token                                 |
|               |                      |                                       |
+---------------+----------------------+---------------------------------------+
| 400           |token_expired         | Token is expired                      |
|               |                      |                                       |
+---------------+----------------------+---------------------------------------+
| 400           |invalid_audience      | Incorrect audience                    |
|               |                      |                                       |
+---------------+----------------------+---------------------------------------+
| 400           |invalid_signature     | Token signature is invalid            |
|               |                      |                                       |
+---------------+----------------------+---------------------------------------+
| 500           |internal_server_error | An error occurred while adding this   |
|               |                      | user                                  |
|               |                      |                                       |
+---------------+----------------------+---------------------------------------+

### Example

```bash
curl \
 -H 'authorization: Bearer YOUR_API_TOKEN' \
 'https://ws.msregistry.s3it.uzh.ch/api/v1.0/user'
```

#### Response

```json
{
  "uniqueID": "auth0|569cf82bfc02d8a0339beef4",
  "consent": true,
  "member_since": "2016-03-04T17:03:37",
  "last_seen": "2016-03-04T17:05:12"
}
```

GET /user/consent
-----------------

Get information about user acceptance of Informed Consent. 

### Resource Information

>     Method                     GET
>     URL                        /api/v1.0/user/consent
>     Requires authentication?   Yes

### Response Parameters

+---------------------+-----------------+--------------------------------------+
| **Parameter**       | **Type**        | **Description**                      |
+=====================+=================+======================================+
| **consent**         | `(bool)`        | Has the Informed Consent been        |
|                     |                 | accepted?                            |
|                     |                 |                                      |
+---------------------+-----------------+--------------------------------------+

### Resource Errors

These are the possible errors returned by this endpoint.

+---------------+----------------------+---------------------------------------+
| **HTTP Code** | **Error Identifier** | **Error Message**                     |
+===============+======================+=======================================+
| 403           |authorization_required| Authorization header is expected      |
|               |                      |                                       |
+---------------+----------------------+---------------------------------------+
| 401           |invalid_header        | Authorization header must start with  |
|               |                      | Bearer                                |
|               |                      |                                       |
+---------------+----------------------+---------------------------------------+
| 401           |invalid_header        | Token not found                       |
|               |                      |                                       |
+---------------+----------------------+---------------------------------------+
| 401           |invalid_header        | Authorization header must be Bearer + |
|               |                      | token                                 |
|               |                      |                                       |
+---------------+----------------------+---------------------------------------+
| 400           |token_expired         | Token is expired                      |
|               |                      |                                       |
+---------------+----------------------+---------------------------------------+
| 400           |invalid_audience      | Incorrect audience                    |
|               |                      |                                       |
+---------------+----------------------+---------------------------------------+
| 400           |invalid_signature     | Token signature is invalid            |
|               |                      |                                       |
+---------------+----------------------+---------------------------------------+
| 500           |internal_server_error | An error occurred while adding this   |
|               |                      | user                                  |
|               |                      |                                       |
+---------------+----------------------+---------------------------------------+

### Example

```bash
curl \
 -H 'authorization: Bearer YOUR_API_TOKEN' \
 'https://ws.msregistry.s3it.uzh.ch/api/v1.0/user/consent'
```

#### Response

```json
{
  "consent": true
}
```

POST /user/consent
-----------------

Set user acceptance of Informed Consent. 

### Resource Information

>     Method                     POST
>     URL                        /api/v1.0/user/consent
>     Requires authentication?   Yes

### Request Parameters

+---------------------+-----------------+--------------------------------------+
| **Parameter**       | **Type**        | **Description**                      |
+=====================+=================+======================================+
| **consent**         | `(bool)`        | Set True is Informed Consent has     |
|                     |                 | been accepted, False otherwise       |
|                     |                 |                                      |
+---------------------+-----------------+--------------------------------------+

### Response Parameters

+---------------------+-----------------+--------------------------------------+
| **Parameter**       | **Type**        | **Description**                      |
+=====================+=================+======================================+
| **success**         | `(bool)`        | Return True if content was accepted  |
|                     |                 | and registered, False otherwise      |
|                     |                 |                                      |
+---------------------+-----------------+--------------------------------------+

### Resource Errors

These are the possible errors returned by this endpoint.

+---------------+----------------------+---------------------------------------+
| **HTTP Code** | **Error Identifier** | **Error Message**                     |
+===============+======================+=======================================+
| 403           |authorization_required| Authorization header is expected      |
|               |                      |                                       |
+---------------+----------------------+---------------------------------------+
| 401           |invalid_header        | Authorization header must start with  |
|               |                      | Bearer                                |
|               |                      |                                       |
+---------------+----------------------+---------------------------------------+
| 401           |invalid_header        | Token not found                       |
|               |                      |                                       |
+---------------+----------------------+---------------------------------------+
| 401           |invalid_header        | Authorization header must be Bearer + |
|               |                      | token                                 |
|               |                      |                                       |
+---------------+----------------------+---------------------------------------+
| 400           |token_expired         | Token is expired                      |
|               |                      |                                       |
+---------------+----------------------+---------------------------------------+
| 400           |invalid_audience      | Incorrect audience                    |
|               |                      |                                       |
+---------------+----------------------+---------------------------------------+
| 400           |invalid_signature     | Token signature is invalid            |
|               |                      |                                       |
+---------------+----------------------+---------------------------------------+
| 500           |internal_server_error | An error occurred while adding this   |
|               |                      | user                                  |
|               |                      |                                       |
+---------------+----------------------+---------------------------------------+

### Example

```bash
curl \
 -i -H "Accept: application/json" \
 -H "Content-Type: application/json" \
 -X POST -d "{'consent': true}" \
 -H 'authorization: Bearer YOUR_API_TOKEN' \
 'https://ws.msregistry.s3it.uzh.ch/api/v1.0/user/consent'
```

#### Response

```json
{
  "success": true
}
```

GET /\<lang\_code\>/consent
-----------------

Get Informed Consent in three different languages. 

### Resource Information

>     Method                     GET
>     URL                        /api/v1.0/<lang_code>/consent
>     Requires authentication?   No

### Method Parameters

+---------------------+-----------------+--------------------------------------+
| **Parameter**       | **Type**        | **Description**                      |
+=====================+=================+======================================+
| **lang_code**       | `(string)`      | Three different languages. Accepted  |
|                     |                 | values are: 'de', 'fr', 'it'         |
|                     |                 |                                      |
+---------------------+-----------------+--------------------------------------+

### Response Parameters

+---------------------+-----------------+--------------------------------------+
| **Parameter**       | **Type**        | **Description**                      |
+=====================+=================+======================================+
| **text**            | `(string)`      | Text of Informed Consent, translated |
|                     |                 | in three different languages         |
|                     |                 |                                      |
+---------------------+-----------------+--------------------------------------+

### Example

```bash
curl \
 -H 'authorization: Bearer YOUR_API_TOKEN' \
 'https://ws.msregistry.s3it.uzh.ch/api/v1.0/de/consent'
```

#### Response

```json
{
  "text": "Einwilligungserklärung"
}
```