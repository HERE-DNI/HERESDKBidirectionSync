---
title: "TMCServiceRequest constructor - TMCServiceRequest - trafficbroadcast library - Dart API"
slug: "sdk-for-flutter-navigate-trafficbroadcast-tmcservicerequest-tmcservicerequest"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="trafficbroadcast/TMCServiceRequest-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">TMCServiceRequest</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">TMCServiceRequest</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-countryCode" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">countryCode</span>, </span>
2.  <span id="sdk-for-flutter-navigate-param-preferredSids" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter">int</span>\></span></span> <span class="parameter-name">preferredSids</span>, </span>
3.  <span id="sdk-for-flutter-navigate-param-supportedLtns" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter">int</span>\></span></span> <span class="parameter-name">supportedLtns</span></span>

)

</div>

<div class="section desc markdown">

Creates a new instance.

- `countryCode` Refers to a country in RDS-TMC format.
- `preferredSids` List of preferred SIDs (up to 8).
- `supportedLtns` List of supported LTNs (up to 8).

</div>

## Implementation

``` dart
TMCServiceRequest(this.countryCode, this.preferredSids, this.supportedLtns);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

