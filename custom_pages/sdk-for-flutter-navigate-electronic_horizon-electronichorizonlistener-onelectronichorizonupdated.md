---
title: "onElectronicHorizonUpdated method - ElectronicHorizonListener class - electronic_horizon library - Dart API"
slug: "sdk-for-flutter-navigate-electronic_horizon-electronichorizonlistener-onelectronichorizonupdated"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- onElectronicHorizonUpdated.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="electronic_horizon/ElectronicHorizonListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">onElectronicHorizonUpdated</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">onElectronicHorizonUpdated</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-onElectronicHorizonUpdated-param-errorCode" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonerrorcode">ElectronicHorizonErrorCode</a>?</span> <span class="parameter-name">errorCode</span>, </span>
2.  <span id="sdk-for-flutter-navigate-onElectronicHorizonUpdated-param-update" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonupdate-class">ElectronicHorizonUpdate</a>?</span> <span class="parameter-name">update</span></span>

)

</div>

<div class="section desc markdown">

Called whenever the electronic horizon subsystem produces:

- a new update,
- an error,

The client must inspect `error_code` to determine whether the call represents an error or a valid update.

- `errorCode` The error associated with the horizon computation. `null` means no error.

- `update` The update describing the current electronic horizon state. May be `null` if an update could not be produced.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

## Implementation

``` dart
void onElectronicHorizonUpdated(ElectronicHorizonErrorCode? errorCode, ElectronicHorizonUpdate? update);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
