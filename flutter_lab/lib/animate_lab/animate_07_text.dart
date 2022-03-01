import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

class ImplicitlyText extends StatefulWidget {
  const ImplicitlyText({Key? key}) : super(key: key);

  @override
  State<StatefulWidget> createState() => _ImplicitlyTextState();
}

class _ImplicitlyTextState extends State<ImplicitlyText> {
  final start = const TextStyle(
      color: Colors.white, fontSize: 50, shadows: [Shadow(offset: Offset(1, 1), color: Colors.black, blurRadius: 3)]);
  final end = const TextStyle(
      color: Colors.white, fontSize: 20, shadows: [Shadow(offset: Offset(1, 1), color: Colors.purple, blurRadius: 3)]);

  late ValueNotifier<TextStyle> _notifier;

  @override
  void initState() {
    _notifier = ValueNotifier(start);
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return Center(
        child: Wrap(direction: Axis.vertical, crossAxisAlignment: WrapCrossAlignment.center, children: [
      Switch(value: _notifier.value == end, onChanged: (value) => setState(() => _notifier.value = value ? end : start)),
      AnimatedDefaultTextStyle(
          child: const Text('Flutter Lab'),
          style: _notifier.value,
          duration: const Duration(seconds: 1),
          curve: Curves.fastOutSlowIn)
    ]));
  }
}
