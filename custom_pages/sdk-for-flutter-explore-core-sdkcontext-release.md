---
title: "release method - SdkContext class - core library - Dart API"
slug: "sdk-for-flutter-explore-core-sdkcontext-release"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- release.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="core/SdkContext-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">release</span> static method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">release</span>(<wbr></wbr>)

</div>

<div class="section desc markdown">

Releases resources used by the SDK

Users should call this method once, when the application shuts down, preferably in the dispose() method of the root widget's State.

</div>

## Implementation

``` dart
static void release() {
  LibraryContext.release();
}
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
