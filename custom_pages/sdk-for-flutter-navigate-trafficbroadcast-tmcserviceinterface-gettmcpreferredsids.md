---
title: "getTMCPreferredSids method - TMCServiceInterface class - trafficbroadcast library - Dart API"
slug: "sdk-for-flutter-navigate-trafficbroadcast-tmcserviceinterface-gettmcpreferredsids"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="trafficbroadcast/TMCServiceInterface-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">getTMCPreferredSids</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">List<span class="signature">\<<wbr></wbr><span class="type-parameter">int</span>\></span></span> <span class="name">getTMCPreferredSids</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-getTMCPreferredSids-param-tmcPreferredSidsRequest" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-trafficbroadcast-tmcpreferredsidsrequest-class">TMCPreferredSidsRequest</a></span> <span class="parameter-name">tmcPreferredSidsRequest</span></span>

)

</div>

<div class="section desc markdown">

Called whenever there is a need to get a list of preferred SIDs for a specific area.

- `tmcPreferredSidsRequest` Specifies the area to request the preferred SIDs.

Returns `List<int>`. List of preferred SIDs.

</div>

## Implementation

``` dart
List<int> getTMCPreferredSids(TMCPreferredSidsRequest tmcPreferredSidsRequest);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

