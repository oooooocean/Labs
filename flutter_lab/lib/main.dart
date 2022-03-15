import 'package:flutter/material.dart';
import 'package:flutter/scheduler.dart';
import 'package:flutter_lab/animate_lab/animate_01_text.dart';
import 'package:flutter_lab/animate_lab/animate_02_typer.dart';
import 'package:flutter_lab/animate_lab/animate_03_tween.dart';
import 'package:flutter_lab/animate_lab/animate_04_shine_image.dart';
import 'package:flutter_lab/animate_lab/animate_06_halo.dart';
import 'package:flutter_lab/animate_lab/animate_07_text.dart';
import 'package:flutter_lab/animate_lab/animate_08_switcher.dart';
import 'package:flutter_lab/components/page_scaffold.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    PageStorageKey
    return MaterialApp(
      title: 'Flutter Lab',
      theme: ThemeData(primarySwatch: Colors.blue, scaffoldBackgroundColor: Colors.white),
      routes: {
        routes[0]: (_) => _pageBuilder(routes[0], const AnimText()),
        routes[1]: (_) => _pageBuilder(routes[1], const TextTyper()),
        routes[2]: (_) => _pageBuilder(routes[2], const CirclePage()),
        routes[3]: (_) => _pageBuilder(routes[3],
            const CircleShineImage(image: NetworkImage('http://img.duoziwang.com/2021/01/1-21041H243490-L.jpg'))),
        routes[4]: (_) => _pageBuilder(routes[4], const CircleHalo()),
        routes[5]: (_) => _pageBuilder(routes[5], const ImplicitlyText()),
        routes[6]: (_) => _pageBuilder(routes[6], const AnimSwitcher()),
      },
      home: Scaffold(
        body: SafeArea(
          child: Builder(
            builder: (ctx) =>
                SingleChildScrollView(child: Column(children: routes.map((e) => _itemBuilder(ctx, e, e)).toList())),
          ),
        ),
      ),
    );
  }

  final routes = const [
    '流光幻影-01-AnimText',
    '流光幻影-02-TextTyper',
    '流光幻影-03-Tween',
    '流光幻影-04-ShineImage',
    '流光幻影-05-Halo',
    '流光幻影-06-ImplicitlyText',
    '流光幻影-07-AnimSwitcher'
  ];

  Widget _itemBuilder(BuildContext context, String route, String text) => TextButton(
        child: Text(text),
        onPressed: () => Navigator.of(context).pushNamed(route),
      );

  Widget _pageBuilder(String title, Widget child) => PageScaffold(title: title, child: child);
}
