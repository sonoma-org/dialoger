package example.com.plugins


import io.ktor.client.*
import io.ktor.client.engine.cio.*
import io.ktor.client.request.*
import io.ktor.http.*
import io.ktor.server.application.*
import io.ktor.server.auth.*


fun Application.configureSecurity(client: HttpClient) {

    install(Authentication) {
        basic {
            validate { credentials ->
                val response = client.post("auth") {
                    basicAuth(credentials.name, credentials.password)
                }
                UserIdPrincipal(credentials.name).takeIf { response.status.isSuccess() }
            }
        }
    }
}



