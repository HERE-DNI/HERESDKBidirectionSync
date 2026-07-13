---
title: "TMCServiceInterface constructor - TMCServiceInterface - trafficbroadcast library - Dart API"
slug: "sdk-for-flutter-navigate-trafficbroadcast-tmcserviceinterface-tmcserviceinterface"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TMCServiceInterface.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="trafficbroadcast/TMCServiceInterface-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">TMCServiceInterface</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">TMCServiceInterface</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-requestTMCServiceLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">requestTMCServiceLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-trafficbroadcast-tmcservicerequest-class">TMCServiceRequest</a></span></span>

    ), </span>
2.  <span id="sdk-for-flutter-navigate-param-getTMCPreferredSidsLambda" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter">int</span>\></span></span> <span class="parameter-name">getTMCPreferredSidsLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-trafficbroadcast-tmcpreferredsidsrequest-class">TMCPreferredSidsRequest</a></span></span>

    ), </span>
3.  <span id="sdk-for-flutter-navigate-param-getRDSEncryptionKeysLambda" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-trafficbroadcast-rdsencryptionkey-class">RDSEncryptionKey</a></span>\></span></span> <span class="parameter-name">getRDSEncryptionKeysLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-trafficbroadcast-rdsencryptionkeysrequest-class">RDSEncryptionKeysRequest</a></span></span>

    )</span>

)

</div>

<div class="section desc markdown">

Contains all outgoing dependencies to the client side.

</div>

## Implementation

``` dart
factory TMCServiceInterface(
  void Function(TMCServiceRequest) requestTMCServiceLambda,
  List<int> Function(TMCPreferredSidsRequest) getTMCPreferredSidsLambda,
  List<RDSEncryptionKey> Function(RDSEncryptionKeysRequest) getRDSEncryptionKeysLambda,

) => TMCServiceInterface$Lambdas(
  requestTMCServiceLambda,
  getTMCPreferredSidsLambda,
  getRDSEncryptionKeysLambda,

);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
