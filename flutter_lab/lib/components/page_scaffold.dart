import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

class PageScaffold extends StatelessWidget {
  final String title;
  final Widget child;

  const PageScaffold({Key? key, required this.title, required this.child}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(appBar: AppBar(title: Text(title)), body: SafeArea(child: child));
  }
}