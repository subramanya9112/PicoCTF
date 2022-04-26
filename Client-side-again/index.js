var _0x5a46 = ['0a029}', '_again_5', 'this', 'Password\x20Verified', 'Incorrect\x20password', 'getElementById', 'value', 'substring', 'picoCTF{', 'not_this'];
(function (_0x4bd822, _0x2bd6f7) {
  var _0xb4bdb3 = function (_0x1d68f6) {
    while (--_0x1d68f6) {
      _0x4bd822['push'](_0x4bd822['shift']());
    }
  };
  _0xb4bdb3(++_0x2bd6f7);
}(_0x5a46, 0x1b3));
var _0x4b5b = function (_0x2d8f05, _0x4b81bb) {
  _0x2d8f05 = _0x2d8f05 - 0x0;
  var _0x4d74cb = _0x5a46[_0x2d8f05];
  return _0x4d74cb;
};
function verify() {
  checkpass = document[_0x4b5b('0x0')]('pass')[_0x4b5b('0x1')];
  split = 0x4;
  if (checkpass['substring'](0x0, 0x8) == 'picoCTF{') {
    if (checkpass['substring'](0x7, 0x9) == '{n') {
      if (checkpass['substring'](0x8, 0x10) == 'not_this') {
        if (checkpass['substring'](0x3, 0x6) == 'oCT') {
          if (checkpass['substring'](0x18, 0x20) == '0a029}') {
            if (checkpass['substring'](0x6, 0xb) == 'F{not') {
              if (checkpass['substring'](0x10, 0x18) == '_again_5') {
                if (checkpass['substring'](0xc, 0x10) == 'this') {
                  alert(_0x4b5b('0x8'));
                }
              }
            }
          }
        }
      }
    }
  } else {
    alert(_0x4b5b('0x9'));
  }
}