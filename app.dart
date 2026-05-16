import 'package:flutter/material.dart';

class LoginScreen extends StatefulWidget {
  const LoginScreen({super.key});

  @override
  State<LoginScreen> createState() => _LoginScreenState();
}

class _LoginScreenState extends State<LoginScreen> {

  final TextEditingController idController = TextEditingController();
  final TextEditingController passwordController = TextEditingController();

  String? errorMessage;

  void login() {

    final value = idController.text.trim();

    if (value.length == 10) {

      // customer login

      print("Customer");

    } else if (value.length == 11) {

      // employee login

      print("Employee");

    } else {

      setState(() {
        errorMessage =
            "10 digits for Customer, 11 digits for Employee";
      });
    }
  }

  @override
  Widget build(BuildContext context) {

    return Scaffold(

      backgroundColor: const Color(0xffeef3f6),

      body: Center(

        child: Container(

          width: 360,
          height: 660,

          decoration: BoxDecoration(
            borderRadius: BorderRadius.circular(42),
            gradient: const LinearGradient(
              colors: [
                Color(0xffc9e7f7),
                Color(0xffdff4ff),
              ],
              begin: Alignment.topCenter,
              end: Alignment.bottomCenter,
            ),
          ),

          child: Padding(

            padding: const EdgeInsets.symmetric(horizontal: 40),

            child: Column(

              children: [

                const SizedBox(height: 90),

                Image.asset(
                  "assets/images/robot.png",
                  width: 145,
                ),

                const SizedBox(height: 40),

                TextField(
                  controller: idController,
                  keyboardType: TextInputType.number,
                  maxLength: 11,

                  decoration: InputDecoration(
                    hintText: "phone / ID Number",
                    filled: true,
                    fillColor: Colors.white,
                    border: OutlineInputBorder(
                      borderRadius: BorderRadius.circular(25),
                      borderSide: BorderSide.none,
                    ),
                  ),
                ),

                const SizedBox(height: 12),

                TextField(
                  controller: passwordController,
                  obscureText: true,

                  decoration: InputDecoration(
                    hintText: "Password",
                    filled: true,
                    fillColor: Colors.white,
                    border: OutlineInputBorder(
                      borderRadius: BorderRadius.circular(25),
                      borderSide: BorderSide.none,
                    ),
                  ),
                ),

                const SizedBox(height: 10),

                Align(
                  alignment: Alignment.center,
                  child: TextButton(
                    onPressed: () {

                      // forgot password route

                    },
                    child: const Text("Forgot Password?"),
                  ),
                ),

                const SizedBox(height: 20),

                SizedBox(

                  width: double.infinity,
                  height: 46,

                  child: ElevatedButton(

                    onPressed: login,

                    child: const Text("Log In"),
                  ),
                ),

                if (errorMessage != null)
                  Padding(
                    padding: const EdgeInsets.only(top: 10),
                    child: Text(
                      errorMessage!,
                      style: const TextStyle(
                        color: Colors.red,
                        fontSize: 12,
                      ),
                    ),
                  ),

                const SizedBox(height: 20),

                Row(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [

                    const Text("New User? "),

                    GestureDetector(

                      onTap: () {

                        // create account route

                      },

                      child: const Text(
                        "Create Account",
                        style: TextStyle(
                          decoration: TextDecoration.underline,
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                    ),
                  ],
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
