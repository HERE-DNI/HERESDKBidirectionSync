---
title: "DeviceIdCallback typedef - core.engine library - Dart API"
slug: "sdk-for-flutter-explore-core-engine-deviceidcallback"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="core.engine/core.engine-library-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-typedef">DeviceIdCallback</span> typedef

</div>

<div class="section multi-line-signature">

<span class="name">DeviceIdCallback</span> = <span class="returntype">void Function<span class="signature">(<span id="sdk-for-flutter-explore-param-deviceId" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">deviceId</span></span>)</span></span>

</div>

<div class="section desc markdown">

This method will be called on the main thread when <a href="sdk-for-flutter-explore-core-engine-sdknativeengine-getdeviceid">SDKNativeEngine.getDeviceId</a> has been completed.

- `deviceId` Represents a deviceId, a unique identifier assigned to the device for this application.

</div>

## Implementation

``` dart
typedef DeviceIdCallback = void Function(String deviceId);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

