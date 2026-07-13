---
title: "shadowQuality property - HereMapController class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-heremapcontroller-shadowquality"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- shadowQuality.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/HereMapController-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">shadowQuality</span> property

</div>

<div id="sdk-for-flutter-navigate-getter" class="section">

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-mapview-shadowquality">ShadowQuality</a></span> <span class="name">shadowQuality</span>

</div>

<div class="section desc markdown">

The current shadow quality. Default shadow quality is <a href="sdk-for-flutter-navigate-mapview-shadowquality">ShadowQuality.medium</a>. Note: This feature is in beta state and thus there can be bugs and unexpected behavior.

</div>

## Implementation

``` dart
static ShadowQuality get shadowQuality => $prototype.shadowQuality;
```

</div>

<div id="sdk-for-flutter-navigate-setter" class="section">

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">shadowQuality=</span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-shadowQuality-param-shadowQuality" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-shadowquality">ShadowQuality</a></span> <span class="parameter-name">shadowQuality</span></span>)</span>

</div>

<div class="section desc markdown">

Sets the desired shadow quality for all instances of HereMap to `shadowQuality`. The quality controls the size of the shadow maps and the cascade count. Default shadow quality is <a href="sdk-for-flutter-navigate-mapview-shadowquality">ShadowQuality.medium</a>. HereMaps can request to render shadows by feature. Enabling shadows has a performance impact and should be considered only for devices with sufficient performance. Note: This feature is in beta state and thus there can be bugs and unexpected behavior.

</div>

## Implementation

``` dart
static void set shadowQuality(ShadowQuality shadowQuality) {
  $prototype.shadowQuality = shadowQuality;
}
```

</pre>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
