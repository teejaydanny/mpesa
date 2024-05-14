package com.example.mindfulmomentapp

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.runtime.Composable
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.compose.rememberNavController
import com.example.mindfulmomentapp.ui.theme.screens.aboutus.AboutUsScreen
import com.example.mindfulmomentapp.ui.theme.screens.home.HomePage
import com.example.mindfulmomentapp.ui.theme.screens.login.LoginScreen
import com.example.mindfulmomentapp.ui.theme.screens.registration.registerscreen
import com.example.mindfulmomentapp.ui.theme.screens.splashscreen.SplashScreen

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            // Create a NavController
            val navController = rememberNavController()
            NavHost(navController, startDestination = "splash") {
                composable("splash") {
                    SplashScreen(navController = navController)
                }

                composable("home") {
                    HomePage(navController = navController)
                }

                composable("login") {
                    LoginScreen(navController = navController)
                }

                composable("registration") {
                    registerscreen(navController = navController)
                }

                composable("aboutus") {
                    AboutUsScreen(navController = navController)
                }


                }
            }
        }
    }

