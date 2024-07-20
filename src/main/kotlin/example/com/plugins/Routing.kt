package example.com.plugins

import io.ktor.client.*
import io.ktor.client.request.*
import io.ktor.http.*
import io.ktor.server.application.*
import io.ktor.server.auth.*
import io.ktor.server.http.content.*
import io.ktor.server.request.*
import io.ktor.server.response.*
import io.ktor.server.routing.*
import io.ktor.server.routing.contentType

fun Application.configureRouting(client: HttpClient) {

    routing {
        get("/") {
            call.respondRedirect("/static/index.html")
        }
        get("/login") {
            call.respondRedirect("/static/login.html")
        }
        get("/register") {
            call.respondRedirect("/static/reg.html")
        }
        authenticate() {}
        post("/api/login") {
            val body = call.receiveText()

            val result = client.get("login") {
                setBody(body)
                contentType(ContentType.Application.Json)
            }
            call.response.status(result.status)
        }
        post("/api/register") {
            val body = call.receiveText()

            val result = client.post("register") {
                setBody(body)
                contentType(ContentType.Application.Json)
            }
            call.response.status(result.status)
        }


        static("/static") {
            resources("static")
        }
    }
}
