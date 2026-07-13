---
title: "getBackgroundLocationAllowed method - LocationEngine class - location library - Dart API"
slug: "sdk-for-flutter-navigate-location-locationengine-getbackgroundlocationallowed"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- getBackgroundLocationAllowed.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="location/LocationEngine-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">getBackgroundLocationAllowed</span> method

</div>

<div class="section multi-line-signature">

<span class="returntype">bool</span> <span class="name">getBackgroundLocationAllowed</span>(<wbr></wbr>)

<div class="features">

<span class="feature">override</span>

</div>

</div>

<div class="section desc markdown">

On iOS devices this checks if application's background location updates are enabled. Returns true if background location updates are allowed, false otherwise.

On Android devices this is not supported and false is returned.

</div>

## Implementation

``` dart
bool getBackgroundLocationAllowed() {
  if (Platform.isIOS) {
    return _location.getBackgroundLocationAllowed();
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
