---
title: "VenueEngine.withSdkEngine constructor - VenueEngine - venue library - Dart API"
slug: "sdk-for-flutter-navigate-venue-venueengine-venueengine-withsdkengine"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- VenueEngine.withSdkEngine.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="venue/VenueEngine-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">VenueEngine.withSdkEngine</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">VenueEngine.withSdkEngine</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-withSdkEngine-param-sdkEngine" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-class">SDKNativeEngine</a></span> <span class="parameter-name">sdkEngine</span>, </span>
2.  <span id="sdk-for-flutter-navigate-withSdkEngine-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-venue-venueengineinitcallback">VenueEngineInitCallback</a>?</span> <span class="parameter-name">callback</span></span>

)

</div>

<div class="section desc markdown">

Creates a new instance of this class.

- `sdkEngine` Instance of existing SDKEngine.

- `callback` The optional callback that will be triggered when a venue engine initialization will be completed. After the initialization, the <a href="sdk-for-flutter-navigate-venue-service-venueservice-class">VenueService</a> should be started using one of its methods or using <a href="sdk-for-flutter-navigate-venue-venueengine-startwithtoken">VenueEngine.startWithToken</a>.

Throws <a href="sdk-for-flutter-navigate-core-errors-instantiationexception-class">InstantiationException</a>. Indicates what went wrong when the instantiation was attempted.

</div>

## Implementation

``` dart
factory VenueEngine.withSdkEngine(SDKNativeEngine sdkEngine, VenueEngineInitCallback? callback) => $prototype.withSdkEngine(sdkEngine, callback);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
