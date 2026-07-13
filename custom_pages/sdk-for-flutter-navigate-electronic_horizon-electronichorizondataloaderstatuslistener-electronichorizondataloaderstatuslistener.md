---
title: "ElectronicHorizonDataLoaderStatusListener constructor - ElectronicHorizonDataLoaderStatusListener - electronic_horizon library - Dart API"
slug: "sdk-for-flutter-navigate-electronic_horizon-electronichorizondataloaderstatuslistener-electronichorizondataloaderstatuslistener"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="electronic_horizon/ElectronicHorizonDataLoaderStatusListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">ElectronicHorizonDataLoaderStatusListener</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">ElectronicHorizonDataLoaderStatusListener</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-onElectronicHorizonDataLoaderStatusUpdatedLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onElectronicHorizonDataLoaderStatusUpdatedLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation">Map<span class="signature">\<<wbr></wbr><span class="type-parameter">int</span>, <span class="type-parameter"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizondataloadedstatus">ElectronicHorizonDataLoadedStatus</a></span>\></span></span></span>

    )</span>

)

</div>

<div class="section desc markdown">

Provides a listener for status updates from the <a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizondataloader-loaddata">ElectronicHorizonDataLoader.loadData</a> method.

The listener receives the current state for different levels of the paths as <a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizondataloadedstatus">ElectronicHorizonDataLoadedStatus</a>.

Note: This is a **beta** release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

Offline availability: This property is available online and offline.

</div>

## Implementation

``` dart
factory ElectronicHorizonDataLoaderStatusListener(
  void Function(Map<int, ElectronicHorizonDataLoadedStatus>) onElectronicHorizonDataLoaderStatusUpdatedLambda,

) => ElectronicHorizonDataLoaderStatusListener$Lambdas(
  onElectronicHorizonDataLoaderStatusUpdatedLambda,

);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

