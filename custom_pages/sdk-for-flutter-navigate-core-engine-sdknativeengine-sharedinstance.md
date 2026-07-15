---
title: "sharedInstance property - SDKNativeEngine class - core.engine library - Dart API"
slug: "sdk-for-flutter-navigate-core-engine-sdknativeengine-sharedinstance"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="core.engine/SDKNativeEngine-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">sharedInstance</span> property

</div>

<div id="sdk-for-flutter-navigate-getter" class="section">

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-class">SDKNativeEngine</a>?</span> <span class="name">sharedInstance</span>

</div>

<div class="section desc markdown">

Shared instance of this SDK engine that can be accessed by any HERE SDK module as the default engine. This is automatically set as a part of the SDK initialization process. Gets the shared instance of this SDK engine that can be accessed by any HERE SDK module as the default engine.

</div>

## Implementation

``` dart
static SDKNativeEngine? get sharedInstance => $prototype.sharedInstance;
```

</div>

<div id="sdk-for-flutter-navigate-setter" class="section">

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">sharedInstance=</span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-sharedInstance-param-value" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-class">SDKNativeEngine</a>?</span> <span class="parameter-name">value</span></span>)</span>

</div>

<div class="section desc markdown">

Shared instance of this SDK engine that can be accessed by any HERE SDK module as the default engine. This is automatically set as a part of the SDK initialization process. Sets the shared instance of this SDK engine that can be accessed by any HERE SDK module as the default engine.

</div>

## Implementation

``` dart
static set sharedInstance(SDKNativeEngine? value) { $prototype.sharedInstance = value; }
```

</pre>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

