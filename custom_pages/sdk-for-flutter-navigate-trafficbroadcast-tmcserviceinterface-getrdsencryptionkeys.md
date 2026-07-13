---
title: "getRDSEncryptionKeys method - TMCServiceInterface class - trafficbroadcast library - Dart API"
slug: "sdk-for-flutter-navigate-trafficbroadcast-tmcserviceinterface-getrdsencryptionkeys"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="trafficbroadcast/TMCServiceInterface-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">getRDSEncryptionKeys</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-trafficbroadcast-rdsencryptionkey-class">RDSEncryptionKey</a></span>\></span></span> <span class="name">getRDSEncryptionKeys</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-getRDSEncryptionKeys-param-rdsEncryptionKeysRequest" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-trafficbroadcast-rdsencryptionkeysrequest-class">RDSEncryptionKeysRequest</a></span> <span class="parameter-name">rdsEncryptionKeysRequest</span></span>

)

</div>

<div class="section desc markdown">

Called whenever there is a need to get RDS encryption keys.

- `rdsEncryptionKeysRequest` Input data to search for keys.

Returns `List<RDSEncryptionKey>`. RDS encryption keys.

</div>

## Implementation

``` dart
List<RDSEncryptionKey> getRDSEncryptionKeys(RDSEncryptionKeysRequest rdsEncryptionKeysRequest);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

