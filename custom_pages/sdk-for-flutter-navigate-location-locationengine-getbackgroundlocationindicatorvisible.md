---
title: "getBackgroundLocationIndicatorVisible method - LocationEngine class - location library - Dart API"
slug: "sdk-for-flutter-navigate-location-locationengine-getbackgroundlocationindicatorvisible"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- getBackgroundLocationIndicatorVisible.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="location/LocationEngine-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">getBackgroundLocationIndicatorVisible</span> method

</div>

<div class="section multi-line-signature">

<span class="returntype">bool</span> <span class="name">getBackgroundLocationIndicatorVisible</span>(<wbr></wbr>)

<div class="features">

<span class="feature">override</span>

</div>

</div>

<div class="section desc markdown">

On iOS devices this checks if application's background location indicator is visible. Returns true if background location indicator is visible, false otherwise.

On Android devices this is not supported and false is returned.

</div>

## Implementation

``` dart
bool getBackgroundLocationIndicatorVisible() {
  if (Platform.isIOS) {
    return _location.getBackgroundLocationIndicatorVisible();
  }
  return false;
}
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
