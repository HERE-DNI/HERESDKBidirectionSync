---
title: "ElectronicHorizonEngine.WithOptionsAndRoutePathEvaluator constructor - ElectronicHorizonEngine - electronic_horizon library - Dart API"
slug: "sdk-for-flutter-navigate-electronic_horizon-electronichorizonengine-electronichorizonengine-withoptionsandroutepathevaluator"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- ElectronicHorizonEngine.WithOptionsAndRoutePathEvaluator.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="electronic_horizon/ElectronicHorizonEngine-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">ElectronicHorizonEngine.WithOptionsAndRoutePathEvaluator</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">ElectronicHorizonEngine.WithOptionsAndRoutePathEvaluator</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-WithOptionsAndRoutePathEvaluator-param-sdkEngine" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-class">SDKNativeEngine</a></span> <span class="parameter-name">sdkEngine</span>, </span>
2.  <span id="sdk-for-flutter-navigate-WithOptionsAndRoutePathEvaluator-param-options" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonoptions-class">ElectronicHorizonOptions</a></span> <span class="parameter-name">options</span>, </span>
3.  <span id="sdk-for-flutter-navigate-WithOptionsAndRoutePathEvaluator-param-transportMode" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode</a></span> <span class="parameter-name">transportMode</span>, </span>
4.  <span id="sdk-for-flutter-navigate-WithOptionsAndRoutePathEvaluator-param-route" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-route-class">Route</a>?</span> <span class="parameter-name">route</span>, </span>

)

</div>

<div class="section desc markdown">

Creates a new instance of <a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonengine-class">ElectronicHorizonEngine</a>.

- `sdkEngine` The <a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-class">SDKNativeEngine</a> instance that provides shared services, such as networking and map data.

- `options` The <a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonoptions-class">ElectronicHorizonOptions</a> instance that configures how the electronic horizon is calculated, including look-ahead distances.

- `transportMode` The <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode</a> that is used when building the electronic horizon paths.

- `route` The <a href="sdk-for-flutter-navigate-routing-route-class">Route</a> that improves the calculation of the most-preferred path (MPP). If `null` is passed, the most-preferred path can deviate from the route.

Throws <a href="sdk-for-flutter-navigate-core-errors-instantiationexception-class">InstantiationException</a>. <a href="sdk-for-flutter-navigate-core-errors-instantiationexception-class">InstantiationException</a> If the electronic horizon engine cannot be created.

</div>

## Implementation

``` dart
factory ElectronicHorizonEngine.WithOptionsAndRoutePathEvaluator(SDKNativeEngine sdkEngine, ElectronicHorizonOptions options, TransportMode transportMode, Route? route) => $prototype.WithOptionsAndRoutePathEvaluator(sdkEngine, options, transportMode, route);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
