import 'package:flutter/material.dart';
import 'package:flutter_lab/animate_lab/animate_01_text.dart';
import 'package:flutter_lab/animate_lab/animate_02_typer.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter 实验室',
      theme: ThemeData(primarySwatch: Colors.blue, scaffoldBackgroundColor: Colors.white),
      routes: {
        'animate_lab_AnimText': (_) => const AnimText(),
        'animate_lab_TextTyper': (_) => const TextTyper(),
      },
      home: Scaffold(
        body: SafeArea(
          child: Builder(
              builder: (ctx) => SingleChildScrollView(
                      child: Column(children: [
                    _itemBuilder(ctx, 'animate_lab_AnimText', '流光幻影-01-AnimText'),
                    _itemBuilder(ctx, 'animate_lab_TextTyper', '流光幻影-02-TextTyper')
                  ]))),
        ),
      ),
    );
  }

  Widget _itemBuilder(BuildContext context, String route, String text) => TextButton(
        child: Text(text),
        onPressed: () => Navigator.of(context).pushNamed(route),
      );
}
