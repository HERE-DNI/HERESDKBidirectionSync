---
title: "AutomotiveCameraBehavior.fromJson constructor - AutomotiveCameraBehavior - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-automotivecamerabehavior-automotivecamerabehavior-fromjson"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- AutomotiveCameraBehavior.fromJson.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/AutomotiveCameraBehavior-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">AutomotiveCameraBehavior.fromJson</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">AutomotiveCameraBehavior.fromJson</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-fromJson-param-configJson" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">configJson</span></span>

)

</div>

<div class="section desc markdown">

Creates a new instance of this class configured from a JSON string.

The JSON configuration is validated during construction and applied to the underlying <a href="sdk-for-flutter-navigate-navigation-trackingcamerabehavior-class">TrackingCameraBehavior</a> and <a href="sdk-for-flutter-navigate-navigation-areacamerabehavior-class">AreaCameraBehavior</a> instances.

- `configJson` A JSON string containing automotive camera configuration settings.

Throws <a href="sdk-for-flutter-navigate-core-errors-instantiationexception-class">InstantiationException</a>. <a href="sdk-for-flutter-navigate-core-errors-instantiationexception-class">InstantiationException</a> when the JSON is malformed or contains invalid values.

</div>

## Implementation

``` dart
factory AutomotiveCameraBehavior.fromJson(String configJson) => $prototype.fromJson(configJson);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
