---
title: "cachePath property - SDKOptions class - core.engine library - Dart API"
slug: "sdk-for-flutter-explore-core-engine-sdkoptions-cachepath"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="core.engine/SDKOptions-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">cachePath</span> property

</div>

<div class="section multi-line-signature">

String <span class="name">cachePath</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

Path to be used for caching purposes. It should be a path to the desired location where the application has read/write permissions. The path can be on internal or external storage. By default, this returns an empty string. Setting a new string, will overwrite the internally used default paths:

`<Application_Home>/Library/Caches` for iOS and

    Context.getCacheDir().getPath()

for Android. If an absolute path is set, it will be used instead. If a relative path is set then directory `<Application_Home>/Library/Caches` for iOS and

    Context.getCacheDir().getPath()

for Android is used as parent path.
</p>

</div>

## Implementation

``` dart
String cachePath;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

