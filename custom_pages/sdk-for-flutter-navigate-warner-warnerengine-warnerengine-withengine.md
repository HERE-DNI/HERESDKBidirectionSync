---
title: "WarnerEngine.WithEngine constructor - WarnerEngine - warner library - Dart API"
slug: "sdk-for-flutter-navigate-warner-warnerengine-warnerengine-withengine"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- WarnerEngine.WithEngine.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="warner/WarnerEngine-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">WarnerEngine.WithEngine</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">WarnerEngine.WithEngine</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-WithEngine-param-sdkEngine" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-class">SDKNativeEngine</a></span> <span class="parameter-name">sdkEngine</span>, </span>
2.  <span id="sdk-for-flutter-navigate-WithEngine-param-enabledWarnings" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-navigation-warningtype">WarningType</a></span>\></span></span> <span class="parameter-name">enabledWarnings</span></span>

)

</div>

<div class="section desc markdown">

Creates a new instance of this class.

- `sdkEngine` A `SDKEngine` instance.

- `enabledWarnings` The list of warning types that should be monitored and processed by the engine. Only warnings of these types will be generated.

Throws <a href="sdk-for-flutter-navigate-core-errors-instantiationexception-class">InstantiationException</a>. Indicates what went wrong when the instantiation was attempted.

</div>

## Implementation

``` dart
factory WarnerEngine.WithEngine(SDKNativeEngine sdkEngine, List<WarningType> enabledWarnings) => $prototype.WithEngine(sdkEngine, enabledWarnings);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
