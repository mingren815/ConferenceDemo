# Copyright (c) 2013 The WebRTC project authors. All Rights Reserved.
#
# Use of this source code is governed by a BSD-style license
# that can be found in the LICENSE file in the root of the source
# tree. An additional intellectual property rights grant can be found
# in the file PATENTS.  All contributing project authors may
# be found in the AUTHORS file in the root of the source tree.

{
  'variables': {
    'media_rtc_root%': '<(DEPTH)',
    'include_tests%': 0,
    'root_additional_dependencies': [
    ],
  },
  'targets': [
    {
      'target_name': 'All',
      'type': 'none',
      'dependencies': [
        'demo_sdk.gyp:*',
        #'3rd/osip/osip.gyp:*',
        #'3rd/ortp/ortp.gyp:*',
      ],
      'conditions': [
        ['OS=="android"', {
          'dependencies': [
           # 'media_mobile/media_mobile.gyp:*',
          ],
        }],
        ['include_tests==1', {
          'dependencies': [
            'media_connection/media_connection_tests.gyp:*',
          ],
        }],
      ],
    },
  ],
}
