---
title: "dispose method - SDKNativeEngine class - core.engine library - Dart API"
slug: "sdk-for-flutter-explore-core-engine-sdknativeengine-dispose"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="core.engine/SDKNativeEngine-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">dispose</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">Future<span class="signature">\<<wbr></wbr><span class="type-parameter">void</span>\></span></span> <span class="name">dispose</span>(<wbr></wbr>)

</div>

<div class="section desc markdown">

Stops pending requests and closes open files and databases in main thread.

Dispose signal is sent to dependent modules. Usage of engine, or dependent modules after calling dispose leads to undefined behavior. Please be aware that this method does not clean any type of storage. **Note:** This method should be called from main thread.

</div>

## Implementation

``` dart
Future<void> dispose();
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

