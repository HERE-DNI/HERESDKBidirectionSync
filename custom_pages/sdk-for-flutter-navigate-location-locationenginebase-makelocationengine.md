---
title: "makeLocationEngine method - LocationEngineBase class - location library - Dart API"
slug: "sdk-for-flutter-navigate-location-locationenginebase-makelocationengine"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- makeLocationEngine.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="location/LocationEngineBase-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">makeLocationEngine</span> static method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-location-locationenginebase-class">LocationEngineBase</a></span> <span class="name">makeLocationEngine</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-makeLocationEngine-param-sdkEngine" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-class">SDKNativeEngine</a></span> <span class="parameter-name">sdkEngine</span></span>

)

</div>

<div class="section desc markdown">

Creates instance of `LocationEngine` using factory, registered on platform side

- `sdkEngine` Instance of <a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-class">SDKNativeEngine</a> used for initialization.

Returns <a href="sdk-for-flutter-navigate-location-locationenginebase-class">LocationEngineBase</a>. A new LocationEngineBase instance.

Throws <a href="sdk-for-flutter-navigate-core-errors-instantiationexception-class">InstantiationException</a>. Instantiation If the instance cannot be created.

</div>

## Implementation

``` dart
static LocationEngineBase makeLocationEngine(SDKNativeEngine sdkEngine) => $prototype.makeLocationEngine(sdkEngine);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
