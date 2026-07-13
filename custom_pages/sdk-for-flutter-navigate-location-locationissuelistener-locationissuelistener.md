---
title: "LocationIssueListener constructor - LocationIssueListener - location library - Dart API"
slug: "sdk-for-flutter-navigate-location-locationissuelistener-locationissuelistener"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="location/LocationIssueListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">LocationIssueListener</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">LocationIssueListener</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-onLocationIssueChangedLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onLocationIssueChangedLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-location-locationissuetype">LocationIssueType</a></span>\></span></span></span>

    )</span>

)

</div>

<div class="section desc markdown">

abstract class receiving notifications when the set of currently active location issues changes.

Location issues represent unexpected or degraded conditions affecting positioning quality, availability, or functionality. The LocationEngine monitors various positioning subsystems and aggregates detected issues into a unified snapshot delivered via this interface.

- Each callback delivers the complete current set of active issues.
- An empty list indicates all previously reported issues have cleared.
- Issues are transient by design and automatically removed once underlying conditions improve. No explicit clear/dismiss API is provided.

</div>

## Implementation

``` dart
factory LocationIssueListener(
  void Function(List<LocationIssueType>) onLocationIssueChangedLambda,

) => LocationIssueListener$Lambdas(
  onLocationIssueChangedLambda,

);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

