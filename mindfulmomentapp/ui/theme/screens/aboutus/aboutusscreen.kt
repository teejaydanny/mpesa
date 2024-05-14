package com.example.mindfulmomentapp.ui.theme.screens.aboutus

import android.graphics.fonts.Font
import androidx.compose.foundation.Image
import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.layout.ContentScale
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.text.font.FontFamily
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.navigation.NavController
import androidx.navigation.NavHostController
import androidx.navigation.compose.rememberNavController
import com.example.mindfulmomentapp.R
import com.example.mindfulmomentapp.navigation.ROUTE_REGISTRATION

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun AboutUsScreen(navController: NavHostController) {

    Box(
        modifier = Modifier
            .fillMaxSize()
    ) {
        Image(
            painter = painterResource(id = R.drawable.aboutus), contentDescription = null,
            modifier = Modifier.fillMaxSize(),
            contentScale = ContentScale.FillBounds
        )

        Column(
            modifier = Modifier
                .fillMaxSize()
                .padding(horizontal = 16.dp),
            verticalArrangement = Arrangement.Top,
            horizontalAlignment = Alignment.CenterHorizontally
        ) {
            Text(
                text = "ABOUT US SECTION",
                style = MaterialTheme.typography.headlineLarge,
                modifier = Modifier.padding(bottom = 16.dp),
                fontFamily = FontFamily.Monospace,
                fontWeight = FontWeight.W900,
                color = Color.Red

            )
            Spacer(modifier = Modifier.height(10.dp))

            // ABOUT US
            Text(
                text = "ABOUT US",
                modifier = Modifier.padding(vertical = 8.dp),
                fontFamily = FontFamily.Cursive,
                fontWeight = FontWeight.W900,
                color = Color.Cyan,
                fontSize = 25.sp
            )
            Text(
                text = "Nikev Hostels is a vibrant and welcoming accommodation option located in the heart of Nikev City offering a unique experience for students seeking comfort and affordability",
                modifier = Modifier.padding(bottom = 16.dp) ,
                fontSize = 17.sp,
                color = Color.Black,
                fontWeight = FontWeight.W500
            )

            // OUR STORY
            Text(
                text = "OUR STORY",
                //style = MaterialTheme.typography.body1,
                modifier = Modifier.padding(vertical = 8.dp),
                fontFamily = FontFamily.Cursive,
                fontWeight = FontWeight.W900,
                color = Color.Cyan,
                fontSize = 25.sp
            )
            Text(
                text = "Founded in the year 2000, Nikev Hostels has been a home away from home for thousands of students all over the country. Our journey began with a vision to create a space for students to connect, explore, and create lasting memories.",

                modifier = Modifier.padding(bottom = 16.dp),
                fontSize = 17.sp,
                color = Color.Black,
                fontWeight = FontWeight.W500
            )

            // SERVICES AND AMENITIES
            Text(
                text = "SERVICES AND AMENITIES",
                modifier = Modifier.padding(vertical = 8.dp),
                fontFamily = FontFamily.Cursive,
                fontWeight = FontWeight.W900,
                color = Color.Cyan,
                fontSize = 25.sp
            )
            Text(
                text = "At Nikev Hostels, we offer a range of accommodation to suit every student's needs from cozy dormitories to private rooms with modern amenities. Our facilities include a spacious common area for socializing and Wi-Fi access throughout the hostel.",
                //style = MaterialTheme.typography.body1,
                modifier = Modifier.padding(bottom = 16.dp),
                fontSize = 17.sp,
                color = Color.Black,
                fontWeight = FontWeight.W500
            )

            // CONTACT US
            Text(
                text = "CONTACT US",
                //style = MaterialTheme.typography.body1,
                modifier = Modifier.padding(vertical = 8.dp),
                fontFamily = FontFamily.Cursive,
                fontWeight = FontWeight.W900,
                color = Color.Cyan,
                fontSize = 25.sp
            )
            Text(
                text = "Ready to experience Nikev Hostels? Book your stay today and discover the perfect comfort. For more information, contact us at [0703765456] or email us at nikevhostels123@gmail.com", //style = MaterialTheme.typography.body1,
                modifier = Modifier.padding(bottom = 16.dp),
                fontSize = 17.sp,
                color = Color.Black,
                fontWeight = FontWeight.W500
            )

         Spacer(modifier = Modifier.height(10.dp))
             Text(text = "BOOK NOW")

        }
    }
}
@Preview(showBackground = true)
@Composable
fun AboutUsScreenPreview() {
    AboutUsScreen(rememberNavController())
}
