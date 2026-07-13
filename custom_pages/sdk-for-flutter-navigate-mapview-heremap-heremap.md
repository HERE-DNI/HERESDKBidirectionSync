---
title: "HereMap constructor - HereMap - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-heremap-heremap"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- HereMap.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/HereMap-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">HereMap</span> constructor

</div>

<div class="section multi-line-signature">

const <span class="name">HereMap</span>(<wbr></wbr>{

1.  <span id="sdk-for-flutter-navigate-param-key" class="parameter"><span class="type-annotation">Key?</span> <span class="parameter-name">key</span>, </span>
2.  <span id="sdk-for-flutter-navigate-param-onMapCreated" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-heremapcreatedcallback">HereMapCreatedCallback</a>?</span> <span class="parameter-name">onMapCreated</span>, </span>
3.  <span id="sdk-for-flutter-navigate-param-gestureRecognizers" class="parameter"><span class="type-annotation">Set<span class="signature">\<<wbr></wbr><span class="type-parameter">Factory<span class="signature">\<<wbr></wbr><span class="type-parameter">OneSequenceGestureRecognizer</span>\></span></span>\></span>?</span> <span class="parameter-name">gestureRecognizers</span>, </span>
4.  <span id="sdk-for-flutter-navigate-param-mode" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-nativeviewmode">NativeViewMode</a></span> <span class="parameter-name">mode</span> = <span class="default-value">NativeViewMode.virtualDisplay</span>, </span>
5.  <span id="sdk-for-flutter-navigate-param-options" class="parameter"><span class="type-annotation">dynamic</span> <span class="parameter-name">options</span>, </span>

})

</div>

<div class="section desc markdown">

Creates a widget that displays a map.

</div>

## Implementation

``` dart
const HereMap({
  Key? key,
  this.onMapCreated,
  this.gestureRecognizers,
  this.mode = NativeViewMode.virtualDisplay,
  options,
})  : this._options = options,
      super(key: key);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
