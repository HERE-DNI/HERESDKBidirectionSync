---
title: "ElectronicHorizonListener constructor - ElectronicHorizonListener - electronic_horizon library - Dart API"
slug: "sdk-for-flutter-navigate-electronic_horizon-electronichorizonlistener-electronichorizonlistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- ElectronicHorizonListener.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="electronic_horizon/ElectronicHorizonListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">ElectronicHorizonListener</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">ElectronicHorizonListener</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-onElectronicHorizonUpdatedLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onElectronicHorizonUpdatedLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonerrorcode">ElectronicHorizonErrorCode</a>?</span>, </span>
    2.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonupdate-class">ElectronicHorizonUpdate</a>?</span></span>

    )</span>

)

</div>

<div class="section desc markdown">

Provides a listener for receiving updates during execution of the <a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonengine-update">ElectronicHorizonEngine.update</a> method.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

Offline availability: This property is available online and offline.

</div>

## Implementation

``` dart
factory ElectronicHorizonListener(
  void Function(ElectronicHorizonErrorCode?, ElectronicHorizonUpdate?) onElectronicHorizonUpdatedLambda,

) => ElectronicHorizonListener$Lambdas(
  onElectronicHorizonUpdatedLambda,

);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
