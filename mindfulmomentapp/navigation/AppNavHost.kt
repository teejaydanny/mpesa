package com.example.mindfulmomentapp.navigation


import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.navigation.NavHostController
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.compose.rememberNavController
import com.example.mindfulmomentapp.ui.theme.screens.aboutus.AboutUsScreen
import com.example.mindfulmomentapp.ui.theme.screens.home.HomePage
import com.example.mindfulmomentapp.ui.theme.screens.login.LoginScreen
import com.example.mindfulmomentapp.ui.theme.screens.registration.registerscreen
import com.example.mindfulmomentapp.ui.theme.screens.splashscreen.SplashScreen

@Composable
fun AppNavHost(modifier: Modifier=Modifier, navController: NavHostController = rememberNavController(), startDestination: String = ROUTE_REGISTRATION){
    NavHost(navController = navController, modifier = Modifier, startDestination = startDestination) {
        composable(ROUTE_HOME){
            HomePage(navController)
        }
        composable(ROUTE_ABOUTUS){
            AboutUsScreen(navController
            )
        }
        composable(ROUTE_REGISTRATION){
            registerscreen(navController)
        }
        composable(ROUTE_LOGIN){
            LoginScreen(navController)

        }

        composable(ROUTE_SPLASHSCREEN){
            SplashScreen(navController)
        }

    }
}
