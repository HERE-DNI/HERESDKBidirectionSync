---
title: "makeSharedInstance method - SDKNativeEngine class - core.engine library - Dart API"
slug: "sdk-for-flutter-explore-core-engine-sdknativeengine-makesharedinstance"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="core.engine/SDKNativeEngine-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">makeSharedInstance</span> static method

</div>

<div class="section multi-line-signature">

<span class="returntype">Future<span class="signature">\<<wbr></wbr><span class="type-parameter">void</span>\></span></span> <span class="name">makeSharedInstance</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-makeSharedInstance-param-options" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-engine-sdkoptions-class">SDKOptions</a></span> <span class="parameter-name">options</span></span>

)

</div>

<div class="section desc markdown">

Makes a new instance of SDKNativeEngine using supplied options and stores it as shared instance see <a href="sdk-for-flutter-explore-core-engine-sdknativeengine-sharedinstance">SDKNativeEngine.sharedInstance</a>.

If there was previously shared instance then it's disposed (see <a href="sdk-for-flutter-explore-core-engine-sdknativeengine-dispose">SDKNativeEngine.dispose</a>) before new instance is created.

- `options` The options for the new engine.

Throws <a href="sdk-for-flutter-explore-core-errors-instantiationexception-class">InstantiationException</a>. Indicates what went wrong when the instantiation was attempted.

</div>

## Implementation

``` dart
static Future<void> makeSharedInstance(SDKOptions options) => $prototype.makeSharedInstance(options);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

