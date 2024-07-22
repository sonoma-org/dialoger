package example.com

import example.com.plugins.*
import io.ktor.client.*
import io.ktor.client.engine.cio.*
import io.ktor.client.plugins.*
import io.ktor.server.application.*
import io.ktor.server.websocket.*

fun main(args: Array<String>) {
    io.ktor.server.netty.EngineMain.main(args)
}

fun Application.module() {
    val client = HttpClient(CIO) {
        this.defaultRequest {
            url(this@module.environment.config.property("auth.address").getString())
        }
    }

    install(WebSockets) {
        maxFrameSize = Long.MAX_VALUE
        masking = false
    }

    configureSecurity(client)
    configureRouting(client)
}
