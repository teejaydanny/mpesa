package com.example.mindfulmomentapp.ui.theme.screens.registration

import androidx.compose.foundation.Image
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxHeight
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.material3.Button
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
 import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.layout.ContentScale
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.text.font.FontFamily
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.input.ImeAction
import androidx.compose.ui.text.input.PasswordVisualTransformation
import androidx.compose.ui.text.input.TextFieldValue
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.navigation.NavController
import androidx.navigation.NavHostController
import androidx.navigation.compose.rememberNavController
import com.example.mindfulmomentapp.R
import com.example.mindfulmomentapp.navigation.ROUTE_ABOUTUS
import com.example.mindfulmomentapp.navigation.ROUTE_LOGIN

@Composable
fun registerscreen(navController: NavHostController){


        Button(onClick = { navController.navigate("login") }) {
            Text("Go to Login")
        }



    var  fullname by remember {
        mutableStateOf(TextFieldValue("")) }
//    var lastname by remember {
//        mutableStateOf(TextFieldValue(""))
//    }
    var gender by remember {
        mutableStateOf(TextFieldValue(""))
    }
    var phonenumber by remember {
        mutableStateOf(TextFieldValue(""))
    }
    var email by remember {
        mutableStateOf(TextFieldValue(""))
    }
    var password by remember {
        mutableStateOf(TextFieldValue("")) }
    var confirmpassword by remember {
        mutableStateOf(TextFieldValue("")) }

    var context= LocalContext.current


    Box(
        modifier = Modifier
            .fillMaxSize()
    ) {
        Image(
            painter = painterResource(id = R.drawable.registration), contentDescription = null,
            modifier = Modifier.fillMaxSize(),
            contentScale = ContentScale.FillBounds
        )
        Column(
            modifier = Modifier
                .fillMaxSize()
                //.background(color = Color.Magenta)
                .fillMaxWidth(),
            horizontalAlignment = Alignment.CenterHorizontally
        ) {
            Text(
                modifier = Modifier,
                text = "REGISTER HERE",
                fontSize = 24.sp
            )
            Spacer(modifier = Modifier.height(10.dp))

            OutlinedTextField(
                value = fullname,
                onValueChange = { fullname = it },
                label = {
                    Text(
                        modifier = Modifier
                            .padding(4.dp)
                            .background(color = Color.Green), text = "Full Name"
                    )
                },
                keyboardOptions = KeyboardOptions.Default.copy(imeAction = ImeAction.Next),
                modifier = Modifier
                    .fillMaxWidth()
                    .padding(8.dp)
            )
            Spacer(modifier = Modifier.height(6.dp))

//            OutlinedTextField(
//                value = lastname,
//                onValueChange = { lastname = it },
//                label = {
//                    Text(
//                        modifier = Modifier
//                            .padding(4.dp)
//                            .background(color = Color.Green),
//                        text = "Last Name"
//                    )
//                },
//                keyboardOptions = KeyboardOptions.Default.copy(imeAction = ImeAction.Next),
//                modifier = Modifier
//                    .fillMaxWidth()
//                    .padding(8.dp)
//            )
//            Spacer(modifier = Modifier.height(6.dp))
            OutlinedTextField(
                value = gender,
                onValueChange = { gender = it },
                label = {
                    Text(
                        modifier = Modifier
                            .padding(4.dp)
                            .background(color = Color.Green), text = "Gender"
                    )
                },
                keyboardOptions = KeyboardOptions.Default.copy(imeAction = ImeAction.Next),
                modifier = Modifier
                    .padding(8.dp)
                    .fillMaxWidth()
            )
            Spacer(modifier = Modifier.height(6.dp))

            OutlinedTextField(
                value = phonenumber,
                onValueChange = { phonenumber = it },
                label = {
                    Text(
                        modifier = Modifier
                            .padding(4.dp)
                            .background(color = Color.Green), text = "Phone Number"
                    )
                },
                keyboardOptions = KeyboardOptions.Default.copy(imeAction = ImeAction.Next),
                modifier = Modifier
                    .fillMaxWidth()
                    .padding(8.dp)
            )
            Spacer(modifier = Modifier.height(6.dp))

            OutlinedTextField(
                value = email,
                onValueChange = { email = it },
                label = {
                    Text(
                        modifier = Modifier
                            .padding(4.dp)
                            .background(color = Color.Green), text = "Email"
                    )
                },
                keyboardOptions = KeyboardOptions.Default.copy(imeAction = ImeAction.Next),
                modifier = Modifier
                    .fillMaxWidth()
                    .padding(8.dp)
            )
            Spacer(modifier = Modifier.height(6.dp))

            OutlinedTextField(
                value = password,
                onValueChange = { password = it },
                visualTransformation = PasswordVisualTransformation(),
                label = {
                    Text(
                        modifier = Modifier
                            .padding(4.dp)
                            .background(color = Color.Green), text = "Password"
                    )
                },
                keyboardOptions = KeyboardOptions.Default.copy(imeAction = ImeAction.Next),
                modifier = Modifier
                    .fillMaxWidth()
                    .padding(8.dp)
            )
            Spacer(modifier = Modifier.height(6.dp))



            OutlinedTextField(
                value = confirmpassword,
                onValueChange = { confirmpassword = it },
                visualTransformation = PasswordVisualTransformation(),
                label = {
                    Text(
                        modifier = Modifier
                            .padding(4.dp)
                            .background(color = Color.Green), text = "Confirm Password"
                    )
                },
                keyboardOptions = KeyboardOptions.Default.copy(imeAction = ImeAction.Next),
                modifier = Modifier
                    .fillMaxWidth()
                    .padding(8.dp)
            )
            Spacer(modifier = Modifier.height(6.dp))

            Button(onClick = { navController.navigate(ROUTE_ABOUTUS) }) {
                Text(
                    modifier = Modifier
                        .padding(4.dp), text = "Register"
                )
            }

            Button(onClick = { navController.navigate(ROUTE_LOGIN) }) {
                Text(
                    modifier = Modifier
                        .padding(4.dp), text = "Already have an account?LOGIN"
                )

            }

        }
    }
}
@Preview(showSystemUi = true, showBackground = true)
@Composable
fun registerscreenpreview(){
    registerscreen(rememberNavController())
}








