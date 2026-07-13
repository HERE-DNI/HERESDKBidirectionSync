---
title: "onElectronicHorizonDataLoaderStatusUpdated method - ElectronicHorizonDataLoaderStatusListener class - electronic_horizon library - Dart API"
slug: "sdk-for-flutter-navigate-electronic_horizon-electronichorizondataloaderstatuslistener-onelectronichorizondataloaderstatusupdated"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- onElectronicHorizonDataLoaderStatusUpdated.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="electronic_horizon/ElectronicHorizonDataLoaderStatusListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">onElectronicHorizonDataLoaderStatusUpdated</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">onElectronicHorizonDataLoaderStatusUpdated</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-onElectronicHorizonDataLoaderStatusUpdated-param-electronicHorizonDataLoaderStatuses" class="parameter"><span class="type-annotation">Map<span class="signature">\<<wbr></wbr><span class="type-parameter">int</span>, <span class="type-parameter"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizondataloadedstatus">ElectronicHorizonDataLoadedStatus</a></span>\></span></span> <span class="parameter-name">electronicHorizonDataLoaderStatuses</span></span>

)

</div>

<div class="section desc markdown">

Called whenever there is a change in the status of the loaded data from <a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizondataloader-class">ElectronicHorizonDataLoader</a>.

- `electronicHorizonDataLoaderStatuses` The updated statuses of the loaded data from <a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizondataloader-class">ElectronicHorizonDataLoader</a>. The key is the level of a `ElectronicHorizonPath`, the value is the current status.

</div>

## Implementation

``` dart
void onElectronicHorizonDataLoaderStatusUpdated(Map<int, ElectronicHorizonDataLoadedStatus> electronicHorizonDataLoaderStatuses);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
