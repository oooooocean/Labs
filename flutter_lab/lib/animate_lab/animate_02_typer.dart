import 'dart:async';

import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

class TextTyper extends StatefulWidget {
  const TextTyper({Key? key}) : super(key: key);

  @override
  State<StatefulWidget> createState() => _TextTypeState();
}

class _TextTypeState extends State with SingleTickerProviderStateMixin {
  final String _text = '西风吹老洞庭波,\n一夜湘君白发多.\n醉后不知天在水,\n满船清梦压星河.\n';
  final ValueNotifier<String> _signal = ValueNotifier('');
  late Timer _timer;
  var _index = 0;

  @override
  void initState() {
    _startAnimation();
    super.initState();
  }

  @override
  void dispose() {
    _timer.cancel();
    _signal.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: AnimatedBuilder(
          animation: _signal,
          builder: (_, __) => Text(
            _signal.value,
            style: const TextStyle(color: Colors.blueGrey, fontSize: 24),
          ),
        ),
      ),
    );
  }

  void _startAnimation() {
    void ticker() {
      if (_index < _text.length) {
        _index++;
        if (_text[_index] == '\n') {
          _index++;
        }
        _signal.value = _text.substring(0, _index);
      } else {
        _timer.cancel();
      }
    }

    _timer = Timer.periodic(const Duration(milliseconds: 200), (timer) => ticker());
  }
}
