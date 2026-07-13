---
title: "init method - SdkContext class - core library - Dart API"
slug: "sdk-for-flutter-explore-core-sdkcontext-init"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- init.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="core/SdkContext-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">init</span> static method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">init</span>(<wbr></wbr>\<a href="sdk-for-flutter-explore-core-isolateorigin">

1.  <span id="sdk-for-flutter-explore-init-param-isolateOrigin" class="parameter"><span class="type-annotation">[IsolateOrigin</a></span> <span class="parameter-name">isolateOrigin</span> = <span class="default-value">IsolateOrigin.main</span></span>

\])

</div>

<div class="section desc markdown">

Prepares the SDK for use

Users should call this method once, when the application starts, preferably in the main() method.

`isolateOrigin` The isolate in which the application is executing. This is IsolateOrigin.main by default, and this is suitable for almost all use cases.

</div>

## Implementation

``` dart
static void init([IsolateOrigin isolateOrigin = IsolateOrigin.main]) {
  LibraryContext.init(isolateOrigin, nativeLibraryPath: _getLibraryName());
  SDKDartInfo.version = Platform.version;
}
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
