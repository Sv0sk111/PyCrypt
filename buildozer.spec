[app]

# (str) Title of your application
title = ProfitCalculator

# (str) Package name
package.name = profitcalculator

# (str) Package domain (reverse DNS style)
package.domain = org.example

# (str) Source code entry point
source.main = main.py

# (list) Source files to include (let empty to include all)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
requirements = python3,kivy

# (str) Supported orientation (portrait, landscape or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (str) Application versioning (method 1)
version = 0.1

# (int) Android API to use
android.api = 31

# (int) Minimum API your APK will support
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 24

# (str) Android NDK version to use
android.ndk = 23b

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (bool) Android entry point, default is 'org.kivy.android.PythonActivity'
# android.entrypoint = org.kivy.android.PythonActivity

# (str) Android app theme, default is 'import android' (can be 'Theme.NoTitleBar')
# android.theme = '@android:style/Theme.NoTitleBar'

# (list) Permissions
android.permissions = INTERNET

# (bool) Indicate if the application should be paused when minimized
pause_on_minimize = True
